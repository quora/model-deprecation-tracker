import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html"

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


def _detect_table_type(headers: list[str]) -> str:
    header_text = " ".join(headers).lower()
    if "eol date" in header_text and "extended" not in header_text:
        return "eol"
    if "legacy date" in header_text:
        return "legacy"
    return "unknown"


def _find_column_indices(headers: list[str]) -> dict[str, int]:
    indices: dict[str, int] = {}
    for i, h in enumerate(headers):
        h_lower = h.lower()
        if "model version" in h_lower and "replacement" not in h_lower:
            indices["model"] = i
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
        elif "recommended model id" in h_lower or ("model id" in h_lower and "recommended" in h_lower):
            indices["replacement_id"] = i
    return indices


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
    if "model" not in indices:
        return []

    entries: list[DeprecationEntry] = []

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        cell_texts = [c.get_text().strip() for c in cells]
        if len(cell_texts) <= indices["model"]:
            continue

        model_name = cell_texts[indices["model"]]
        if not model_name:
            continue

        deprecated_date = UNKNOWN_DATE
        if "legacy" in indices and indices["legacy"] < len(cell_texts):
            deprecated_date = _parse_date_safe(cell_texts[indices["legacy"]])

        shutdown_date = UNKNOWN_DATE
        if "eol" in indices and indices["eol"] < len(cell_texts):
            shutdown_date = _parse_date_safe(cell_texts[indices["eol"]])

        replacement_parts = []
        if "replacement_name" in indices and indices["replacement_name"] < len(cell_texts):
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

        entries.append(
            DeprecationEntry(
                provider="Bedrock",
                model_name=model_name,
                deprecated_date=deprecated_date,
                shutdown_date=shutdown_date,
                replacement=replacement,
                status=status,
            )
        )

    return entries


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    soup = BeautifulSoup(html, "html.parser")
    entries: list[DeprecationEntry] = []

    for table in soup.find_all("table"):
        entries.extend(_parse_table(table))

    return entries
