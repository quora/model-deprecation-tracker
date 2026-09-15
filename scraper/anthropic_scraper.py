import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://platform.claude.com/docs/en/about-claude/model-deprecations"

DEPRECATION_HEADING_RE = re.compile(r"^(\d{4}-\d{2}-\d{2}):")


def _clean_model_name(text: str) -> str:
    return text.strip().strip("`").strip()


def _parse_date_safe(text: str) -> datetime.date:
    text = text.strip()
    if not text or text.upper() == "N/A" or text == "-" or text == "—":
        return UNKNOWN_DATE

    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _parse_history_table(
    table: BeautifulSoup, deprecated_date: datetime.date
) -> list[DeprecationEntry]:
    """Parse confirmed retirement dates from a deprecation-history table."""
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [th.get_text().strip().lower() for th in rows[0].find_all(["th", "td"])]

    model_idx = -1
    retirement_idx = -1
    replacement_idx = -1

    for i, h in enumerate(headers):
        if "deprecated model" in h or "model" in h:
            model_idx = i
        if "retirement date" in h:
            retirement_idx = i
        if "replacement" in h or "recommended" in h:
            replacement_idx = i

    if model_idx == -1 or retirement_idx == -1:
        return []

    entries: list[DeprecationEntry] = []
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) <= max(model_idx, retirement_idx):
            continue

        cell_texts = [c.get_text().strip() for c in cells]
        model_name = _clean_model_name(cell_texts[model_idx])
        retirement_date = _parse_date_safe(cell_texts[retirement_idx])
        replacement = ""
        if replacement_idx >= 0 and replacement_idx < len(cell_texts):
            replacement = cell_texts[replacement_idx].strip()

        if not model_name:
            continue
        if retirement_date == UNKNOWN_DATE:
            raise ValueError(
                f"Could not parse Anthropic retirement date for {model_name}"
            )

        status = "retired" if retirement_date <= datetime.date.today() else "deprecated"
        entries.append(
            DeprecationEntry(
                provider="Anthropic",
                model_name=model_name,
                deprecated_date=deprecated_date,
                shutdown_date=retirement_date,
                replacement=replacement,
                status=status,
            )
        )

    return entries


def _is_history_table(headers: list[str]) -> bool:
    header_text = " ".join(headers).lower()
    return "retirement date" in header_text and "deprecated model" in header_text


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    soup = BeautifulSoup(html, "html.parser")
    entries: list[DeprecationEntry] = []
    history_table_count = 0

    for table in soup.find_all("table"):
        first_row = table.find("tr")
        if not first_row:
            continue
        headers = [th.get_text().strip() for th in first_row.find_all(["th", "td"])]
        if _is_history_table(headers):
            history_table_count += 1
            deprecated_date = UNKNOWN_DATE
            heading = table.find_previous(["h2", "h3", "h4"])
            if heading:
                match = DEPRECATION_HEADING_RE.match(heading.get_text().strip())
                if match:
                    deprecated_date = datetime.date.fromisoformat(match.group(1))
            table_entries = _parse_history_table(table, deprecated_date)
            if not table_entries:
                raise ValueError(
                    "Anthropic deprecation-history table has no valid rows"
                )
            entries.extend(table_entries)

    if history_table_count == 0:
        raise ValueError("Anthropic deprecation-history tables not found")

    return entries
