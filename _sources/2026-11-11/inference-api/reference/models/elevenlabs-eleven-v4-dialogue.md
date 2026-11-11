---
source: https://docs.oxen.ai/inference-api/reference/models/elevenlabs-eleven-v4-dialogue
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Eleven v4 Dialogue

> Multi-speaker dialogue audio with audio tags

> [card] [Try Eleven v4 Dialogue in the Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-eleven-v4-dialogue)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `elevenlabs-eleven-v4-dialogue`

Eleven v4 Dialogue generates a single audio clip of several voices in conversation, with natural turn-taking, interruptions, and emotional delivery across more than 90 languages.

Each line pairs a piece of text with a voice, and the model performs the exchange as one scene rather than stitching separate clips, so timing and reactions carry across speakers. Audio tags such as `[laughing]`, `[sarcastic]`, or `[interrupting]` direct the delivery line by line. It suits podcast-style conversations, audio drama, game and animation scenes, and training data for conversational speech. A request can use up to 10 distinct voices and 10,000 characters of text in total.

| Metric | Value |
| - | - |
| Context Length | 10,000 characters, 10 voices |
| Multilingual | Yes, 90+ languages |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-eleven-v4-dialogue) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-eleven-v4-dialogue",
>   "inputs": [
>     {}
>   ],
>   "input": "Welcome to Oxen"
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/audio/speech",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "elevenlabs-eleven-v4-dialogue",
>         "inputs": [
>             {}
>         ],
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

> [tab] All parameters
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-eleven-v4-dialogue",
>   "inputs": [
>     {}
>   ],
>   "stability": 0.5,
>   "similarity_boost": 0.75,
>   "input": "Welcome to Oxen"
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/audio/speech",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "elevenlabs-eleven-v4-dialogue",
>         "inputs": [
>             {}
>         ],
>         "stability": 0.5,
>         "similarity_boost": 0.75,
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/elevenlabs-eleven-v4-dialogue
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `inputs` | `array<object>` | — | The lines of the conversation in order, each spoken by its own voice. Up to 10 distinct voices and 10,000 characters in total. Audio tags in square brackets direct each line's delivery. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `language_code` | `string` | — | Optional ISO 639-1 language code (e.g. en, es, ja) to force the language and its text normalization. Leave empty to detect it from the text. |
| `stability` | `number` | `0.5` | Lower values give more varied, expressive delivery; higher values keep the performance consistent across generations. Range: 0.0 – 1.0. |
| `similarity_boost` | `number` | `0.75` | How closely each line follows its voice. Higher values match it more closely at some cost to naturalness. Range: 0.0 – 1.0. |
| `seed` | `integer` | — | Optional seed for best-effort deterministic output. Range: 0 – 4294967295. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.