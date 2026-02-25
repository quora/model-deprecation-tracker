import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models"

DEPRECATED_AS_OF_RE = re.compile(r"deprecated\s+as\s+of\s+(.+?)(?:\.|,|$)", re.IGNORECASE)
SHUTDOWN_ON_RE = re.compile(r"shutdown\s+(?:on|date[:\s]+)\s*(.+?)(?:\.|,|$)", re.IGNORECASE)
DISCONTINUE_RE = re.compile(r"discontinue[ds]?\s+(?:on|as\s+of)\s+(.+?)(?:\.|,|$)", re.IGNORECASE)
MODEL_ID_RE = re.compile(r"`([^`]+)`")


def _parse_date_safe(text: str) -> datetime.date:
    text = text.strip().rstrip(".")
    if not text:
        return UNKNOWN_DATE
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _extract_dates_from_text(text: str) -> tuple[datetime.date, datetime.date]:
    deprecated_date = UNKNOWN_DATE
    shutdown_date = UNKNOWN_DATE

    match = DEPRECATED_AS_OF_RE.search(text)
    if match:
        deprecated_date = _parse_date_safe(match.group(1))

    match = SHUTDOWN_ON_RE.search(text)
    if match:
        shutdown_date = _parse_date_safe(match.group(1))

    if shutdown_date == UNKNOWN_DATE:
        match = DISCONTINUE_RE.search(text)
        if match:
            shutdown_date = _parse_date_safe(match.group(1))

    return deprecated_date, shutdown_date


def _parse_sections(soup: BeautifulSoup) -> list[DeprecationEntry]:
    entries: list[DeprecationEntry] = []

    for section in soup.find_all(["section", "div", "article"]):
        heading = section.find(["h2", "h3", "h4"])
        if not heading:
            continue

        section_text = section.get_text()
        heading_text = heading.get_text().strip()

        if "deprecat" not in section_text.lower() and "shutdown" not in section_text.lower():
            continue

        model_id = heading_text
        code_in_heading = heading.find("code")
        if code_in_heading:
            model_id = code_in_heading.get_text().strip()

        deprecated_date, shutdown_date = _extract_dates_from_text(section_text)

        if deprecated_date == UNKNOWN_DATE and shutdown_date == UNKNOWN_DATE:
            continue

        status = "deprecated"
        if shutdown_date != UNKNOWN_DATE and shutdown_date <= datetime.date.today():
            status = "retired"

        entries.append(
            DeprecationEntry(
                provider="Vertex AI",
                model_name=heading_text,
                model_id=model_id,
                deprecated_date=deprecated_date,
                shutdown_date=shutdown_date,
                status=status,
            )
        )

    return entries


def _parse_tables(soup: BeautifulSoup) -> list[DeprecationEntry]:
    entries: list[DeprecationEntry] = []

    for table in soup.find_all("table"):
        rows = table.find_all("tr")
        if not rows:
            continue

        headers = [th.get_text().strip().lower() for th in rows[0].find_all(["th", "td"])]

        model_idx = -1
        deprecation_idx = -1
        shutdown_idx = -1

        for i, h in enumerate(headers):
            if "model" in h and model_idx == -1:
                model_idx = i
            elif "deprecat" in h:
                deprecation_idx = i
            elif "shutdown" in h or "end of life" in h or "eol" in h or "discontinu" in h:
                shutdown_idx = i

        if model_idx == -1:
            continue

        for row in rows[1:]:
            cells = row.find_all(["td", "th"])
            if len(cells) <= model_idx:
                continue

            cell_texts = [c.get_text().strip() for c in cells]
            model_name = cell_texts[model_idx]
            if not model_name:
                continue

            deprecated_date = UNKNOWN_DATE
            if deprecation_idx >= 0 and deprecation_idx < len(cell_texts):
                deprecated_date = _parse_date_safe(cell_texts[deprecation_idx])

            shutdown_date = UNKNOWN_DATE
            if shutdown_idx >= 0 and shutdown_idx < len(cell_texts):
                shutdown_date = _parse_date_safe(cell_texts[shutdown_idx])

            status = "deprecated"
            if shutdown_date != UNKNOWN_DATE and shutdown_date <= datetime.date.today():
                status = "retired"

            entries.append(
                DeprecationEntry(
                    provider="Vertex AI",
                    model_name=model_name,
                    deprecated_date=deprecated_date,
                    shutdown_date=shutdown_date,
                    status=status,
                )
            )

    return entries


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    soup = BeautifulSoup(html, "html.parser")

    entries = _parse_tables(soup)
    if not entries:
        entries = _parse_sections(soup)

    seen: set[str] = set()
    deduplicated: list[DeprecationEntry] = []
    for entry in entries:
        key = (entry.model_name, entry.model_id)
        if key not in seen:
            seen.add(key)
            deduplicated.append(entry)

    return deduplicated
