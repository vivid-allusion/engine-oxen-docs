---
source: https://docs.oxen.ai/inference-api/reference/models/qwen-image-edit-plus
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image Edit - 2509

> Multi-image natural-language editing

> [card] [Try Qwen Image Edit - 2509 in the Workbench](https://www.oxen.ai/ai/workbench?model=qwen-image-edit-plus)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `qwen-image-edit-plus`

Qwen/Qwen-Image-Edit-Plus is a 20B parameter image generation model designed for complex image editing, with particular strengths in multi-image manipulation and high-fidelity text and style preservation.

It excels in blending up to three images while maintaining critical details like facial features, text consistency, and product textures. The model supports both semantic and appearance-level edits, advanced bilingual (Chinese and English) text editing directly on images, and robust preservation of original style elements such as color, lighting, and font.

Some other noteworthy features of Qwen/Qwen-Image-Edit-Plus include native ControlNet integration for depth, edge, and keypoint mapping, making it suitable for professional portrait retouching, e-commerce product visualization, complex multi-subject compositions, and precise creative tasks like meme and marketing material generation.

| Metric | Value |
| - | - |
| Parameter Count | 20 billion |
| Mixture of Experts | No |
| Multilingual | Yes |
| Quantized\* | No |

\**Quantization is specific to the inference provider and the model may be offered with different quantization levels by other providers.*

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=qwen-image-edit-plus) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

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
> >   "model": "qwen-image-edit-plus",
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
> >         "model": "qwen-image-edit-plus",
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
> >   "model": "qwen-image-edit-plus",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "output_format": "png"
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
> >         "model": "qwen-image-edit-plus",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "output_format": "png"
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
> >   "model": "qwen-image-edit-plus",
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
> >         "model": "qwen-image-edit-plus",
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
> >   "model": "qwen-image-edit-plus",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "output_format": "png"
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
> >         "model": "qwen-image-edit-plus",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "output_format": "png"
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
> >   "model": "qwen-image-edit-plus",
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
> >         "model": "qwen-image-edit-plus",
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
> >   "model": "qwen-image-edit-plus",
> >   "prompt": "<prompt>",
> >   "input_image": [
> >     "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >   ],
> >   "aspect_ratio": "16:9",
> >   "output_format": "png"
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
> >         "model": "qwen-image-edit-plus",
> >         "prompt": "<prompt>",
> >         "input_image": [
> >             "https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"
> >         ],
> >         "aspect_ratio": "16:9",
> >         "output_format": "png"
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/qwen-image-edit-plus
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Text description of what you want to generate, or the instruction on how to edit the given image. Use @Image1, @Image2, etc. to reference the input images. |
| `input_image` | `array<string>` | — | Input images to transform or use as reference. Reference them in the prompt as @Image1, @Image2, etc. |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `aspect_ratio` | `string` | `"16:9"` | Aspect Ratio One of: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3. |
| `negative_prompt` | `string` | — | Negative prompt for generated image |
| `output_format` | `string` | `"png"` | Format of the output images One of: webp, jpg, png. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.