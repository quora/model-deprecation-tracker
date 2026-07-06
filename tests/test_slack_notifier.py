import datetime
from unittest.mock import patch

from generators.slack_notifier import (
    find_new_deprecations,
    find_notifiable_deprecations,
    find_upcoming_deprecations,
    format_slack_message,
    send_notification,
)
from scraper.base import DeprecationEntry


def _make_entries() -> list[DeprecationEntry]:
    today = datetime.date.today()
    return [
        DeprecationEntry(
            provider="OpenAI",
            model_name="fourteen-day-model",
            shutdown_date=today + datetime.timedelta(days=14),
            replacement="new-model",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="OpenAI",
            model_name="seven-day-model",
            shutdown_date=today + datetime.timedelta(days=7),
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
    def test_notifies_at_14_and_1_days(self):
        upcoming = find_upcoming_deprecations(_make_entries())
        names = {e.model_name for e in upcoming}
        assert names == {"fourteen-day-model", "one-day-model"}

    def test_skips_non_matching_days(self):
        upcoming = find_upcoming_deprecations(_make_entries())
        names = {e.model_name for e in upcoming}
        assert "seven-day-model" not in names
        assert "three-day-model" not in names

    def test_custom_notify_days(self):
        upcoming = find_upcoming_deprecations(_make_entries(), notify_at_days={3})
        assert len(upcoming) == 1
        assert upcoming[0].model_name == "three-day-model"


class TestFindNewDeprecations:
    def test_notifies_on_deprecation_date(self):
        today = datetime.date.today()
        entries = [
            DeprecationEntry(
                provider="Fireworks",
                model_name="newly-deprecated-model",
                deprecated_date=today,
                status="deprecated",
            ),
            DeprecationEntry(
                provider="Fireworks",
                model_name="old-deprecated-model",
                deprecated_date=today - datetime.timedelta(days=1),
                status="deprecated",
            ),
        ]
        announced = find_new_deprecations(entries)
        assert [e.model_name for e in announced] == ["newly-deprecated-model"]

    def test_combines_new_and_upcoming_without_duplicates(self):
        today = datetime.date.today()
        entry = DeprecationEntry(
            provider="Fireworks",
            model_name="same-entry",
            deprecated_date=today,
            shutdown_date=today + datetime.timedelta(days=14),
            status="deprecated",
        )
        notifiable = find_notifiable_deprecations([entry])
        assert notifiable == [entry]


class TestFormatSlackMessage:
    def test_message_structure(self):
        entries = [_make_entries()[0]]
        payload = format_slack_message(entries)
        blocks = payload["blocks"]
        assert blocks[0]["type"] == "header"
        assert blocks[1]["type"] == "section"
        assert blocks[1]["text"]["type"] == "mrkdwn"

    def test_formats_deprecation_without_shutdown_date(self):
        today = datetime.date.today()
        payload = format_slack_message(
            [
                DeprecationEntry(
                    provider="Fireworks",
                    model_name="newly-deprecated-model",
                    deprecated_date=today,
                    replacement="replacement-model",
                    status="deprecated",
                )
            ]
        )
        assert f"Deprecated: {today.isoformat()}" in payload["text"]
        assert "Shutdown:" not in payload["text"]


class TestSendNotification:
    def test_sends_when_upcoming_exists(self):
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(_make_entries(), ["https://hooks.slack.com/test"])
            mock_post.assert_called_once()

    def test_sends_to_multiple_webhooks(self):
        urls = [
            "https://hooks.slack.com/first",
            "https://hooks.slack.com/second",
        ]
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(_make_entries(), urls)
            assert mock_post.call_count == 2
            called_urls = [call.args[0] for call in mock_post.call_args_list]
            assert called_urls == urls

    def test_skips_when_no_upcoming(self):
        entries = [_make_entries()[3]]
        with patch("generators.slack_notifier.requests.post") as mock_post:
            send_notification(entries, ["https://hooks.slack.com/test"])
            mock_post.assert_not_called()
