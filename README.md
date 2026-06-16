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

*Last updated: 2026-06-16*

### Anthropic

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-opus-4-20250514 |  | retired | 2026-04-14 | 🔴 2026-06-15 | claude-opus-4-8 |
| claude-opus-4-1-20250805 |  | deprecated | 2026-06-05 | 2026-08-05 | claude-opus-4-8 |
| claude-opus-4-5-20251101 |  | active | TBD | 2026-11-24 |  |
| claude-opus-4-6 |  | active | TBD | 2027-02-05 |  |
| claude-opus-4-7 |  | active | TBD | 2027-04-16 |  |
| claude-opus-4-8 |  | active | TBD | 2027-05-28 |  |

### Gemini

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gemini-2.5-flash-lite-preview-09-2025 |  | retired | TBD | 🔴 2026-03-31 | gemini-3.1-flash-lite |
| gemini-robotics-er-1.5-preview |  | retired | TBD | 🔴 2026-04-30 | gemini-robotics-er-1.6-preview |
| gemini-3.1-flash-lite-preview |  | retired | TBD | 🔴 2026-05-25 | gemini-3.1-flash-lite |
| gemini-2.0-flash |  | retired | TBD | 🔴 2026-06-01 | gemini-3.5-flash |
| gemini-2.0-flash-001 |  | retired | TBD | 🔴 2026-06-01 | gemini-3.5-flash |
| gemini-2.0-flash-lite |  | retired | TBD | 🔴 2026-06-01 | gemini-3.1-flash-lite |
| gemini-2.0-flash-lite-001 |  | retired | TBD | 🔴 2026-06-01 | gemini-3.1-flash-lite |
| gemini-3.1-flash-image-preview |  | deprecated | TBD | 🟡 2026-06-25 | gemini-3.1-flash-image |
| gemini-3-pro-image-preview |  | deprecated | TBD | 🟡 2026-06-25 | gemini-3-pro-image |
| veo-3.0-generate-001 |  | deprecated | TBD | 🟡 2026-06-30 | veo-3.1-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| veo-3.0-fast-generate-001 |  | deprecated | TBD | 🟡 2026-06-30 | veo-3.1-fast-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| veo-2.0-generate-001 |  | deprecated | TBD | 🟡 2026-06-30 | veo-3.1-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| gemini-embedding-001 |  | deprecated | TBD | 🟡 2026-07-14 | gemini-embedding-2 |
| imagen-4.0-generate-001 |  | deprecated | TBD | 2026-08-17 | gemini-3.1-flash-image |
| imagen-4.0-ultra-generate-001 |  | deprecated | TBD | 2026-08-17 | gemini-3.1-flash-image |
| imagen-4.0-fast-generate-001 |  | deprecated | TBD | 2026-08-17 | gemini-3.1-flash-image |
| gemini-2.5-flash-image |  | deprecated | TBD | 2026-10-02 | gemini-3.1-flash-image-preview |
| gemini-2.5-pro |  | deprecated | TBD | 2026-10-16 | gemini-3.1-pro-preview |
| gemini-2.5-flash |  | deprecated | TBD | 2026-10-16 | gemini-3.5-flash |
| gemini-2.5-flash-lite |  | deprecated | TBD | 2026-10-16 | gemini-3.1-flash-lite |
| gemini-3.1-flash-lite |  | deprecated | TBD | 2027-05-07 |  |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gpt-4-0314 |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-1106-preview |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-0125-preview (including gpt-4-turbo-preview and gpt-4-turbo-preview-completions, which point to this snapshot) |  | deprecated | TBD | 🔴 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4o-realtime-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2025-06-03 |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2024-12-17 |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-mini-realtime-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-mini |
| gpt-4o-audio-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-audio-1.5 |
| gpt-4o-mini-audio-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-audio-mini |
| dall-e-2 |  | deprecated | TBD | 🔴 2026-05-12 | gpt-image-2, gpt-image-1, or gpt-image-1-mini |
| dall-e-3 |  | deprecated | TBD | 🔴 2026-05-12 | gpt-image-2, gpt-image-1, or gpt-image-1-mini |
| OpenAI-Beta: realtime=v1 |  | deprecated | TBD | 🔴 2026-05-12 | Realtime API |
| computer-use-preview-2025-03-11 | computer-use-preview |  | deprecated | TBD | 2026-07-23 | gpt-5.4-mini |
| gpt-4o-mini-search-preview-2025-03-11 |  | deprecated | TBD | 2026-07-23 | gpt-5.4-mini |
| gpt-4o-mini-tts-2025-03-20 |  | deprecated | TBD | 2026-07-23 | gpt-4o-mini-tts-2025-12-15 |
| gpt-4o-search-preview-2025-03-11 |  | deprecated | TBD | 2026-07-23 | gpt-5.4-mini |
| gpt-5-chat-latest |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5-codex |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5.1-chat-latest |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex-max |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex-mini |  | deprecated | TBD | 2026-07-23 | gpt-5.4-mini |
| gpt-audio-mini-2025-10-06 |  | deprecated | TBD | 2026-07-23 | gpt-audio-1.5 |
| gpt-realtime-mini-2025-10-06 |  | deprecated | TBD | 2026-07-23 | gpt-realtime-mini |
| o3-deep-research-2025-06-26 | o3-deep-research |  | deprecated | TBD | 2026-07-23 | gpt-5.5-pro |
| o4-mini-deep-research-2025-06-26 | o4-mini-deep-research |  | deprecated | TBD | 2026-07-23 | gpt-5.5-pro |
| gpt-5.2-codex |  | deprecated | TBD | 2026-07-23 | gpt-5.5 |
| gpt-5.2-chat-latest |  | deprecated | TBD | 2026-08-10 | gpt-5.5 |
| gpt-5.3-chat-latest |  | deprecated | TBD | 2026-08-10 | gpt-5.5 |
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
| gpt-3.5-turbo-0125 | gpt-3.5-turbo, gpt-3.5-turbo-completions |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| gpt-4-0613 | gpt-4, gpt-4-0613-completions, gpt-4-completions |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| gpt-4-1106-preview |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| gpt-4-turbo | gpt-4-turbo-2024-04-09, gpt-4-turbo-completions |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| gpt-4.1-nano | gpt-4.1-nano-2025-04-14 |  | deprecated | TBD | 2026-10-23 | gpt-5.4-nano |
| gpt-4o-2024-05-13 |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| gpt-image-1 |  | deprecated | TBD | 2026-10-23 | gpt-image-2 |
| o1-2024-12-17 | o1 |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| o1-pro-2025-03-19 | o1-pro |  | deprecated | TBD | 2026-10-23 | gpt-5.5-pro |
| o3-mini-2025-01-31 | o3-mini |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| ft-o4-mini-2025-04-16 |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| o4-mini-2025-04-16 | o4-mini |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| ft-gpt-3.5-turbo |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| ft-gpt-4 |  | deprecated | TBD | 2026-10-23 | gpt-5.5 |
| ft-gpt-4.1-nano-2025-04-14 |  | deprecated | TBD | 2026-10-23 | gpt-5.4-nano |
| ft-babbage-002 |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| ft-davinci-002 |  | deprecated | TBD | 2026-10-23 | gpt-5.4-mini |
| gpt-image-1-mini |  | deprecated | TBD | 2026-12-01 | gpt-image-2 |
| gpt-image-1.5 |  | deprecated | TBD | 2026-12-01 | gpt-image-2 |
| chatgpt-image-latest |  | deprecated | TBD | 2026-12-01 | gpt-image-2 |
| gpt-5-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.5 |
| gpt-5-mini-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.4-mini |
| gpt-5-nano-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.4-nano |
| gpt-5-pro-2025-10-06 |  | deprecated | TBD | 2026-12-11 | gpt-5.5-pro |
| o3-2025-04-16 |  | deprecated | TBD | 2026-12-11 | gpt-5.5 |
| o3-pro-2025-06-10 |  | deprecated | TBD | 2026-12-11 | gpt-5.5-pro |

### Vertex AI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Claude 3.7 Sonnet | Claude 3.7 Sonnet | retired | 2026-11-11 | 🔴 2026-05-11 |  |
| Claude 3.5 Haiku | Claude 3.5 Haiku | deprecated | 2026-01-05 | 🟡 2026-07-05 |  |
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
