import datetime
from pathlib import Path

from scraper.base import UNKNOWN_DATE, DeprecationEntry
from scraper.openai_scraper import scrape as scrape_openai
from scraper.anthropic_scraper import scrape as scrape_anthropic
from scraper.vertex_scraper import scrape as scrape_vertex
from scraper.bedrock_scraper import scrape as scrape_bedrock
from scraper.gemini_scraper import scrape as scrape_gemini

FIXTURES_DIR = Path(__file__).parent / "fixtures"


def _load_fixture(name: str) -> str:
    return (FIXTURES_DIR / name).read_text()


def _by_name(entries: list[DeprecationEntry]) -> dict[str, DeprecationEntry]:
    return {e.model_name: e for e in entries}


class TestOpenAIScraper:
    def test_parses_all_entries(self):
        entries = scrape_openai(_load_fixture("openai.html"))
        assert len(entries) == 4
        assert [e.model_name for e in entries] == [
            "chatgpt-4o-latest",
            "gpt-4-0314",
            "gpt-3.5-turbo-instruct",
            "gpt-4-vision-preview",
        ]

    def test_three_column_entry_with_non_breaking_hyphens(self):
        entries = scrape_openai(_load_fixture("openai.html"))
        entry = _by_name(entries)["chatgpt-4o-latest"]
        assert entry == DeprecationEntry(
            provider="OpenAI",
            model_name="chatgpt-4o-latest",
            shutdown_date=datetime.date(2026, 2, 17),
            replacement="gpt-5.1-chat-latest",
            status="deprecated",
        )

    def test_four_column_entry(self):
        entries = scrape_openai(_load_fixture("openai.html"))
        entry = _by_name(entries)["gpt-4-vision-preview"]
        assert entry == DeprecationEntry(
            provider="OpenAI",
            model_name="gpt-4-vision-preview",
            shutdown_date=datetime.date(2024, 6, 6),
            replacement="gpt-4o",
            status="deprecated",
        )


class TestAnthropicScraper:
    def test_parses_active_model(self):
        entries = scrape_anthropic(_load_fixture("anthropic.html"))
        entry = _by_name(entries)["claude-opus-4-6"]
        assert entry == DeprecationEntry(
            provider="Anthropic",
            model_name="claude-opus-4-6",
            shutdown_date=datetime.date(2027, 2, 5),
            status="active",
        )

    def test_parses_retired_model_with_replacement(self):
        entries = scrape_anthropic(_load_fixture("anthropic.html"))
        entry = _by_name(entries)["claude-3-7-sonnet-20250219"]
        assert entry == DeprecationEntry(
            provider="Anthropic",
            model_name="claude-3-7-sonnet-20250219",
            deprecated_date=datetime.date(2025, 10, 28),
            shutdown_date=datetime.date(2026, 2, 19),
            replacement="claude-opus-4-6",
            status="retired",
        )

    def test_parses_deprecated_model_with_replacement(self):
        entries = scrape_anthropic(_load_fixture("anthropic.html"))
        entry = _by_name(entries)["claude-3-haiku-20240307"]
        assert entry == DeprecationEntry(
            provider="Anthropic",
            model_name="claude-3-haiku-20240307",
            deprecated_date=datetime.date(2026, 2, 19),
            shutdown_date=datetime.date(2026, 4, 20),
            replacement="claude-haiku-4-5-20251001",
            status="deprecated",
        )


class TestVertexScraper:
    def test_parses_all_entries(self):
        entries = scrape_vertex(_load_fixture("vertex.html"))
        assert len(entries) == 3
        assert {e.model_name for e in entries} == {
            "claude-3-haiku",
            "claude-3-5-haiku",
            "claude-3-7-sonnet",
        }

    def test_parses_entry_dates(self):
        entries = scrape_vertex(_load_fixture("vertex.html"))
        entry = _by_name(entries)["claude-3-haiku"]
        assert entry == DeprecationEntry(
            provider="Vertex AI",
            model_name="claude-3-haiku",
            deprecated_date=datetime.date(2026, 2, 23),
            shutdown_date=datetime.date(2026, 8, 23),
            status="deprecated",
        )


class TestBedrockScraper:
    def test_parses_legacy_entry(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        haiku = _by_name(entries)["Claude 3.5 Haiku"]
        assert haiku == DeprecationEntry(
            provider="Bedrock",
            model_name="Claude 3.5 Haiku",
            deprecated_date=datetime.date(2025, 12, 19),
            shutdown_date=datetime.date(2026, 6, 19),
            replacement="Claude Haiku 4.5 / anthropic.claude-haiku-4-5-20251001-v1:0",
            status="legacy",
        )

    def test_parses_eol_entry(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        v2 = _by_name(entries)["Claude v2"]
        assert v2 == DeprecationEntry(
            provider="Bedrock",
            model_name="Claude v2",
            deprecated_date=datetime.date(2025, 1, 21),
            shutdown_date=datetime.date(2025, 7, 21),
            replacement="Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0",
            status="retired",
        )

    def test_total_count(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        assert len(entries) == 3


class TestGeminiScraper:
    def test_parses_all_entries(self):
        entries = scrape_gemini(_load_fixture("gemini.html"))
        assert len(entries) == 5

    def test_parses_entry_with_future_shutdown(self):
        entries = scrape_gemini(_load_fixture("gemini.html"))
        pro = _by_name(entries)["gemini-2.5-pro"]
        assert pro == DeprecationEntry(
            provider="Gemini",
            model_name="gemini-2.5-pro",
            shutdown_date=datetime.date(2026, 6, 17),
            replacement="gemini-3-pro-preview",
            status="deprecated",
        )

    def test_retired_entry(self):
        entries = scrape_gemini(_load_fixture("gemini.html"))
        embedding = _by_name(entries)["embedding-001"]
        assert embedding == DeprecationEntry(
            provider="Gemini",
            model_name="embedding-001",
            shutdown_date=datetime.date(2025, 10, 30),
            replacement="gemini-embedding-001",
            status="retired",
        )
