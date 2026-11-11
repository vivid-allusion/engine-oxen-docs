---
source: https://docs.oxen.ai/inference-api/reference/models/claude-opus-4-8
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Opus 4.8

> Agentic coding, 1M-token context

> [card] [Try Claude Opus 4.8 in the Workbench](https://www.oxen.ai/ai/workbench?model=claude-opus-4-8)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `claude-opus-4-8`

**Claude Opus 4.8 is Anthropic's Opus-tier Multimodal LLM for complex reasoning, long-horizon agentic coding, and high-autonomy professional work.** It builds on Claude Opus 4.7 with gains across agentic coding, agentic terminal use, multidisciplinary reasoning, and computer use, while keeping a native 1M-token context window at standard pricing.

Other noteworthy features of Claude Opus 4.8 include adaptive thinking with user-controllable effort levels (defaulting to high), computer use for multi-step workflows, image processing, and a fast mode that runs at roughly 2.5x output speed. Opus 4.8 is also markedly less likely than Opus 4.7 to leave undetected flaws in generated code, and is the recommended migration target for the deprecated Claude Opus 4 and Claude Sonnet 4.

| Metric | Value |
| - | - |
| Context Length | 1,000,000 tokens |
| Max Output | 128,000 tokens |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=claude-opus-4-8) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "claude-opus-4-8",
>   "messages": [
>     {
>       "role": "user",
>       "content": "Hello, what can you do?"
>     }
>   ]
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/chat/completions",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "claude-opus-4-8",
>         "messages": [
>             {
>                 "role": "user",
>                 "content": "Hello, what can you do?"
>             }
>         ]
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

> [tab] Basic parameters
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "claude-opus-4-8",
>   "messages": [
>     {
>       "role": "user",
>       "content": "Hello, what can you do?"
>     }
>   ],
>   "temperature": 0.7,
>   "max_tokens": 1024,
>   "stream": false
> }'
> ```
>
> ```python Python theme={null}
> import os
> import requests
>
> response = requests.post(
>     "https://hub.oxen.ai/api/ai/chat/completions",
>     headers={
>         "Content-Type": "application/json",
>         "Authorization": f"Bearer {os.environ['OXEN_API_KEY']}",
>     },
>     json={
>         "model": "claude-opus-4-8",
>         "messages": [
>             {
>                 "role": "user",
>                 "content": "Hello, what can you do?"
>             }
>         ],
>         "temperature": 0.7,
>         "max_tokens": 1024,
>         "stream": false
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/claude-opus-4-8
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.