---
source: https://docs.oxen.ai/inference-api/reference/models/claude-sonnet-4-6
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Sonnet 4.6

> Balanced coding and agents, 1M context

> [card] [Try Claude Sonnet 4.6 in the Workbench](https://www.oxen.ai/ai/workbench?model=claude-sonnet-4-6)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `claude-sonnet-4-6`

**Claude Sonnet 4.6 is a Multimodal LLM designed for coding, agent workflows, and knowledge work.** It balances speed and intelligence while improving reliability for complex, multi-step tasks.

Some other noteworthy features of Claude Sonnet 4.6 include adaptive thinking, extended thinking support, and a native 1M-token context window for long-context reasoning workloads.

| Metric | Value |
| - | - |
| Context Length | 1,000,000 tokens |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=claude-sonnet-4-6) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "claude-sonnet-4-6",
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
>         "model": "claude-sonnet-4-6",
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
>   "model": "claude-sonnet-4-6",
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
>         "model": "claude-sonnet-4-6",
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/claude-sonnet-4-6
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.