import os
from pathlib import Path

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


def main() -> None:
    all_entries: list[DeprecationEntry] = []

    for _name, scrape_fn in ALL_SCRAPERS:
        entries = scrape_fn()
        all_entries.extend(entries)

    DATA_DIR.mkdir(parents=True, exist_ok=True)
    serialized = [entry.to_dict() for entry in all_entries]
    DEPRECATIONS_FILE.write_bytes(
        orjson.dumps(serialized, option=orjson.OPT_INDENT_2)
    )

    update_readme(str(README_PATH), all_entries)
    write_ics(all_entries, str(ICS_PATH))

    slack_webhook = os.environ.get("SLACK_WEBHOOK_URL", "")
    if slack_webhook:
        send_notification(all_entries, slack_webhook)


main()
