---
source: https://docs.oxen.ai/inference-api/reference/models/qwen-image
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Qwen Image

> Text-to-image with strong text rendering

> [card] [Try Qwen Image in the Workbench](https://www.oxen.ai/ai/workbench?model=qwen-image)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `qwen-image`

Qwen/Qwen-Image is an image generation model that excels in **complex text rendering**—including for both alphabetic and logographic languages such as English and Chinese—and **precise image editing**.

It is particularly strong in producing images with high-fidelity embedded text, making it well-suited for tasks where maintaining the integrity and clarity of text within generated images is critical. The model also provides consistent and realistic editing capabilities, such as style transfer, object addition/removal, and detailed attribute editing, with improved preservation of identity for people and products.

Some other noteworthy features of Qwen/Qwen-Image include robust support for image understanding tasks—such as object detection, semantic segmentation, depth and edge estimation, novel view synthesis, and super-resolution—and native integration with ControlNet for enhanced conditioning and control of outputs.

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
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=qwen-image) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Sync
>
> See the [image generation reference](https://docs.oxen.ai/inference-api/reference/image_generation.md) for more details.
>
> > [tab] Minimal
> >
> > ```bash cURL theme={null}
> > curl -X POST https://hub.oxen.ai/api/ai/images/generate \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "qwen-image",
> >   "prompt": "<prompt>"
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/images/generate",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "qwen-image",
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
> > curl -X POST https://hub.oxen.ai/api/ai/images/generate \
> >   -H "Content-Type: application/json" \
> >   -H "Authorization: Bearer $OXEN_API_KEY" \
> >   -d '{
> >   "model": "qwen-image",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "image_size": "optimize_for_quality",
> >   "num_inference_steps": 30,
> >   "guidance": 3,
> >   "output_format": "jpg",
> >   "output_quality": 80,
> >   "disable_safety_checker": false
> > }'
> > ```
> >
> > ```python Python theme={null}
> > import os
> > import requests
> >
> > response = requests.post(
> >     "https://hub.oxen.ai/api/ai/images/generate",
> >     headers={
> >         "Content-Type": "application/json",
> >         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
> >     },
> >     json={
> >         "model": "qwen-image",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "image_size": "optimize_for_quality",
> >         "num_inference_steps": 30,
> >         "guidance": 3,
> >         "output_format": "jpg",
> >         "output_quality": 80,
> >         "disable_safety_checker": false
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
> >   "model": "qwen-image",
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
> >         "model": "qwen-image",
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
> >   "model": "qwen-image",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "image_size": "optimize_for_quality",
> >   "num_inference_steps": 30,
> >   "guidance": 3,
> >   "output_format": "jpg",
> >   "output_quality": 80,
> >   "disable_safety_checker": false
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
> >         "model": "qwen-image",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "image_size": "optimize_for_quality",
> >         "num_inference_steps": 30,
> >         "guidance": 3,
> >         "output_format": "jpg",
> >         "output_quality": 80,
> >         "disable_safety_checker": false
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
> >   "model": "qwen-image",
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
> >         "model": "qwen-image",
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
> >   "model": "qwen-image",
> >   "prompt": "<prompt>",
> >   "aspect_ratio": "16:9",
> >   "image_size": "optimize_for_quality",
> >   "num_inference_steps": 30,
> >   "guidance": 3,
> >   "output_format": "jpg",
> >   "output_quality": 80,
> >   "disable_safety_checker": false
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
> >         "model": "qwen-image",
> >         "prompt": "<prompt>",
> >         "aspect_ratio": "16:9",
> >         "image_size": "optimize_for_quality",
> >         "num_inference_steps": 30,
> >         "guidance": 3,
> >         "output_format": "jpg",
> >         "output_quality": 80,
> >         "disable_safety_checker": false
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/qwen-image
```

## Request parameters

### Required parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `prompt` | `string` | — | Prompt for generated image |

### Optional parameters

| Field | Type | Default | Description |
| - | - | - | - |
| `negative_prompt` | `string` | — | Negative prompt for generated image |
| `aspect_ratio` | `string` | `"16:9"` | Aspect Ratio One of: 1:1, 16:9, 9:16, 4:3, 3:4, 3:2, 2:3. |
| `image_size` | `string` | `"optimize_for_quality"` | Image size for the generated image One of: optimize\_for\_quality, optimize\_for\_speed. |
| `num_inference_steps` | `integer` | `30` | Number of denoising steps. Recommended range is 28-50, and lower number of steps produce lower quality outputs, faster. Range: 1 – 50. |
| `guidance` | `number` | `3` | Guidance for generated image. Lower values can give more realistic images. Good values to try are 2, 2.5, 3 and 3.5 Range: 0 – 10. |
| `seed` | `integer` | — | Random seed. Set for reproducible generation |
| `output_format` | `string` | `"jpg"` | Format of the output images One of: webp, jpg, png. |
| `output_quality` | `integer` | `80` | Quality when saving the output images, from 0 to 100. 100 is best quality, 0 is lowest quality. Not relevant for .png outputs Range: 0 – 100. |
| `disable_safety_checker` | `boolean` | `false` | Disable safety checker for generated images. |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.