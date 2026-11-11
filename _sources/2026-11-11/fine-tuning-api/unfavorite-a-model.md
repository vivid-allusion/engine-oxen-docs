---
title: "Unfavorite a model"
source: https://docs.oxen.ai/fine-tuning-api/unfavorite-a-model
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Unfavorite a model



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json delete /api/ai/models/{id}/favorite
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
  /api/ai/models/{id}/favorite:
    delete:
      tags: []
      summary: Unfavorite a model
      operationId: OxenApiWeb.Controllers.ModelsController.delete_favorite
      parameters:
        - description: ''
          in: path
          name: id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Model'
          description: Model unfavorited
      callbacks: {}
components:
  schemas:
    Model:
      description: >-
        Represents a model available for inference or fine-tuning. Compatible
        with the OpenAI model object.
      properties:
        capabilities:
          properties:
            input:
              items:
                type: string
              type: array
            output:
              items:
                type: string
              type: array
            recommended_for:
              description: >-
                What an agent should pick this model for, among models with its
                output.
              items:
                enum:
                  - fast
                  - cheap
                  - best
                type: string
              type: array
            tools:
              description: True for a chat model that can call tools.
              type: boolean
          type: object
        context_length:
          description: >-
            Provider-documented context window: total tokens the model can
            attend to. Null for models without a documented window (e.g.
            image/video models).
          nullable: true
          type: integer
        created:
          description: Unix timestamp when the model was registered
          type: integer
        deployments:
          description: Active deployments. Empty for base models.
          items:
            properties:
              status:
                enum:
                  - active
                  - inactive
                  - deploying
                  - deactivating
                  - error
                  - unknown
                type: string
            type: object
          type: array
        description:
          nullable: true
          type: string
        developer:
          nullable: true
          properties:
            logo:
              nullable: true
              type: string
            name:
              type: string
          type: object
        display_name:
          type: string
        endpoint:
          description: API endpoint to call this model
          enum:
            - /chat/completions
            - /images/generate
            - /videos/generate
            - /audio/generate
            - /ai/queue
          type: string
        fine_tuning:
          description: Fine-tuning info, or null if model is not fine-tuneable
          nullable: true
          properties:
            actions:
              description: Supported fine-tune action types
              items:
                type: string
              type: array
            cost_per_second:
              nullable: true
              type: number
          type: object
        id:
          description: Model identifier used in API calls
          type: string
        image_url:
          nullable: true
          type: string
        max_output_tokens:
          description: >-
            Maximum tokens a single completion can produce. Null when the
            provider does not document a cap.
          nullable: true
          type: integer
        model_type:
          enum:
            - base
            - custom
          type: string
        object:
          enum:
            - model
          type: string
        owned_by:
          description: '"oxen" for base models, owner namespace for custom models'
          type: string
        pricing:
          properties:
            cached_input_cost_per_token:
              description: >-
                Rate billed per prompt token served from the provider's prompt
                cache (reported as prompt_tokens_details.cached_tokens in
                usage). Absent means cached tokens bill at input_cost_per_token.
              nullable: true
              type: number
            cost_per_character:
              description: >-
                Rate billed per character of input text, for per_character
                models.
              nullable: true
              type: number
            cost_per_credit:
              description: >-
                Rate billed per provider credit the run consumes, for
                per_provider_credit models. Prefer the estimate endpoint, which
                prices a request in dollars.
              nullable: true
              type: number
            cost_per_image:
              nullable: true
              type: number
            cost_per_image_grid:
              additionalProperties:
                additionalProperties:
                  type: number
                type: object
              description: >-
                Cost per image keyed by quality then resolution tier (e.g.
                {"high": {"4K": 1.47}}). An "input_image" row, when present, is
                the charge per reference image on top of the output.
              nullable: true
              type: object
            cost_per_input_second:
              description: >-
                Rate billed per second of the uploaded input audio, for
                per_audio_input_second models.
              nullable: true
              type: number
            cost_per_megapixel:
              description: >-
                Rate billed per megapixel of output image, for models priced by
                output area. It takes precedence when the response reports an
                output size; a model may still carry cost_per_image or
                cost_per_image_grid, which bill when no size is reported.
              nullable: true
              type: number
            cost_per_second:
              nullable: true
              type: number
            cost_per_second_by_resolution:
              additionalProperties:
                type: number
              description: >-
                Cost per output second keyed by resolution (e.g. {"480p":
                0.096})
              nullable: true
              type: object
            cost_per_second_high_res:
              nullable: true
              type: number
            cost_per_second_with_audio:
              nullable: true
              type: number
            input_cost_per_token:
              nullable: true
              type: number
            megapixels_per_credit:
              description: >-
                Output megapixels one credit covers, for per_provider_credit
                image models billed ceil(output MP / megapixels_per_credit)
                credits. cost_per_credit / megapixels_per_credit is the price
                per output megapixel, charged in whole steps.
              nullable: true
              type: number
            method:
              enum:
                - token
                - time
                - per_image
                - per_video_output_second
                - per_audio_output_second
                - per_audio_input_second
                - per_character
                - per_provider_credit
              type: string
            output_cost_per_token:
              nullable: true
              type: number
          type: object
        released_at:
          nullable: true
          type: string
        request_schema:
          description: JSON Schema describing model-specific parameters
          nullable: true
          type: object
        showcase:
          description: >-
            Optional marketing content rendered on the public model showcase
            page
          nullable: true
          properties:
            gallery:
              items:
                properties:
                  alt:
                    type: string
                  category:
                    nullable: true
                    type: string
                  details:
                    nullable: true
                    type: string
                  prompt:
                    nullable: true
                    type: string
                  src:
                    description: Absolute URL
                    type: string
                  title:
                    nullable: true
                    type: string
                required:
                  - src
                  - alt
                type: object
              type: array
            hero_image:
              description: Absolute URL
              nullable: true
              type: string
            tagline:
              nullable: true
              type: string
          type: object
        source_model:
          description: Base model this was fine-tuned from
          nullable: true
          type: string
        summary:
          nullable: true
          type: string
      required:
        - id
        - object
        - created
        - owned_by
      title: Model
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.