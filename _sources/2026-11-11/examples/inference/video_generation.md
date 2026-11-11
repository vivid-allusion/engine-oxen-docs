---
title: "\ud83c\udfa5 Video Generation"
source: https://docs.oxen.ai/examples/inference/video_generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🎥 Video Generation

> How to generate videos with the Oxen.ai API.

### Video Generation

Generate a video from a text prompt. Videos can take several minutes. To find models, filter the
[Models](https://www.oxen.ai/ai/models?modalities=text-to-video) page by "Text to video".

> [tab] cURL
>
> ```bash Start the generation theme={null}
> GEN_ID=$(curl -s -X POST \
>   https://hub.oxen.ai/api/ai/queue \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>     "model": "bytedance-seedance-2-5-text-to-video",
>     "prompt": "An ox walking in a field",
>     "duration": 5
>   }' | jq -r '.generations[0].generation_id')
> ```
>
> ```bash Wait for it to finish theme={null}
> while true; do
>   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
>   case $STATUS in succeeded|failed|cancelled) break;; esac
>   sleep 15
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
>         "model": "bytedance-seedance-2-5-text-to-video",
>         "prompt": "An ox walking in a field",
>         "duration": 5,
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
>     time.sleep(15)
>
> print(f"Generated video: {data['result_url']}")
> ```

## Parameters

* **model**: Model name, for example `bytedance-seedance-2-5-text-to-video`
* **prompt**: What to generate
* **duration**: Length in seconds (optional, defaults vary by model)

Models can take more parameters, listed in each model's
[API reference](https://docs.oxen.ai/inference-api/reference/model-references.md). The
[queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md) covers the rest of the queue API.

To skip polling, listen for [completion events](https://docs.oxen.ai/inference-api/reference/async_queue.md#completion-events)
instead.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.