---
source: https://docs.oxen.ai/inference-api/reference/models/gemini-3-8-flash
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Gemini 3.8 Flash

> Long-horizon coding agents, 1M context

> [card] [Try Gemini 3.8 Flash in the Workbench](https://www.oxen.ai/ai/workbench?model=gemini-3-8-flash)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `gemini-3-8-flash`

**gemini-3.8-flash is a Multimodal LLM.** It is Google's Flash-tier model for long-horizon software engineering, autonomous agents, and multi-step enterprise workflows, with gains over Gemini 3.7 Flash across software engineering, agentic tasks, and specialized-domain reasoning. Google reports 54.9% on HLE-Verified and says it outperforms most larger models on DeepSWE v1.1, its long-horizon engineering benchmark.

Some other noteworthy features of gemini-3.8-flash include configurable thinking levels (low, medium, high; minimal is not supported and returns an error), structured output, function calling, code execution, context caching, search grounding, URL context, file search, computer use (preview), and batch processing. It accepts text, images, audio, video, and PDFs and outputs text only. On hard tasks it tends to run extra reasoning steps and iterative tool calls, so token usage per task can be higher than 3.7 Flash, especially at higher thinking levels. The Live API, image generation, and audio generation are not supported.

| Metric | Value |
| - | - |
| Context Length | 1M tokens |
| Max Output | 64K tokens |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=gemini-3-8-flash) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/audio/transcriptions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $OXEN_API_KEY" \
  -d '{
  "model": "gemini-3-8-flash",
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
        "model": "gemini-3-8-flash",
        "audio_url": "https://example.com/audio.mp3"
    },
)
response.raise_for_status()
print(response.json())
```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/gemini-3-8-flash
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.