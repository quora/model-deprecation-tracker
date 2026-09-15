import datetime
from pathlib import Path

import pytest

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


def _status_at(shutdown_date: datetime.date, before_retirement: str) -> str:
    if shutdown_date <= datetime.date.today():
        return "retired"
    return before_retirement


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
    def test_ignores_status_table(self):
        entries = scrape_anthropic(_load_fixture("anthropic.html"))
        assert "claude-opus-4-6" not in _by_name(entries)

    def test_fails_closed_when_only_unconfirmed_status_exists(self):
        html = """<table>
        <tr><th>API Model Name</th><th>Current State</th>
        <th>Deprecated</th><th>Tentative Retirement Date</th></tr>
        <tr><td>claude-example</td><td>Deprecated</td>
        <td>September 1, 2026</td><td>Not before December 1, 2026</td></tr>
        </table>"""
        with pytest.raises(ValueError, match="history tables not found"):
            scrape_anthropic(html)

    def test_fails_closed_for_bare_date_in_tentative_column(self):
        today = datetime.date.today()
        tentative_date = today + datetime.timedelta(days=14)
        html = f"""<table>
        <tr><th>API Model Name</th><th>Current State</th>
        <th>Deprecated</th><th>Tentative Retirement Date</th></tr>
        <tr><td>claude-tentative</td><td>Deprecated</td>
        <td>September 1, 2026</td><td>{tentative_date.isoformat()}</td></tr>
        </table>"""
        with pytest.raises(ValueError, match="history tables not found"):
            scrape_anthropic(html)

    def test_fails_closed_for_unparseable_confirmed_date(self):
        html = """<h3>2026-09-01: Claude example</h3><table>
        <tr><th>Retirement Date</th><th>Deprecated Model</th>
        <th>Recommended Replacement</th></tr>
        <tr><td>date pending</td><td>claude-example</td><td>claude-new</td></tr>
        </table>"""
        with pytest.raises(
            ValueError, match="Could not parse Anthropic retirement date"
        ):
            scrape_anthropic(html)

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
            status=_status_at(datetime.date(2026, 4, 20), "deprecated"),
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
            status=_status_at(datetime.date(2026, 8, 23), "deprecated"),
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
            status=_status_at(datetime.date(2026, 7, 5), "deprecated"),
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
            status=_status_at(datetime.date(2026, 6, 19), "legacy"),
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
            status=_status_at(datetime.date(2026, 3, 1), "legacy"),
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
            status=_status_at(datetime.date(2026, 6, 17), "deprecated"),
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
