---
source: https://docs.oxen.ai/inference-api/reference/models/glm-5-3-flash
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# GLM 5.3 Flash

> Efficient multimodal coding, 1M context

> [card] [Try GLM 5.3 Flash in the Workbench](https://www.oxen.ai/ai/workbench?model=glm-5-3-flash)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `glm-5-3-flash`

GLM-5.3-Flash is a native multimodal model from Z AI built for efficient coding and long-horizon agent tasks. With 320 billion total parameters and just 18 billion active, it outperforms GLM-5.2 across benchmarks at a fraction of the cost while approaching Claude Opus 4.8 on coding and agentic tasks.

It is the first multimodal model in the GLM-5 series, combining sparse and linear attention in a hybrid architecture that cuts long-context serving costs. Reasoning is always on and cannot be disabled; the reasoning\_effort parameter accepts low, high, and max, with max as the default. Weights are published under an MIT license.

Fine-tuning trains an adapter over attention while the routed experts stay frozen in 4 bits, so a fine tune of this model costs about what a far smaller one would.

| Metric | Value |
| - | - |
| Parameter Count | 320 billion |
| Active Parameter Count | 18 billion |
| Mixture of Experts | Yes |
| Context Length | 1,048,576 tokens |
| Max Output | 131,072 tokens |
| Multilingual | Yes |
| Tool Use | Yes |
| Structured Outputs | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=glm-5-3-flash) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "glm-5-3-flash",
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
>         "model": "glm-5-3-flash",
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
>   "model": "glm-5-3-flash",
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
>         "model": "glm-5-3-flash",
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
>   "model": "glm-5-3-flash",
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
>         "model": "glm-5-3-flash",
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/glm-5-3-flash
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.