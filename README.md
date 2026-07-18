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

*Last updated: 2026-07-18*

### Anthropic

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-3-haiku-20240307 |  | retired | 2026-02-19 | 🔴 2026-04-20 | claude-haiku-4-5-20251001 |
| claude-opus-4-20250514 |  | retired | 2026-04-14 | 🔴 2026-06-15 | claude-opus-4-8 |
| claude-sonnet-4-20250514 |  | retired | 2026-04-14 | 🔴 2026-06-15 | claude-sonnet-4-6 |
| claude-opus-4-1-20250805 |  | deprecated | 2026-06-05 | 🟡 2026-08-05 | claude-opus-4-8 |
| claude-sonnet-4-5-20250929 |  | active | TBD | 2026-09-29 |  |
| claude-haiku-4-5-20251001 |  | active | TBD | 2026-10-15 |  |
| claude-opus-4-5-20251101 |  | active | TBD | 2026-11-24 |  |
| claude-opus-4-6 |  | active | TBD | 2027-02-05 |  |
| claude-sonnet-4-6 |  | active | TBD | 2027-02-17 |  |
| claude-opus-4-7 |  | active | TBD | 2027-04-16 |  |
| claude-opus-4-8 |  | active | TBD | 2027-05-28 |  |
| claude-fable-5 |  | active | TBD | 2027-06-09 |  |
| claude-sonnet-5 |  | active | TBD | 2027-06-30 |  |

### Azure Foundry (Anthropic)

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-opus-4-1 |  | active | TBD | 🟡 2026-08-05 | claude-opus-4-8 |
| claude-haiku-4-5 |  | active | TBD | 2026-10-19 |  |
| claude-opus-4-5 |  | active | TBD | 2026-10-19 |  |
| claude-sonnet-4-5 |  | active | TBD | 2026-10-19 |  |
| claude-opus-4-6 |  | active | TBD | 2027-02-02 |  |
| claude-sonnet-4-6 |  | active | TBD | 2027-02-10 |  |
| claude-mythos-preview (gated research preview) |  | active | TBD | 2027-04-02 |  |
| claude-opus-4-7 |  | active | TBD | 2027-04-06 |  |

