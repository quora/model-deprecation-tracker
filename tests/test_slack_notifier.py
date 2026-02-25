import datetime
from unittest.mock import patch

from scraper.base import DeprecationEntry
from generators.slack_notifier import (
    find_upcoming_deprecations,
    format_slack_message,
    send_notification,
)


def _make_entries() -> list[DeprecationEntry]:
    today = datetime.date.today()
    return [
        DeprecationEntry(
            provider="OpenAI",
            model_name="seven-day-model",
            shutdown_date=today + datetime.timedelta(days=7),
            replacement="new-model",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Anthropic",
            model_name="one-day-model",
            shutdown_date=today + datetime.timedelta(days=1),
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Gemini",
            model_name="today-model",
            shutdown_date=today,
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Bedrock",
            model_name="three-day-model",
            shutdown_date=today + datetime.timedelta(days=3),
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Bedrock",
            model_name="no-date-model",
            status="active",
        ),
    ]


class TestFindUpcomingDeprecations:
    def test_notifies_at_7_and_1_days(self):
        upcoming = find_upcoming_deprecations(_make_entries())
        names = {e.model_name for e in upcoming}
        assert names == {"seven-day-model", "one-day-model"}

    def test_skips_non_matching_days(self):
        upcoming = find_upcoming_deprecations(_make_entries())
        names = {e.model_name for e in upcoming}
        assert "three-day-model" not in names

    def test_custom_notify_days(self):
        upcoming = find_upcoming_deprecations(_make_entries(), notify_at_days={3})
        assert len(upcoming) == 1
        assert upcoming[0].model_name == "three-day-model"


class TestFormatSlackMessage:
    def test_message_structure(self):
        entries = [_make_entries()[0]]
        payload = format_slack_message(entries)
        blocks = payload["blocks"]
        assert blocks[0]["type"] == "header"
        assert blocks[1]["type"] == "section"
        text = blocks[1]["text"]["text"]
        expected_parts = ["OpenAI", "seven-day-model", "new-model"]
        for part in expected_parts:
            assert part in text, f"Expected {part!r} in Slack message text"


class TestSendNotification:
    def test_sends_when_upcoming_exists(self):
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(_make_entries(), "https://hooks.slack.com/test")
            mock_post.assert_called_once()

    def test_skips_when_no_upcoming(self):
        entries = [_make_entries()[3]]
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(entries, "https://hooks.slack.com/test")
            mock_post.assert_not_called()
