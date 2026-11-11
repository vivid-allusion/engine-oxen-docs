---
title: "Image Generation"
source: https://docs.oxen.ai/inference-api/quickstart/image-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Image Generation

> Generate images from text prompts in minutes

Generate images with the Oxen.ai API. Each request returns a generation ID right away, and you poll
it until the image is ready, usually in under 30 seconds.

## Generate an image

> [tab] Python
>
> ```python theme={null}
> import os
> import requests
> import time
>
> HEADERS = {
>     "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     "Content-Type": "application/json",
> }
>
> enqueue = requests.post(
>     "https://hub.oxen.ai/api/ai/queue",
>     headers=HEADERS,
>     json={
>         "model": "gpt-image-2-5-sunburst",
>         "prompt": "A red cube on a white background, minimal",
>     },
> )
> enqueue.raise_for_status()
> generation_id = enqueue.json()["generations"][0]["generation_id"]
> print(f"Enqueued {generation_id}")
>
> while True:
>     data = requests.get(
>         f"https://hub.oxen.ai/api/ai/queue/{generation_id}",
>         headers=HEADERS,
>     ).json()
>     print(f"  {data['status']}")
>     if data["status"] in {"succeeded", "failed", "cancelled"}:
>         break
>     time.sleep(3)
>
> if data["status"] != "succeeded":
>     raise SystemExit(f"{data['status']}: {data['error_message']}")
>
> with open("output.png", "wb") as f:
>     f.write(requests.get(data["result_url"]).content)
> print("Saved output.png")
> ```

> [tab] cURL
>
> ```bash Start the generation theme={null}
> GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "model": "gpt-image-2-5-sunburst",
>     "prompt": "A red cube on a white background, minimal"
>   }' | jq -r '.generations[0].generation_id')
> ```
>
> ```bash Wait for it to finish theme={null}
> while true; do
>   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
>   echo "$STATUS"
>   case $STATUS in succeeded|failed|cancelled) break;; esac
>   sleep 3
> done
> ```
>
> ```bash Download the result theme={null}
> curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>   "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.result_url' \
>   | xargs curl -o output.png
> ```

## Start from an image

Add `input_image` to start from an image. Editing models like `qwen-image-edit` change it, and many
generation models use it as a reference.

```python Python theme={null}
import os
import requests

response = requests.post(
    "https://hub.oxen.ai/api/ai/queue",
    headers={
        "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-image-2-5-sunburst",
        "prompt": "Make the background blue",
        "input_image": ["https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"],
    },
)

print(response.json())
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/queue \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-5-sunburst",
    "prompt": "Make the background blue",
    "input_image": ["https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"]
  }'
```

The URLs must be public, since the model downloads them.

## Generate several at once

Set `num_generations` to get up to 4 images from one request. Each has its own generation ID.

```bash theme={null}
curl -X POST https://hub.oxen.ai/api/ai/queue \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-image-2-5-sunburst",
    "prompt": "Abstract geometric pattern in blue and gold",
    "num_generations": 4
  }'
```

## What's next

* [Queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md)
* [Model API references](https://docs.oxen.ai/inference-api/reference/model-references.md)
* [Video generation quickstart](https://docs.oxen.ai/inference-api/quickstart/video-generation.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.