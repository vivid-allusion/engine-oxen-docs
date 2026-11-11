---
title: "Video Generation"
source: https://docs.oxen.ai/inference-api/quickstart/video-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Video Generation

> Generate videos from text prompts, images, or other videos

Generate videos with the Oxen.ai API. Each request returns a generation ID right away, and you poll
it until the video is ready. Videos can take several minutes.

## Generate a video

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
>         "model": "bytedance-seedance-2-5-text-to-video",
>         "prompt": "A red balloon floating upward through blue sky",
>         "duration": 5,
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
>     time.sleep(15)
>
> if data["status"] != "succeeded":
>     raise SystemExit(f"{data['status']}: {data['error_message']}")
>
> with open("output.mp4", "wb") as f:
>     f.write(requests.get(data["result_url"]).content)
> print("Saved output.mp4")
> ```

> [tab] cURL
>
> ```bash Start the generation theme={null}
> GEN_ID=$(curl -s -X POST https://hub.oxen.ai/api/ai/queue \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -H "Content-Type: application/json" \
>   -d '{
>     "model": "bytedance-seedance-2-5-text-to-video",
>     "prompt": "A red balloon floating upward through blue sky",
>     "duration": 5
>   }' | jq -r '.generations[0].generation_id')
> ```
>
> ```bash Wait for it to finish theme={null}
> while true; do
>   STATUS=$(curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>     "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.status')
>   echo "$STATUS"
>   case $STATUS in succeeded|failed|cancelled) break;; esac
>   sleep 15
> done
> ```
>
> ```bash Download the result theme={null}
> curl -s -H "Authorization: Bearer $OXEN_API_KEY" \
>   "https://hub.oxen.ai/api/ai/queue/$GEN_ID" | jq -r '.result_url' \
>   | xargs curl -o output.mp4
> ```

## Add images, video or audio

Many video models take more than a prompt. Seedance 2.5 Reference to Video takes lists of images
(`input_images`), videos (`input_videos`) and audio clips (`input_audios`). Each model's
[API reference](https://docs.oxen.ai/inference-api/reference/model-references.md) lists the inputs it accepts.

```bash theme={null}
curl -X POST https://hub.oxen.ai/api/ai/queue \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "bytedance-seedance-2-5-reference-to-video",
    "prompt": "The ox from the image walks through a misty forest",
    "input_images": ["https://hub.oxen.ai/api/repos/elau/assets/file/main/bloxy/bloxy_cropped_512x512.png"],
    "duration": 5
  }'
```

## Get notified when it's ready

Instead of polling, subscribe to `GET /api/events` before you start the generation. You'll get an
event when the video is ready. See [completion events](https://docs.oxen.ai/inference-api/reference/async_queue.md#completion-events).

## What's next

* [Queue reference](https://docs.oxen.ai/inference-api/reference/async_queue.md)
* [Model API references](https://docs.oxen.ai/inference-api/reference/model-references.md)
* [Seedance 2.5: Draft Mode](https://docs.oxen.ai/inference-api/reference/models/walkthroughs/seedance_2_5_draft_mode.md)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.