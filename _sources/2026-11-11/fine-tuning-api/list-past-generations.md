---
title: "List past generations"
source: https://docs.oxen.ai/fine-tuning-api/list-past-generations
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List past generations

> Paginated browse view of completed and in-flight generations for a namespace. Use `/api/ai/queue` for the lean polling view of in-flight rows.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/ai/generations
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
  /api/ai/generations:
    get:
      tags: []
      summary: List past generations
      description: >-
        Paginated browse view of completed and in-flight generations for a
        namespace. Use `/api/ai/queue` for the lean polling view of in-flight
        rows.
      operationId: OxenApiWeb.Controllers.GenerationsController.index
      parameters:
        - description: ''
          in: query
          name: namespace
          required: false
          schema:
            type: string
        - description: ''
          in: query
          name: model
          required: false
          schema:
            type: string
        - description: ''
          in: query
          name: media_type
          required: false
          schema:
            enum:
              - image
              - video
            type: string
        - description: ''
          in: query
          name: status
          required: false
          schema:
            enum:
              - queued
              - processing
              - succeeded
              - failed
              - cancelled
            type: string
        - description: ''
          in: query
          name: repo
          required: false
          schema:
            type: string
        - description: ''
          in: query
          name: folder
          required: false
          schema:
            type: string
        - description: ''
          in: query
          name: user_id
          required: false
          schema:
            format: uuid
            type: string
        - description: ''
          in: query
          name: page
          required: false
          schema:
            default: 1
            minimum: 1
            type: integer
        - description: ''
          in: query
          name: page_size
          required: false
          schema:
            default: 50
            maximum: 1000
            minimum: 1
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerationsListResponse'
          description: Generation list
      callbacks: {}
components:
  schemas:
    GenerationsListResponse:
      description: >-
        Paginated browse view of past generations for a namespace. Includes the
        per-filter cost aggregate. Each row carries any additional request
        params (prompt, duration, etc.) merged in at the top level.
      properties:
        count:
          description: Number of entries in this response (<= page_size)
          type: integer
        generations:
          items:
            properties:
              audios:
                items:
                  additionalProperties: true
                  description: >-
                    The stored media's `url`, with whatever else the model
                    returned beside it: a Seedance 2.5 draft (`draft: true`)
                    returns `draft_task_id` and `draft_expires_at`. Pass
                    `draft_task_id` back as the request param of the same name
                    to render the final video, with `resolution` set to `1080p`
                    (the default) or `4k`.
                  properties:
                    draft_expires_at:
                      nullable: true
                      type: string
                    draft_task_id:
                      nullable: true
                      type: string
                    text:
                      description: >-
                        A text result's text (a transcript); the full JSON
                        result is the file at `url`.
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
                    `draft_task_id` back as the request param of the same name
                    to render the final video, with `resolution` set to `1080p`
                    (the default) or `4k`.
                  properties:
                    draft_expires_at:
                      nullable: true
                      type: string
                    draft_task_id:
                      nullable: true
                      type: string
                    text:
                      description: >-
                        A text result's text (a transcript); the full JSON
                        result is the file at `url`.
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
                    `draft_task_id` back as the request param of the same name
                    to render the final video, with `resolution` set to `1080p`
                    (the default) or `4k`.
                  properties:
                    draft_expires_at:
                      nullable: true
                      type: string
                    draft_task_id:
                      nullable: true
                      type: string
                    text:
                      description: >-
                        A text result's text (a transcript); the full JSON
                        result is the file at `url`.
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
                    `draft_task_id` back as the request param of the same name
                    to render the final video, with `resolution` set to `1080p`
                    (the default) or `4k`.
                  properties:
                    draft_expires_at:
                      nullable: true
                      type: string
                    draft_task_id:
                      nullable: true
                      type: string
                    text:
                      description: >-
                        A text result's text (a transcript); the full JSON
                        result is the file at `url`.
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
          type: array
        page_number:
          description: Current page number (1-indexed)
          type: integer
        page_size:
          type: integer
        total_cost:
          description: >-
            Sum of charged amounts across the filter set (decimal as string).
            Null when nothing in the set has been charged.
          nullable: true
          type: string
        total_entries:
          type: integer
        total_pages:
          type: integer
      required:
        - count
        - generations
        - page_number
        - page_size
        - total_pages
        - total_entries
        - total_cost
      title: GenerationsListResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.