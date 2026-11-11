---
source: https://docs.oxen.ai/inference-api/reference/models/gpt-audio
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT Audio

> OpenAI audio-input chat model

> [card] [Try GPT Audio in the Workbench](https://www.oxen.ai/ai/workbench?model=gpt-audio)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `gpt-audio`

GPT Audio is OpenAI's generally available audio model. It accepts audio as an input alongside text, so a chat model can answer questions about spoken audio.

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=gpt-audio) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/audio/transcriptions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -d '{
  "model": "gpt-audio",
  "audio_url": "https://example.com/audio.mp3"
}'
```

```python Python theme={null}
import os
import requests

response = requests.post(
    "https://hub.oxen.ai/api/ai/audio/transcriptions",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
    },
    json={
        "model": "gpt-audio",
        "audio_url": "https://example.com/audio.mp3"
    },
)
response.raise_for_status()
print(response.json())
```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/gpt-audio
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.