### Azure Foundry (OpenAI)

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gpt-5-chat (2025-10-03) |  | retired | TBD | 🔴 2026-05-13 | gpt-chat-latest |
| gpt-5-chat (2025-10-03) |  | retired | TBD | 🔴 2026-05-13 | gpt-chat-latest |
| gpt-5.2-chat (2025-12-11) |  | retired | TBD | 🔴 2026-05-13 | gpt-chat-latest |
| gpt-5.2-chat (2025-12-11) |  | retired | TBD | 🔴 2026-05-13 | gpt-chat-latest |
| gpt-5-chat (2025-08-07) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5-chat (2025-08-07) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.1-chat (2025-11-13) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.1-chat (2025-11-13) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.2-chat (2026-02-10) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.2-chat (2026-02-10) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.3-chat (2026-03-03) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| gpt-5.3-chat (2026-03-03) |  | retired | TBD | 🔴 2026-06-29 | gpt-chat-latest |
| sora-2 (2025-10-06) |  | retired | TBD | 🔴 2026-07-15 | sora-2 (2025-12-08) |
| gpt-realtime-mini (2025-10-06) |  | active | TBD | 🟡 2026-07-23 |  |
| gpt-chat-latest (2026-05-05) |  | active | TBD | 🟡 2026-08-05 |  |
| gpt-chat-latest (2026-05-28) |  | active | TBD | 2026-08-28 |  |
| gpt-chat-latest (2026-06-24) |  | active | TBD | 2026-08-28 |  |
| sora-2 (2025-12-08) |  | active | TBD | 2026-09-15 |  |
| o1 (2024-12-17) |  | deprecated | TBD | 2026-09-16 |  |
| o1-pro (2025-03-19) |  | active | TBD | 2026-09-18 |  |
| gpt-audio-mini (2025-10-06) |  | active | TBD | 2026-09-21 |  |
| gpt-4o (2024-05-13) |  | deprecated | TBD | 2026-10-01 | gpt-5.1 |
| gpt-4o (2024-08-06) |  | deprecated | TBD | 2026-10-01 | gpt-5.1 |
| gpt-4o (2024-11-20) |  | deprecated | TBD | 2026-10-01 | gpt-5.1 |
| gpt-4o-mini (2024-07-18) |  | deprecated | TBD | 2026-10-01 | gpt-4.1-mini |
| gpt-4o (2024-11-20) |  | deprecated | TBD | 2026-10-01 | gpt-5.1 |
| gpt-4o-mini (2024-07-18) |  | deprecated | TBD | 2026-10-01 | gpt-4.1-mini |
| o3-mini (2025-01-31) |  | deprecated | TBD | 2026-10-01 | o4-mini |
| gpt-4.1 (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4.1-mini (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4.1-nano (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4.1 (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4.1-mini (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4.1-nano (2025-04-14) |  | deprecated | TBD | 2026-10-14 |  |
| gpt-4o-mini-transcribe (2025-03-20) |  | active | TBD | 2026-10-15 |  |
| gpt-4o-mini-tts (2025-03-20) |  | active | TBD | 2026-10-15 |  |
| gpt-4o-transcribe (2025-03-20) |  | active | TBD | 2026-10-15 |  |
| gpt-4o-transcribe-diarize (2025-10-15) |  | active | TBD | 2026-10-15 |  |
| o3 (2025-04-16) |  | active | TBD | 2026-10-16 |  |
| o4-mini (2025-04-16) |  | deprecated | TBD | 2026-10-16 |  |
| gpt-image-1 (2025-04-15) |  | active | TBD | 2026-10-23 |  |
| codex-mini (2025-05-16) |  | deprecated | TBD | 2026-11-15 |  |
| codex-mini (2025-05-16) |  | deprecated | TBD | 2026-11-15 |  |
| gpt-5.1-codex-max (2025-12-04) |  | active | TBD | 2026-12-05 |  |
| o3-pro (2025-06-10) |  | active | TBD | 2026-12-10 |  |
| gpt-5.2 (2025-12-11) |  | active | TBD | 2026-12-12 |  |
| gpt-4o-mini-transcribe (2025-12-15) |  | active | TBD | 2026-12-15 |  |
| gpt-4o-mini-tts (2025-12-15) |  | active | TBD | 2026-12-15 |  |
| gpt-audio-mini (2025-12-15) |  | active | TBD | 2026-12-15 |  |
| gpt-realtime-mini (2025-12-15) |  | active | TBD | 2026-12-15 |  |
| tts (001) |  | active | TBD | 2026-12-15 |  |
| tts-hd (001) |  | active | TBD | 2026-12-15 |  |
| whisper (001) |  | active | TBD | 2026-12-15 |  |
| gpt-image-1.5 (2025-12-16) |  | active | TBD | 2026-12-16 |  |
| o3-deep-research (2025-06-26) |  | active | TBD | 2026-12-26 |  |
| gpt-5.2-codex (2026-01-14) |  | active | TBD | 2027-01-14 |  |
| gpt-5 (2025-08-07) |  | active | TBD | 2027-02-06 |  |
| gpt-5-mini (2025-08-07) |  | active | TBD | 2027-02-06 |  |
| gpt-5-nano (2025-08-07) |  | active | TBD | 2027-02-06 |  |
| gpt-audio-1.5 (2026-02-23) |  | active | TBD | 2027-02-23 |  |
| gpt-realtime-1.5 (2026-02-23) |  | active | TBD | 2027-02-23 |  |
| gpt-5.3-codex (2026-02-24) |  | active | TBD | 2027-02-25 |  |
| gpt-audio (2025-08-28) |  | active | TBD | 2027-02-28 |  |
| gpt-realtime (2025-08-28) |  | active | TBD | 2027-02-28 |  |
| gpt-5.4 (2026-03-05) |  | active | TBD | 2027-03-05 |  |
| gpt-5.4-pro (2026-03-05) |  | active | TBD | 2027-03-06 |  |
| gpt-5-codex (2025-09-15) |  | active | TBD | 2027-03-17 |  |
| gpt-5.4-mini (2026-03-17) |  | active | TBD | 2027-03-18 |  |
| gpt-5.4-nano (2026-03-17) |  | active | TBD | 2027-03-18 |  |
| gpt-5-pro (2025-10-06) |  | active | TBD | 2027-04-07 |  |
| gpt-image-1-mini (2025-10-06) |  | active | TBD | 2027-04-07 |  |
| text-embedding-3-large (1) |  | active | TBD | 2027-04-15 |  |
| text-embedding-3-small (1) |  | active | TBD | 2027-04-15 |  |
| text-embedding-ada-002 (1) |  | active | TBD | 2027-04-15 |  |
| text-embedding-ada-002 (2) |  | active | TBD | 2027-04-15 |  |
| gpt-image-2 (2026-04-21) |  | active | TBD | 2027-04-21 |  |
| gpt-5.5 (2026-04-24) |  | active | TBD | 2027-04-23 |  |
| gpt-realtime-2 (2026-05-06) |  | active | TBD | 2027-05-06 |  |
| gpt-5.1 (2025-11-13) |  | active | TBD | 2027-05-15 |  |
| gpt-5.1-codex (2025-11-13) |  | active | TBD | 2027-05-15 |  |
| gpt-5.1-codex-mini (2025-11-13) |  | active | TBD | 2027-05-15 |  |
| gpt-realtime-2.1 (2026-07-07) |  | active | TBD | 2027-06-25 |  |
| gpt-realtime-2.1-mini (2026-07-07) |  | active | TBD | 2027-06-25 |  |
| gpt-5.6-luna (2026-07-09) |  | active | TBD | 2027-07-09 |  |
| gpt-5.6-sol (2026-07-09) |  | active | TBD | 2027-07-09 |  |
| gpt-5.6-terra (2026-07-09) |  | active | TBD | 2027-07-09 |  |

### Gemini

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gemini-robotics-er-1.5-preview |  | retired | TBD | 🔴 2026-04-30 | gemini-robotics-er-1.6-preview |
| gemini-3.1-flash-lite-preview |  | retired | TBD | 🔴 2026-05-25 | gemini-3.1-flash-lite |
| gemini-2.0-flash |  | retired | TBD | 🔴 2026-06-01 | gemini-3.5-flash |
| gemini-2.0-flash-001 |  | retired | TBD | 🔴 2026-06-01 | gemini-3.5-flash |
| gemini-2.0-flash-lite |  | retired | TBD | 🔴 2026-06-01 | gemini-3.1-flash-lite |
| gemini-2.0-flash-lite-001 |  | retired | TBD | 🔴 2026-06-01 | gemini-3.1-flash-lite |
| gemini-3.1-flash-image-preview |  | retired | TBD | 🔴 2026-06-25 | gemini-3.1-flash-image |
| gemini-3-pro-image-preview |  | retired | TBD | 🔴 2026-06-25 | gemini-3-pro-image |
| veo-3.0-generate-001 |  | retired | TBD | 🔴 2026-06-30 | veo-3.1-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| veo-3.0-fast-generate-001 |  | retired | TBD | 🔴 2026-06-30 | veo-3.1-fast-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| veo-2.0-generate-001 |  | retired | TBD | 🔴 2026-06-30 | veo-3.1-generate-previewor the GA models on the Gemini Enterprise Agent Platform |
| gemini-embedding-001 |  | retired | TBD | 🔴 2026-07-14 | gemini-embedding-2 |
| embedding-2-preview |  | deprecated | TBD | 🟡 2026-08-10 | gemini-embedding-2 |
| imagen-4.0-generate-001 |  | deprecated | TBD | 🟡 2026-08-17 | gemini-3.1-flash-image |
| imagen-4.0-ultra-generate-001 |  | deprecated | TBD | 🟡 2026-08-17 | gemini-3.1-flash-image |
| imagen-4.0-fast-generate-001 |  | deprecated | TBD | 🟡 2026-08-17 | gemini-3.1-flash-image |
| gemini-2.5-flash-image |  | deprecated | TBD | 2026-10-02 | gemini-3.1-flash-image-preview |
| gemini-2.5-pro |  | deprecated | TBD | 2026-10-16 | gemini-3.1-pro-preview |
| gemini-2.5-flash |  | deprecated | TBD | 2026-10-16 | gemini-3.5-flash |
| gemini-2.5-flash-lite |  | deprecated | TBD | 2026-10-16 | gemini-3.1-flash-lite |
| gemini-3.1-flash-lite |  | deprecated | TBD | 2027-05-07 |  |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| gpt-4o-realtime-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2025-06-03 |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-realtime-preview-2024-12-17 |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-1.5 |
| gpt-4o-mini-realtime-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-realtime-mini |
| gpt-4o-audio-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-audio-1.5 |
| gpt-4o-mini-audio-preview |  | deprecated | TBD | 🔴 2026-05-07 | gpt-audio-mini |
| dall-e-2 |  | deprecated | TBD | 🔴 2026-05-12 | gpt-image-2, gpt-image-1, or gpt-image-1-mini |
| dall-e-3 |  | deprecated | TBD | 🔴 2026-05-12 | gpt-image-2, gpt-image-1, or gpt-image-1-mini |
| OpenAI-Beta: realtime=v1 |  | deprecated | TBD | 🔴 2026-05-12 | Realtime API |
| computer-use-preview-2025-03-11 | computer-use-preview |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.4-mini |
| gpt-4o-mini-search-preview-2025-03-11 |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.4-mini |
| gpt-4o-mini-tts-2025-03-20 |  | deprecated | TBD | 🟡 2026-07-23 | gpt-4o-mini-tts-2025-12-15 |
| gpt-4o-search-preview-2025-03-11 |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.4-mini |
| gpt-5-chat-latest |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5-codex |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5.1-chat-latest |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex-max |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5.1-codex-mini |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.4-mini |
| gpt-audio-mini-2025-10-06 |  | deprecated | TBD | 🟡 2026-07-23 | gpt-audio-1.5 |
| gpt-realtime-mini-2025-10-06 |  | deprecated | TBD | 🟡 2026-07-23 | gpt-realtime-mini |
| o3-deep-research-2025-06-26 | o3-deep-research |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5-pro |
| o4-mini-deep-research-2025-06-26 | o4-mini-deep-research |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5-pro |
| gpt-5.2-codex |  | deprecated | TBD | 🟡 2026-07-23 | gpt-5.5 |
| gpt-5.2-chat-latest |  | deprecated | TBD | 🟡 2026-08-10 | gpt-5.5 |
| gpt-5.3-chat-latest |  | deprecated | TBD | 🟡 2026-08-10 | gpt-5.5 |
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
| Claude 3.7 Sonnet on Google Cloud | Claude 3.7 Sonnet on Google Cloud | retired | 2026-11-11 | 🔴 2026-05-11 |  |
| Claude 3.5 Haiku on Google Cloud | Claude 3.5 Haiku on Google Cloud | retired | 2026-01-05 | 🔴 2026-07-05 |  |
| Claude 3 Opus on Google Cloud | Claude 3 Opus on Google Cloud | deprecated | 2026-06-30 | 🟡 2026-08-01 |  |
| Anthropic's Claude 3 Haiku on Google Cloud | Anthropic's Claude 3 Haiku on Google Cloud | deprecated | 2026-02-23 | 2026-08-23 |  |

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
