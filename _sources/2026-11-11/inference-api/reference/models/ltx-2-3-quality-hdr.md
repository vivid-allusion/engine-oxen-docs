---
source: https://docs.oxen.ai/inference-api/reference/models/ltx-2-3-quality-hdr
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LTX 2.3 Quality: Video to HDR

> Lift SDR video into HDR

> [card] [Try LTX 2.3 Quality: Video to HDR in the Workbench](https://www.oxen.ai/ai/workbench?model=ltx-2-3-quality-hdr)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `ltx-2-3-quality-hdr`

LTX 2.3 Quality (Video to HDR) is the HDR preset of Lightricks LTX-2.3 on fal, lifting a standard dynamic range (SDR) input video into high dynamic range using an IC-LoRA HDR workflow guided by a text prompt. The official Lightricks HDR workflow is video-conditioned, so an input video is required.

The model returns an MP4 preview of the HDR result for quick inspection alongside a ZIP archive of 16-bit EXR frames (one per output frame) for downstream compositing and grading. Output is generated at up to roughly 720p (shorter side capped at 704px); larger requested sizes are scaled down while preserving aspect ratio. It exposes a quality preset control and supports up to 481 frames at 1 to 60 FPS.

| Metric | Value |
| - | - |
| Parameter Count | 22 billion |
| Mixture of Experts | No |

\**Quantization is specific to the inference provider and the model may be offered with different quantization levels by other providers.*

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=ltx-2-3-quality-hdr) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Sync
>
> This blocks until the video is ready (typically 5-15 minutes). Prefer **Async** or **Async with SSE** for anything beyond quick experimentation.
>
> See the [video generation reference](https://docs.oxen.ai/inference-api/reference/video_generation.md) for more details.
>
> > [tab] Minimal
> >
> > ```bash cURL theme={null}
> > curl -X POST https://hub.oxen.ai/api/ai/videos/generate \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/videos/generate",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >     },
> > )
> > response.raise_for_status()
> > print(response.json())
> > ```
>
> > [tab] All parameters
> >
> > ```bash cURL theme={null}
> > curl -X POST https://hub.oxen.ai/api/ai/videos/generate \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "num_frames": 121,
> >   "generate_audio": true,
> >   "resolution": "auto",
> >   "frames_per_second": 24,
> >   "video_quality": "high"
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/videos/generate",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "num_frames": 121,
> >         "generate_audio": true,
> >         "resolution": "auto",
> >         "frames_per_second": 24,
> >         "video_quality": "high"
> >     },
> > )
> > response.raise_for_status()
> > print(response.json())
> > ```

> [tab] Async
>
> See the [async queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md) for more details.
>
> > [tab] Minimal
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> > }' | jq -r '.generations[0].generation_id')
> >
> > # Poll until the generation reaches a terminal status.
> > while true; do
> >   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
> >     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
> >   echo "Status: $STATUS"
> >   case $STATUS in succeeded|failed|cancelled) break;; esac
> >   sleep 5
> > done
> >
> > # Print the result.
> > curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
> >   "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq .
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import time
> > import requests
> >
> > HEADERS = {
> >     "Content-Type": "application/json",
> >     "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> > }
> >
> > enqueue = requests.post(
> >     "https://hub.oxen.ai/api/ai/queue",
> >     headers=HEADERS,
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >     },
> > )
> > enqueue.raise_for_status()
> > generation_id = enqueue.json()["generations"][0]["generation_id"]
> >
> > while True:
> >     data = requests.get(
> >         f"https://hub.oxen.ai/api/ai/queue/{generation_id}",
> >         headers=HEADERS,
> >     ).json()
> >     if data["status"] in {"succeeded", "failed", "cancelled"}:
> >         break
> >     time.sleep(5)
> >
> > if data["status"] == "succeeded":
> >     print(f"Result: {data['result_url']}")
> > else:
> >     print(f"Generation {data['status']}: {data.get('error_message')}")
> > ```
>
> > [tab] All parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "num_frames": 121,
> >   "generate_audio": true,
> >   "resolution": "auto",
> >   "frames_per_second": 24,
> >   "video_quality": "high"
> > }' | jq -r '.generations[0].generation_id')
> >
> > # Poll until the generation reaches a terminal status.
> > while true; do
> >   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
> >     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
> >   echo "Status: $STATUS"
> >   case $STATUS in succeeded|failed|cancelled) break;; esac
> >   sleep 5
> > done
> >
> > # Print the result.
> > curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
> >   "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq .
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import time
> > import requests
> >
> > HEADERS = {
> >     "Content-Type": "application/json",
> >     "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> > }
> >
> > enqueue = requests.post(
> >     "https://hub.oxen.ai/api/ai/queue",
> >     headers=HEADERS,
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "num_frames": 121,
> >         "generate_audio": true,
> >         "resolution": "auto",
> >         "frames_per_second": 24,
> >         "video_quality": "high"
> >     },
> > )
> > enqueue.raise_for_status()
> > generation_id = enqueue.json()["generations"][0]["generation_id"]
> >
> > while True:
> >     data = requests.get(
> >         f"https://hub.oxen.ai/api/ai/queue/{generation_id}",
> >         headers=HEADERS,
> >     ).json()
> >     if data["status"] in {"succeeded", "failed", "cancelled"}:
> >         break
> >     time.sleep(5)
> >
> > if data["status"] == "succeeded":
> >     print(f"Result: {data['result_url']}")
> > else:
> >     print(f"Generation {data['status']}: {data.get('error_message')}")
> > ```

