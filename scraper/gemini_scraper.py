import datetime
import re
from html import escape

from bs4 import BeautifulSoup
from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://ai.google.dev/gemini-api/docs/deprecations"
# The page moved to AI Studio and renders client-side, so its HTML carries no
# tables. The same tables are published as Markdoc on the markdown alternate.
MARKDOWN_URL = "https://aistudio.google.com/docs/deprecations.md"

MARKDOC_TABLE_RE = re.compile(
    r"\{%\s*table\b[^%]*%\}(.*?)\{%\s*/table\s*%\}", re.DOTALL
)
MARKDOC_ROW_SEPARATOR_RE = re.compile(r"^\s*---\s*$")
MARKDOC_CELL_RE = re.compile(r"^\s*\*(?:\s(.*))?$")
MARKDOWN_LINK_RE = re.compile(r"\[([^\]]*)\]\([^)]*\)")


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

        non_empty_cells = sum(1 for t in cell_texts if t and t != "-")
        if non_empty_cells <= 1:
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


def _markdoc_cell_text(text: str) -> str:
    text = MARKDOWN_LINK_RE.sub(r"\1", text)
    return " ".join(text.replace("`", "").split())


def _markdoc_tables_to_html(markdown: str) -> str:
    """Rewrite Markdoc `{% table %}` blocks as HTML tables for `_parse_table`.

    Rows are separated by `---` lines and each cell is a `*` list item; the
    first row is the header.
    """
    tables: list[str] = []

    for block in MARKDOC_TABLE_RE.findall(markdown):
        rows: list[list[str]] = [[]]
        for line in block.splitlines():
            cell = MARKDOC_CELL_RE.match(line)
            if cell:
                rows[-1].append(_markdoc_cell_text(cell.group(1) or ""))
            elif MARKDOC_ROW_SEPARATOR_RE.match(line):
                rows.append([])
            elif line.strip() and rows[-1]:
                rows[-1][-1] = _markdoc_cell_text(f"{rows[-1][-1]} {line}")

        html_rows = []
        for i, row in enumerate(r for r in rows if r):
            tag = "th" if i == 0 else "td"
            cells = "".join(f"<{tag}>{escape(text)}</{tag}>" for text in row)
            html_rows.append(f"<tr>{cells}</tr>")
        tables.append(f"<table>{''.join(html_rows)}</table>")

    return "".join(tables)


def _parse_html_tables(html: str) -> list[DeprecationEntry]:
    soup = BeautifulSoup(html, "html.parser")
    entries: list[DeprecationEntry] = []

    for table in soup.find_all("table"):
        entries.extend(_parse_table(table))

    return entries


def scrape(html: str = "", markdown: str = "") -> list[DeprecationEntry]:
    fetched = not html and not markdown
    if fetched:
        html = fetch_page(URL)

    entries = _parse_html_tables(html)
    if fetched and not entries:
        markdown = fetch_page(MARKDOWN_URL)
    if markdown:
        entries.extend(_parse_html_tables(_markdoc_tables_to_html(markdown)))

    return entries
