---
title: "Fine-Tune: Image To Text"
source: https://docs.oxen.ai/fine-tuning-api/reference/image_to_text
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fine-Tune: Image To Text

> Image to text fine-tuning schema

## Overview

This schema is used for fine-tuning models with **image to text** capabilities.

### Schema Type

When creating a fine-tune with this schema, use:

```json theme={null}
{
  "resource": "main/your-dataset.parquet",
  "base_model": "<model-canonical-name>",
  "script_type": "image_to_text",
  "training_params": {
    ...
  }
}
```

**Key Parameters:**

* `script_type`: `image_to_text` (the fine-tune type)
* `base_model`: One of the supported model canonical names below

### Supported Models

* Qwen3 VL 8B - Instruct (`Qwen/Qwen3-VL-8B-Instruct`)
* Qwen3 VL 2B - Instruct (`Qwen/Qwen3-VL-2B-Instruct`)
* Qwen3 VL 4B - Instruct (`Qwen/Qwen3-VL-4B-Instruct`)

## Request Schema

### Required Fields

| Field | Type | Required | Description |
| - | - | - | - |
| `answer_column` | string | Yes | Response Column (DataFrame column name) |
| `batch_size` | integer | No | (default: 1) (min: 1) |
| `enable_thinking` | boolean | No | enable\_thinking |
| `epochs` | integer | No | (default: 1) (min: 1) |
| `grad_accum` | integer | No | (default: 1) (min: 1) |
| `image_columns` | array | Yes | Image Columns (array of string) (Multiple DataFrame column names) |
| `learning_rate` | number | No | (default: 0.0001) |
| `logging_steps` | integer | No | (default: 10) (min: 1) |
| `lora_alpha` | integer | No | (default: 16) (min: 1) |
| `lora_rank` | integer | No | (default: 16) (min: 1) |
| `neftune_noise_alpha` | number | No | (default: 0) |
| `question_column` | string | Yes | Prompt Column (DataFrame column name) |
| `save_steps_ratio` | number | No | (default: 0.25) |
| `save_strategy` | string | No | save\_strategy |
| `seq_length` | integer | No | (default: 4096) (min: 1) |
| `use_lora` | boolean | No | Use LoRA |

## Example Request

```json Request Body theme={null}
{
  "resource": "main/your-dataset.parquet",
  "base_model": "<model-canonical-name>",
  "script_type": "image_to_text",
  "training_params": {
    "answer_column": "<answer_column>",
    "batch_size": 1,
    "enable_thinking": false,
    "epochs": 1,
    "grad_accum": 1,
    "image_columns": [],
    "learning_rate": 0.0001,
    "logging_steps": 10,
    "lora_alpha": 16,
    "lora_rank": 16,
    "neftune_noise_alpha": 0,
    "question_column": "<question_column>",
    "save_steps_ratio": 0.25,
    "save_strategy": "epoch",
    "seq_length": 4096,
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
  "script_type": "image_to_text",
  "training_params": {{
    "answer_column": "<answer_column>",
    "batch_size": 1,
    "enable_thinking": false,
    "epochs": 1,
    "grad_accum": 1,
    "image_columns": [],
    "learning_rate": 0.0001,
    "logging_steps": 10,
    "lora_alpha": 16,
    "lora_rank": 16,
    "neftune_noise_alpha": 0,
    "question_column": "<question_column>",
    "save_steps_ratio": 0.25,
    "save_strategy": "epoch",
    "seq_length": 4096,
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
  -d '{   "resource": "main/your-dataset.parquet",   "base_model": "<model-canonical-name>",   "script_type": "image_to_text",   "training_params": {     "answer_column": "<answer_column>",     "batch_size": 1,     "enable_thinking": false,     "epochs": 1,     "grad_accum": 1,     "image_columns": [],     "learning_rate": 0.0001,     "logging_steps": 10,     "lora_alpha": 16,     "lora_rank": 16,     "neftune_noise_alpha": 0,     "question_column": "<question_column>",     "save_steps_ratio": 0.25,     "save_strategy": "epoch",     "seq_length": 4096,     "use_lora": true   } }'
```

## Field Details

### `answer_column`

**Response Column**

**Type:** `string`

Column containing the captions or responses

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

### `image_columns`

**Image Columns**

**Type:** `array`

Columns containing image file paths

**Default:** `[]`

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

### `neftune_noise_alpha`

**Type:** `number`

**Default:** `0`

**Minimum:** `0`

### `question_column`

**Prompt Column**

**Type:** `string`

Column containing the prompts or questions for each image

### `save_steps_ratio`

**Type:** `number`

**Default:** `0.25`

### `save_strategy`

**Type:** `string`

**Default:** `"epoch"`

### `seq_length`

**Type:** `integer`

**Default:** `4096`

**Minimum:** `1`

### `use_lora`

**Use LoRA**

**Type:** `boolean`

Enable LoRA for faster fine-tuning and lower memory use

**Default:** `true`


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.