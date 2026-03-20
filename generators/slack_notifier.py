import datetime
import logging

import requests

log = logging.getLogger(__name__)

from scraper.base import DeprecationEntry


NOTIFY_AT_DAYS = {7, 1}


def find_upcoming_deprecations(
    entries: list[DeprecationEntry], notify_at_days: set[int] = NOTIFY_AT_DAYS
) -> list[DeprecationEntry]:
    today = datetime.date.today()
    return [
        e
        for e in entries
        if e.has_shutdown_date() and (e.shutdown_date - today).days in notify_at_days
    ]


def format_slack_message(entries: list[DeprecationEntry]) -> dict:
    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Upcoming Model Deprecations",
            },
        },
    ]

    for entry in entries:
        days_until = (entry.shutdown_date - datetime.date.today()).days
        text = f"*{entry.provider}* - {entry.model_name}"
        if entry.model_id:
            text += f" (`{entry.model_id}`)"
        text += f"\nShutdown: {entry.shutdown_date.isoformat()} ({days_until} days)"
        if entry.replacement:
            text += f"\nReplacement: {entry.replacement}"

        blocks.append(
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": text,
                },
            }
        )

    # Build plain-text fallback for Slack event ingestion
    lines = ["Upcoming Model Deprecations"]
    for entry in entries:
        days_until = (entry.shutdown_date - datetime.date.today()).days
        line = f"{entry.provider} - {entry.model_name}"
        if entry.model_id:
            line += f" ({entry.model_id})"
        line += f" | Shutdown: {entry.shutdown_date.isoformat()} ({days_until} days)"
        if entry.replacement:
            line += f" | Replacement: {entry.replacement}"
        lines.append(line)

    return {"text": "\n".join(lines), "blocks": blocks}


def send_notification(
    entries: list[DeprecationEntry], webhook_urls: list[str]
) -> None:
    upcoming = find_upcoming_deprecations(entries)
    if not upcoming:
        return

    payload = format_slack_message(upcoming)
    log.info("Sending Slack notification:\n%s", payload)
    for url in webhook_urls:
        requests.post(url, json=payload, timeout=10)
