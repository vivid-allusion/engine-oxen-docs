---
title: "Inference API Overview"
source: https://docs.oxen.ai/inference-api/overview
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Inference API Overview

> Run inference on hundreds of AI models through a unified API for text, image, and video generation

## What is the Inference API?

The Inference API gives you access to hundreds of AI models through a single, consistent interface. Generate text, images, and videos without managing infrastructure or juggling multiple provider SDKs.

**Capabilities:**

* **Text Generation**: Chat completions, tool calling, vision, audio, documents (PDFs), structured output
* **Image Generation**: Text-to-image, image-to-image editing
* **Video Generation**: Text-to-video, image-to-video, reference-to-video, video-to-video editing

## Where to find things

| Looking for... | Go to |
| - | - |
| General API info | [Keep reading below](#authentication) |
| Getting started fast | [Quick Starts](#quick-starts) |
| Endpoint specs and parameters | [API Reference](#api-reference) |
| Running inference with a specific model | [Model API References](https://docs.oxen.ai/inference-api/reference/model-references.md) |
| Model discovery | [Models page](https://www.oxen.ai/ai/models) |

## Quick Starts

> [card] [Chat](https://docs.oxen.ai/inference-api/quickstart/chat.md)
>
> Text generation in minutes

> [card] [Images](https://docs.oxen.ai/inference-api/quickstart/image-generation.md)
>
> Text-to-image in minutes

> [card] [Videos](https://docs.oxen.ai/inference-api/quickstart/video-generation.md)
>
> Text-to-video in minutes

> [card] [Async Queue](https://docs.oxen.ai/inference-api/quickstart/async-queue.md)
>
> Generate in background

## API Reference

> [card] [Chat Completions](https://docs.oxen.ai/inference-api/reference/chat_completions.md)
>
> Text generation, vision, audio, documents, tool calling, prompt caching

> [card] [Image Generation](https://docs.oxen.ai/inference-api/reference/image_generation.md)
>
> Text-to-image generation

> [card] [Image Editing](https://docs.oxen.ai/inference-api/reference/image_editing.md)
>
> Edit images with text prompts

> [card] [Video Generation](https://docs.oxen.ai/inference-api/reference/video_generation.md)
>
> Text-to-video, image-to-video, multi-shot

> [card] [Async Queue](https://docs.oxen.ai/inference-api/reference/async_queue.md)
>
> Background image/video generation

> [card] [Models](https://docs.oxen.ai/inference-api/reference/models/overview.md)
>
> List, search, and manage models

## Individual Model API References

> [card] [Browse per-model API references](https://docs.oxen.ai/inference-api/reference/model-references.md)
>
> Sample requests, parameter tables, and workbench links for every model.

## Individual Model Walkthroughs

> [card] [Kling O3 Pro: Reference to Video](https://docs.oxen.ai/inference-api/reference/models/walkthroughs/kling_o3_pro_reference_to_video.md)
>
> Multi-shot with references

> [card] [Kling O3 Pro: Video to Video Edit](https://docs.oxen.ai/inference-api/reference/models/walkthroughs/kling_o3_pro_video_to_video_edit.md)
>
> Text-guided video edits

> [card] [Seedance 2.0: Reference to Video](https://docs.oxen.ai/inference-api/reference/models/walkthroughs/seedance_2_reference_to_video.md)
>
> Mixed-reference video

> [card] [Topaz Starlight Precise 2.5](https://docs.oxen.ai/inference-api/reference/models/walkthroughs/topaz_starlight_precise_2_5.md)
>
> Upscale and restore to 4K

***

## Authentication

All requests require a bearer token:

```bash theme={null}
curl -H "Authorization: Bearer YOUR_API_KEY" \
  https://hub.oxen.ai/api/ai/...
```

Get your API key from your [account settings](https://oxen.ai/settings/profile).

## Base URL

All inference endpoints live under:

```
https://hub.oxen.ai/api/ai
```

If you're using the OpenAI SDK, set the base URL to `https://hub.oxen.ai/api/ai`. The SDK appends `/chat/completions` automatically.

## Endpoints

| Endpoint | Method | Description |
| - | - | - |
| `/ai/chat/completions` | POST | Text generation (chat, vision, documents, tool use) |
| `/ai/images/generate` | POST | Image generation |
| `/ai/images/edit` | POST | Image editing |
| `/ai/videos/generate` | POST | Video generation |
| `/ai/queue` | POST | Async image/video generation |
| `/ai/queue` | GET | List generations (active by default, filterable by status) |
| `/ai/queue/:generation_id` | GET | Get generation status and result |
| `/ai/queue/:generation_id` | DELETE | Cancel a queued generation |
| `/ai/models` | GET | List available models |
| `/ai/models/:id` | GET | Get model details and parameter schema |
| `/ai/models/search` | GET | Search models by name |
| `/ai/models/:id/activate` | POST | Activate a custom model deployment |
| `/ai/models/:id/deactivate` | POST | Deactivate a custom model deployment |

## Common Parameters

These parameters are accepted across multiple endpoints:

| Parameter | Type | Description |
| - | - | - |
| `model` | string | Required. The model to use (e.g. `claude-sonnet-4-6`, `flux-2-dev`, `kling-video-o3-pro-reference-to-video`). |
| `response_format` | string | `"url"` (default) returns a hosted URL. `"b64_json"` returns base64-encoded bytes inline. Supported on image and video endpoints. |
| `target_namespace` | string | Namespace to save results and bill to. Defaults to your user. Can be an organization name. |

## Discovering Models

List all models, optionally filtered by developer:

```bash theme={null}
# All models
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models"

# Search by name
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models/search?search=kling"
```

Get full details for a specific model (including its parameter schema):

```bash theme={null}
curl -H "Authorization: Bearer $OXEN_API_KEY" \
  "https://hub.oxen.ai/api/ai/models/kling-video-o3-pro-reference-to-video"
```

The response includes a `request_schema` field with the complete parameter definitions, types, defaults, and constraints for that model.

## Pricing

Pricing varies by model:

| Method | How it works | Examples |
| - | - | - |
| `token` | Per input/output token | GPT, Claude, Gemini |
| `time` | Per second of compute time | Custom models, Llama, Qwen |
| `per_image` | Fixed cost per image | FLUX, DALL-E |
| `per_video_output_second` | Cost per second of output video | Kling, Sora |

Check the [model detail endpoint](https://docs.oxen.ai/inference-api/reference/models/overview.md#retrieve-model) for exact pricing. Relevant fields: `input_cost_per_token`, `output_cost_per_token`, `cost_per_image`, `cost_per_second`, `cost_per_second_with_audio`, `cost_per_second_high_res`.

## Error Format

Errors use one of two formats:

```json theme={null}
{
  "error": {
    "type": "invalid_params",
    "title": "Invalid parameters supplied, please check your request and try again.",
    "detail": "Specific error details"
  },
  "status": "error",
  "status_message": "invalid_params"
}
```

```json theme={null}
{
  "error": {
    "message": "Model not found: bad-model-name"
  }
}
```

Common error types: `unauthenticated`, `invalid_params`, `resource_not_found`, `unknown_error`.

Need help? Join our [Discord community](https://discord.com/invite/s3tBEn7Ptg).


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.