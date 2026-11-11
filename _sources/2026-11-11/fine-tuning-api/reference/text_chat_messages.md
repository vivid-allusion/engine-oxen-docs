---
title: "Fine-Tune: Text Chat Messages"
source: https://docs.oxen.ai/fine-tuning-api/reference/text_chat_messages
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fine-Tune: Text Chat Messages

> Default fine-tune schema

## Overview

This schema is used for fine-tuning models with **text chat messages** capabilities.

### Schema Type

When creating a fine-tune with this schema, use:

```json theme={null}
{
  "resource": "main/your-dataset.parquet",
  "base_model": "<model-canonical-name>",
  "script_type": "text_chat_messages",
  "training_params": {
    ...
  }
}
```

**Key Parameters:**

* `script_type`: `text_chat_messages` (the fine-tune type)
* `base_model`: One of the supported model canonical names below

### Supported Models

* OpenAI/GPT-OSS-20B (`openai/gpt-oss-20b`)
* Llama 3.1 8B Instruct (`meta-llama/Llama-3.1-8B-Instruct`)
* Llama 4 Scout (`meta-llama/Llama-4-Scout-17B-16E-Instruct`)
* Llama 3.2 3B Instruct (`meta-llama/Llama-3.2-3B-Instruct`)
* Qwen/Qwen3-1.7B (`Qwen/Qwen3-1.7B`)
* Qwen/Qwen3-4B (`Qwen/Qwen3-4B`)
* Qwen/Qwen3-0.6B (`Qwen/Qwen3-0.6B`)

## Request Schema

### Required Fields

| Field | Type | Required | Description |
| - | - | - | - |
| `batch_size` | integer | No | (default: 1) (min: 1) |
| `enable_thinking` | boolean | No | enable\_thinking |
| `epochs` | integer | No | (default: 1) (min: 1) |
| `grad_accum` | integer | No | (default: 1) (min: 1) |
| `learning_rate` | number | No | (default: 0.0001) |
| `logging_steps` | integer | No | (default: 10) (min: 1) |
| `lora_alpha` | integer | No | (default: 16) (min: 1) |
| `lora_rank` | integer | No | (default: 16) (min: 1) |
| `messages_column` | string | Yes | Messages (input) Column (DataFrame column name) |
| `neftune_noise_alpha` | number | No | (default: 0) |
| `save_steps_ratio` | number | No | (default: 0.25) |
| `save_strategy` | string | No | save\_strategy |
| `seq_length` | integer | No | (default: 1024) (min: 1) |
| `use_lora` | boolean | No | Use LoRA |

## Example Request

```json Request Body theme={null}
{
  "resource": "main/your-dataset.parquet",
  "base_model": "<model-canonical-name>",
  "script_type": "text_chat_messages",
  "training_params": {
    "batch_size": 1,
    "enable_thinking": false,
    "epochs": 1,
    "grad_accum": 1,
    "learning_rate": 0.0001,
    "logging_steps": 10,
    "lora_alpha": 16,
    "lora_rank": 16,
    "messages_column": "<messages_column>",
    "neftune_noise_alpha": 0,
    "save_steps_ratio": 0.25,
    "save_strategy": "epoch",
    "seq_length": 1024,
    "use_lora": true
  }
}
```

```python Python theme={null}
import requests

url = "https://hub.oxen.ai/api/repos/{namespace}/{repo_name}/fine_tunes"
headers = {
    "Authorization": "Bearer YOUR_API_KEY",
    "Content-Type": "application/json"
}

data = {{
  "resource": "main/your-dataset.parquet",
  "base_model": "<model-canonical-name>",
  "script_type": "text_chat_messages",
  "training_params": {{
    "batch_size": 1,
    "enable_thinking": false,
    "epochs": 1,
    "grad_accum": 1,
    "learning_rate": 0.0001,
    "logging_steps": 10,
    "lora_alpha": 16,
    "lora_rank": 16,
    "messages_column": "<messages_column>",
    "neftune_noise_alpha": 0,
    "save_steps_ratio": 0.25,
    "save_strategy": "epoch",
    "seq_length": 1024,
    "use_lora": true
  }}
}}

response = requests.post(url, headers=headers, json=data)
print(response.json())
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/repos/{namespace}/{repo_name}/fine_tunes \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{   "resource": "main/your-dataset.parquet",   "base_model": "<model-canonical-name>",   "script_type": "text_chat_messages",   "training_params": {     "batch_size": 1,     "enable_thinking": false,     "epochs": 1,     "grad_accum": 1,     "learning_rate": 0.0001,     "logging_steps": 10,     "lora_alpha": 16,     "lora_rank": 16,     "messages_column": "<messages_column>",     "neftune_noise_alpha": 0,     "save_steps_ratio": 0.25,     "save_strategy": "epoch",     "seq_length": 1024,     "use_lora": true   } }'
```

## Field Details

### `batch_size`

**Type:** `integer`

**Default:** `1`

**Minimum:** `1`

### `enable_thinking`

**Type:** `boolean`

**Default:** `false`

### `epochs`

**Type:** `integer`

**Default:** `1`

**Minimum:** `1`

### `grad_accum`

**Type:** `integer`

**Default:** `1`

**Minimum:** `1`

### `learning_rate`

**Type:** `number`

**Default:** `0.0001`

**Minimum:** `0`

### `logging_steps`

**Type:** `integer`

**Default:** `10`

**Minimum:** `1`

### `lora_alpha`

**Type:** `integer`

**Default:** `16`

**Minimum:** `1`

### `lora_rank`

**Type:** `integer`

**Default:** `16`

**Minimum:** `1`

### `messages_column`

**Messages (input) Column**

**Type:** `string`

### `neftune_noise_alpha`

**Type:** `number`

**Default:** `0`

**Minimum:** `0`

### `save_steps_ratio`

**Type:** `number`

**Default:** `0.25`

### `save_strategy`

**Type:** `string`

**Default:** `"epoch"`

### `seq_length`

**Type:** `integer`

**Default:** `1024`

**Minimum:** `1`

### `use_lora`

**Use LoRA**

**Type:** `boolean`

Enable LoRA for faster fine-tuning and lower memory use

**Default:** `true`


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.