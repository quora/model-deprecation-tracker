import datetime

import pytest

from main import _preserve_confirmed_history, _validate_anthropic_history
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
