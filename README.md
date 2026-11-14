# AI Model Deprecation Tracker

Automatically tracks model deprecation schedules from major AI providers.

## Providers

- **OpenAI** — [Deprecations page](https://developers.openai.com/api/docs/deprecations/)
- **Anthropic** — [Model deprecations](https://platform.claude.com/docs/en/about-claude/model-deprecations)
- **Vertex AI** — [Google model retirements](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/learn/model-versions) and [partner model deprecations](https://docs.cloud.google.com/vertex-ai/generative-ai/docs/deprecations/partner-models). Only confirmed retirement dates are tracked; minimum availability dates such as “or later” or “no sooner than” are excluded.
- **AWS Bedrock** — [Model lifecycle](https://docs.aws.amazon.com/bedrock/latest/userguide/model-lifecycle.html)
- **Gemini** — [API deprecations](https://ai.google.dev/gemini-api/docs/deprecations)

## Calendar

Download [deprecations.ics](deprecations.ics) and import it into your calendar app to get reminders 7 and 30 days before model shutdowns.

## Deprecation Schedule

<!-- DEPRECATION_TABLE_START -->

*Last updated: 2026-11-14*

### Anthropic

Note: Slack deprecation alerts disabled since we rely on Bedrock dates.

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| claude-sonnet-4-5-20250929 |  | deprecated | 2026-09-30 | 🟡 2026-11-30 | claude-sonnet-5-5 |

### Bedrock

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Claude 3 Haiku | anthropic.claude-3-haiku-20240307-v1:0 | retired | 2026-03-10 | 🔴 2026-09-10 |  |
| Claude Sonnet 4 | anthropic.claude-sonnet-4-20250514-v1:0 | retired | 2026-04-14 | 🔴 2026-10-14 |  |
| Claude 3 Sonnet | anthropic.claude-3-sonnet-20240229-v1:0 | retired | 2026-10-10 | 🔴 2026-11-13 |  |
| Claude 3.5 Sonnet | anthropic.claude-3-5-sonnet-20240620-v1:0 | retired | 2026-10-10 | 🔴 2026-11-13 |  |
| Claude 3.5 Sonnet v2 | anthropic.claude-3-5-sonnet-20241022-v2:0 | retired | 2026-10-10 | 🔴 2026-11-13 |  |
| Claude 3.7 Sonnet | anthropic.claude-3-7-sonnet-20250219-v1:0 | retired | 2026-10-10 | 🔴 2026-11-13 |  |
| Claude Opus 4.1 | anthropic.claude-opus-4-1-20250805-v1:0 | legacy | 2026-07-08 | 2027-01-08 |  |
| Gemma 3 12B IT | google.gemma-3-12b-it | legacy | 2026-09-30 | 2027-03-30 |  |
| Gemma 3 27B PT | google.gemma-3-27b-it | legacy | 2026-09-30 | 2027-03-30 |  |
| Gemma 3 4B IT | google.gemma-3-4b-it | legacy | 2026-09-30 | 2027-03-30 |  |
| Claude Sonnet 4.5 | anthropic.claude-sonnet-4-5-20250929-v1:0 | legacy | 2026-10-08 | 2027-04-08 |  |

### OpenAI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Assistants API |  | deprecated | TBD | 🔴 2026-08-26 | Aug 26, 2025 |
| Videos API |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| sora-2 |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| sora-2-pro |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| sora-2-2025-10-06 |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| sora-2-2025-12-08 |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| sora-2-pro-2025-10-06 |  | deprecated | TBD | 🔴 2026-09-24 | Mar 24, 2026 |
| gpt-3.5-turbo-instruct |  | deprecated | TBD | 🔴 2026-09-28 | Sep 26, 2025 |
| babbage-002 |  | deprecated | TBD | 🔴 2026-09-28 | Sep 26, 2025 |
| davinci-002 |  | deprecated | TBD | 🔴 2026-09-28 | Sep 26, 2025 |
| gpt-3.5-turbo-1106 |  | deprecated | TBD | 🔴 2026-09-28 | Sep 26, 2025 |
| gpt-5.4-cyber |  | deprecated | TBD | 🔴 2026-10-01 | Sep 11, 2026 |
| gpt-3.5-turbo-0125 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-3.5-turbo |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-3.5-turbo-completions |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-0613 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-0613-completions |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-completions |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-1106-preview |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-turbo |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-turbo-2024-04-09 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4-turbo-completions |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4.1-nano |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4.1-nano-2025-04-14 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-4o-2024-05-13 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| gpt-image-1 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o1-2024-12-17 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o1 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o1-pro-2025-03-19 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o1-pro |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o3-mini-2025-01-31 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o3-mini |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| ft-o4-mini-2025-04-16 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o4-mini-2025-04-16 |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| o4-mini |  | deprecated | TBD | 🔴 2026-10-23 | Apr 22, 2026 |
| /v1/prompts and reusable prompt objects |  | deprecated | TBD | 🟡 2026-11-30 | Jun 3, 2026 |
| Evals dashboard, API, and graders for eval workflows |  | deprecated | TBD | 🟡 2026-11-30 | Jun 3, 2026 |
| Agent Builder |  | deprecated | TBD | 🟡 2026-11-30 | Jun 3, 2026 |
| gpt-image-1-mini |  | deprecated | TBD | 🟡 2026-12-01 | Jun 2, 2026 |
| gpt-image-1.5 |  | deprecated | TBD | 🟡 2026-12-01 | Jun 2, 2026 |
| gpt-image-1.5-2025-12-16 |  | deprecated | TBD | 🟡 2026-12-01 | Jun 2, 2026 |
| chatgpt-image-latest |  | deprecated | TBD | 🟡 2026-12-01 | Jun 2, 2026 |
| gpt-5 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-2025-08-07 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-mini |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-mini-2025-08-07 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-nano |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-nano-2025-08-07 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-pro |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| gpt-5-pro-2025-10-06 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| o3 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| o3-2025-04-16 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| o3-pro |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| o3-pro-2025-06-10 |  | deprecated | TBD | 🟡 2026-12-11 | Jun 11, 2026 |
| tts-1 |  | deprecated | TBD | 2027-01-06 | Oct 1, 2026 |
| tts-1-hd |  | deprecated | TBD | 2027-01-06 | Oct 1, 2026 |
| gpt-4o-mini-tts |  | deprecated | TBD | 2027-01-06 | Oct 1, 2026 |
| gpt-4o-mini-tts-2025-03-20 |  | deprecated | TBD | 2027-01-06 | Oct 1, 2026 |
| gpt-4o-mini-tts-2025-12-15 |  | deprecated | TBD | 2027-01-06 | Oct 1, 2026 |
| Self-serve fine-tuning job creation |  | deprecated | TBD | 2027-01-06 | May 7, 2026 |
| GPT-4o (gpt-4o-2024-08-06, gpt-4o-2024-11-20) |  | deprecated | TBD | 2027-01-14 | Oct 14, 2026 |
| GPT-4o mini (gpt-4o-mini-2024-07-18) |  | deprecated | TBD | 2027-01-14 | Oct 14, 2026 |
| GPT-4.1 (gpt-4.1-2025-04-14) |  | deprecated | TBD | 2027-01-14 | Oct 14, 2026 |
| GPT-4.1 mini (gpt-4.1-mini-2025-04-14) |  | deprecated | TBD | 2027-01-14 | Oct 14, 2026 |
| gpt-realtime |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-realtime-2025-08-28 |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-audio |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-audio-2025-08-28 |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-4o-audio |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-4o-realtime |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-realtime-mini |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-realtime-mini-2025-12-15 |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-audio-mini |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-audio-mini-2025-12-15 |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-4o-mini-realtime |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-4o-mini-audio |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-4o-mini-transcribe-2025-03-20 |  | deprecated | TBD | 2027-01-20 | Jul 20, 2026 |
| gpt-5.5-cyber-preview |  | deprecated | TBD | 2027-02-01 | Nov 5, 2026 |
| gpt-image-2 |  | deprecated | TBD | 2027-02-10 | Nov 10, 2026 |
| gpt-image-2-2026-04-21 |  | deprecated | TBD | 2027-02-10 | Nov 10, 2026 |
| whisper-1 |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| gpt-4o-transcribe |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| gpt-4o-mini-transcribe |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| gpt-4o-mini-transcribe-2025-12-15 |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| gpt-4o-transcribe-diarize |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| /v1/audio/translations |  | deprecated | TBD | 2027-02-26 | Aug 26, 2026 |
| gpt-5.3-codex |  | deprecated | TBD | 2027-04-01 | Oct 1, 2026 |
| gpt-5.4-nano |  | deprecated | TBD | 2027-04-01 | Oct 1, 2026 |
| gpt-5.4-nano-2026-03-17 |  | deprecated | TBD | 2027-04-01 | Oct 1, 2026 |
| gpt-5.1 |  | deprecated | TBD | 2027-04-01 | Oct 1, 2026 |
| gpt-5.1-2025-11-13 |  | deprecated | TBD | 2027-04-01 | Oct 1, 2026 |

### Vertex AI

| Model | Model ID | Status | Deprecated | Shutdown | Replacement |
|-------|----------|--------|------------|----------|-------------|
| Anthropic's Claude 3 Haiku on Google Cloud | Anthropic's Claude 3 Haiku on Google Cloud | retired | 2026-02-23 | 🔴 2026-08-23 |  |
| gemini-2.5-pro | gemini-2.5-pro | retired | TBD | 🔴 2026-10-20 | gemini-3.8-flash or gemini-3.5-flash |
| gemini-2.5-flash | gemini-2.5-flash | retired | TBD | 🔴 2026-10-20 | gemini-3.8-flash or gemini-3.5-flash-lite |
| gemini-2.5-flash-lite | gemini-2.5-flash-lite | retired | TBD | 🔴 2026-10-20 | gemini-3.8-flash or gemini-3.5-flash-lite or Gemma 4 |
| gemini-3.6-flash | gemini-3.6-flash | deprecated | TBD | 🟡 2026-11-19 | gemini-3.8-flash |
| Anthropic's Claude Sonnet 4.5 on Google Cloud | Anthropic's Claude Sonnet 4.5 on Google Cloud | deprecated | 2026-09-29 | 🟡 2026-11-30 |  |
| gemini-live-2.5-flash-native-audio | gemini-live-2.5-flash-native-audio | deprecated | TBD | 🟡 2026-12-13 | gemini-3.8-live |
| gemini-3.7-flash | gemini-3.7-flash | deprecated | TBD | 2027-01-28 | gemini-3.8-flash |
| gemini-2.5-flash-image | gemini-2.5-flash-image | deprecated | TBD | 2027-03-15 | gemini-3.1-flash-lite-image |
| text-embedding-005 | text-embedding-005 | deprecated | TBD | 2027-04-01 |  |
| text-embedding-004 | text-embedding-004 | deprecated | TBD | 2027-04-01 |  |
| text-multilingual-embedding-002 | text-multilingual-embedding-002 | deprecated | TBD | 2027-04-01 |  |
| multimodalembedding@001 | multimodalembedding@001 | deprecated | TBD | 2027-04-01 |  |

<!-- DEPRECATION_TABLE_END -->

## Slack Alerts

Set the `SLACK_WEBHOOK_URL` environment variable (or GitHub Actions secret) to receive Slack notifications 7 days and 1 day before a model shutdown. Multiple webhook URLs can be provided as a comma-separated list to notify multiple channels.

Vertex AI alerts include both Google and partner models. Vertex dates are tracked separately from the Gemini API because their shutdown schedules can differ.

Use `SLACK_DISABLED_PROVIDERS` for a comma-separated list of tracked providers that should not produce Slack alerts. Anthropic is disabled by default because Bedrock lifecycle dates are used for Slack deprecation alerts; Anthropic entries remain in the tracker, calendar, and README. Set `SLACK_DISABLED_PROVIDERS` to an empty value to enable alerts for every provider.

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
