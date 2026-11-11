---
source: https://docs.oxen.ai/inference-api/reference/models/elevenlabs-scribe-v2
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Scribe v2

> Speech-to-text with diarization, 90+ languages

> [card] [Try Scribe v2 in the Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-scribe-v2)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `elevenlabs-scribe-v2`

Scribe v2 is a speech-to-text model that transcribes audio and video in more than 90 languages with word-level timestamps and speaker diarization.

It labels up to 32 speakers, tags non-speech events such as laughter or applause, and detects entities like names, numbers, and medical or financial terms with their timestamps. Keyterm prompting biases recognition toward product names, jargon, or proper nouns, and a no-verbatim mode drops filler words and false starts. It suits meeting and interview transcripts, subtitles, podcast and video indexing, and labeling speech datasets. Files can run up to 10 hours.

| Metric | Value |
| - | - |
| Max Input | 10 hours |
| Multilingual | Yes, 90+ languages |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=elevenlabs-scribe-v2) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/transcriptions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-scribe-v2",
>   "input_audio": "https://example.com/audio.mp3",
>   "audio_url": "https://example.com/audio.mp3"
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/audio/transcriptions",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "elevenlabs-scribe-v2",
>         "input_audio": "https://example.com/audio.mp3",
>         "audio_url": "https://example.com/audio.mp3"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

> [tab] All parameters
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/audio/transcriptions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "elevenlabs-scribe-v2",
>   "input_audio": "https://example.com/audio.mp3",
>   "diarize": false,
>   "timestamps_granularity": "word",
>   "tag_audio_events": true,
>   "no_verbatim": false,
>   "audio_url": "https://example.com/audio.mp3"
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/audio/transcriptions",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "elevenlabs-scribe-v2",
>         "input_audio": "https://example.com/audio.mp3",
>         "diarize": false,
>         "timestamps_granularity": "word",
>         "tag_audio_events": true,
>         "no_verbatim": false,
>         "audio_url": "https://example.com/audio.mp3"
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/elevenlabs-scribe-v2
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_audio` | `string` | — | Audio or video file to transcribe. Most audio and video formats are supported. Format: uri. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `language_code` | `string` | — | Optional ISO 639-1 or 639-3 language code of the audio. Leave empty to detect it. |
| `diarize` | `boolean` | `false` | Label which speaker is talking for each word. |
| `num_speakers` | `integer` | — | Maximum number of speakers in the audio, if known. Helps diarization. Range: 1 – 32. |
| `timestamps_granularity` | `string` | `"word"` | Timestamp detail in the transcript. One of: none, word, character. |
| `tag_audio_events` | `boolean` | `true` | Mark non-speech sounds such as (laughter) or (applause) in the transcript. |
| `no_verbatim` | `boolean` | `false` | Remove filler words, false starts, and non-speech sounds from the transcript. |
| `keyterms` | `array<string>` | — | Words or phrases to recognize more accurately, such as product names or jargon. Up to 1,000 terms. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.