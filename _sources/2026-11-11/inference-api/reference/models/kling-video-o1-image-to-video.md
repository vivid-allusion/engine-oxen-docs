---
source: https://docs.oxen.ai/inference-api/reference/models/kling-video-o1-image-to-video
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling O1 - Image to Video

> Cinematic image-to-video generation

> [card] [Try Kling O1 - Image to Video in the Workbench](https://www.oxen.ai/ai/workbench?model=kling-video-o1-image-to-video)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `kling-video-o1-image-to-video`

Kling O1 - Image to Video is a diffusion-based **multimodal video generation model** designed for turning images (optionally combined with text and other visual references) into short, coherent video clips.

It excels in **image-to-video generation** where a single image or a small set of reference images is transformed into cinematic clips with stable characters, controlled motion, and consistent environments, while respecting prompts for style, mood, and camera movement.

Some other noteworthy features of Kling O1 - Image to Video include support for multiple image references (up to 7 in some workflows) to refine character identity and scene details, and controls such as start/end frame specification and motion/camera behavior guidance to achieve smoother, more intentional transitions and storytelling shots.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=kling-video-o1-image-to-video) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >     },
> > )
> > response.raise_for_status()
> > print(response.json())
> > ```
>
> > [tab] Basic parameters
> >
> > ```bash cURL theme={null}
> > curl -X POST https://hub.oxen.ai/api/ai/videos/generate \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "duration": 5
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "duration": 5
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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> > [tab] Basic parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "duration": 5
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "duration": 5
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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> > [tab] Basic parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >   "model": "kling-video-o1-image-to-video",
> >   "prompt": "<prompt>",
> >   "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >   "duration": 5
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
> >         "model": "kling-video-o1-image-to-video",
> >         "prompt": "<prompt>",
> >         "input_image": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "tail_image_url": "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png",
> >         "duration": 5
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/kling-video-o1-image-to-video
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Text description of what you want to generate, or the instruction on how to edit the given image. |
| `input_image` | `string` | — | Image to use as reference. Must be jpeg, png, gif, or webp. Format: uri. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `tail_image_url` | `string` | — | Image to use as reference. Must be jpeg, png, gif, or webp. Format: uri. |
| `duration` | `integer` | `5` | Duration (seconds) Range: 5 – 10. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.