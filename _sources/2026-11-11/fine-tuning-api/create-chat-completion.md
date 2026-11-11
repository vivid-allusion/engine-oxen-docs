---
title: "Create chat completion"
source: https://docs.oxen.ai/fine-tuning-api/create-chat-completion
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create chat completion

> Generates a model response for the given conversation. Compatible with the OpenAI chat completions API.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/chat/completions
openapi: 3.0.0
info:
  title: oxen
  version: v282
servers:
  - url: https://hub.oxen.ai
    variables: {}
security: []
tags: []
paths:
  /api/ai/chat/completions:
    post:
      tags: []
      summary: Create chat completion
      description: >-
        Generates a model response for the given conversation. Compatible with
        the OpenAI chat completions API.
      operationId: OxenApiWeb.Controllers.ModelController.get_model_response
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ChatCompletionRequest'
        description: Chat completion request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ChatCompletionResponse'
          description: Chat completion
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    ChatCompletionRequest:
      description: >-
        Request to generate a chat completion. Compatible with the OpenAI chat
        completions API.
      properties:
        frequency_penalty:
          nullable: true
          type: number
        max_tokens:
          nullable: true
          type: integer
        messages:
          items:
            properties:
              content:
                oneOf:
                  - type: string
                  - items:
                      type: object
                    type: array
              name:
                nullable: true
                type: string
              role:
                enum:
                  - system
                  - user
                  - assistant
                  - tool
                type: string
              tool_call_id:
                nullable: true
                type: string
              tool_calls:
                items:
                  type: object
                nullable: true
                type: array
            required:
              - role
              - content
            type: object
          type: array
        model:
          description: Model ID to use
          example: gpt-4o
          type: string
        presence_penalty:
          nullable: true
          type: number
        reasoning_effort:
          description: >-
            Reasoning/thinking effort for models that support it (e.g. "low",
            "medium", "high"). Accepted values vary by model: OpenAI reasoning
            models take minimal/low/medium/high, Claude models take
            low/medium/high/xhigh/max, Kimi K3 only supports max. Ignored by
            models without configurable reasoning.
          nullable: true
          type: string
        response_format:
          nullable: true
          type: object
        service_tier:
          default: auto
          description: >-
            Processing tier, as on OpenAI and OpenRouter. "auto" (the default)
            runs at the standard tier; "ultrafast" opts into OpenAI's Ultrafast
            mode on models that offer it (GPT 6.1 Sol, GPT 6 Astra) at its
            higher per-token price. The other tier names (default, flex,
            priority, fast) are accepted; a tier the model does not price runs
            at the standard tier. The response's top-level `service_tier`
            reports the tier actually served, and the request bills at that
            tier's rates.
          nullable: true
          type: string
        stream:
          default: false
          type: boolean
        temperature:
          nullable: true
          type: number
        tool_choice:
          nullable: true
          oneOf:
            - type: string
            - type: object
        tools:
          items:
            type: object
          nullable: true
          type: array
        top_p:
          nullable: true
          type: number
      required:
        - model
        - messages
      title: ChatCompletionRequest
      type: object
    ChatCompletionResponse:
      properties:
        choices:
          items:
            properties:
              finish_reason:
                type: string
              index:
                type: integer
              message:
                properties:
                  content:
                    nullable: true
                    type: string
                  role:
                    type: string
                  tool_calls:
                    items:
                      type: object
                    nullable: true
                    type: array
                type: object
            type: object
          type: array
        created:
          type: integer
        id:
          type: string
        model:
          type: string
        object:
          enum:
            - chat.completion
          type: string
        usage:
          nullable: true
          properties:
            completion_tokens:
              type: integer
            prompt_tokens:
              type: integer
            prompt_tokens_details:
              description: >-
                Present when the provider reported prompt-cache activity.
                cached_tokens counts prompt tokens served from the provider's
                prompt cache; they are included in prompt_tokens.
              nullable: true
              properties:
                cached_tokens:
                  type: integer
              type: object
            total_tokens:
              type: integer
          type: object
      title: ChatCompletionResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.