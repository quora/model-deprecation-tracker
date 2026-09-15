import datetime

import pytest

from main import _validate_anthropic_history
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
