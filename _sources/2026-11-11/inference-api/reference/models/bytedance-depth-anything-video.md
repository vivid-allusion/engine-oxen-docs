---
source: https://docs.oxen.ai/inference-api/reference/models/bytedance-depth-anything-video
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Depth Anything Video

> Consistent depth maps from video

> [card] [Try Depth Anything Video in the Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-depth-anything-video)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `bytedance-depth-anything-video`

Estimate temporally consistent depth maps from video using Video Depth Anything.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-depth-anything-video) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

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
> >   "model": "bytedance-depth-anything-video",
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
> >         "model": "bytedance-depth-anything-video",
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
> >   "model": "bytedance-depth-anything-video",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "depth_model": "VDA-Large",
> >   "colormap": "grayscale",
> >   "resolution": "auto",
> >   "side_by_side": false,
> >   "include_raw_depths": false
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
> >         "model": "bytedance-depth-anything-video",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "depth_model": "VDA-Large",
> >         "colormap": "grayscale",
> >         "resolution": "auto",
> >         "side_by_side": false,
> >         "include_raw_depths": false
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
> >   "model": "bytedance-depth-anything-video",
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
> >         "model": "bytedance-depth-anything-video",
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
> >   "model": "bytedance-depth-anything-video",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "depth_model": "VDA-Large",
> >   "colormap": "grayscale",
> >   "resolution": "auto",
> >   "side_by_side": false,
> >   "include_raw_depths": false
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
> >         "model": "bytedance-depth-anything-video",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "depth_model": "VDA-Large",
> >         "colormap": "grayscale",
> >         "resolution": "auto",
> >         "side_by_side": false,
> >         "include_raw_depths": false
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
> >   "model": "bytedance-depth-anything-video",
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
> >         "model": "bytedance-depth-anything-video",
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
> >   "model": "bytedance-depth-anything-video",
> >   "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >   "depth_model": "VDA-Large",
> >   "colormap": "grayscale",
> >   "resolution": "auto",
> >   "side_by_side": false,
> >   "include_raw_depths": false
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
> >         "model": "bytedance-depth-anything-video",
> >         "input_video": "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4",
> >         "depth_model": "VDA-Large",
> >         "colormap": "grayscale",
> >         "resolution": "auto",
> >         "side_by_side": false,
> >         "include_raw_depths": false
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/bytedance-depth-anything-video
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_video` | `string` | — | URL of the input video to estimate depth for. Format: uri. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `depth_model` | `string` | `"VDA-Large"` | Depth estimation model size. VDA-Large = best quality, VDA-Small = fastest. One of: VDA-Small, VDA-Base, VDA-Large. |
| `colormap` | `string` | `"grayscale"` | Colormap for depth visualization. One of: grayscale, turbo, inferno, magma, viridis. |
| `resolution` | `string` | `"auto"` | Resolution One of: auto, 360p, 480p, 720p, 1080p. |
| `max_frames` | `integer` | — | Maximum number of frames to process. Leave unset to process all frames. |
| `output_fps` | `number` | — | Output video FPS. Leave unset to use the input frame rate. |
| `side_by_side` | `boolean` | `false` | If true, output a side-by-side original and depth comparison video. |
| `include_raw_depths` | `boolean` | `false` | If true, exports raw float32 depths as an NPZ file. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.