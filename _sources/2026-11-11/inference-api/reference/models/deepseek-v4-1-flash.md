---
source: https://docs.oxen.ai/inference-api/reference/models/deepseek-v4-1-flash
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# DeepSeek V4.1 Flash

> Multimodal MoE for agents, 1M context

> [card] [Try DeepSeek V4.1 Flash in the Workbench](https://www.oxen.ai/ai/workbench?model=deepseek-v4-1-flash)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `deepseek-v4-1-flash`

DeepSeek V4.1 Flash is a natively multimodal Mixture-of-Experts model built for coding, reasoning, and long-horizon agent tasks. It is the cost-efficient tier of the V4.1 family, and DeepSeek reports it ahead of V4 Pro on quality, speed, cost, and total task completion time, with V4 Flash and V4 Pro both retired in its favor.

The model uses DeepSeek's Causal Encoder-Decoder architecture, which activates 8B parameters while reading input and 16B while generating output, and compresses the KV cache to roughly a quarter of V4 Flash's footprint. It reads images and text through a DeepSeek-ViT vision encoder and supports a 1M-token context window, tool use, structured outputs, and a continuously adjustable reasoning-effort setting (1-100) that trades inference cost for accuracy. Pretraining covers 45T multimodal tokens, followed by SFT, RL, and on-policy distillation post-training. Weights are published under the MIT license.

| Metric | Value |
| - | - |
| Parameter Count | 552 billion |
| Mixture of Experts | Yes |
| Active Parameter Count | 8 billion (prefill) / 16 billion (decode) |
| Context Length | 1,048,576 tokens |
| Max Output | 384,000 tokens |
| Multilingual | Yes |
| Tool Use | Yes |
| Structured Outputs | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=deepseek-v4-1-flash) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "deepseek-v4-1-flash",
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
>         "model": "deepseek-v4-1-flash",
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
>   "model": "deepseek-v4-1-flash",
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
>         "model": "deepseek-v4-1-flash",
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
>   "model": "deepseek-v4-1-flash",
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
>         "model": "deepseek-v4-1-flash",
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/deepseek-v4-1-flash
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.