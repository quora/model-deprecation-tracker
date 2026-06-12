import datetime
from pathlib import Path

from scraper.base import UNKNOWN_DATE, DeprecationEntry
from scraper.openai_scraper import scrape as scrape_openai
from scraper.anthropic_scraper import scrape as scrape_anthropic
from scraper.vertex_scraper import scrape as scrape_vertex
from scraper.bedrock_scraper import scrape as scrape_bedrock
from scraper.gemini_scraper import scrape as scrape_gemini
from scraper.azure_foundry_scraper import scrape as scrape_azure_foundry

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

    def test_parses_section_based_format(self):
        html = """<html><body>
        <div><h3>Claude 3.5 Haiku</h3>
        <p>Claude 3.5 Haiku is deprecated as of January 5, 2026 and will be
        shut down on July 5, 2026. Claude 3.5 Haiku is available to existing
        customers only.</p></div>
        </body></html>"""
        entries = scrape_vertex(html)
        assert len(entries) == 1
        assert entries[0] == DeprecationEntry(
            provider="Vertex AI",
            model_name="Claude 3.5 Haiku",
            model_id="Claude 3.5 Haiku",
            deprecated_date=datetime.date(2026, 1, 5),
            shutdown_date=datetime.date(2026, 7, 5),
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

    def test_deduplicates_rowspan_entries_keeping_earliest_shutdown(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        sonnet = _by_name(entries)["Claude 3.5 Sonnet v1"]
        assert sonnet == DeprecationEntry(
            provider="Bedrock",
            model_name="Claude 3.5 Sonnet v1",
            deprecated_date=datetime.date(2025, 8, 25),
            shutdown_date=datetime.date(2026, 3, 1),
            replacement="Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0",
            status="legacy",
        )

    def test_total_count(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        assert len(entries) == 4


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


from scraper.azure_foundry_scraper import _is_empty_value


class TestIsEmptyValue:
    """Unit tests for the _is_empty_value() helper that guards against encoding artefacts."""

    def test_empty_string(self):
        assert _is_empty_value("") is True

    def test_whitespace_only(self):
        assert _is_empty_value("   ") is True

    def test_ascii_hyphen(self):
        assert _is_empty_value("-") is True

    def test_em_dash_unicode(self):
        assert _is_empty_value("\u2014") is True  # U+2014 em dash

    def test_en_dash_unicode(self):
        assert _is_empty_value("\u2013") is True  # U+2013 en dash

    def test_garbled_em_dash_artefact(self):
        # UTF-8 em dash bytes (E2 80 94) mis-decoded as Latin-1 → 'â' + ctrl chars
        garbled = "\xe2\x80\x94"  # raw Latin-1 bytes
        assert _is_empty_value(garbled) is True

    def test_real_value_not_empty(self):
        assert _is_empty_value("claude-haiku-4-5") is False

    def test_real_date_not_empty(self):
        assert _is_empty_value("2026-10-19") is False

    def test_real_version_not_empty(self):
        assert _is_empty_value("2025-04-14") is False


class TestAzureFoundryScraper:
    def test_only_openai_and_anthropic_sections_are_scraped(self):
        """The Cohere section (and any other non-target section) must be ignored."""
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        providers = {e.provider for e in entries}
        assert providers == {"Azure Foundry (OpenAI)", "Azure Foundry (Anthropic)"}

    def test_fine_tuned_models_table_is_excluded(self):
        """The fine-tuned models table (different headers) must not produce entries."""
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        # Fine-tuned rows have version '2024-08-06'; if the table were parsed they
        # would appear as 'gpt-4o (2024-08-06)' — verify they are absent.
        fine_tuned_model_names = {
            e.model_name for e in entries if "2024-08-06" in e.model_name
        }
        assert fine_tuned_model_names == set()

    def test_parses_openai_deprecated_model(self):
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        entry = _by_name(entries)["gpt-4o (2024-05-13)"]
        assert entry == DeprecationEntry(
            provider="Azure Foundry (OpenAI)",
            model_name="gpt-4o (2024-05-13)",
            shutdown_date=datetime.date(2026, 10, 1),
            replacement="gpt-5.1",
            status="deprecated",
        )

    def test_parses_openai_active_model_no_replacement(self):
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        entry = _by_name(entries)["gpt-5 (2025-08-07)"]
        assert entry == DeprecationEntry(
            provider="Azure Foundry (OpenAI)",
            model_name="gpt-5 (2025-08-07)",
            shutdown_date=datetime.date(2027, 2, 6),
            replacement="",
            status="active",
        )

    def test_past_retirement_date_becomes_retired(self):
        """An entry whose retirement date is in the past must have status='retired'."""
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        entry = _by_name(entries)["o1 (2024-12-17)"]
        assert entry.status == "retired"
        assert entry.shutdown_date == datetime.date(2025, 1, 1)

    def test_parses_openai_model_with_replacement(self):
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        entry = _by_name(entries)["gpt-4o-mini (2024-07-18)"]
        assert entry.replacement == "gpt-4.1-mini"
        assert entry.provider == "Azure Foundry (OpenAI)"

    def test_parses_anthropic_models(self):
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        anthropic_entries = [
            e for e in entries if e.provider == "Azure Foundry (Anthropic)"
        ]
        assert len(anthropic_entries) == 3
        names = {e.model_name for e in anthropic_entries}
        assert names == {"claude-haiku-4-5", "claude-sonnet-4-5", "claude-opus-4-1"}

    def test_anthropic_model_has_correct_date_and_provider(self):
        entries = scrape_azure_foundry(_load_fixture("azure_foundry.html"))
        entry = _by_name(entries)["claude-haiku-4-5"]
        assert entry == DeprecationEntry(
            provider="Azure Foundry (Anthropic)",
            model_name="claude-haiku-4-5",
            shutdown_date=datetime.date(2026, 10, 19),
            replacement="",
            status="active",
        )
