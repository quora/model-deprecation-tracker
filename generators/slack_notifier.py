import datetime
import logging

import requests

log = logging.getLogger(__name__)

from scraper.base import DeprecationEntry

NOTIFY_AT_DAYS = {14, 1}
DEPRECATION_NOTIFY_AT_DAYS = {0}


def find_upcoming_deprecations(
    entries: list[DeprecationEntry], notify_at_days: set[int] = NOTIFY_AT_DAYS
) -> list[DeprecationEntry]:
    today = datetime.date.today()
    return [
        e
        for e in entries
        if e.has_shutdown_date() and (e.shutdown_date - today).days in notify_at_days
    ]


def find_new_deprecations(
    entries: list[DeprecationEntry],
    notify_at_days: set[int] = DEPRECATION_NOTIFY_AT_DAYS,
) -> list[DeprecationEntry]:
    today = datetime.date.today()
    return [
        e
        for e in entries
        if e.has_deprecated_date() and (e.deprecated_date - today).days in notify_at_days
    ]


def find_notifiable_deprecations(entries: list[DeprecationEntry]) -> list[DeprecationEntry]:
    seen: set[tuple[str, str, str]] = set()
    notifiable: list[DeprecationEntry] = []

    for entry in find_new_deprecations(entries) + find_upcoming_deprecations(entries):
        key = (entry.provider, entry.model_name, entry.model_id)
        if key in seen:
            continue
        seen.add(key)
        notifiable.append(entry)

    return notifiable


def format_slack_message(entries: list[DeprecationEntry]) -> dict:
    blocks: list[dict] = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Model Deprecation Alerts",
            },
        },
    ]

    for entry in entries:
        today = datetime.date.today()
        text = f"*{entry.provider}* - {entry.model_name}"
        if entry.model_id:
            text += f" (`{entry.model_id}`)"
        if entry.has_deprecated_date():
            text += f"\nDeprecated: {entry.deprecated_date.isoformat()}"
        if entry.has_shutdown_date():
            days_until = (entry.shutdown_date - today).days
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
    lines = ["Model Deprecation Alerts"]
    for entry in entries:
        today = datetime.date.today()
        line = f"{entry.provider} - {entry.model_name}"
        if entry.model_id:
            line += f" ({entry.model_id})"
        if entry.has_deprecated_date():
            line += f" | Deprecated: {entry.deprecated_date.isoformat()}"
        if entry.has_shutdown_date():
            days_until = (entry.shutdown_date - today).days
            line += f" | Shutdown: {entry.shutdown_date.isoformat()} ({days_until} days)"
        if entry.replacement:
            line += f" | Replacement: {entry.replacement}"
        lines.append(line)

    return {"text": "\n".join(lines), "blocks": blocks}


def send_notification(entries: list[DeprecationEntry], webhook_urls: list[str]) -> None:
    """Send Slack notifications for deprecations at configured day thresholds."""
    notifiable = find_notifiable_deprecations(entries)
    if not notifiable:
        return

    payload = format_slack_message(notifiable)
    log.info("Sending Slack notification:\n%s", payload)
    for url in webhook_urls:
        requests.post(url, json=payload, timeout=10)
