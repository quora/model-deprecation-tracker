# AI Model Deprecation Tracker

Automatically tracks model deprecation schedules from major AI providers.

## Providers

- **OpenAI** — [Deprecations page](https://developers.openai.com/api/docs/deprecations/)
- **Anthropic** — [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **Vertex AI** — [Partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models)
- **AWS Bedrock** — [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html)
- **Gemini** — [API deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

## Deprecation Schedule

<!-- DEPRECATION_TABLE_START -->

*Last updated: 2026-02-25*

### Anthropic

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-3-7-sonnet-20250219 |  | retired | 2025-10-28 | 2026-02-19 | claude-opus-4-6 |
| claude-3-5-haiku-20241022 |  | retired | 2025-12-19 | 2026-02-19 | claude-haiku-4-5-20251001 |
| claude-3-haiku-20240307 |  | deprecated | 2026-02-19 | 2026-04-20 | claude-haiku-4-5-20251001 |
| claude-opus-4-20250514 |  | active | TBD | 2026-05-14 |  |
| claude-sonnet-4-20250514 |  | active | TBD | 2026-05-14 |  |
| claude-opus-4-1-20250805 |  | active | TBD | 2026-08-05 |  |
| claude-sonnet-4-5-20250929 |  | active | TBD | 2026-09-29 |  |
| claude-haiku-4-5-20251001 |  | active | TBD | 2026-10-15 |  |
| claude-opus-4-5-20251101 |  | active | TBD | 2026-11-24 |  |
| claude-opus-4-6 |  | active | TBD | 2027-02-05 |  |
| claude-sonnet-4-6 |  | active | TBD | 2027-02-17 |  |

### Bedrock

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Claude 3 Opus |  | retired | 2025-07-15 | 2026-01-15 | Claude Opus 4.1, Claude Sonnet 4.5 / anthropic.claude-opus-4-1-20250805-v1:0,
                            anthropic.claude-sonnet-4-5-20250929-v1:0 |
| Claude 3.5 Sonnet v2 |  | legacy | 2025-08-25 | 2026-03-01 | Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0 |
| Claude 3.7 Sonnet |  | legacy | 2025-10-28 | 2026-04-28 | Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0 |
| Claude Opus 4 |  | legacy | 2025-10-01 | 2026-05-31 | Claude Opus 4.1 / anthropic.claude-opus-4-1-20250805-v1:0 |
| Claude 3.5 Haiku |  | legacy | 2025-12-19 | 2026-06-19 | Claude Haiku 4.5 / anthropic.claude-haiku-4-5-20251001-v1:0 |
| Titan Image Generator G1 v2 |  | legacy | 2025-12-30 | 2026-06-30 | Nova Canvas or Nova 2 Omni / amazon.nova-canvas-v1:0 |
| Llama 3.1 405B Instruct |  | legacy | 2026-01-07 | 2026-07-07 | Llama 4 Maverick 17B Instruct or Llama 4 Scout 17B Instruct / meta.llama4-maverick-17b-instruct-v1:0 or meta.llama4-scout-17b-instruct-v1:0 |
| Claude 3.5 Sonnet v1 |  | legacy | TBD | TBD | Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0 |
| August 25, 2025 (eu-central-2 Region) |  | legacy | 2025-12-01 | TBD |  |
| January 30, 2026 (us-gov-east-1, us-gov-west-1, ap-northeast-1, ap-south-1, and ap-southeast-2
                            Regions) |  | legacy | 2026-04-30 | TBD |  |
| January 30, 2026 (ap-northeast-1, ap-northeast-3, ap-south-1, ap-south-2, and ap-southeast-2
                            Regions) |  | legacy | 2026-04-30 | TBD |  |
| January 30, 2026 (us-gov-east-1 and us-gov-west-1
                            Regions) |  | legacy | 2026-04-30 | TBD |  |
| Llama 3.2 1B Instruct |  | legacy | TBD | TBD | Llama 4 Maverick 17B Instruct or Llama 4 Scout 17B Instruct / meta.llama4-maverick-17b-instruct-v1:0 or meta.llama4-scout-17b-instruct-v1:0 |
| Llama 3.2 3B Instruct |  | legacy | TBD | TBD | Llama 4 Maverick 17B Instruct or Llama 4 Scout 17B Instruct / meta.llama4-maverick-17b-instruct-v1:0 or meta.llama4-scout-17b-instruct-v1:0 |
| Llama 3.2 11B Instruct |  | legacy | TBD | TBD | Llama 4 Maverick 17B Instruct or Llama 4 Scout 17B Instruct / meta.llama4-maverick-17b-instruct-v1:0 or meta.llama4-scout-17b-instruct-v1:0 |
| Llama 3.2 90B Instruct |  | legacy | TBD | TBD | Llama 4 Maverick 17B Instruct or Llama 4 Scout 17B Instruct / meta.llama4-maverick-17b-instruct-v1:0 or meta.llama4-scout-17b-instruct-v1:0 |
| Claude 3 Sonnet |  | retired | TBD | TBD | Claude Sonnet 4.5 / anthropic.claude-sonnet-4-5-20250929-v1:0 |

### Gemini

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gemini-2.5-pro-preview-03-25 |  | retired | TBD | 2025-12-02 | gemini-3-pro-preview |
| gemini-2.5-pro-preview-05-06 |  | retired | TBD | 2025-12-02 | gemini-3-pro-preview |
| gemini-2.5-pro-preview-06-05 |  | retired | TBD | 2025-12-02 | gemini-3-pro-preview |
| gemini-2.0-flash-lite-preview |  | retired | TBD | 2025-12-09 | gemini-2.5-flash-lite |
| gemini-2.0-flash-lite-preview-02-05 |  | retired | TBD | 2025-12-09 | gemini-2.5-flash-lite |
| gemini-2.0-flash-live-001 |  | retired | TBD | 2025-12-09 | gemini-2.5-flash-native-audio-preview-12-2025 |
| gemini-live-2.5-flash-preview |  | retired | TBD | 2025-12-09 | gemini-2.5-flash-native-audio-preview-12-2025 |
| text-embedding-004 |  | retired | TBD | 2026-01-14 | gemini-embedding-001 |
| gemini-2.5-flash-image-preview |  | retired | TBD | 2026-01-15 | gemini-2.5-flash-image |
| gemini-2.5-flash-preview-09-25 |  | retired | TBD | 2026-02-17 | gemini-3-flash-preview |
| imagen-4.0-generate-preview-06-06 |  | retired | TBD | 2026-02-17 | imagen-4.0-generate-001 |
| imagen-4.0-ultra-generate-preview-06-06 |  | retired | TBD | 2026-02-17 | imagen-4.0-ultra-generate-001 |
| gemini-2.0-flash |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash |
| gemini-2.0-flash-001 |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash |
| gemini-2.0-flash-lite |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash-lite |
| gemini-2.0-flash-lite-001 |  | deprecated | TBD | 2026-06-01 | gemini-2.5-flash-lite |
| gemini-2.5-pro |  | deprecated | TBD | 2026-06-17 | gemini-3-pro-preview |
| gemini-2.5-flash |  | deprecated | TBD | 2026-06-17 | gemini-3-flash-preview |
| imagen-4.0-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| imagen-4.0-ultra-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| imagen-4.0-fast-generate-001 |  | deprecated | TBD | 2026-06-24 | gemini-3-pro-image-preview orgemini-2.5-flash-image |
| gemini-embedding-001 |  | deprecated | TBD | 2026-07-14 |  |
| gemini-2.5-flash-lite |  | deprecated | TBD | 2026-07-22 |  |
| gemini-2.5-flash-image |  | deprecated | TBD | 2026-10-02 |  |
| Preview models |  | active | TBD | TBD |  |
| gemini-3-pro-preview |  | active | TBD | TBD |  |
| gemini-3-pro-image-preview |  | active | TBD | TBD |  |
| gemini-3-flash-preview |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| gemini-2.5-flash-lite-preview-09-25 |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |
| Preview models |  | active | TBD | TBD |  |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| codex-mini-latest |  | deprecated | TBD | 2026-02-12 | gpt-5-codex-mini |
| chatgpt-4o-latest |  | deprecated | TBD | 2026-02-17 | gpt-5.1-chat-latest |
| OpenAI-Beta: realtime=v1 |  | deprecated | TBD | 2026-03-24 | Realtime API |
| gpt-4o-realtime-preview |  | deprecated | TBD | 2026-03-24 | gpt-realtime |
| gpt-4o-realtime-preview-2025-06-03 |  | deprecated | TBD | 2026-03-24 | gpt-realtime |
| gpt-4o-realtime-preview-2024-12-17 |  | deprecated | TBD | 2026-03-24 | gpt-realtime |
| gpt-4o-mini-realtime-preview |  | deprecated | TBD | 2026-03-24 | gpt-realtime-mini |
| gpt-4o-audio-preview |  | deprecated | TBD | 2026-03-24 | gpt-audio |
| gpt-4o-mini-audio-preview |  | deprecated | TBD | 2026-03-24 | gpt-audio-mini |
| gpt-4-0314 |  | deprecated | TBD | 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-1106-preview |  | deprecated | TBD | 2026-03-26 | gpt-5 or gpt-4.1* |
| gpt-4-0125-preview (including gpt-4-turbo-preview and gpt-4-turbo-preview-completions, which point to this snapshot) |  | deprecated | TBD | 2026-03-26 | gpt-5 or gpt-4.1* |
| dall-e-2 |  | deprecated | TBD | 2026-05-12 | gpt-image-1 or gpt-image-1-mini |
| dall-e-3 |  | deprecated | TBD | 2026-05-12 | gpt-image-1 or gpt-image-1-mini |
| Assistants API |  | deprecated | TBD | 2026-08-26 | Responses API and Conversations API |
| gpt-3.5-turbo-instruct |  | deprecated | TBD | 2026-09-28 | gpt-5-mini or gpt-4.1-mini* |
| babbage-002 |  | deprecated | TBD | 2026-09-28 | gpt-5-mini or gpt-4.1-mini* |
| davinci-002 |  | deprecated | TBD | 2026-09-28 | gpt-5-mini or gpt-4.1-mini* |
| gpt-3.5-turbo-1106 |  | deprecated | TBD | 2026-09-28 | gpt-5-mini or gpt-4.1-mini* |

### Vertex AI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Launch stage |  | deprecated | TBD | TBD |  |
| Supported inputs & outputs |  | deprecated | TBD | TBD |  |
| Token limits |  | deprecated | TBD | TBD |  |
| Capabilities |  | deprecated | TBD | TBD |  |
| Usage types |  | deprecated | TBD | TBD |  |
| Technical specifications |  | deprecated | TBD | TBD |  |
| Images |  | deprecated | TBD | TBD |  |
| Documents |  | deprecated | TBD | TBD |  |
| Knowledge cutoff date |  | deprecated | TBD | TBD |  |
| Versions |  | deprecated | TBD | TBD |  |
| Supported regions |  | deprecated | TBD | TBD |  |
| Model availability
(Includes fixed quota & Provisioned Throughput) |  | deprecated | TBD | TBD |  |
| ML processing |  | deprecated | TBD | TBD |  |
| Quota limits |  | deprecated | TBD | TBD |  |
| Pricing |  | deprecated | TBD | TBD |  |
| Model availability |  | deprecated | TBD | TBD |  |

<!-- DEPRECATION_TABLE_END -->

## Calendar

Download [deprecations.ics](deprecations.ics) and import it into your calendar app to get reminders 7 and 30 days before model shutdowns.

## Slack Alerts

Set the `SLACK_WEBHOOK_URL` environment variable (or GitHub Actions secret) to receive Slack notifications when a model shutdown is within 7 days.

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
