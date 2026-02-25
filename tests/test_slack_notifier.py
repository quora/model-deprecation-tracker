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
            model_name="soon-model",
            shutdown_date=today + datetime.timedelta(days=3),
            replacement="new-model",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Anthropic",
            model_name="later-model",
            shutdown_date=today + datetime.timedelta(days=30),
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Gemini",
            model_name="past-model",
            shutdown_date=today - datetime.timedelta(days=5),
            status="retired",
        ),
        DeprecationEntry(
            provider="Bedrock",
            model_name="no-date-model",
            status="active",
        ),
    ]


class TestFindUpcomingDeprecations:
    def test_finds_only_within_window(self):
        upcoming = find_upcoming_deprecations(_make_entries(), days=7)
        assert len(upcoming) == 1
        assert upcoming[0].model_name == "soon-model"

    def test_wider_window_includes_more(self):
        upcoming = find_upcoming_deprecations(_make_entries(), days=31)
        names = {e.model_name for e in upcoming}
        assert names == {"soon-model", "later-model"}

    def test_empty_when_no_matches(self):
        upcoming = find_upcoming_deprecations(_make_entries(), days=1)
        assert upcoming == []


class TestFormatSlackMessage:
    def test_message_structure(self):
        entries = [_make_entries()[0]]
        payload = format_slack_message(entries)
        blocks = payload["blocks"]
        assert blocks[0]["type"] == "header"
        assert blocks[1]["type"] == "section"
        text = blocks[1]["text"]["text"]
        expected_parts = ["OpenAI", "soon-model", "new-model"]
        for part in expected_parts:
            assert part in text, f"Expected {part!r} in Slack message text"


class TestSendNotification:
    def test_sends_when_upcoming_exists(self):
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(_make_entries(), "https://hooks.slack.com/test")
            mock_post.assert_called_once()

    def test_skips_when_no_upcoming(self):
        entries = [_make_entries()[1]]
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(entries, "https://hooks.slack.com/test")
            mock_post.assert_not_called()
