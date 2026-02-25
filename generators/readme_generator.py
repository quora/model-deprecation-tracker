import datetime
from itertools import groupby
from pathlib import Path

from scraper.base import UNKNOWN_DATE, DeprecationEntry

MARKER_START = "<!-- DEPRECATION_TABLE_START -->"
MARKER_END = "<!-- DEPRECATION_TABLE_END -->"

RETENTION_DAYS = 90
WARN_DAYS = 30


def _sort_key(entry: DeprecationEntry) -> tuple[int, datetime.date]:
    if entry.has_shutdown_date():
        return (0, entry.shutdown_date)
    return (1, UNKNOWN_DATE)


def _should_include(entry: DeprecationEntry, today: datetime.date) -> bool:
    if not entry.has_shutdown_date():
        return False
    cutoff = today - datetime.timedelta(days=RETENTION_DAYS)
    return entry.shutdown_date >= cutoff


def _format_date(d: datetime.date) -> str:
    if d == UNKNOWN_DATE:
        return "TBD"
    return d.isoformat()


def _format_shutdown(d: datetime.date, today: datetime.date) -> str:
    if d == UNKNOWN_DATE:
        return "TBD"
    date_str = d.isoformat()
    if d <= today:
        return f"\U0001f534 {date_str}"
    if (d - today).days <= WARN_DAYS:
        return f"\U0001f7e1 {date_str}"
    return date_str


def generate_readme(entries: list[DeprecationEntry]) -> str:
    today = datetime.date.today()
    relevant = [e for e in entries if _should_include(e, today)]
    relevant.sort(key=lambda e: e.provider)

    lines: list[str] = []
    lines.append(MARKER_START)
    lines.append("")
    lines.append(f"*Last updated: {today.isoformat()}*")
    lines.append("")

    for provider, group in groupby(relevant, key=lambda e: e.provider):
        group_entries = sorted(group, key=_sort_key)
        lines.append(f"### {provider}")
        lines.append("")
        lines.append("| Model | Model ID | Status | Deprecated | Shutdown | Replacement |")
        lines.append("|-------|----------|--------|------------|----------|-------------|")

        for entry in group_entries:
            model = " ".join(entry.model_name.split())
            model_id = entry.model_id
            status = entry.status
            deprecated = _format_date(entry.deprecated_date)
            shutdown = _format_shutdown(entry.shutdown_date, today)
            replacement = " ".join(entry.replacement.split())
            lines.append(
                f"| {model} | {model_id} | {status} | {deprecated} | {shutdown} | {replacement} |"
            )

        lines.append("")

    lines.append(MARKER_END)
    return "\n".join(lines)


def update_readme(readme_path: str, entries: list[DeprecationEntry]) -> None:
    path = Path(readme_path)
    content = path.read_text() if path.exists() else ""
    new_table = generate_readme(entries)

    start_idx = content.find(MARKER_START)
    end_idx = content.find(MARKER_END)

    if start_idx != -1 and end_idx != -1:
        end_idx += len(MARKER_END)
        content = content[:start_idx] + new_table + content[end_idx:]
    else:
        if content and not content.endswith("\n"):
            content += "\n"
        content += "\n" + new_table + "\n"

    path.write_text(content)
