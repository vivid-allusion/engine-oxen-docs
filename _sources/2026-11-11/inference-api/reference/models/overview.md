---
title: "Models"
source: https://docs.oxen.ai/inference-api/reference/models/overview
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Models

> List, search, and manage AI models available for inference and fine-tuning

> [card] [Browse per-model API references](https://docs.oxen.ai/inference-api/reference/model-references.md)
>
> Sample requests, parameter tables, and workbench links for every model.

> [card] [Discover models on our Models page](https://www.oxen.ai/ai/models)
>
> Filter by modality, search by name, and preview every model side-by-side.

## List Models

```
GET /api/ai/models
```

Lists all available models. OpenAI-compatible.

### Query Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `developer_name` | string | no | Filter by developer (e.g. `openai`, `anthropic`, `google`) |
| `action` | string | no | Filter by fine-tuning action type |

### Response

```json theme={null}
{
  "object": "list",
  "data": [
    {
      "id": "claude-sonnet-4-6",
      "object": "model",
      "created": 1750000000,
      "owned_by": "oxen",
      "display_name": "Claude Sonnet 4.6",
      "description": "Anthropic's balanced model for a wide range of tasks",
      "summary": "Balanced performance and speed",
      "model_type": "base",
      "endpoint": "/chat/completions",
      "capabilities": {
        "input": ["text", "image"],
        "output": ["text"]
      },
      "pricing": {
        "method": "token",
        "input_cost_per_token": 3e-6,
        "output_cost_per_token": 1.5e-5
      },
      "fine_tuning": null,
      "deployments": [],
      "developer": {
        "name": "Anthropic",
        "logo": "https://..."
      },
      "source_model": null,
      "image_url": null,
      "released_at": "2025-06-19T00:00:00Z",
      "request_schema": null
    }
  ]
}
```

### Examples

```python Python theme={null}
import requests

response = requests.get(
    "https://hub.oxen.ai/api/ai/models",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

for model in response.json()["data"]:
    print(f"{model['id']} ({model['endpoint']})")
```

```bash cURL theme={null}
# All models
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models"

# Filter by developer
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models?developer_name=openai"
```

***

## Search Models

```
GET /api/ai/models/search
```

Search models by name.

### Query Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `search` | string | **yes** | Search query |

### Examples

```python Python theme={null}
import requests

response = requests.get(
    "https://hub.oxen.ai/api/ai/models/search",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
    params={"search": "kling"},
)

for model in response.json()["data"]:
    print(f"{model['id']} - {model['display_name']}")
```

```bash cURL theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models/search?search=kling"
```

***

## Retrieve Model

```
GET /api/ai/models/:id
```

Retrieves a model by name. Returns the full model object including the `request_schema` describing model-specific parameters.

### Path Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `id` | string | **yes** | Model name (e.g. `claude-sonnet-4-6`, `flux-2-dev`) |

### Query Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `deployment_status` | string | no | Pass `"live"` to refresh deployment status from provider before responding |

### Examples

```python Python theme={null}
import requests

response = requests.get(
    "https://hub.oxen.ai/api/ai/models/kling-video-o3-pro-reference-to-video",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

model = response.json()
print(f"Endpoint: {model['endpoint']}")
print(f"Pricing: {model['pricing']}")

# Get the model's parameter schema
if model.get("request_schema"):
    print(f"Parameters: {model['request_schema']}")
```

```bash cURL theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models/kling-video-o3-pro-reference-to-video"

# With live deployment status refresh
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models/my-custom-model?deployment_status=live"
```

***

## Activate Model

```
POST /api/ai/models/:id/activate
```

Activates an inactive custom model deployment. Base models are always active and do not need activation.

### Path Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `id` | string | **yes** | Model name |

### Examples

```python Python theme={null}
import requests

response = requests.post(
    "https://hub.oxen.ai/api/ai/models/my-custom-model/activate",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

model = response.json()
print(f"Status: {model['deployments'][0]['status']}")
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/models/my-custom-model/activate \
  -H "Authorization: Bearer $OXEN_API_KEY"
```

***

## Deactivate Model

```
POST /api/ai/models/:id/deactivate
```

Deactivates an active custom model deployment to stop billing.

### Path Parameters

| Parameter | Type | Required | Description |
| - | - | - | - |
| `id` | string | **yes** | Model name |

### Examples

```python Python theme={null}
import requests

response = requests.post(
    "https://hub.oxen.ai/api/ai/models/my-custom-model/deactivate",
    headers={"Authorization": "Bearer YOUR_API_KEY"},
)

model = response.json()
print(f"Status: {model['deployments'][0]['status']}")
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/models/my-custom-model/deactivate \
  -H "Authorization: Bearer $OXEN_API_KEY"
```

***

## Model Object

Every endpoint above returns one or more model objects with this schema:

| Field | Type | Description |
| - | - | - |
| `id` | string | Model identifier used in API calls (e.g. `claude-sonnet-4-6`) |
| `object` | string | Always `"model"` |
| `created` | integer | Unix timestamp when the model was registered |
| `owned_by` | string | `"oxen"` for base models, owner namespace for custom models |
| `display_name` | string | Human-readable name |
| `description` | string/null | Full description |
| `summary` | string/null | Brief summary |
| `model_type` | string | `"base"` or `"custom"` |
| `endpoint` | string | API endpoint to call: `"/chat/completions"`, `"/images/generate"`, or `"/videos/generate"` |
| `capabilities` | object | Input/output modalities, e.g. `input: ["text", "image"]`, `output: ["text"]` |
| `pricing` | object | See [Pricing](#pricing) below |
| `fine_tuning` | object/null | Fine-tuning config with `actions` and `cost_per_second`, or `null` if not fine-tuneable |
| `deployments` | array | Deployment status objects. Possible statuses: `active`, `inactive`, `deploying`, `deactivating`, `error`, `unknown`. Empty for base models. |
| `developer` | object/null | Developer info with `name` and `logo` fields |
| `source_model` | string/null | Base model this was fine-tuned from |
| `image_url` | string/null | Image asset URL |
| `released_at` | string/null | Release timestamp |
| `request_schema` | object/null | JSON Schema describing model-specific request parameters |

### Pricing

The `pricing` object describes how the model is billed:

| Field | Type | Description |
| - | - | - |
| `method` | string | `"token"`, `"time"`, `"per_image"`, or `"per_video_output_second"` |
| `input_cost_per_token` | number/null | Cost per input token (token-based models) |
| `output_cost_per_token` | number/null | Cost per output token (token-based models) |
| `cost_per_second` | number/null | Cost per second (time-based models) |
| `cost_per_image` | number/null | Fixed cost per image (image generation models) |
| `cost_per_second_high_res` | number/null | High-resolution video cost per second |
| `cost_per_second_with_audio` | number/null | Video with audio cost per second |

## Errors

| Condition | Status | Error |
| - | - | - |
| Model not found | 404 | `"Model not found: <name>"` |
| Not authenticated | 401 | `"unauthenticated"` |


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.