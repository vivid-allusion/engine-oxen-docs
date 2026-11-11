---
title: "\ud83d\uddbc\ufe0f Image Generation"
source: https://docs.oxen.ai/examples/inference/image_generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🖼️ Image Generation

> How to generate images with the Oxen.ai API.

### Image Generation

Generate an image from a text prompt. To find models, filter the
[Models](https://www.oxen.ai/ai/models?modalities=text-to-image) page by "Text to image".

> [tab] cURL
>
> ```bash Start the generation theme={null}
> GEN_ID=$(curl -s -X POST \
>   https://hub.oxen.ai/api/ai/queue \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>     "model": "gpt-image-2-5-sunburst",
>     "prompt": "A majestic ox standing in a field at sunset"
>   }' | jq -r '.generations[0].generation_id')
> ```
>
> ```bash Wait for it to finish theme={null}
> while true; do
>   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
>   case $STATUS in succeeded|failed|cancelled) break;; esac
>   sleep 3
> done
>
> curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>   "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.result_url'
> ```

> [tab] Python
>
> ```python theme={null}
> import os
> import requests
> import time
>
> HEADERS = {
>     "Authorization": f"Bearer {os.getenv('OXEN_API_KEY')}",
>     "Content-Type": "application/json",
> }
>
> enqueue = requests.post(
>     "https://hub.oxen.ai/api/ai/queue",
>     headers=HEADERS,
>     json={
>         "model": "gpt-image-2-5-sunburst",
>         "prompt": "A majestic ox standing in a field at sunset",
>     },
> )
> enqueue.raise_for_status()
> generation_id = enqueue.json()["generations"][0]["generation_id"]
>
> while True:
>     data = requests.get(
>         f"https://hub.oxen.ai/api/ai/queue/{generation_id}",
>         headers=HEADERS,
>     ).json()
>     if data["status"] in {"succeeded", "failed", "cancelled"}:
>         break
>     time.sleep(3)
>
> print(f"Generated image: {data['result_url']}")
> ```

## Parameters

* **model**: Model name, for example `gpt-image-2-5-sunburst`
* **prompt**: What to generate
* **num\_generations**: Number of images, 1 to 4 (optional, default 1)

Models can take more parameters, listed in each model's
[API reference](https://docs.oxen.ai/inference-api/reference/model-references.md). The
[queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md) covers the rest of the queue API.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.