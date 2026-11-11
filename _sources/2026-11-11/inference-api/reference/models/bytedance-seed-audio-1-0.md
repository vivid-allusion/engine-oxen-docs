---
source: https://docs.oxen.ai/inference-api/reference/models/bytedance-seed-audio-1-0
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seed Audio 1.0

> Text-to-speech with voice cloning and prosody control

> [card] [Try Seed Audio 1.0 in the Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-seed-audio-1-0)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `bytedance-seed-audio-1-0`

ByteDance Seed Audio 1.0 is a text-to-speech and audio generation model. It synthesizes natural speech from a text prompt with control over voice, output format, sample rate, speed, volume, and pitch. It supports voice cloning from up to three reference audio clips, or from a single reference image.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-seed-audio-1-0) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "bytedance-seed-audio-1-0",
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
>         "model": "bytedance-seed-audio-1-0",
>         "prompt": "<prompt>",
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

> [tab] Basic parameters
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/speech \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "bytedance-seed-audio-1-0",
>   "prompt": "<prompt>",
>   "input_audios": [
>     "https://example.com/audio.mp3"
>   ],
>   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
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
>         "model": "bytedance-seed-audio-1-0",
>         "prompt": "<prompt>",
>         "input_audios": [
>             "https://example.com/audio.mp3"
>         ],
>         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
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
>   "model": "bytedance-seed-audio-1-0",
>   "prompt": "<prompt>",
>   "input_audios": [
>     "https://example.com/audio.mp3"
>   ],
>   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
>   "output_format": "mp3",
>   "sample_rate": 24000,
>   "speed": 1.0,
>   "volume": 1.0,
>   "pitch": 0,
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
>         "model": "bytedance-seed-audio-1-0",
>         "prompt": "<prompt>",
>         "input_audios": [
>             "https://example.com/audio.mp3"
>         ],
>         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
>         "output_format": "mp3",
>         "sample_rate": 24000,
>         "speed": 1.0,
>         "volume": 1.0,
>         "pitch": 0,
>         "input": "Welcome to Oxen"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/bytedance-seed-audio-1-0
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Prompt or text to synthesize. Reference audio inputs by order with @Audio1, @Audio2, @Audio3. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_audios` | `array<string>` | — | Up to 3 reference audio URLs for voice cloning (max 30s and 10MB each). Reference them in the prompt as @Audio1, @Audio2, @Audio3. Supported formats: wav, mp3, pcm, ogg\_opus. |
| `input_image` | `string` | — | Optional single reference image URL (jpeg, png, or webp, max 10MB). Incompatible with audio references. Format: uri. |
| `output_format` | `string` | `"mp3"` | Output audio file format. One of: wav, mp3, pcm, ogg\_opus. |
| `sample_rate` | `integer` | `24000` | Output sample rate in Hz. One of: 8000, 16000, 24000, 32000, 44100, 48000. |
| `speed` | `number` | `1.0` | Speech tempo multiplier (typical range 0.5-2.0). Range: 0.5 – 2.0. |
| `volume` | `number` | `1.0` | Audio amplitude multiplier (typical range 0.5-2.0). Range: 0.5 – 2.0. |
| `pitch` | `integer` | `0` | Pitch shift in semitones (range -12 to 12; 0 leaves the pitch unchanged). Range: -12 – 12. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.