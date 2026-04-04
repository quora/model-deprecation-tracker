# AI Model Deprecation Tracker

Automatically tracks model deprecation schedules from major AI providers.

## Providers

- **OpenAI** — [Deprecations page](https://developers.openai.com/api/docs/deprecations/)
- **Anthropic** — [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **Vertex AI** — [Partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models)
- **AWS Bedrock** — [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html)
- **Gemini** — [API deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

## Calendar

Download [deprecations.ics](deprecations.ics) and import it into your calendar app to get reminders 7 and 30 days before model shutdowns.

## Deprecation Schedule

<!-- DEPRECATION_TABLE_START -->

*Last updated: 2026-04-04*

### Anthropic

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-opus-4-20250514 |  | active | TBD | 2026-05-14 |  |
| claude-opus-4-1-20250805 |  | active | TBD | 2026-08-05 |  |
| claude-opus-4-5-20251101 |  | active | TBD | 2026-11-24 |  |
| claude-opus-4-6 |  | active | TBD | 2027-02-05 |  |

### Gemini

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| text-embedding-004 |  | retired | TBD | 🔴 2026-01-14 | gemini-embedding-001 |
| gemini-2.5-flash-image-preview |  | retired | TBD | 🔴 2026-01-15 | gemini-2.5-flash-image |
| gemini-2.5-flash-preview-09-25 |  | retired | TBD | 🔴 2026-02-17 | gemini-3-flash-preview |
| imagen-4.0-generate-preview-06-06 |  | retired | TBD | 🔴 2026-02-17 | imagen-4.0-generate-001 |
| imagen-4.0-ultra-generate-preview-06-06 |  | retired | TBD | 🔴 2026-02-17 | imagen-4.0-ultra-generate-001 |
| gemini-3-pro-preview |  | retired | TBD | 🔴 2026-03-09 | gemini-3.1-pro-preview |
| gemini-2.5-flash-lite-preview-09-2025 |  | retired | TBD | 🔴 2026-03-31 | gemini-3.1-flash-lite-preview |
| gemini-2.0-flash |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash |
| gemini-2.0-flash-001 |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash |
| gemini-2.0-flash-lite |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash-lite |
| gemini-2.0-flash-lite-001 |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash-lite |
| gemini-2.5-pro |  | deprecated | TBD | 2026-06-17 | gemini-3.1-pro-preview |
| gemini-2.5-flash |  | deprecated | TBD | 2026-06-17 | gemini-3-flash-preview |
| imagen-4.0-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| imagen-4.0-ultra-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| imagen-4.0-fast-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| gemini-embedding-001 |  | deprecated | TBD | 2026-07-14 |  |
| gemini-2.5-flash-lite |  | deprecated | TBD | 2026-07-22 | gemini-3.1-flash-lite-preview |
| gemini-2.5-flash-image |  | deprecated | TBD | 2026-10-02 | gemini-3.1-flash-image-preview |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| codex-mini-latest |  | deprecated | TBD | 🔴 2026-02-12 | gpt-5-codex-mini |
| chatgpt-4o-latest |  | deprecated | TBD | 🔴 2026-02-17 | gpt-5.1-chat-latest |
| gpt-4-0314 |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-1106-preview |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-0125-preview (including gpt-4-turbo-preview and gpt-4-turbo-preview-completions, which point to this snapshot) |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| OpenAI-Beta: realtime=v1 |  | deprecated | TBD | 2026-05-07 | Realtime API |
| gpt-4o-realtime-preview |  | deprecated | TBD | 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2025-06-03 |  | deprecated | TBD | 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2024-12-17 |  | deprecated | TBD | 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-mini-realtime-preview |  | deprecated | TBD | 2026-05-07 | gpt-realtime-mini |
| gpt-4o-audio-preview |  | deprecated | TBD | 2026-05-07 | gpt-audio-1.5 |
| gpt-4o-mini-audio-preview |  | deprecated | TBD | 2026-05-07 | gpt-audio-mini |
| dall-e-2 |  | deprecated | TBD | 2026-05-12 | gpt-image-1 or gpt-image-1-mini |
| dall-e-3 |  | deprecated | TBD | 2026-05-12 | gpt-image-1 or gpt-image-1-mini |
| Assistants API |  | deprecated | TBD | 2026-08-26 | Responses API and Conversations API |
| Videos API |  | deprecated | TBD | 2026-09-24 | --- |
| sora-2 |  | deprecated | TBD | 2026-09-24 | --- |
| sora-2-pro |  | deprecated | TBD | 2026-09-24 | --- |
| sora-2-2025-10-06 |  | deprecated | TBD | 2026-09-24 | --- |
| sora-2-2025-12-08 |  | deprecated | TBD | 2026-09-24 | --- |
| sora-2-pro-2025-10-06 |  | deprecated | TBD | 2026-09-24 | --- |
| gpt-3.5-turbo-instruct |  | deprecated | TBD | 2026-09-28 | gpt-5.4-mini or gpt-5-mini |
| babbage-002 |  | deprecated | TBD | 2026-09-28 | gpt-5.4-mini or gpt-5-mini |
| davinci-002 |  | deprecated | TBD | 2026-09-28 | gpt-5.4-mini or gpt-5-mini |
| gpt-3.5-turbo-1106 |  | deprecated | TBD | 2026-09-28 | gpt-5.4-mini or gpt-5-mini |

### Vertex AI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Claude 3.5 Sonnet v2 | Claude 3.5 Sonnet v2 | retired | 2026-08-20 | 🔴 2026-02-19 |  |
| Claude 3.5 Sonnet | Claude 3.5 Sonnet | retired | 2026-08-20 | 🔴 2026-02-19 |  |
| Jamba 1.5 Large | Jamba 1.5 Large | retired | 2026-08-27 | 🔴 2026-02-27 |  |
| Jamba 1.5 Mini | Jamba 1.5 Mini | retired | 2026-08-27 | 🔴 2026-02-27 |  |
| Claude 3.7 Sonnet | Claude 3.7 Sonnet | deprecated | 2026-11-11 | 2026-05-11 |  |
| Claude 3.5 Haiku | Claude 3.5 Haiku | deprecated | 2026-01-05 | 2026-07-05 |  |
| Claude 3 Opus | Claude 3 Opus | deprecated | 2026-06-30 | 2026-08-01 |  |
| Anthropic's Claude 3 Haiku | Anthropic's Claude 3 Haiku | deprecated | 2026-02-23 | 2026-08-23 |  |

<!-- DEPRECATION_TABLE_END -->

## Slack Alerts

Set the `SLACK_WEBHOOK_URL` environment variable (or GitHub Actions secret) to receive Slack notifications when a model shutdown is within 7 days. Multiple webhook URLs can be provided as a comma-separated list to notify multiple channels.

## Setup

```bash
pip install -r requirements.txt
python main.py
```

## Adding a New Provider

1. Create `scraper/<provider>_scraper.py` with a `scrape(html: str = "") -> list[DeprecationEntry]` function
2. Add the scraper to `ALL_SCRAPERS` in `scraper/__init__.py`
3. Add a test fixture HTML file in `tests/fixtures/`
4. Add test cases in `tests/test_scrapers.py`
