---
source: https://docs.oxen.ai/inference-api/reference/models/nano-banana-2-1
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Nano Banana 2.1

> Fast 4K image generation and editing

> [card] [Try Nano Banana 2.1 in the Workbench](https://www.oxen.ai/ai/workbench?model=nano-banana-2-1)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `nano-banana-2-1`

Nano Banana 2.1 is Google's Flash-tier image generation and editing model, an update to Nano Banana 2 with better visual quality, prompt adherence, text rendering, and character consistency across edits.

It generates from a text prompt alone, or edits and fuses up to 14 reference images, keeping up to 4 characters and 10 objects consistent. Output comes at 1K, 2K, or 4K across standard and panoramic aspect ratios (up to 8:1 and 1:8), with fewer tiling artifacts on wide formats at 2K and 4K than Nano Banana 2. Images can be grounded in Google Web Search and Google Image Search for factual or current subjects, and a configurable thinking level trades latency for better handling of complex compositions.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=nano-banana-2-1) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Sync
>
> See the [image editing reference](https://docs.oxen.ai/inference-api/reference/image_editing.md) for more details.
>
> > [tab] Minimal
> >
> > ```bash cURL theme={null}
> > curl -X POST https://hub.oxen.ai/api/ai/images/edit \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>"
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/images/edit",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "nano-banana-2-1",
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
> > curl -X POST https://hub.oxen.ai/api/ai/images/edit \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ]
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/images/edit",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> > curl -X POST https://hub.oxen.ai/api/ai/images/edit \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "resolution": "2K",
> >   "google_search": false,
> >   "image_search": false,
> >   "thinking_level": "medium"
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/images/edit",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "resolution": "2K",
> >         "google_search": false,
> >         "image_search": false,
> >         "thinking_level": "medium"
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
> >   "model": "nano-banana-2-1",
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
> >         "model": "nano-banana-2-1",
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
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "resolution": "2K",
> >   "google_search": false,
> >   "image_search": false,
> >   "thinking_level": "medium"
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
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "resolution": "2K",
> >         "google_search": false,
> >         "image_search": false,
> >         "thinking_level": "medium"
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
> >   "model": "nano-banana-2-1",
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
> >         "model": "nano-banana-2-1",
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
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
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
> >   "model": "nano-banana-2-1",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "resolution": "2K",
> >   "google_search": false,
> >   "image_search": false,
> >   "thinking_level": "medium"
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
> >         "model": "nano-banana-2-1",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "resolution": "2K",
> >         "google_search": false,
> >         "image_search": false,
> >         "thinking_level": "medium"
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/nano-banana-2-1
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Text description of what you want to generate, or the instruction on how to edit the given image. Use @Image1, @Image2, etc. to reference the input images. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `input_image` | `array<string>` | — | Optional reference image(s) to edit or combine, up to 14. Leave empty to generate from the prompt alone. Reference them in the prompt as @Image1, @Image2, etc. |
| `aspect_ratio` | `string` | `"16:9"` | Aspect Ratio One of: auto, 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3, 4:5, 5:4, 21:9, 4:1, 1:4, 8:1, 1:8. |
| `resolution` | `string` | `"2K"` | Resolution One of: 1K, 2K, 4K. |
| `google_search` | `boolean` | `false` | Use live web results for current facts. |
| `image_search` | `boolean` | `false` | Use Google images as visual references. |
| `thinking_level` | `string` | `"medium"` | Higher levels handle complex scenes but run slower. One of: minimal, medium, high. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.