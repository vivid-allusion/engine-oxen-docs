---
source: https://docs.oxen.ai/inference-api/reference/models/ministral-3b-latest
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Ministral 3B

> Model for on-device and edge

> [card] [Try Ministral 3B in the Workbench](https://www.oxen.ai/ai/workbench?model=ministral-3b-latest)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `ministral-3b-latest`

Ministral 3B is a 3B parameter LLM optimized for on-device and edge computing. It excels in knowledge, commonsense reasoning, and function-calling, outperforming larger models like Mistral 7B on most benchmarks. Supporting up to 128k context length, it’s ideal for orchestrating agentic workflows and specialist tasks with efficient inference.

| Metric | Value |
| - | - |
| Context Length | 128,000 tokens |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=ministral-3b-latest) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "ministral-3b-latest",
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
>         "model": "ministral-3b-latest",
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
>   "model": "ministral-3b-latest",
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
>         "model": "ministral-3b-latest",
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

> [tab] All parameters
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "ministral-3b-latest",
>   "messages": [
>     {
>       "role": "user",
>       "content": "Hello, what can you do?"
>     }
>   ],
>   "temperature": 0.7,
>   "max_tokens": 1024,
>   "stream": false,
>   "top_p": 1.0
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
>         "model": "ministral-3b-latest",
>         "messages": [
>             {
>                 "role": "user",
>                 "content": "Hello, what can you do?"
>             }
>         ],
>         "temperature": 0.7,
>         "max_tokens": 1024,
>         "stream": false,
>         "top_p": 1.0
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/ministral-3b-latest
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.