---
title: "Get generation details"
source: https://docs.oxen.ai/fine-tuning-api/get-generation-details
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get generation details

> Full metadata for a single generation, including cost and the user who triggered it.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/ai/generations/{generation_id}
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
  /api/ai/generations/{generation_id}:
    get:
      tags: []
      summary: Get generation details
      description: >-
        Full metadata for a single generation, including cost and the user who
        triggered it.
      operationId: OxenApiWeb.Controllers.GenerationsController.show
      parameters:
        - description: ''
          in: path
          name: generation_id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerationsShowResponse'
          description: Generation details
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Generation not found
      callbacks: {}
components:
  schemas:
    GenerationsShowResponse:
      description: >-
        Standard success envelope wrapping a single generation under
        `generation`. The inner object is the same per-row shape returned by the
        list endpoint (request params merged in at the top level), so the
        frontend can reuse one type for both.
      properties:
        generation:
          properties:
            audios:
              items:
                additionalProperties: true
                description: >-
                  The stored media's `url`, with whatever else the model
                  returned beside it: a Seedance 2.5 draft (`draft: true`)
                  returns `draft_task_id` and `draft_expires_at`. Pass
                  `draft_task_id` back as the request param of the same name to
                  render the final video, with `resolution` set to `1080p` (the
                  default) or `4k`.
                properties:
                  draft_expires_at:
                    nullable: true
                    type: string
                  draft_task_id:
                    nullable: true
                    type: string
                  text:
                    description: >-
                      A text result's text (a transcript); the full JSON result
                      is the file at `url`.
                    nullable: true
                    type: string
                  url:
                    type: string
                type: object
              nullable: true
              type: array
            completed_at:
              description: Unix timestamp
              nullable: true
              type: integer
            cost:
              description: Charged amount for this row (decimal as string).
              nullable: true
              type: string
            enqueued_at:
              description: Unix timestamp
              type: integer
            error_message:
              nullable: true
              type: string
            generation_id:
              format: uuid
              type: string
            images:
              items:
                additionalProperties: true
                description: >-
                  The stored media's `url`, with whatever else the model
                  returned beside it: a Seedance 2.5 draft (`draft: true`)
                  returns `draft_task_id` and `draft_expires_at`. Pass
                  `draft_task_id` back as the request param of the same name to
                  render the final video, with `resolution` set to `1080p` (the
                  default) or `4k`.
                properties:
                  draft_expires_at:
                    nullable: true
                    type: string
                  draft_task_id:
                    nullable: true
                    type: string
                  text:
                    description: >-
                      A text result's text (a transcript); the full JSON result
                      is the file at `url`.
                    nullable: true
                    type: string
                  url:
                    type: string
                type: object
              nullable: true
              type: array
            media_type:
              enum:
                - image
                - video
                - audio
                - text
              type: string
            model_name:
              type: string
            result_url:
              nullable: true
              type: string
            started_at:
              description: Unix timestamp
              nullable: true
              type: integer
            status:
              enum:
                - queued
                - processing
                - succeeded
                - failed
                - cancelled
              type: string
            target_directory:
              nullable: true
              type: string
            target_namespace:
              nullable: true
              type: string
            target_repo:
              nullable: true
              type: string
            texts:
              items:
                additionalProperties: true
                description: >-
                  The stored media's `url`, with whatever else the model
                  returned beside it: a Seedance 2.5 draft (`draft: true`)
                  returns `draft_task_id` and `draft_expires_at`. Pass
                  `draft_task_id` back as the request param of the same name to
                  render the final video, with `resolution` set to `1080p` (the
                  default) or `4k`.
                properties:
                  draft_expires_at:
                    nullable: true
                    type: string
                  draft_task_id:
                    nullable: true
                    type: string
                  text:
                    description: >-
                      A text result's text (a transcript); the full JSON result
                      is the file at `url`.
                    nullable: true
                    type: string
                  url:
                    type: string
                type: object
              nullable: true
              type: array
            user_id:
              format: uuid
              nullable: true
              type: string
            user_image:
              nullable: true
              type: string
            username:
              nullable: true
              type: string
            videos:
              items:
                additionalProperties: true
                description: >-
                  The stored media's `url`, with whatever else the model
                  returned beside it: a Seedance 2.5 draft (`draft: true`)
                  returns `draft_task_id` and `draft_expires_at`. Pass
                  `draft_task_id` back as the request param of the same name to
                  render the final video, with `resolution` set to `1080p` (the
                  default) or `4k`.
                properties:
                  draft_expires_at:
                    nullable: true
                    type: string
                  draft_task_id:
                    nullable: true
                    type: string
                  text:
                    description: >-
                      A text result's text (a transcript); the full JSON result
                      is the file at `url`.
                    nullable: true
                    type: string
                  url:
                    type: string
                type: object
              nullable: true
              type: array
          required:
            - generation_id
            - model_name
            - media_type
            - status
            - enqueued_at
          type: object
        status:
          example: success
          type: string
        status_message:
          example: resource_found
          type: string
      required:
        - status
        - generation
        - status_message
      title: GenerationsShowResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.