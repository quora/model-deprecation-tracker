import datetime

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://ai.google.dev/gemini-api/docs/deprecations"


def _parse_date_safe(text: str) -> datetime.date:
    text = text.strip()
    if not text or text == "-" or text == "—" or text.upper() == "N/A":
        return UNKNOWN_DATE
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _parse_table(table: BeautifulSoup) -> list[DeprecationEntry]:
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [th.get_text().strip().lower() for th in rows[0].find_all(["th", "td"])]
    if not headers:
        return []

    model_idx = -1
    release_idx = -1
    shutdown_idx = -1
    replacement_idx = -1

    for i, h in enumerate(headers):
        if "model" in h and model_idx == -1:
            model_idx = i
        elif "release" in h:
            release_idx = i
        elif "shutdown" in h or "cutoff" in h or "sunset" in h:
            shutdown_idx = i
        elif "replacement" in h or "recommended" in h:
            replacement_idx = i

    if model_idx == -1:
        return []

    entries: list[DeprecationEntry] = []

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        cell_texts = [c.get_text().strip() for c in cells]
        if len(cell_texts) <= model_idx:
            continue

        model_name = cell_texts[model_idx]
        if not model_name:
            continue

        shutdown_date = UNKNOWN_DATE
        if shutdown_idx >= 0 and shutdown_idx < len(cell_texts):
            shutdown_date = _parse_date_safe(cell_texts[shutdown_idx])

        replacement = ""
        if replacement_idx >= 0 and replacement_idx < len(cell_texts):
            replacement = cell_texts[replacement_idx].strip()

        status = "active"
        if shutdown_date != UNKNOWN_DATE:
            if shutdown_date <= datetime.date.today():
                status = "retired"
            else:
                status = "deprecated"

        entries.append(
            DeprecationEntry(
                provider="Gemini",
                model_name=model_name,
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
