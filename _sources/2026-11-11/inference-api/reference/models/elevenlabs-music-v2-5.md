---
source: https://docs.oxen.ai/inference-api/reference/models/elevenlabs-music-v2-5
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Eleven Music v2.5

> Full songs with vocals or instrumental from text

> [card] [Try Eleven Music v2.5 in the Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-music-v2-5)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `elevenlabs-music-v2-5`

Eleven Music v2.5 generates complete songs from a text prompt, with or without vocals, in any genre and in multiple languages.

Describe the genre, mood, instrumentation, tempo, and structure in natural language, and optionally supply your own lyrics. Tracks run from 3 seconds to 10 minutes, and an instrumental switch guarantees no vocals for background and score use. Compared with Music v2 it improves prompt adherence and gives richer melodies and more layered arrangements, with the largest gains in vocal-led and acoustic genres. Output is 44.1 kHz stereo.

| Metric | Value |
| - | - |
| Max Output | 10 minutes |
| Multilingual | Yes (vocals in English, Spanish, German, Japanese, and more) |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-music-v2-5) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-music-v2-5",
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
>         "model": "elevenlabs-music-v2-5",
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
>   "model": "elevenlabs-music-v2-5",
>   "prompt": "<prompt>",
>   "duration": 30,
>   "force_instrumental": false,
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
>         "model": "elevenlabs-music-v2-5",
>         "prompt": "<prompt>",
>         "duration": 30,
>         "force_instrumental": false,
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/elevenlabs-music-v2-5
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Describe the song: genre, mood, instruments, tempo, vocals, and structure. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `lyrics_text` | `string` | — | Optional lyrics to sing. Leave empty to let the model write lyrics from the prompt. |
| `duration` | `integer` | `30` | Duration Range: 3 – 600. |
| `force_instrumental` | `boolean` | `false` | Guarantee an instrumental track with no vocals. Cannot be combined with lyrics. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.