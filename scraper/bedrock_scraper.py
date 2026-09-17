import datetime
import re
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, create_session, fetch_page

LEGACY_URL = (
    "https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle-legacy.html"
)
MODEL_CARDS_URL = (
    "https://docs.aws.amazon.com/bedrock/latest/userguide/model-cards.html"
)
URL = LEGACY_URL

TRACKED_MODEL_PROVIDERS = {"anthropic", "google", "openai"}
UNCONFIRMED_DATE_QUALIFIERS = (
    "at earliest",
    "at the earliest",
    "earliest possible",
    "no earlier than",
    "no sooner than",
    "not before",
)
MISSING_MODEL_IDS = {"", "-", "—", "n/a", "na", "not supported"}

DATE_WITH_PARENS_RE = re.compile(r"^(.*?)(?:\s*\(.*\))?\s*$")


def _strip_region_info(text: str) -> str:
    """Extract the date portion, removing region info in parentheses."""
    match = DATE_WITH_PARENS_RE.match(text)
    if match:
        return match.group(1).strip()
    return text.strip()


def _parse_date_safe(text: str) -> datetime.date:
    text = _strip_region_info(text)
    if not text or text == "-" or text == "—" or text.upper() == "N/A":
        return UNKNOWN_DATE
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _parse_confirmed_eol_date(text: str, header: str = "") -> datetime.date:
    normalized = " ".join(f"{header} {text}".lower().split())
    if any(qualifier in normalized for qualifier in UNCONFIRMED_DATE_QUALIFIERS):
        return UNKNOWN_DATE
    return _parse_date_safe(text)


def _is_tracked_model(model_provider: str, model_id: str) -> bool:
    if model_id:
        model_id_provider = model_id.split(".", 1)[0].lower()
        return model_id_provider in TRACKED_MODEL_PROVIDERS
    return model_provider.strip().lower() in TRACKED_MODEL_PROVIDERS


def _detect_table_type(headers: list[str]) -> str:
    header_text = " ".join(headers).lower()
    if "eol date" in header_text and "legacy date" in header_text:
        return "legacy"
    if "eol date" in header_text:
        return "eol"
    return "unknown"


def _find_column_indices(headers: list[str]) -> dict[str, int]:
    indices: dict[str, int] = {}
    for i, h in enumerate(headers):
        h_lower = h.lower()
        if h_lower in ("model name", "model version"):
            indices["model"] = i
        elif h_lower == "model provider":
            indices["provider"] = i
        elif h_lower == "model id":
            indices["model_id"] = i
        elif "legacy date" in h_lower:
            indices["legacy"] = i
        elif "extended" in h_lower:
            indices["extended"] = i
        elif "eol" in h_lower or "end of life" in h_lower:
            indices["eol"] = i
        elif "recommended model version" in h_lower or (
            "recommended" in h_lower and "id" not in h_lower
        ):
            indices["replacement_name"] = i
        elif "recommended model id" in h_lower or (
            "model id" in h_lower and "recommended" in h_lower
        ):
            indices["replacement_id"] = i
    return indices


def _is_lifecycle_table(table: BeautifulSoup) -> bool:
    rows = table.find_all("tr")
    if not rows:
        return False
    headers = [cell.get_text().strip() for cell in rows[0].find_all(["th", "td"])]
    indices = _find_column_indices(headers)
    return (
        _detect_table_type(headers) != "unknown"
        and "model" in indices
        and "eol" in indices
    )


def _build_row_cells(
    row, num_columns: int, rowspan_tracker: dict[int, tuple[str, int]]
) -> list[str]:
    """Build a full-width cell list, accounting for active rowspans from previous rows."""
    raw_cells = row.find_all(["td", "th"])
    result: list[str] = []
    raw_idx = 0

    for col in range(num_columns):
        if col in rowspan_tracker:
            text, remaining = rowspan_tracker[col]
            result.append(text)
            if remaining <= 1:
                del rowspan_tracker[col]
            else:
                rowspan_tracker[col] = (text, remaining - 1)
        elif raw_idx < len(raw_cells):
            cell = raw_cells[raw_idx]
            text = " ".join(cell.get_text().split())
            result.append(text)
            span = int(cell.get("rowspan", 1))
            if span > 1:
                rowspan_tracker[col] = (text, span - 1)
            raw_idx += 1
        else:
            result.append("")

    return result


