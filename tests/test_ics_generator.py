import datetime

from scraper.base import DeprecationEntry
from generators.ics_generator import generate_ics


def _make_entries() -> list[DeprecationEntry]:
    return [
        DeprecationEntry(
            provider="OpenAI",
            model_name="gpt-4-0314",
            model_id="gpt-4-0314",
            shutdown_date=datetime.date(2026, 3, 26),
            replacement="gpt-5",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Anthropic",
            model_name="claude-3-haiku",
            shutdown_date=datetime.date(2026, 4, 20),
            replacement="claude-haiku-4-5",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Gemini",
            model_name="no-date-model",
            status="active",
        ),
    ]


class TestGenerateIcs:
    def test_valid_ics_structure(self):
        result = generate_ics(_make_entries())
        expected_substrings = [
            "BEGIN:VCALENDAR",
            "END:VCALENDAR",
            "BEGIN:VEVENT",
            "END:VEVENT",
            "BEGIN:VALARM",
            "END:VALARM",
        ]
        for substr in expected_substrings:
            assert substr in result, f"Expected {substr!r} in ICS output"

    def test_event_summaries(self):
        result = generate_ics(_make_entries())
        expected_summaries = [
            "[OpenAI] Model deprecation: gpt-4-0314",
            "[Anthropic] Model deprecation: claude-3-haiku",
        ]
        for summary in expected_summaries:
            assert summary in result, f"Expected summary {summary!r} in ICS output"

    def test_skips_entries_without_shutdown_date(self):
        result = generate_ics(_make_entries())
        assert "no-date-model" not in result

    def test_includes_replacement_in_description(self):
        result = generate_ics(_make_entries())
        assert "gpt-5" in result
        assert "claude-haiku-4-5" in result

    def test_two_alarms_per_event(self):
        result = generate_ics(_make_entries())
        # 2 events with shutdown dates, each with 2 alarms = 4 VALARM blocks
        assert result.count("BEGIN:VALARM") == 4