> [tab] Async with SSE
>
> See the [async queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md) for more details.
>
> > [tab] Minimal
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> > }' | jq -r '.generations[0].generation_id')
> >
> > # Stream the SSE channel, grab the data line that follows a
> > # media_generation_completed event for our id, and pretty-print it.
> > curl -sN -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/events \
> >   | awk -v id="$GEN_ID" '
> >     /^event: media_generation_completed$/ { expect=1; next }
> >     /^data: / && expect {
> >       payload = substr($0, 7)
> >       if (index(payload, "\"generation_id\":\"" id "\"")) { print payload; exit }
> >       expect = 0
> >     }
> >   ' | jq .
> > ```
> >
> > ```python Python theme={null}
> > import json
> > import os
> > import requests
> >
> > API_KEY = os.environ["OXEN_API_KEY"]
> > AUTH = {"Authorization": f"Bearer {API_KEY}"}
> >
> > enqueue = requests.post(
> >     "https://hub.oxen.ai/api/ai/queue",
> >     headers={**AUTH, "Content-Type": "application/json"},
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >     },
> > )
> > enqueue.raise_for_status()
> > generation_id = enqueue.json()["generations"][0]["generation_id"]
> >
> > with requests.get(
> >     "https://hub.oxen.ai/api/events",
> >     headers=AUTH,
> >     stream=True,
> > ) as stream:
> >     event_name = None
> >     for line in stream.iter_lines(decode_unicode=True):
> >         if line.startswith("event: "):
> >             event_name = line.removeprefix("event: ")
> >         elif line.startswith("data: ") and event_name == "media_generation_completed":
> >             payload = json.loads(line.removeprefix("data: "))
> >             if payload.get("generation_id") == generation_id:
> >                 print(payload)
> >                 break
> > ```
>
> > [tab] All parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "ltx-2-3-quality-hdr",
> >   "prompt": "<prompt>",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "num_frames": 121,
> >   "generate_audio": true,
> >   "resolution": "auto",
> >   "frames_per_second": 24,
> >   "video_quality": "high"
> > }' | jq -r '.generations[0].generation_id')
> >
> > # Stream the SSE channel, grab the data line that follows a
> > # media_generation_completed event for our id, and pretty-print it.
> > curl -sN -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/events \
> >   | awk -v id="$GEN_ID" '
> >     /^event: media_generation_completed$/ { expect=1; next }
> >     /^data: / && expect {
> >       payload = substr($0, 7)
> >       if (index(payload, "\"generation_id\":\"" id "\"")) { print payload; exit }
> >       expect = 0
> >     }
> >   ' | jq .
> > ```
> >
> > ```python Python theme={null}
> > import json
> > import os
> > import requests
> >
> > API_KEY = os.environ["OXEN_API_KEY"]
> > AUTH = {"Authorization": f"Bearer {API_KEY}"}
> >
> > enqueue = requests.post(
> >     "https://hub.oxen.ai/api/ai/queue",
> >     headers={**AUTH, "Content-Type": "application/json"},
> >     json={
> >         "model": "ltx-2-3-quality-hdr",
> >         "prompt": "<prompt>",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "num_frames": 121,
> >         "generate_audio": true,
> >         "resolution": "auto",
> >         "frames_per_second": 24,
> >         "video_quality": "high"
> >     },
> > )
> > enqueue.raise_for_status()
> > generation_id = enqueue.json()["generations"][0]["generation_id"]
> >
> > with requests.get(
> >     "https://hub.oxen.ai/api/events",
> >     headers=AUTH,
> >     stream=True,
> > ) as stream:
> >     event_name = None
> >     for line in stream.iter_lines(decode_unicode=True):
> >         if line.startswith("event: "):
> >             event_name = line.removeprefix("event: ")
> >         elif line.startswith("data: ") and event_name == "media_generation_completed":
> >             payload = json.loads(line.removeprefix("data: "))
> >             if payload.get("generation_id") == generation_id:
> >                 print(payload)
> >                 break
> > ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/ltx-2-3-quality-hdr
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | The prompt to guide generation. |
| `input_video` | `string` | — | SDR input video to lift into HDR. The official Lightricks HDR workflow is video-conditioned. Format: uri. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `num_frames` | `integer` | `121` | The number of frames to generate. Range: 9 – 481. |
| `generate_audio` | `boolean` | `true` | Whether to include audio in the returned video. When disabled, the final MP4 is returned without an audio track. |
| `resolution` | `string` | `"auto"` | Resolution One of: auto, square\_hd, square, portrait\_4\_3, portrait\_16\_9, landscape\_4\_3, landscape\_16\_9. |
| `frames_per_second` | `number` | `24` | Frames per second of the generated video. Range: 1 – 60. |
| `video_quality` | `string` | `"high"` | The quality preset of the generated video. One of: low, medium, high, maximum. |
| `negative_prompt` | `string` | — | The negative prompt to steer generation away from. |
| `seed` | `integer` | — | Random seed for reproducibility. If None, a random seed is chosen. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.