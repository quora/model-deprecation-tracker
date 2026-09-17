import datetime
from pathlib import Path

import pytest

from scraper.base import UNKNOWN_DATE, DeprecationEntry
from scraper.openai_scraper import scrape as scrape_openai
from scraper.anthropic_scraper import scrape as scrape_anthropic
from scraper.vertex_scraper import scrape as scrape_vertex
from scraper.bedrock_scraper import (
    _deduplicate,
    _find_tracked_model_card_urls,
    _parse_model_card,
    scrape as scrape_bedrock,
)
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

    def test_splits_snapshot_and_aliases_into_separate_entries(self):
        html = """<table>
        <tr><th>Shutdown date</th><th>Model snapshot</th><th>Substitute model</th></tr>
        <tr><td>October 23, 2026</td><td>
        <code>gpt-3.5-turbo-0125</code> | <code>gpt-3.5-turbo</code>,
        <code>gpt-3.5-turbo-completions</code></td><td><code>gpt-5.6-terra</code></td></tr>
        <tr><td>October 23, 2026</td><td>
        <code>gpt-4-0613</code> | <code>gpt-4</code>,
        <code>gpt-4-0613-completions</code>, <code>gpt-4-completions</code></td>
        <td><code>gpt-5.6-sol</code></td></tr>
        </table>"""
        entries = scrape_openai(html)

        assert [entry.model_name for entry in entries] == [
            "gpt-3.5-turbo-0125",
            "gpt-3.5-turbo",
            "gpt-3.5-turbo-completions",
            "gpt-4-0613",
            "gpt-4",
            "gpt-4-0613-completions",
            "gpt-4-completions",
        ]
        assert {entry.shutdown_date for entry in entries} == {
            datetime.date(2026, 10, 23)
        }
        assert {entry.replacement for entry in entries[:3]} == {"gpt-5.6-terra"}
        assert {entry.replacement for entry in entries[3:]} == {"gpt-5.6-sol"}

    def test_preserves_qualified_single_model_description(self):
        html = """<table>
        <tr><th>Shutdown date</th><th>Model / system</th><th>Substitute</th></tr>
        <tr><td>October 28, 2024</td>
        <td>New fine-tuning training on <code>babbage-002</code></td>
        <td><code>gpt-4o-mini</code></td></tr>
        </table>"""

        assert scrape_openai(html) == [
            DeprecationEntry(
                provider="OpenAI",
                model_name="New fine-tuning training on babbage-002",
                shutdown_date=datetime.date(2024, 10, 28),
                replacement="gpt-4o-mini",
                status="deprecated",
            )
        ]

    def test_splits_comma_separated_model_identifiers(self):
        html = """<table>
        <tr><th>Shutdown date</th><th>Model snapshot</th><th>Substitute</th></tr>
        <tr><td>October 23, 2026</td>
        <td><code>model-a</code>, <code>model-b</code></td>
        <td><code>replacement</code></td></tr>
        </table>"""

        assert [entry.model_name for entry in scrape_openai(html)] == [
            "model-a",
            "model-b",
        ]

    def test_splits_explicit_snapshot_alias_prose(self):
        html = """<table>
        <tr><th>Shutdown date</th><th>Model snapshot</th><th>Substitute</th></tr>
        <tr><td>March 26, 2026</td><td><code>gpt-4-0125-preview</code> (including
        <code>gpt-4-turbo-preview</code> and <code>gpt-4-turbo-preview-completions</code>,
        which point to this snapshot)</td>
        <td><code>gpt-5 or gpt-4.1*</code></td></tr>
        </table>"""

        assert [entry.model_name for entry in scrape_openai(html)] == [
            "gpt-4-0125-preview",
            "gpt-4-turbo-preview",
            "gpt-4-turbo-preview-completions",
        ]


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

    def test_preserves_explicit_year_after_comma(self):
        html = """<html><body>
        <div><h3>Claude 3 Opus</h3>
        <p>Claude 3 Opus was deprecated as of February 14, 2025 and was
        shut down on August 1, 2025.</p></div>
        </body></html>"""
        entries = scrape_vertex(html)
        assert len(entries) == 1
        assert entries[0].deprecated_date == datetime.date(2025, 2, 14)
        assert entries[0].shutdown_date == datetime.date(2025, 8, 1)

    def test_does_not_infer_year_for_incomplete_shutdown_date(self):
        html = """<html><body>
        <div><h3>Example model</h3>
        <p>Example model will be shut down on August 1.</p></div>
        </body></html>"""
        assert scrape_vertex(html) == []


