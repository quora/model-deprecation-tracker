import datetime

import requests

from scraper.base import DeprecationEntry


def find_upcoming_deprecations(
    entries: list[DeprecationEntry], days: int = 7
) -> list[DeprecationEntry]:
    today = datetime.date.today()
    cutoff = today + datetime.timedelta(days=days)
    return [
        e
        for e in entries
        if e.has_shutdown_date() and today <= e.shutdown_date <= cutoff
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

    return {"blocks": blocks}


def send_notification(
    entries: list[DeprecationEntry], webhook_url: str
) -> None:
    upcoming = find_upcoming_deprecations(entries)
    if not upcoming:
        return

    payload = format_slack_message(upcoming)
    requests.post(webhook_url, json=payload, timeout=10)
