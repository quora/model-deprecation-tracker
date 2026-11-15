import datetime

import orjson
import pytest

import main as main_module
from main import _preserve_confirmed_history, _validate_anthropic_history
from scraper import ALL_SCRAPERS
from scraper.base import DeprecationEntry


def _anthropic(model_name: str) -> DeprecationEntry:
    return DeprecationEntry(
        provider="Anthropic",
        model_name=model_name,
        shutdown_date=datetime.date(2026, 10, 1),
        status="deprecated",
    )


def test_allows_new_confirmed_anthropic_models():
    previous = [_anthropic("claude-existing")]
    current = [_anthropic("claude-existing"), _anthropic("claude-new")]
    _validate_anthropic_history(current, previous)


def test_rejects_silent_partial_anthropic_history_loss():
    previous = [_anthropic("claude-one"), _anthropic("claude-two")]
    current = [_anthropic("claude-one")]

    with pytest.raises(ValueError, match="dropped models: claude-two"):
        _validate_anthropic_history(current, previous)


@pytest.mark.parametrize("provider", ["Bedrock", "Vertex AI"])
def test_preserves_confirmed_provider_history(provider):
    previous = [
        DeprecationEntry(
            provider=provider,
            model_name="removed-model",
            model_id="provider.removed-model",
            shutdown_date=datetime.date(2025, 8, 1),
            status="retired",
        )
    ]

    assert _preserve_confirmed_history([], previous) == previous


def test_does_not_restore_superseded_provider_record():
    previous = [
        DeprecationEntry(
            provider="Bedrock",
            model_name="same model",
            model_id="openai.same-model",
            shutdown_date=datetime.date(2026, 8, 1),
        )
    ]
    current = [
        DeprecationEntry(
            provider="Bedrock",
            model_name="renamed model",
            model_id="openai.same-model",
            shutdown_date=datetime.date(2026, 9, 1),
        )
    ]

    assert _preserve_confirmed_history(current, previous) == current


PROVIDERS = [name for name, _scrape in ALL_SCRAPERS]


def _redirect_outputs(tmp_path, monkeypatch):
    """Point main() at a temporary folder so no test touches the repository's data."""
    data_dir = tmp_path / "data"
    data_file = data_dir / "deprecations.json"
    monkeypatch.setattr(main_module, "DATA_DIR", data_dir)
    monkeypatch.setattr(main_module, "DEPRECATIONS_FILE", data_file)
    monkeypatch.setattr(main_module, "README_PATH", tmp_path / "README.md")
    monkeypatch.setattr(main_module, "ICS_PATH", tmp_path / "deprecations.ics")
    monkeypatch.delenv("SLACK_WEBHOOK_URL", raising=False)


def _entry(provider: str) -> DeprecationEntry:
    return DeprecationEntry(
        provider=provider,
        model_name=f"{provider} model",
        shutdown_date=datetime.date(2099, 1, 1),
        status="deprecated",
    )


def _stub_scrapers(monkeypatch, empty_providers=()):
    stubs = []
    for name in PROVIDERS:
        entries = [] if name in empty_providers else [_entry(name)]
        stubs.append((name, lambda entries=entries: entries))
    monkeypatch.setattr(main_module, "ALL_SCRAPERS", stubs)


def test_main_writes_all_outputs_when_scrapers_return_entries(tmp_path, monkeypatch):
    _redirect_outputs(tmp_path, monkeypatch)
    _stub_scrapers(monkeypatch)

    main_module.main()

    written = orjson.loads((tmp_path / "data" / "deprecations.json").read_bytes())
    assert {row["provider"] for row in written} == set(PROVIDERS)
    assert (tmp_path / "README.md").exists()
    assert (tmp_path / "deprecations.ics").exists()


@pytest.mark.parametrize("provider", PROVIDERS)
def test_main_fails_before_writing_when_a_scraper_returns_nothing(
    provider, tmp_path, monkeypatch
):
    _redirect_outputs(tmp_path, monkeypatch)
    data_file = tmp_path / "data" / "deprecations.json"
    data_file.parent.mkdir()
    previous = DeprecationEntry(
        provider=provider,
        model_name="previous model",
        shutdown_date=datetime.date(2025, 8, 1),
        status="retired",
    )
    data_file.write_bytes(orjson.dumps([previous.to_dict()]))
    previous_bytes = data_file.read_bytes()
    (tmp_path / "README.md").write_text("previous readme\n")
    _stub_scrapers(monkeypatch, empty_providers={provider})

    with pytest.raises(ValueError, match=f"no entries for: {provider}"):
        main_module.main()

    assert data_file.read_bytes() == previous_bytes
    assert (tmp_path / "README.md").read_text() == "previous readme\n"
    assert not (tmp_path / "deprecations.ics").exists()


def test_main_names_every_provider_that_returned_nothing(tmp_path, monkeypatch):
    _redirect_outputs(tmp_path, monkeypatch)
    _stub_scrapers(monkeypatch, empty_providers={"Bedrock", "Gemini"})

    with pytest.raises(ValueError, match="no entries for: Bedrock, Gemini"):
        main_module.main()

    assert list(tmp_path.iterdir()) == []
