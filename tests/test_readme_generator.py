import datetime

from scraper.base import DeprecationEntry
from generators.readme_generator import generate_readme, MARKER_START, MARKER_END


def _make_entries() -> list[DeprecationEntry]:
    return [
        DeprecationEntry(
            provider="OpenAI",
            model_name="gpt-4-0314",
            shutdown_date=datetime.date(2026, 3, 26),
            replacement="gpt-5",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="Anthropic",
            model_name="claude-3-haiku",
            deprecated_date=datetime.date(2026, 2, 19),
            shutdown_date=datetime.date(2026, 4, 20),
            replacement="claude-haiku-4-5",
            status="deprecated",
        ),
        DeprecationEntry(
            provider="OpenAI",
            model_name="gpt-3.5-turbo",
            shutdown_date=datetime.date(2026, 9, 28),
            status="deprecated",
        ),
    ]


class TestGenerateReadme:
    def test_output_structure(self):
        result = generate_readme(_make_entries())
        expected_substrings = [
            MARKER_START,
            MARKER_END,
            "### Anthropic",
            "### OpenAI",
            datetime.date.today().isoformat(),
            "gpt-4-0314",
            "claude-3-haiku",
            "gpt-5",
            "claude-haiku-4-5",
        ]
        for substr in expected_substrings:
            assert substr in result, f"Expected {substr!r} in output"

    def test_sorts_by_shutdown_date_within_provider(self):
        result = generate_readme(_make_entries())
        openai_section = result.split("### OpenAI")[1].split("###")[0]
        assert openai_section.index("gpt-4-0314") < openai_section.index("gpt-3.5-turbo")

    def test_excludes_entries_without_shutdown_date(self):
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="no-shutdown-model",
                status="active",
            ),
        ]
        assert "no-shutdown-model" not in generate_readme(entries)

    def test_excludes_old_entries(self):
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="very-old-model",
                shutdown_date=datetime.date(2020, 1, 1),
                status="retired",
            ),
        ]
        assert "very-old-model" not in generate_readme(entries)

    def test_red_indicator_for_past_dates(self):
        today = datetime.date.today()
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="past-model",
                shutdown_date=today - datetime.timedelta(days=5),
                status="retired",
            ),
        ]
        result = generate_readme(entries)
        assert "\U0001f534" in result

    def test_yellow_indicator_for_upcoming_dates(self):
        today = datetime.date.today()
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="soon-model",
                shutdown_date=today + datetime.timedelta(days=10),
                status="deprecated",
            ),
        ]
        result = generate_readme(entries)
        assert "\U0001f7e1" in result

    def test_no_indicator_for_distant_dates(self):
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="distant-model",
                shutdown_date=datetime.date(2027, 6, 1),
                status="deprecated",
            ),
        ]
        result = generate_readme(entries)
        assert "\U0001f534" not in result
        assert "\U0001f7e1" not in result
