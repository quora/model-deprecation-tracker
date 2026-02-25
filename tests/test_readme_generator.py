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

    def test_unknown_date_shows_tbd(self):
        entries = [
            DeprecationEntry(
                provider="TestProvider",
                model_name="test-model",
                status="active",
            ),
        ]
        assert "TBD" in generate_readme(entries)

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
