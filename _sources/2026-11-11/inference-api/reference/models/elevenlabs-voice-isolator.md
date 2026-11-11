---
source: https://docs.oxen.ai/inference-api/reference/models/elevenlabs-voice-isolator
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Eleven Voice Isolator

> Remove background noise and music from speech

> [card] [Try Eleven Voice Isolator in the Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-voice-isolator)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `elevenlabs-voice-isolator`

Eleven Voice Isolator extracts clean speech from a recording, removing background noise, music, reverb, and ambient sound.

It keeps the speaker's voice and delivery intact while stripping everything around it, which makes it useful for cleaning up field and phone recordings, preparing voiceover, rescuing interview audio, and cleaning speech before transcription or voice cloning.

| Metric | Value |
| - | - |
| Min Input | 4.6 seconds |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-voice-isolator) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -d '{
  "model": "elevenlabs-voice-isolator",
  "input_audio": "https://example.com/audio.mp3",
  "input": "Welcome to Oxen"
}'
```

```python Python theme={null}
import os
import requests

response = requests.post(
    "https://hub.oxen.ai/api/ai/audio/speech",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
    },
    json={
        "model": "elevenlabs-voice-isolator",
        "input_audio": "https://example.com/audio.mp3",
        "input": "Welcome to Oxen"
    },
)
response.raise_for_status()
print(response.json())
```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/elevenlabs-voice-isolator
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_audio` | `string` | — | Recording to clean up, between 4.6 seconds and 1 hour long. Format: uri. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.