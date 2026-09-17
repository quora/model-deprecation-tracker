import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://developers.openai.com/api/docs/deprecations/"

NON_BREAKING_HYPHEN = "\u2011"


def _normalize_text(text: str) -> str:
    return text.replace(NON_BREAKING_HYPHEN, "-").strip()


def _parse_date_safe(text: str) -> datetime.date:
    text = _normalize_text(text)
    if not text or text == "-":
        return UNKNOWN_DATE
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _extract_model_names(cell: BeautifulSoup) -> list[str]:
    model_name = _normalize_text(cell.get_text())
    code_tags = cell.find_all("code")
    code_names = [_normalize_text(code.get_text()) for code in code_tags]
    separator_text = "".join(
        str(text)
        for text in cell.find_all(string=True)
        if text.find_parent("code") is None
    )
    is_separator_list = not re.sub(r"[\s|,]+", "", separator_text)
    is_snapshot_alias_group = (
        "including" in model_name.lower()
        and "which point to this snapshot" in model_name.lower()
    )
    if len(code_names) > 1 and (is_separator_list or is_snapshot_alias_group):
        return list(dict.fromkeys(name for name in code_names if name))

    return [model_name] if model_name else []


def _parse_table(table: BeautifulSoup) -> list[DeprecationEntry]:
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [_normalize_text(th.get_text()) for th in rows[0].find_all(["th", "td"])]
    num_cols = len(headers)
    entries = []

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) < num_cols:
            continue

        cell_texts = [_normalize_text(cell.get_text()) for cell in cells]

        if num_cols == 3:
            shutdown_text, replacement = cell_texts[0], cell_texts[2]
        elif num_cols >= 4:
            shutdown_text = cell_texts[0]
            replacement = cell_texts[-1]
        else:
            continue

        for model_name in _extract_model_names(cells[1]):
            entries.append(
                DeprecationEntry(
                    provider="OpenAI",
                    model_name=model_name,
                    shutdown_date=_parse_date_safe(shutdown_text),
                    replacement=replacement,
                    status="deprecated",
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
