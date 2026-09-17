import logging
import os
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

import orjson

from generators.ics_generator import write_ics
from generators.readme_generator import update_readme
from generators.slack_notifier import send_notification
from scraper import ALL_SCRAPERS
from scraper.base import DeprecationEntry

PROJECT_DIR = Path(__file__).parent
DATA_DIR = PROJECT_DIR / "data"
DEPRECATIONS_FILE = DATA_DIR / "deprecations.json"
README_PATH = PROJECT_DIR / "README.md"
ICS_PATH = PROJECT_DIR / "deprecations.ics"
HISTORY_PRESERVED_PROVIDERS = {"Bedrock", "Vertex AI"}


def _load_previous_entries() -> list[DeprecationEntry]:
    if not DEPRECATIONS_FILE.exists():
        return []
    return [
        DeprecationEntry.from_dict(item)
        for item in orjson.loads(DEPRECATIONS_FILE.read_bytes())
    ]


def _validate_anthropic_history(
    entries: list[DeprecationEntry], previous_entries: list[DeprecationEntry]
) -> None:
    previous_models = {
        entry.model_name
        for entry in previous_entries
        if entry.provider == "Anthropic" and entry.has_shutdown_date()
    }
    current_models = {
        entry.model_name
        for entry in entries
        if entry.provider == "Anthropic" and entry.has_shutdown_date()
    }
    missing_models = previous_models - current_models
    if missing_models:
        missing = ", ".join(sorted(missing_models))
        raise ValueError(f"Anthropic deprecation history dropped models: {missing}")


def _entry_identity(entry: DeprecationEntry) -> tuple[str, str]:
    return entry.provider, entry.model_id or entry.model_name.casefold()


def _preserve_confirmed_history(
    entries: list[DeprecationEntry], previous_entries: list[DeprecationEntry]
) -> list[DeprecationEntry]:
    """Keep confirmed records after source pages remove completed shutdowns."""
    identities = {_entry_identity(entry) for entry in entries}
    preserved = list(entries)
    for entry in previous_entries:
        identity = _entry_identity(entry)
        if (
            entry.provider in HISTORY_PRESERVED_PROVIDERS
            and entry.has_shutdown_date()
            and identity not in identities
        ):
            preserved.append(entry)
            identities.add(identity)
    return preserved


def main() -> None:
    previous_entries = _load_previous_entries()
    all_entries: list[DeprecationEntry] = []

    for _name, scrape_fn in ALL_SCRAPERS:
        entries = scrape_fn()
        all_entries.extend(entries)

    all_entries = _preserve_confirmed_history(all_entries, previous_entries)
    _validate_anthropic_history(all_entries, previous_entries)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    serialized = [entry.to_dict() for entry in all_entries]
    DEPRECATIONS_FILE.write_bytes(orjson.dumps(serialized, option=orjson.OPT_INDENT_2))

    update_readme(str(README_PATH), all_entries)
    write_ics(all_entries, str(ICS_PATH))

    slack_webhooks = [
        url.strip()
        for url in os.environ.get("SLACK_WEBHOOK_URL", "").split(",")
        if url.strip()
    ]
    if slack_webhooks:
        send_notification(all_entries, slack_webhooks)


if __name__ == "__main__":
    main()
