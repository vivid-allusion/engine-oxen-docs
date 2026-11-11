---
source: https://docs.oxen.ai/inference-api/reference/models/gpt-6-1-sol
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GPT 6.1 Sol

> Near-Astra agentic coding at lower cost, 1M context

> [card] [Try GPT 6.1 Sol in the Workbench](https://www.oxen.ai/ai/workbench?model=gpt-6-1-sol)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `gpt-6-1-sol`

GPT 6.1 Sol is OpenAI's GPT-6 generation reasoning model for complex coding, computer use, and professional work, delivering performance close to GPT 6 Astra at a much lower per-token price. It is the newer Sol model and succeeds GPT 6 Sol, and OpenAI recommends comparing it against Astra on your own tasks to weigh quality against cost.

It accepts text and images and supports configurable reasoning effort (low, medium, high, xhigh, and max), streaming, structured outputs, and function calling, with the web search, file search, image generation, code interpreter, hosted shell, apply patch, skills, computer use, MCP, and tool search tools. The none and minimal reasoning efforts are not supported, and tool calling requires the Responses API because Chat Completions works only without tools. Fine-tuning and predicted outputs are not available.

| Metric | Value |
| - | - |
| Context Length | 1,050,000 tokens |
| Max Output Tokens | 128,000 tokens |
| Knowledge Cutoff | Apr 30, 2026 |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=gpt-6-1-sol) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "gpt-6-1-sol",
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
>         "model": "gpt-6-1-sol",
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
>   "model": "gpt-6-1-sol",
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
>         "model": "gpt-6-1-sol",
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
>   "model": "gpt-6-1-sol",
>   "messages": [
>     {
>       "role": "user",
>       "content": "Hello, what can you do?"
>     }
>   ],
>   "temperature": 0.7,
>   "max_tokens": 1024,
>   "stream": false,
>   "top_p": 1.0,
>   "frequency_penalty": 0,
>   "presence_penalty": 0
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
>         "model": "gpt-6-1-sol",
>         "messages": [
>             {
>                 "role": "user",
>                 "content": "Hello, what can you do?"
>             }
>         ],
>         "temperature": 0.7,
>         "max_tokens": 1024,
>         "stream": false,
>         "top_p": 1.0,
>         "frequency_penalty": 0,
>         "presence_penalty": 0
>     },
> )
> response.raise_for_status()
> print(response.json())
> ```

## Fetch model details

The [models endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md) returns the full model object, including its `json_request_schema`.

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/gpt-6-1-sol
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.