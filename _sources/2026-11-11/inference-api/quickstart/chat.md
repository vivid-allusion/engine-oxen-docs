---
title: "Chat Completions"
source: https://docs.oxen.ai/inference-api/quickstart/chat
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Chat Completions

> Generate text with language models in minutes

## Overview

Generate text responses from language models using the OpenAI-compatible chat completions API. Supports streaming, vision, audio, documents (PDFs), tool calling, and structured output.

## Minimal Example

```python Python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://hub.oxen.ai/api/ai",
    api_key="YOUR_API_KEY",
)

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": "What is Oxen.ai?"}],
    max_tokens=200,
)

print(response.choices[0].message.content)
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{"role": "user", "content": "What is Oxen.ai?"}],
    "max_tokens": 200
  }'
```

## With Streaming

```python Python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://hub.oxen.ai/api/ai",
    api_key="YOUR_API_KEY",
)

stream = client.chat.completions.create(
    model="gemini-3-1-flash-lite-preview",
    messages=[{"role": "user", "content": "Write a haiku about data"}],
    stream=True,
)

for chunk in stream:
    content = chunk.choices[0].delta.content
    if content:
        print(content, end="", flush=True)
print()
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3-1-flash-lite-preview",
    "messages": [{"role": "user", "content": "Write a haiku about data"}],
    "stream": true
  }'
```

## With a Document (PDF)

Attach a PDF with a `file` content part. Oxen.ai translates the document to each
provider's native format, so it works the same regardless of which model you
call.

```python Python theme={null}
import base64
from openai import OpenAI

client = OpenAI(
    base_url="https://hub.oxen.ai/api/ai",
    api_key="YOUR_API_KEY",
)

with open("report.pdf", "rb") as f:
    file_data = "data:application/pdf;base64," + base64.standard_b64encode(f.read()).decode()

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "file", "file": {"filename": "report.pdf", "file_data": file_data}},
                {"type": "text", "text": "Summarize the key findings."},
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

```bash cURL theme={null}
FILE_DATA="data:application/pdf;base64,$(base64 < report.pdf | tr -d '\n')"
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "file", "file": {"filename": "report.pdf", "file_data": "'"$FILE_DATA"'"}},
        {"type": "text", "text": "Summarize the key findings."}
      ]
    }]
  }'
```

### Reference a document by URL

You can also point at a PDF by URL (handy for files generated in a
[workspace](https://docs.oxen.ai/concepts/workspaces)):

```python Python theme={null}
from openai import OpenAI

client = OpenAI(
    base_url="https://hub.oxen.ai/api/ai",
    api_key="YOUR_API_KEY",
)

pdf_url = "https://arxiv.org/pdf/1706.03762"

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "file", "file": {"file_url": pdf_url}},
                {"type": "text", "text": "Summarize the key findings."},
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

```bash cURL theme={null}
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [{
      "role": "user",
      "content": [
        {"type": "file", "file": {"file_url": "https://arxiv.org/pdf/1706.03762"}},
        {"type": "text", "text": "Summarize the key findings."}
      ]
    }]
  }'
```

The URL must be publicly accessible (and unexpired, if presigned). Only
`application/pdf` is supported, and a document must be 24 MB or smaller;
other inputs return a `400`. See the
[reference](https://docs.oxen.ai/inference-api/reference/chat_completions.md) for details.

## What's Next

* [Chat Completions Reference](https://docs.oxen.ai/inference-api/reference/chat_completions.md) for the full parameter list
* [Prompt caching](https://docs.oxen.ai/inference-api/reference/chat_completions.md#prompt-caching) to make repeated long prompts faster
* [Image Generation Quick Start](https://docs.oxen.ai/inference-api/quickstart/image-generation.md) to generate images
* [Video Generation Quick Start](https://docs.oxen.ai/inference-api/quickstart/video-generation.md) to generate videos


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.