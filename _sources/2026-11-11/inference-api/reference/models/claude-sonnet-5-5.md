---
source: https://docs.oxen.ai/inference-api/reference/models/claude-sonnet-5-5
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Claude Sonnet 5.5

> Fastest Sonnet for coding and agents

> [card] [Try Claude Sonnet 5.5 in the Workbench](https://www.oxen.ai/ai/workbench?model=claude-sonnet-5-5)
>
> Run this model interactively, tune parameters, and compare outputs.

**Model ID:** `claude-sonnet-5-5`

**Claude Sonnet 5.5 is Anthropic's Sonnet-tier Multimodal LLM for everyday coding, agent tasks, and knowledge work, and the fastest Sonnet model to date.** It is a clear upgrade over Claude Sonnet 5, generating output more than 30% faster while typically needing far fewer tokens per task, at the same per-token pricing.

Adaptive thinking is steered by the effort parameter (defaulting to high), and the model ships with a native 1M-token context window and up to 128k output tokens, with a reliable knowledge cutoff of June 2026. Migrating from Sonnet 5 requires attention to breaking changes: forced tool use returns an error, thinking blocks are readable only by the model that produced them, and text between tool calls is returned in thinking blocks. It is the first Sonnet model to launch with the cyber safeguards developed for Anthropic's most capable models.

| Metric | Value |
| - | - |
| Context Length | 1,000,000 tokens |
| Max Output | 128,000 tokens |
| Multilingual | Yes |

## Example request

> [!TIP]
>
> Use the [Workbench](https://www.oxen.ai/ai/workbench?model=claude-sonnet-5-5) as a request builder: configure parameters for this model in the UI, then open the **API** tab to copy the exact cURL or Python call.

> [tab] Minimal
>
> ```bash cURL theme={null}
> curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
>   -H "Content-Type: application/json" \
>   -H "Authorization: Bearer $OXEN_API_KEY" \
>   -d '{
>   "model": "claude-sonnet-5-5",
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
>         "model": "claude-sonnet-5-5",
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
>   "model": "claude-sonnet-5-5",
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
>         "model": "claude-sonnet-5-5",
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
curl -H "Authorization: Bearer $OXEN_API_KEY" https://hub.oxen.ai/api/ai/models/claude-sonnet-5-5
```

## Request parameters

This model follows the standard OpenAI chat completions request body. See the [chat completions reference](../inference-api.mdx) for the full parameter list.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.