def _parse_table(table: BeautifulSoup) -> list[DeprecationEntry]:
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [th.get_text().strip() for th in rows[0].find_all(["th", "td"])]
    if not headers:
        return []

    table_type = _detect_table_type(headers)
    if table_type == "unknown":
        return []

    indices = _find_column_indices(headers)
    if "model" not in indices or "eol" not in indices:
        return []

    num_columns = len(headers)
    raw_entries: list[DeprecationEntry] = []
    rowspan_tracker: dict[int, tuple[str, int]] = {}

    for row in rows[1:]:
        cell_texts = _build_row_cells(row, num_columns, rowspan_tracker)

        model_name = (
            cell_texts[indices["model"]] if indices["model"] < len(cell_texts) else ""
        )
        if not model_name:
            continue

        model_provider = ""
        if "provider" in indices and indices["provider"] < len(cell_texts):
            model_provider = cell_texts[indices["provider"]].strip()
        model_id = ""
        if "model_id" in indices and indices["model_id"] < len(cell_texts):
            model_id = cell_texts[indices["model_id"]].strip()
        if not _is_tracked_model(model_provider, model_id):
            continue

        deprecated_date = UNKNOWN_DATE
        if "legacy" in indices and indices["legacy"] < len(cell_texts):
            deprecated_date = _parse_date_safe(cell_texts[indices["legacy"]])

        shutdown_date = UNKNOWN_DATE
        if "eol" in indices and indices["eol"] < len(cell_texts):
            shutdown_date = _parse_confirmed_eol_date(
                cell_texts[indices["eol"]], headers[indices["eol"]]
            )

        replacement_parts = []
        if "replacement_name" in indices and indices["replacement_name"] < len(
            cell_texts
        ):
            val = cell_texts[indices["replacement_name"]].strip()
            if val and val != "-" and val != "—":
                replacement_parts.append(val)
        if "replacement_id" in indices and indices["replacement_id"] < len(cell_texts):
            val = cell_texts[indices["replacement_id"]].strip()
            if val and val != "-" and val != "—":
                replacement_parts.append(val)

        replacement = " / ".join(replacement_parts) if replacement_parts else ""

        status = "legacy"
        if table_type == "eol":
            status = "retired"
        elif shutdown_date != UNKNOWN_DATE and shutdown_date <= datetime.date.today():
            status = "retired"

        raw_entries.append(
            DeprecationEntry(
                provider="Bedrock",
                model_name=model_name,
                model_id=model_id,
                deprecated_date=deprecated_date,
                shutdown_date=shutdown_date,
                replacement=replacement,
                status=status,
            )
        )

    return _deduplicate(raw_entries)


def _entry_identity(entry: DeprecationEntry) -> str:
    return entry.model_id or entry.model_name.casefold()


def _deduplicate(entries: list[DeprecationEntry]) -> list[DeprecationEntry]:
    """Collapse regional rows while preserving distinct model versions."""
    best: dict[str, DeprecationEntry] = {}
    for entry in entries:
        identity = _entry_identity(entry)
        existing = best.get(identity)
        if existing is None:
            best[identity] = entry
        elif entry.has_shutdown_date() and (
            not existing.has_shutdown_date()
            or entry.shutdown_date < existing.shutdown_date
        ):
            best[identity] = entry

    return list(best.values())


def _extract_model_id(soup: BeautifulSoup) -> str:
    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if len(rows) < 2:
            continue
        headers = [
            cell.get_text().strip().lower() for cell in rows[0].find_all(["th", "td"])
        ]
        if "model id" not in headers:
            continue
        model_id_idx = headers.index("model id")
        for row in rows[1:]:
            cells = row.find_all(["th", "td"])
            if model_id_idx >= len(cells):
                continue
            model_id = cells[model_id_idx].get_text().strip()
            if model_id.lower() not in MISSING_MODEL_IDS:
                return model_id
    return ""


def _parse_model_card(html: str) -> DeprecationEntry | None:
    soup = BeautifulSoup(html, "html.parser")
    heading = soup.find("h1")
    if heading is None:
        raise ValueError("Bedrock model card is missing its model name")

    eol_text = ""
    eol_header = ""
    for label in soup.find_all("b"):
        label_text = " ".join(label.get_text().split())
        if label_text.lower().rstrip(":") == "model eol date":
            eol_header = label_text
            parent_text = " ".join(label.parent.get_text(" ", strip=True).split())
            eol_text = (
                parent_text.split(":", 1)[1].strip() if ":" in parent_text else ""
            )
            break
    if not eol_header:
        raise ValueError(
            f"Bedrock model card is missing Model EOL date: {heading.get_text().strip()}"
        )

    shutdown_date = _parse_confirmed_eol_date(eol_text, eol_header)
    if shutdown_date == UNKNOWN_DATE:
        return None

    model_id = _extract_model_id(soup)
    if not model_id:
        raise ValueError(
            f"Bedrock model card is missing Model ID: {heading.get_text().strip()}"
        )

    return DeprecationEntry(
        provider="Bedrock",
        model_name=heading.get_text().strip(),
        model_id=model_id,
        shutdown_date=shutdown_date,
        status="retired" if shutdown_date <= datetime.date.today() else "legacy",
    )


def _find_tracked_model_card_urls(html: str) -> list[str]:
    soup = BeautifulSoup(html, "html.parser")
    urls: list[str] = []
    for row in soup.find_all("tr"):
        cells = row.find_all(["th", "td"])
        if len(cells) < 3:
            continue
        provider = cells[1].get_text().strip().lower()
        if provider not in TRACKED_MODEL_PROVIDERS:
            continue
        for link in cells[2].find_all("a", href=True):
            urls.append(urljoin(MODEL_CARDS_URL, link["href"]))
    if not urls:
        raise ValueError("Bedrock model-card index has no tracked providers")
    return urls


def scrape(html: str = "") -> list[DeprecationEntry]:
    if html:
        return _parse_lifecycle_page(html)

    session = create_session()
    entries = _parse_lifecycle_page(fetch_page(LEGACY_URL, session))
    model_card_urls = _find_tracked_model_card_urls(
        fetch_page(MODEL_CARDS_URL, session)
    )
    for url in model_card_urls:
        entry = _parse_model_card(fetch_page(url, session))
        if entry is not None:
            entries.append(entry)
    return _deduplicate(entries)


def _parse_lifecycle_page(html: str) -> list[DeprecationEntry]:
    soup = BeautifulSoup(html, "html.parser")
    entries: list[DeprecationEntry] = []

    lifecycle_tables = [
        table for table in soup.find_all("table") if _is_lifecycle_table(table)
    ]
    if not lifecycle_tables:
        raise ValueError("Bedrock EOL table not found")

    for table in lifecycle_tables:
        entries.extend(_parse_table(table))

    return entries
