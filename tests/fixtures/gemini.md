> ## AI Agent Context
> Get the complete documentation index at: https://aistudio.google.com/llms.txt
> Use this file to discover all available pages.

# Gemini deprecations

This page lists the known deprecation schedules for [stable
(GA)](/docs/models#stable) models in the Gemini API.

{% callout type="note" %}
  Note: The **shutdown dates listed in the table indicate the *earliest possible
  dates* on which a model might be retired**.

  * This list item sits outside every table and must not be read as a cell.

{% /callout %}

## Gemini 3 models  {% id="gemini-3-models" %}

{% table %}
  * Model
  * Release date
  * Shutdown date
  * Recommended replacement

  ---

  * `gemini-3.8-flash-tts`
  * September 22, 2026
  * No shutdown date announced
  * 

  ---

  * `gemini-3.7-flash`
  * August 13, 2026
  * N/A
  * `gemini-3.8-flash` (`gemini-3.7-flash` is no longer available in Google AI Studio; the endpoint is not shutting down and automatically routes API requests to `gemini-3.8-flash`)

  ---

  * `gemini-3.1-flash-lite`
  * May 7, 2026
  * May 7, 2027
  * `gemini-3.5-flash-lite`
{% /table %}

### Deprecated models  {% id="gemini-3-deprecated-models" %}

{% table %}
  * Model
  * Release date
  * Shutdown date
  * Recommended replacement

  ---

  * `embedding-001`
  * April 9, 2024
  * October 30, 2025
  * `gemini-embedding-2`

  ---

  * `embedding-gecko-001`
  * 
  * October 30, 2025
  * `gemini-embedding-2`
{% /table %}

## Veo models  {% id="veo-models" %}

### Deprecated models  {% id="veo-deprecated-models" %}

{% table %}
  * Model
  * Release date
  * Shutdown date
  * Recommended replacement

  ---

  * `veo-3.0-generate-001`
  * September 9, 2025
  * June 30, 2026
  * `gemini-omni-1.1-flash` or the GA models on the [Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/veo/3-1-generate)
{% /table %}
