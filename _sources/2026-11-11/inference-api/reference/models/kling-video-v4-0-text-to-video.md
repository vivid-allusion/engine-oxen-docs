---
source: https://docs.oxen.ai/inference-api/reference/models/kling-video-v4-0-text-to-video
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kling 4.0 - Text to Video

> Cinematic text-to-video with audio, up to 30s

> [card] [Try Kling 4.0 - Text to Video in the Workbench](https://www.oxen.ai/ai/workbench?model=kling-video-v4-0-text-to-video)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `kling-video-v4-0-text-to-video`

Kling 4.0 generates cinematic video with native audio from a text prompt, in single takes of 3 to 30 seconds at 720p or 1080p. It handles fast, complex motion and camera moves, and a prompt can lay out a sequence of events, dialogue, ambient sound, and music for the whole clip.

Choose 16:9, 9:16, 1:1, or 21:9 framing. Describe the scene, visual style, camera movement, action, and audio in the prompt; when no duration is set, the model follows a length stated in the prompt.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=kling-video-v4-0-text-to-video) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>"
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>"
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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "resolution": "1080p",
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "resolution": "1080p",
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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>"
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>"
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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "resolution": "1080p",
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "resolution": "1080p",
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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>"
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>"
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
> >   "model": "kling-video-v4-0-text-to-video",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "resolution": "1080p",
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
> >         "model": "kling-video-v4-0-text-to-video",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "resolution": "1080p",
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/kling-video-v4-0-text-to-video
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Describe the scene, style, camera movement, sequence of events, dialogue, and sound. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `aspect_ratio` | `string` | `"16:9"` | Aspect Ratio One of: 16:9, 9:16, 1:1, 21:9. |
| `resolution` | `string` | `"1080p"` | Resolution One of: 720p, 1080p. |
| `duration` | `integer` | `5` | Duration (seconds) Range: 3 – 30. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.