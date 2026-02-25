import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://platform.claude.com/docs/en/about-claude/model-deprecations"

STATUS_MAP = {
    "active": "active",
    "legacy": "legacy",
    "deprecated": "deprecated",
    "retired": "retired",
}

NOT_SOONER_THAN_RE = re.compile(r"not\s+sooner\s+than\s+(.+)", re.IGNORECASE)


def _clean_model_name(text: str) -> str:
    return text.strip().strip("`").strip()


def _parse_date_safe(text: str) -> datetime.date:
    text = text.strip()
    if not text or text.upper() == "N/A" or text == "-" or text == "—":
        return UNKNOWN_DATE

    match = NOT_SOONER_THAN_RE.search(text)
    if match:
        text = match.group(1).strip()

    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _parse_status_table(table: BeautifulSoup) -> list[DeprecationEntry]:
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [th.get_text().strip().lower() for th in rows[0].find_all(["th", "td"])]

    name_idx = -1
    state_idx = -1
    deprecated_idx = -1
    retirement_idx = -1

    for i, h in enumerate(headers):
        if "model name" in h or "api model" in h:
            name_idx = i
        elif "current state" in h or "state" in h:
            state_idx = i
        elif "deprecated" in h and "retirement" not in h and "date" not in h:
            deprecated_idx = i
        elif "retirement" in h or "tentative" in h:
            retirement_idx = i

    if name_idx == -1:
        return []

    entries = []
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) <= name_idx:
            continue

        cell_texts = [c.get_text().strip() for c in cells]
        model_name = _clean_model_name(cell_texts[name_idx])
        if not model_name:
            continue

        status = "active"
        if state_idx >= 0 and state_idx < len(cell_texts):
            raw_status = cell_texts[state_idx].strip().lower()
            status = STATUS_MAP.get(raw_status, raw_status)

        deprecated_date = UNKNOWN_DATE
        if deprecated_idx >= 0 and deprecated_idx < len(cell_texts):
            deprecated_date = _parse_date_safe(cell_texts[deprecated_idx])

        shutdown_date = UNKNOWN_DATE
        if retirement_idx >= 0 and retirement_idx < len(cell_texts):
            shutdown_date = _parse_date_safe(cell_texts[retirement_idx])

        entries.append(
            DeprecationEntry(
                provider="Anthropic",
                model_name=model_name,
                deprecated_date=deprecated_date,
                shutdown_date=shutdown_date,
                status=status,
            )
        )

    return entries


def _parse_history_table(table: BeautifulSoup) -> dict[str, str]:
    """Returns a mapping of model_name -> replacement from deprecation history tables."""
    rows = table.find_all("tr")
    if not rows:
        return {}

    headers = [th.get_text().strip().lower() for th in rows[0].find_all(["th", "td"])]

    model_idx = -1
    replacement_idx = -1

    for i, h in enumerate(headers):
        if "deprecated model" in h or "model" in h:
            model_idx = i
        if "replacement" in h or "recommended" in h:
            replacement_idx = i

    if model_idx == -1 or replacement_idx == -1:
        return {}

    replacements: dict[str, str] = {}
    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) <= max(model_idx, replacement_idx):
            continue

        cell_texts = [c.get_text().strip() for c in cells]
        model_name = _clean_model_name(cell_texts[model_idx])
        replacement = cell_texts[replacement_idx].strip()

        if model_name and replacement:
            replacements[model_name] = replacement

    return replacements


def _is_status_table(headers: list[str]) -> bool:
    header_text = " ".join(headers).lower()
    return "current state" in header_text or "api model name" in header_text


def _is_history_table(headers: list[str]) -> bool:
    header_text = " ".join(headers).lower()
    return "retirement date" in header_text and "deprecated model" in header_text


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    soup = BeautifulSoup(html, "html.parser")
    entries: list[DeprecationEntry] = []
    replacements: dict[str, str] = {}

    tables = soup.find_all("table")

    status_tables = []
    history_tables = []

    for table in tables:
        first_row = table.find("tr")
        if not first_row:
            continue
        headers = [th.get_text().strip() for th in first_row.find_all(["th", "td"])]
        if _is_status_table(headers):
            status_tables.append(table)
        elif _is_history_table(headers):
            history_tables.append(table)

    for table in history_tables:
        replacements.update(_parse_history_table(table))

    for table in status_tables:
        entries.extend(_parse_status_table(table))

    for entry in entries:
        if entry.model_name in replacements:
            entry.replacement = replacements[entry.model_name]

    return entries