class TestBedrockScraper:
    def test_parses_legacy_entry(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        opus = _by_name(entries)["Claude Opus 4.1"]
        assert opus == DeprecationEntry(
            provider="Bedrock",
            model_name="Claude Opus 4.1",
            model_id="anthropic.claude-opus-4-1-20250805-v1:0",
            deprecated_date=datetime.date(2026, 7, 8),
            shutdown_date=datetime.date(2027, 1, 8),
            status=_status_at(datetime.date(2027, 1, 8), "legacy"),
        )

    def test_ignores_non_shutdown_lifecycle_dates(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        gemma = _by_name(entries)["Gemma example"]
        assert gemma.deprecated_date == datetime.date(2026, 8, 1)
        assert gemma.shutdown_date == UNKNOWN_DATE

    def test_deduplicates_rowspan_entries(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        sonnet = _by_name(entries)["Claude Sonnet 4"]
        assert sonnet == DeprecationEntry(
            provider="Bedrock",
            model_name="Claude Sonnet 4",
            model_id="anthropic.claude-sonnet-4-20250514-v1:0",
            deprecated_date=datetime.date(2026, 4, 14),
            shutdown_date=datetime.date(2026, 10, 14),
            status=_status_at(datetime.date(2026, 10, 14), "legacy"),
        )

    def test_preserves_distinct_model_ids_with_same_name(self):
        html = """<table>
        <tr><th>Model provider</th><th>Model name</th><th>Model ID</th>
        <th>Legacy date</th><th>EOL date</th></tr>
        <tr><td>OpenAI</td><td>GPT Same</td><td>openai.gpt-v1</td>
        <td>January 1, 2027</td><td>July 1, 2027</td></tr>
        <tr><td>OpenAI</td><td>GPT Same</td><td>openai.gpt-v2</td>
        <td>February 1, 2027</td><td>August 1, 2027</td></tr>
        </table>"""
        entries = scrape_bedrock(html)
        assert {entry.model_id for entry in entries} == {
            "openai.gpt-v1",
            "openai.gpt-v2",
        }

    def test_only_tracks_requested_model_providers(self):
        entries = scrape_bedrock(_load_fixture("bedrock.html"))
        assert "Nova Canvas" not in _by_name(entries)
        assert "Command R+" not in _by_name(entries)

    def test_tracks_openai_model_with_confirmed_eol(self):
        html = """<table>
        <tr><th>Model provider</th><th>Model name</th><th>Model ID</th>
        <th>Legacy date</th><th>EOL date</th>
        <th>Public extended access start date</th></tr>
        <tr><td>OpenAI</td><td>GPT example</td><td>openai.gpt-example</td>
        <td>January 1, 2027</td><td>July 1, 2027</td>
        <td>April 1, 2027</td></tr>
        </table>"""
        entry = scrape_bedrock(html)[0]
        assert entry.model_id == "openai.gpt-example"
        assert entry.shutdown_date == datetime.date(2027, 7, 1)

    def test_does_not_substitute_other_lifecycle_dates_for_missing_eol(self):
        html = """<table>
        <tr><th>Model provider</th><th>Model name</th><th>Model ID</th>
        <th>Legacy date</th><th>EOL date</th>
        <th>Public extended access start date</th></tr>
        <tr><td>Google</td><td>Gemma example</td><td>google.gemma-example</td>
        <td>January 1, 2027</td><td>N/A</td><td>April 1, 2027</td></tr>
        </table>"""
        entry = scrape_bedrock(html)[0]
        assert entry.deprecated_date == datetime.date(2027, 1, 1)
        assert entry.shutdown_date == UNKNOWN_DATE

    def test_rejects_qualifier_in_eol_header(self):
        html = """<table>
        <tr><th>Model provider</th><th>Model name</th><th>Model ID</th>
        <th>Legacy date</th><th>EOL date (no sooner than)</th></tr>
        <tr><td>OpenAI</td><td>GPT example</td><td>openai.gpt-example</td>
        <td>January 1, 2027</td><td>July 1, 2027</td></tr>
        </table>"""
        assert scrape_bedrock(html)[0].shutdown_date == UNKNOWN_DATE

    def test_parses_only_explicit_model_card_eol(self):
        confirmed = """<html><h1>GPT example</h1>
        <p><b>EOL no sooner than:</b> January 1, 2027</p>
        <p><b>Model EOL date:</b> July 1, 2027</p>
        <table><tr><th>Endpoint</th><th>Model ID</th></tr>
        <tr><td>bedrock-runtime</td><td>openai.gpt-example</td></tr></table></html>"""
        unconfirmed = confirmed.replace("July 1, 2027", "N/A")

        entry = _parse_model_card(confirmed)
        assert entry is not None
        assert entry.shutdown_date == datetime.date(2027, 7, 1)
        assert _parse_model_card(unconfirmed) is None

    def test_model_cards_skip_placeholder_ids_without_colliding(self):
        card_template = """<html><h1>{name}</h1>
        <p><b>Model EOL date:</b> {eol}</p>
        <table><tr><th>Endpoint</th><th>Model ID</th></tr>
        <tr><td>bedrock-runtime</td><td>N/A</td></tr>
        <tr><td>bedrock-mantle</td><td>{model_id}</td></tr></table></html>"""
        first = _parse_model_card(
            card_template.format(
                name="Claude First",
                eol="July 1, 2027",
                model_id="anthropic.claude-first",
            )
        )
        second = _parse_model_card(
            card_template.format(
                name="Claude Second",
                eol="August 1, 2027",
                model_id="anthropic.claude-second",
            )
        )

        assert first is not None and second is not None
        assert first.model_id == "anthropic.claude-first"
        assert second.model_id == "anthropic.claude-second"
        assert len(_deduplicate([first, second])) == 2

    def test_model_card_index_only_returns_tracked_providers(self):
        html = """<table>
        <tr><th>Logo</th><th>Provider</th><th>Supported models</th></tr>
        <tr><td></td><td>OpenAI</td><td><a href="openai.html">GPT</a></td></tr>
        <tr><td></td><td>Cohere</td><td><a href="cohere.html">Command</a></td></tr>
        </table>"""
        assert _find_tracked_model_card_urls(html) == [
            "https://docs.aws.amazon.com/bedrock/latest/userguide/openai.html"
        ]

    def test_fails_closed_when_eol_table_disappears(self):
        with pytest.raises(ValueError, match="Bedrock EOL table not found"):
            scrape_bedrock("<html><body><p>No lifecycle table</p></body></html>")

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
