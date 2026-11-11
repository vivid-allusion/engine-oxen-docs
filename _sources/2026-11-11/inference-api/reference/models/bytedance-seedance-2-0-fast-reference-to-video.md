---
source: https://docs.oxen.ai/inference-api/reference/models/bytedance-seedance-2-0-fast-reference-to-video
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Seedance 2.0 Fast - Reference to Video

> Fast reference-guided video generation

> [card] [Try Seedance 2.0 Fast - Reference to Video in the Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-seedance-2-0-fast-reference-to-video)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `bytedance-seedance-2-0-fast-reference-to-video`

ByteDance Seedance 2.0 Fast generates video from a text prompt guided by reference images, videos, and audio. Supports 480p and 720p output.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=bytedance-seedance-2-0-fast-reference-to-video) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>"
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ]
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ]
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ],
> >   "generate_audio": true,
> >   "aspect_ratio": "16:9",
> >   "duration": -1,
> >   "resolution": "720p",
> >   "watermark": false
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ],
> >         "generate_audio": true,
> >         "aspect_ratio": "16:9",
> >         "duration": -1,
> >         "resolution": "720p",
> >         "watermark": false
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
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
> > [tab] Basic parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ]
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ]
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ],
> >   "generate_audio": true,
> >   "aspect_ratio": "16:9",
> >   "duration": -1,
> >   "resolution": "720p",
> >   "watermark": false
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ],
> >         "generate_audio": true,
> >         "aspect_ratio": "16:9",
> >         "duration": -1,
> >         "resolution": "720p",
> >         "watermark": false
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
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
> > [tab] Basic parameters
> >
> > ```bash cURL theme={null}
> > # Enqueue, capture the generation id.
> > GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ]
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ]
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
> >   "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >   "prompt": "<prompt>",
> >   "input_face_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_images": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "input_face_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_videos": [
> >     "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >   ],
> >   "input_audios": [
> >     "https://example.com/audio.mp3"
> >   ],
> >   "generate_audio": true,
> >   "aspect_ratio": "16:9",
> >   "duration": -1,
> >   "resolution": "720p",
> >   "watermark": false
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
> >         "model": "bytedance-seedance-2-0-fast-reference-to-video",
> >         "prompt": "<prompt>",
> >         "input_face_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_images": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "input_face_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_videos": [
> >             "https://hub.oxen.ai/api/repos/ox/Oxen-AI-Assets/file/main/images/winter_summer_ox.mp4"
> >         ],
> >         "input_audios": [
> >             "https://example.com/audio.mp3"
> >         ],
> >         "generate_audio": true,
> >         "aspect_ratio": "16:9",
> >         "duration": -1,
> >         "resolution": "720p",
> >         "watermark": false
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/bytedance-seedance-2-0-fast-reference-to-video
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | The text prompt used to generate the video. Use @Image1, @Image2, @Video1, @Audio1, etc. to reference inputs. Face-containing media is indexed before non-face media within its type. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_face_images` | `array<string>` | — | Place reference images here when they show faces, people, or characters. Content filters may block the request otherwise. |
| `input_images` | `array<string>` | — | Reference images that guide the generated video. Up to 9 total reference images and up to 15 total references across all types may be used. |
| `input_face_videos` | `array<string>` | — | Place reference videos here when they show faces, people, or characters. Content filters may block the request otherwise. |
| `input_videos` | `array<string>` | — | Reference videos that guide the generated video. Up to 3 total reference videos and up to 15 total references across all types may be used. |
| `input_audios` | `array<string>` | — | Reference audios that guide the generated video. Up to 3 reference audio clips, each 2-15 seconds long with a combined duration of at most 15 seconds, and up to 15 total references across all types may be used. |
| `generate_audio` | `boolean` | `true` | Whether to generate synchronized audio. |
| `aspect_ratio` | `string` | `"16:9"` | Aspect Ratio One of: adaptive, 21:9, 16:9, 4:3, 1:1, 3:4, 9:16. |
| `duration` | `integer` | `-1` | Duration Range: 4 – 15. |
| `resolution` | `string` | `"720p"` | Resolution One of: 480p, 720p. |
| `watermark` | `boolean` | `false` | Whether to add an 'AI generated' watermark to the output. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.