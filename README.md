# AI Model Deprecation Tracker

Automatically tracks model deprecation schedules from major AI providers.

## Providers

- **OpenAI** — [Deprecations page](https://developers.openai.com/api/docs/deprecations/)
- **Anthropic** — [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **Vertex AI** — [Partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models)
- **AWS Bedrock** — [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html)
- **Gemini** — [API deprecations](https://ai.google.dev/gemini-api/docs/deprecations)
- **Azure Foundry** — [Model retirement schedule](https://learn.microsoft.com/en-us/azure/foundry/openai/concepts/model-retirement-schedule)

## Calendar

Download [deprecations.ics](deprecations.ics) and import it into your calendar app to get reminders 7 and 30 days before model shutdowns.

## Deprecation Schedule

<!-- DEPRECATION_TABLE_START -->

*Last updated: 2026-11-05*

### Anthropic

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-haiku-4-5-20251001 |  | active | TBD | 🔴 2026-10-15 |  |
| claude-opus-4-5-20251101 |  | active | TBD | 🟡 2026-11-24 |  |
| claude-sonnet-4-5-20250929 |  | deprecated | 2026-09-30 | 🟡 2026-11-30 | claude-sonnet-5-5 |
| claude-opus-4-6 |  | active | TBD | 2027-02-05 |  |
| claude-sonnet-4-6 |  | active | TBD | 2027-02-17 |  |
| claude-opus-4-7 |  | active | TBD | 2027-04-16 |  |
| claude-opus-4-8 |  | active | TBD | 2027-05-28 |  |
| claude-fable-5 |  | active | TBD | 2027-06-09 |  |
| claude-mythos-5 |  | active | TBD | 2027-06-09 |  |
| claude-sonnet-5 |  | active | TBD | 2027-06-30 |  |
| claude-opus-5 |  | active | TBD | 2027-07-24 |  |
| claude-fable-5-1 |  | active | TBD | 2027-09-01 |  |
| claude-mythos-5-1 |  | active | TBD | 2027-09-01 |  |
| claude-opus-5-5 |  | active | TBD | 2027-09-22 |  |
| claude-sonnet-5-5 |  | active | TBD | 2027-09-28 |  |
| claude-haiku-5-5 |  | active | TBD | 2027-10-07 |  |

### Azure Foundry (Anthropic)

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-haiku-4-5 (1) |  | active | TBD | 🟡 2026-11-15 |  |
| claude-haiku-4-5 (2) |  | active | TBD | 🟡 2026-11-15 |  |
| claude-opus-4-5 (1) |  | active | TBD | 🟡 2026-11-24 |  |
| claude-sonnet-4-5 (1) |  | active | TBD | 🟡 2026-11-30 | claude-sonnet-5-5 |
| claude-opus-5-5-fast (2) |  | active | TBD | 2027-01-15 |  |
| claude-opus-4-6 (1) |  | active | TBD | 2027-02-02 |  |
| claude-sonnet-4-6 (1) |  | active | TBD | 2027-02-10 |  |
| claude-mythos-preview (gated research preview) |  | active | TBD | 2027-04-02 |  |
| claude-opus-4-7 (1) |  | active | TBD | 2027-04-06 |  |
| claude-sonnet-5 (2) |  | active | TBD | 2027-06-30 |  |
| claude-sonnet-5 (1) |  | active | TBD | 2027-06-30 |  |
| claude-opus-5 (2) |  | active | TBD | 2027-07-08 |  |
| claude-opus-5 (1) |  | active | TBD | 2027-07-08 |  |
| claude-opus-4-8 (2) |  | active | TBD | 2027-09-01 |  |
| claude-opus-4-8 (1) |  | active | TBD | 2027-09-01 |  |
| claude-mythos-5-1 (1) |  | active | TBD | 2027-09-01 |  |
| claude-fable-5-1 (1) |  | active | TBD | 2027-12-05 |  |
| claude-fable-5 (1) |  | active | TBD | 2027-12-05 |  |

### Azure Foundry (OpenAI)

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gpt-realtime-mini (2025-10-06) |  | retired | TBD | 🔴 2026-09-21 |  |
| gpt-4o-mini-transcribe (2025-03-20) |  | retired | TBD | 🔴 2026-10-15 |  |
| gpt-4o-mini-tts (2025-03-20) |  | retired | TBD | 🔴 2026-10-15 |  |
| gpt-4o-transcribe (2025-03-20) |  | retired | TBD | 🔴 2026-10-15 |  |
| sora-2 (2025-12-08) |  | retired | TBD | 🔴 2026-10-15 |  |
| gpt-image-1 (2025-04-15) |  | retired | TBD | 🔴 2026-10-23 |  |
| codex-mini (2025-05-16) |  | deprecated | TBD | 🟡 2026-11-15 |  |
| gpt-chat-latest (2026-05-05) |  | active | TBD | 🟡 2026-11-17 |  |
| gpt-chat-latest (2026-06-24) |  | active | TBD | 🟡 2026-11-17 |  |
| o1 (2024-12-17) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-sol |
| o1-pro (2025-03-19) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-sol |
| o3 (2025-04-16) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-sol |
| o3-deep-research (2025-06-26) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-sol |
| o3-mini (2025-01-31) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-terra |
| o3-pro (2025-06-10) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-sol |
| o4-mini (2025-04-16) |  | deprecated | TBD | 🟡 2026-11-19 | gpt-5.6-terra |
| gpt-chat-latest (2026-05-28) |  | active | TBD | 2026-12-08 |  |
| gpt-realtime-mini (2025-12-15) |  | active | TBD | 2026-12-15 |  |
| tts (001) |  | active | TBD | 2026-12-15 |  |
| tts-hd (001) |  | active | TBD | 2026-12-15 |  |
| whisper (001) |  | active | TBD | 2026-12-15 |  |
| gpt-image-1.5 (2025-12-16) |  | active | TBD | 2026-12-16 |  |
| gpt-chat-latest (2026-08-06) |  | active | TBD | 2027-01-12 |  |
| gpt-4o (2024-05-13) |  | deprecated | TBD | 2027-01-14 | gpt-5.1 (2025-11-13) |
| gpt-realtime-2 (2026-05-06) |  | active | TBD | 2027-01-20 | gpt-realtime-2.1 |
| gpt-5 (2025-08-07) |  | active | TBD | 2027-02-09 |  |
| gpt-5-nano (2025-08-07) |  | active | TBD | 2027-02-09 |  |
| gpt-audio (2025-08-28) |  | active | TBD | 2027-03-02 |  |
| gpt-realtime (2025-08-28) |  | active | TBD | 2027-03-02 |  |
| gpt-5-codex (2025-09-15) |  | active | TBD | 2027-03-17 |  |
| gpt-audio-mini (2025-10-06) |  | active | TBD | 2027-04-06 |  |
| gpt-realtime-mini (2025-10-06) |  | active | TBD | 2027-04-06 |  |
| gpt-5-pro (2025-10-06) |  | active | TBD | 2027-04-07 |  |
| gpt-image-1-mini (2025-10-06) |  | active | TBD | 2027-04-07 |  |
| gpt-4.1 (2025-04-14) |  | deprecated | TBD | 2027-04-14 |  |
| gpt-4.1-mini (2025-04-14) |  | deprecated | TBD | 2027-04-14 |  |
| gpt-4.1-nano (2025-04-14) |  | deprecated | TBD | 2027-04-14 |  |
| gpt-4o (2024-08-06) |  | deprecated | TBD | 2027-04-14 | gpt-5.1 |
| gpt-4o (2024-11-20) |  | deprecated | TBD | 2027-04-14 | gpt-5.1 |
| gpt-4o-mini (2024-07-18) |  | deprecated | TBD | 2027-04-14 |  |
| gpt-4o-transcribe-diarize (2025-10-15) |  | active | TBD | 2027-04-15 |  |
| gpt-5.1-codex (2025-11-13) |  | active | TBD | 2027-05-15 |  |
| gpt-5.1-codex-mini (2025-11-13) |  | active | TBD | 2027-05-15 |  |
| gpt-5.1-codex-max (2025-12-04) |  | active | TBD | 2027-05-18 |  |
| gpt-chat-latest (2026-10-07) |  | active | TBD | 2027-05-18 |  |
| gpt-5.2 (2025-12-11) |  | active | TBD | 2027-06-08 |  |
| gpt-4o-mini-transcribe (2025-12-15) |  | active | TBD | 2027-06-15 |  |
| gpt-4o-mini-tts (2025-12-15) |  | active | TBD | 2027-06-15 |  |
| gpt-audio-mini (2025-12-15) |  | active | TBD | 2027-06-15 |  |
| gpt-realtime-mini (2025-12-15) |  | active | TBD | 2027-06-15 |  |
| gpt-realtime-2.1 (2026-07-07) |  | active | TBD | 2027-06-25 |  |
| gpt-realtime-2.1-mini (2026-07-07) |  | active | TBD | 2027-06-25 |  |
| gpt-5-mini (2025-08-07) |  | active | TBD | 2027-07-13 |  |
| gpt-5.1 (2025-11-13) |  | active | TBD | 2027-07-13 |  |
| gpt-5.2-codex (2026-01-14) |  | active | TBD | 2027-07-13 |  |
| gpt-5.3-codex (2026-02-24) |  | active | TBD | 2027-08-24 |  |
| gpt-audio-1.5 (2026-02-23) |  | active | TBD | 2027-08-24 |  |
| gpt-realtime-1.5 (2026-02-23) |  | active | TBD | 2027-08-24 |  |
| gpt-5.4 (2026-03-05) |  | active | TBD | 2027-09-02 |  |
| gpt-5.4-pro (2026-03-05) |  | active | TBD | 2027-09-07 |  |
| gpt-image-2.5-flare (2026-09-09) |  | active | TBD | 2027-09-09 |  |
| gpt-image-2.5-sunburst (2026-09-09) |  | active | TBD | 2027-09-09 |  |
| gpt-5.4-mini (2026-03-17) |  | active | TBD | 2027-09-21 |  |
| gpt-5.4-nano (2026-03-17) |  | active | TBD | 2027-09-21 |  |
| gpt-image-2 (2026-04-21) |  | active | TBD | 2027-10-21 |  |
| gpt-5.5 (2026-04-24) |  | active | TBD | 2027-10-26 |  |
| gpt-5.6-luna (2026-07-09) |  | active | TBD | 2028-01-11 |  |
| gpt-5.6-sol (2026-07-09) |  | active | TBD | 2028-01-11 |  |
| gpt-5.6-terra (2026-07-09) |  | active | TBD | 2028-01-11 |  |
| text-embedding-3-large (1) |  | active | TBD | 2028-02-09 |  |
| text-embedding-3-small (1) |  | active | TBD | 2028-02-09 |  |
| text-embedding-ada-002 (1) |  | active | TBD | 2028-02-09 |  |
| text-embedding-ada-002 (2) |  | active | TBD | 2028-02-09 |  |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gpt-5.2-chat-latest |  | deprecated | TBD | 🔴 2026-08-10 | gpt-5.6-sol |
| gpt-5.3-chat-latest |  | deprecated | TBD | 🔴 2026-08-10 | gpt-5.6-sol |
| Assistants API |  | deprecated | TBD | 🔴 2026-08-26 | Responses API and Conversations API |
| Videos API |  | deprecated | TBD | 🔴 2026-09-24 | — |
| sora-2 |  | deprecated | TBD | 🔴 2026-09-24 | — |
| sora-2-pro |  | deprecated | TBD | 🔴 2026-09-24 | — |
| sora-2-2025-10-06 |  | deprecated | TBD | 🔴 2026-09-24 | — |
| sora-2-2025-12-08 |  | deprecated | TBD | 🔴 2026-09-24 | — |
| sora-2-pro-2025-10-06 |  | deprecated | TBD | 🔴 2026-09-24 | — |
| gpt-3.5-turbo-instruct |  | deprecated | TBD | 🔴 2026-09-28 | gpt-5.6-terra |
| babbage-002 |  | deprecated | TBD | 🔴 2026-09-28 | gpt-5.6-terra |
| davinci-002 |  | deprecated | TBD | 🔴 2026-09-28 | gpt-5.6-terra |
| gpt-3.5-turbo-1106 |  | deprecated | TBD | 🔴 2026-09-28 | gpt-5.6-terra |
| gpt-5.4-cyber |  | deprecated | TBD | 🔴 2026-10-01 | The most capable cyber model available to you. |
| gpt-3.5-turbo-0125 | gpt-3.5-turbo, gpt-3.5-turbo-completions |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-terra |
| gpt-4-0613 | gpt-4, gpt-4-0613-completions, gpt-4-completions |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| gpt-4-1106-preview |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| gpt-4-turbo | gpt-4-turbo-2024-04-09, gpt-4-turbo-completions |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| gpt-4.1-nano | gpt-4.1-nano-2025-04-14 |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-luna |
| gpt-4o-2024-05-13 |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| gpt-image-1 |  | deprecated | TBD | 🔴 2026-10-23 | gpt-image-2.5-sunburst or gpt-image-2.5-flare |
| o1-2024-12-17 | o1 |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| o1-pro-2025-03-19 | o1-pro |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol (reasoning.mode: pro) |
| o3-mini-2025-01-31 | o3-mini |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-sol |
| ft-o4-mini-2025-04-16 |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-terra |
| o4-mini-2025-04-16 | o4-mini |  | deprecated | TBD | 🔴 2026-10-23 | gpt-5.6-terra |
| gpt-image-1-mini |  | deprecated | TBD | 🟡 2026-12-01 | gpt-image-2.5-sunburst or gpt-image-2.5-flare |
| gpt-image-1.5 | gpt-image-1.5-2025-12-16 |  | deprecated | TBD | 🟡 2026-12-01 | gpt-image-2.5-sunburst or gpt-image-2.5-flare |
| chatgpt-image-latest |  | deprecated | TBD | 🟡 2026-12-01 | gpt-image-2.5-sunburst or gpt-image-2.5-flare |
| gpt-5 | gpt-5-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-sol |
| gpt-5-mini | gpt-5-mini-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-terra |
| gpt-5-nano | gpt-5-nano-2025-08-07 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-luna |
| gpt-5-pro | gpt-5-pro-2025-10-06 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-sol (reasoning.mode: pro) |
| o3 | o3-2025-04-16 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-sol |
| o3-pro | o3-pro-2025-06-10 |  | deprecated | TBD | 2026-12-11 | gpt-5.6-sol (reasoning.mode: pro) |
| tts-1 |  | deprecated | TBD | 2027-01-06 | gpt-realtime-2.1-mini |
| tts-1-hd |  | deprecated | TBD | 2027-01-06 | gpt-realtime-2.1-mini |
| gpt-4o-mini-tts | gpt-4o-mini-tts-2025-03-20 |  | deprecated | TBD | 2027-01-06 | gpt-realtime-2.1-mini |
| gpt-4o-mini-tts | gpt-4o-mini-tts-2025-12-15 |  | deprecated | TBD | 2027-01-06 | gpt-realtime-2.1-mini |
| GPT-4o (gpt-4o-2024-08-06, gpt-4o-2024-11-20) |  | deprecated | TBD | 2027-01-14 | gpt-6-luna |
| GPT-4o mini (gpt-4o-mini-2024-07-18) |  | deprecated | TBD | 2027-01-14 | gpt-6-luna |
| GPT-4.1 (gpt-4.1-2025-04-14) |  | deprecated | TBD | 2027-01-14 | gpt-6-luna |
| GPT-4.1 mini (gpt-4.1-mini-2025-04-14) |  | deprecated | TBD | 2027-01-14 | gpt-6-luna |
| gpt-realtime | gpt-realtime-2025-08-28 |  | deprecated | TBD | 2027-01-20 | gpt-realtime-2.1 |
| gpt-audio | gpt-audio-2025-08-28 |  | deprecated | TBD | 2027-01-20 | gpt-audio-1.5 |
| gpt-4o-audio |  | deprecated | TBD | 2027-01-20 | gpt-audio-1.5 |
| gpt-4o-realtime |  | deprecated | TBD | 2027-01-20 | gpt-realtime-2.1 |
| gpt-realtime-mini | gpt-realtime-mini-2025-12-15 |  | deprecated | TBD | 2027-01-20 | gpt-realtime-2.1-mini |
| gpt-audio-mini | gpt-audio-mini-2025-12-15 |  | deprecated | TBD | 2027-01-20 | gpt-audio-1.5 |
| gpt-4o-mini-realtime |  | deprecated | TBD | 2027-01-20 | gpt-realtime-2.1-mini |
| gpt-4o-mini-audio |  | deprecated | TBD | 2027-01-20 | gpt-audio-1.5 |
| gpt-4o-mini-transcribe-2025-03-20 |  | deprecated | TBD | 2027-01-20 | gpt-4o-mini-transcribe-2025-12-15 |
| whisper-1 |  | deprecated | TBD | 2027-02-26 | gpt-live-transcribe or gpt-transcribe |
| gpt-4o-transcribe |  | deprecated | TBD | 2027-02-26 | gpt-live-transcribe or gpt-transcribe |
| gpt-4o-mini-transcribe | gpt-4o-mini-transcribe-2025-12-15 |  | deprecated | TBD | 2027-02-26 | gpt-live-transcribe or gpt-transcribe |
| gpt-4o-transcribe-diarize |  | deprecated | TBD | 2027-02-26 | gpt-live-transcribe or gpt-transcribe |
| /v1/audio/translations |  | deprecated | TBD | 2027-02-26 | v1/realtime/translations |
| gpt-5.3-codex |  | deprecated | TBD | 2027-04-01 | gpt-6-sol |
| gpt-5.4-nano | gpt-5.4-nano-2026-03-17 |  | deprecated | TBD | 2027-04-01 | gpt-6-luna |
| gpt-5.1 | gpt-5.1-2025-11-13 |  | deprecated | TBD | 2027-04-01 | gpt-6-sol |

### Vertex AI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Anthropic's Claude 3 Haiku on Google Cloud | Anthropic's Claude 3 Haiku on Google Cloud | retired | 2026-02-23 | 🔴 2026-08-23 |  |
| Anthropic's Claude Sonnet 4.5 on Google Cloud | Anthropic's Claude Sonnet 4.5 on Google Cloud | deprecated | 2026-09-29 | 🟡 2026-11-30 |  |

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
