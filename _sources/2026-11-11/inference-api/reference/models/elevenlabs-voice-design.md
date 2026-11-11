---
source: https://docs.oxen.ai/inference-api/reference/models/elevenlabs-voice-design
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Eleven Voice Design

> Design new voices from a text description

> [card] [Try Eleven Voice Design in the Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-voice-design)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `elevenlabs-voice-design`

Eleven Voice Design creates a new synthetic voice from a written description and returns three takes of it speaking your sample text.

Describe age, gender, accent, tone, pacing, and character, such as "a raspy older sea captain with a warm Scottish accent, slow and amused", and each run gives three distinct interpretations to choose from. It suits casting character voices for games and animation, narrators for a brand, and voices for synthetic speech data without recording anyone.

| Metric | Value |
| - | - |
| Outputs | 3 previews per run |
| Multilingual | Yes, 70+ languages |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-voice-design) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-voice-design",
>   "voice_description": "<voice_description>",
>   "prompt": "<prompt>",
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
>         "model": "elevenlabs-voice-design",
>         "voice_description": "<voice_description>",
>         "prompt": "<prompt>",
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
>   "model": "elevenlabs-voice-design",
>   "voice_description": "<voice_description>",
>   "prompt": "<prompt>",
>   "guidance_scale": 5,
>   "loudness": 0.5,
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
>         "model": "elevenlabs-voice-design",
>         "voice_description": "<voice_description>",
>         "prompt": "<prompt>",
>         "guidance_scale": 5,
>         "loudness": 0.5,
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/elevenlabs-voice-design
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `voice_description` | `string` | — | Describe the voice: age, gender, accent, tone, pacing, and character. |
| `prompt` | `string` | — | What the new voice says in its previews, 100 to 1,000 characters. Billed per character. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `guidance_scale` | `number` | `5` | How closely the voice follows the description. Higher values follow it more strictly at some cost to audio quality. Range: 0 – 100. |
| `loudness` | `number` | `0.5` | Volume of the previews, from -1 (quietest) to 1 (loudest). Range: -1 – 1. |
| `seed` | `integer` | — | Optional seed. The same seed and inputs give the same voices. Range: 0 – 2147483647. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.