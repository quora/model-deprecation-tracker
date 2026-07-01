import datetime
import re

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule"

# IDs (or partial IDs) of h3 headings whose tables we want to scrape.
# "azure-openai" covers the main Azure OpenAI table.
# "anthropic" (no suffix) covers the Foundry-partners Anthropic table.
TARGET_SECTION_IDS = {"azure-openai", "anthropic"}

# Map lifecycle strings from the page to internal status values.
LIFECYCLE_STATUS_MAP = {
    "ga": "active",
    "preview": "active",
    "deprecated": "deprecated",
    "retired": "retired",
    "legacy": "deprecated",
}


def _is_empty_value(text: str) -> bool:
    """Return True when a cell represents a missing/unknown value.

    Handles:
    - Empty string / whitespace-only
    - ASCII hyphen '-' and Unicode dashes (en dash U+2013, em dash U+2014, U+2015)
    - Garbled UTF-8 artefacts: the em dash bytes \xe2\x80\x94 mis-decoded as
      Latin-1 produce 'â' (\xe2) followed by control characters (\x80, \x94);
      after stripping non-printable ASCII only 'â' (or nothing) remains.
    """
    if not text:
        return True
    # Remove dashes and whitespace
    stripped = re.sub(r"[\s\-\u2013\u2014\u2015]+", "", text)
    # Remove non-printable / non-ASCII characters (catches encoding artefacts)
    stripped = re.sub(r"[^\x20-\x7e]", "", stripped)
    return not stripped


def _parse_date_safe(text: str) -> datetime.date:
    text = text.strip()
    if _is_empty_value(text):
        return UNKNOWN_DATE
    # Strip footnote-number suffixes added by the page after <sup> tags, e.g.
    # "2026-10-141" where "1" is a stray superscript digit. Such digits appear
    # directly after the last digit of the year (no separator), so we remove a
    # trailing single digit only when it would make the string look like a valid
    # date without it. We do this by removing a trailing digit that is preceded
    # by another digit (i.e. "20261" -> "2026") — a simple heuristic that avoids
    # corrupting actual numeric versions like "001".
    text = re.sub(r"(?<=\d{4})\d$", "", text).strip()
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _cell_text(cell) -> str:
    """Return the text of a cell, removing any <sup> footnote elements first."""
    for sup in cell.find_all("sup"):
        sup.decompose()
    return " ".join(cell.get_text().split())


def _find_col(headers: list[str], *keywords) -> int:
    """Return the index of the first header that contains any of the keywords."""
    for i, h in enumerate(headers):
        h_lower = h.lower()
        if any(kw in h_lower for kw in keywords):
            return i
    return -1


def _parse_standard_table(
    table, provider: str, section_label: str
) -> list[DeprecationEntry]:
    """
    Parse tables with columns: Model | Version | Lifecycle | Retirement date | Replacement
    """
    rows = table.find_all("tr")
    if not rows:
        return []

    headers = [_cell_text(th) for th in rows[0].find_all(["th", "td"])]
    model_idx = _find_col(headers, "model")
    version_idx = _find_col(headers, "version")
    lifecycle_idx = _find_col(headers, "lifecycle")
    retirement_idx = _find_col(headers, "retirement")
    replacement_idx = _find_col(headers, "replacement")

    if model_idx == -1:
        return []

    entries: list[DeprecationEntry] = []

    for row in rows[1:]:
        cells = row.find_all(["td", "th"])
        if len(cells) <= model_idx:
            continue

        cell_texts = [_cell_text(c) for c in cells]

        model = cell_texts[model_idx] if model_idx < len(cell_texts) else ""
        if not model:
            continue

        version = ""
        if version_idx >= 0 and version_idx < len(cell_texts):
            v = cell_texts[version_idx]
            if not _is_empty_value(v):
                version = v

        model_name = f"{model} ({version})" if version else model

        raw_lifecycle = ""
        if lifecycle_idx >= 0 and lifecycle_idx < len(cell_texts):
            raw_lifecycle = cell_texts[lifecycle_idx].strip()

        status = LIFECYCLE_STATUS_MAP.get(raw_lifecycle.lower(), "active")
        if status == "retired" and raw_lifecycle.lower() == "deprecated":
            status = "deprecated"

        shutdown_date = UNKNOWN_DATE
        if retirement_idx >= 0 and retirement_idx < len(cell_texts):
            shutdown_date = _parse_date_safe(cell_texts[retirement_idx])

        # Treat entries with a past shutdown date as retired
        if shutdown_date != UNKNOWN_DATE and shutdown_date <= datetime.date.today():
            status = "retired"

        replacement = ""
        if replacement_idx >= 0 and replacement_idx < len(cell_texts):
            r = cell_texts[replacement_idx]
            if not _is_empty_value(r):
                replacement = r

        entries.append(
            DeprecationEntry(
                provider=section_label,
                model_name=model_name,
                shutdown_date=shutdown_date,
                replacement=replacement,
                status=status,
            )
        )

    return entries


def _get_section_entries(soup: BeautifulSoup) -> list[DeprecationEntry]:
    """
    Walk all h2/h3/h4 headings and collect entries from tables that immediately
    follow headings whose `id` attribute matches our target section IDs.
    """
    entries: list[DeprecationEntry] = []

    for heading in soup.find_all(["h2", "h3", "h4"]):
        section_id = heading.get("id", "")

        # Only process sections we care about.
        if section_id not in TARGET_SECTION_IDS:
            continue

        # Determine provider label based on the section.
        if section_id == "azure-openai":
            provider_label = "Azure Foundry (OpenAI)"
        elif section_id == "anthropic":
            provider_label = "Azure Foundry (Anthropic)"
        else:
            continue

        # Collect the first <table> sibling that appears immediately before any
        # subsequent heading tag. We stop at ANY heading (h1-h5) to avoid
        # reading tables from sub-sections like the fine-tuned models h4.
        for sibling in heading.next_siblings:
            sib_name = getattr(sibling, "name", None)
            if sib_name in ("h1", "h2", "h3", "h4", "h5", "h6"):
                break
            if sib_name == "table":
                entries.extend(
                    _parse_standard_table(sibling, provider_label, provider_label)
                )

    return entries


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    soup = BeautifulSoup(html, "html.parser")
    return _get_section_entries(soup)
