import datetime
import re

from dateutil.parser import parse as parse_date

from scraper.base import UNKNOWN_DATE, DeprecationEntry, fetch_page

URL = "https://docs.fireworks.ai/updates/changelog.md"

UPDATE_RE = re.compile(
    r"<Update\s+label=[\"'](?P<label>[^\"']+)[\"']\s*>(?P<body>.*?)</Update>",
    re.DOTALL | re.IGNORECASE,
)
HEADING_RE = re.compile(r"^\s*#\s+(?P<title>.+)$", re.MULTILINE)
DEPRECATION_RE = re.compile(
    r"\b(deprecat(?:e|ed|ion)|decommission(?:ed)?|retir(?:e|ed)|sunset|removed)\b",
    re.IGNORECASE,
)
MIGRATION_RE = re.compile(r"^\s*[*-]\s+(?P<model>.+?)\s+-\s*migrate\s+to\s+(?P<replacement>.+)$", re.IGNORECASE)
DEPRECATED_SENTENCE_RE = re.compile(
    r"(?P<models>.+?)\s+(?:is|are)\s+deprecated\b(?P<rest>.*)",
    re.IGNORECASE,
)
MIGRATE_TO_RE = re.compile(r"\bmigrate\s+to\s+(?P<replacement>.+)$", re.IGNORECASE)
APP_MODEL_RE = re.compile(r"https://app\.fireworks\.ai/models/(?P<model_id>[^)\s]+)")

MONTH_DATE = (
    r"(?:Jan(?:uary)?|Feb(?:ruary)?|Mar(?:ch)?|Apr(?:il)?|May|Jun(?:e)?|"
    r"Jul(?:y)?|Aug(?:ust)?|Sep(?:tember)?|Oct(?:ober)?|Nov(?:ember)?|Dec(?:ember)?)"
    r"\s+\d{1,2},\s+\d{4}"
)
ISO_DATE = r"\d{4}-\d{2}-\d{2}"
DATE_RE = rf"(?:{MONTH_DATE}|{ISO_DATE})"
SHUTDOWN_DATE_PATTERNS = [
    re.compile(
        rf"\b(?:decommissioned|removed|shut\s*down|shutdown|retired|sunset)\b"
        rf".{{0,80}}?\b(?:on|after|before)?\s*({DATE_RE})",
        re.IGNORECASE,
    ),
    re.compile(
        rf"\bno\s+longer\s+be\s+available\b.{{0,80}}?\b(?:on|after)?\s*({DATE_RE})",
        re.IGNORECASE,
    ),
]


def _parse_date_safe(text: str) -> datetime.date:
    text = _clean_markdown(text)
    if not text:
        return UNKNOWN_DATE
    try:
        return parse_date(text, fuzzy=True).date()
    except (ValueError, OverflowError):
        return UNKNOWN_DATE


def _clean_markdown(text: str) -> str:
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = text.replace("**", "").replace("__", "").replace("`", "")
    text = text.replace("\u2014", "-").replace("\u2013", "-")
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip().strip("*").strip()


def _extract_model_id(markdown: str) -> str:
    match = APP_MODEL_RE.search(markdown)
    return match.group("model_id") if match else ""


def _title_from_update(body: str) -> str:
    match = HEADING_RE.search(body)
    if not match:
        return ""
    return _clean_markdown(match.group("title"))


def _extract_shutdown_date(title: str, body: str) -> datetime.date:
    text = _clean_markdown(f"{title}\n{body}")
    for pattern in SHUTDOWN_DATE_PATTERNS:
        match = pattern.search(text)
        if match:
            return _parse_date_safe(match.group(1))
    return UNKNOWN_DATE


def _split_model_names(text: str) -> list[str]:
    text = text.replace(", and ", ", ")
    text = re.sub(r"\s+and\s+", ", ", text)
    return [part.strip(" .") for part in text.split(",") if part.strip(" .")]


def _status_for(shutdown_date: datetime.date) -> str:
    if shutdown_date != UNKNOWN_DATE and shutdown_date <= datetime.date.today():
        return "retired"
    return "deprecated"


def _entry(
    model_name: str,
    deprecated_date: datetime.date,
    shutdown_date: datetime.date,
    replacement: str = "",
    model_id: str = "",
) -> DeprecationEntry:
    return DeprecationEntry(
        provider="Fireworks",
        model_name=model_name,
        model_id=model_id,
        deprecated_date=deprecated_date,
        shutdown_date=shutdown_date,
        replacement=replacement,
        status=_status_for(shutdown_date),
    )


def _parse_migration_line(
    line: str, deprecated_date: datetime.date, shutdown_date: datetime.date
) -> DeprecationEntry | None:
    normalized = line.replace("\u2014", "-").replace("\u2013", "-")
    match = MIGRATION_RE.match(normalized)
    if not match:
        return None

    model_part = match.group("model")
    replacement_part = match.group("replacement")
    model_name = _clean_markdown(model_part)
    if not model_name:
        return None

    return _entry(
        model_name=model_name,
        model_id=_extract_model_id(model_part),
        deprecated_date=deprecated_date,
        shutdown_date=shutdown_date,
        replacement=_clean_markdown(replacement_part).rstrip("."),
    )


def _parse_deprecated_sentence(
    line: str, deprecated_date: datetime.date, shutdown_date: datetime.date
) -> list[DeprecationEntry]:
    if "**" not in line and "[" not in line:
        return []

    clean_line = _clean_markdown(line)
    match = DEPRECATED_SENTENCE_RE.search(clean_line)
    if not match:
        return []

    replacement = ""
    replacement_match = MIGRATE_TO_RE.search(clean_line)
    if replacement_match:
        replacement = _clean_markdown(replacement_match.group("replacement")).rstrip(".")

    return [
        _entry(
            model_name=model_name,
            deprecated_date=deprecated_date,
            shutdown_date=shutdown_date,
            replacement=replacement,
        )
        for model_name in _split_model_names(match.group("models"))
    ]


def _deduplicate(entries: list[DeprecationEntry]) -> list[DeprecationEntry]:
    by_model: dict[str, DeprecationEntry] = {}
    for entry in entries:
        key = entry.model_name.lower()
        existing = by_model.get(key)
        if existing is None:
            by_model[key] = entry
            continue

        if not existing.model_id and entry.model_id:
            existing.model_id = entry.model_id
        if not existing.replacement and entry.replacement:
            existing.replacement = entry.replacement
        if not existing.has_shutdown_date() and entry.has_shutdown_date():
            existing.shutdown_date = entry.shutdown_date
            existing.status = entry.status

    return list(by_model.values())


def _parse_update(label: str, body: str) -> list[DeprecationEntry]:
    title = _title_from_update(body)
    if not DEPRECATION_RE.search(_clean_markdown(f"{title}\n{body}")):
        return []

    deprecated_date = _parse_date_safe(label)
    shutdown_date = _extract_shutdown_date(title, body)

    entries: list[DeprecationEntry] = []
    for line in body.splitlines():
        migration_entry = _parse_migration_line(line, deprecated_date, shutdown_date)
        if migration_entry:
            entries.append(migration_entry)
            continue
        entries.extend(_parse_deprecated_sentence(line, deprecated_date, shutdown_date))

    return _deduplicate(entries)


def scrape(html: str = "") -> list[DeprecationEntry]:
    if not html:
        html = fetch_page(URL)

    entries: list[DeprecationEntry] = []
    for match in UPDATE_RE.finditer(html):
        entries.extend(_parse_update(match.group("label"), match.group("body")))

    return entries
