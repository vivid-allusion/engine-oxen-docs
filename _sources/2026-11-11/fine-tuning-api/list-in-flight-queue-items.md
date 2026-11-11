---
title: "List in-flight queue items"
source: https://docs.oxen.ai/fine-tuning-api/list-in-flight-queue-items
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List in-flight queue items

> Lean polling view of the workbench render queue. Returns active generations (status queued or processing) by default; pass an explicit `status=` filter to include terminal rows. For paginated history with cost aggregates, use `/api/ai/generations`.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/ai/queue
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
  /api/ai/queue:
    get:
      tags: []
      summary: List in-flight queue items
      description: >-
        Lean polling view of the workbench render queue. Returns active
        generations (status queued or processing) by default; pass an explicit
        `status=` filter to include terminal rows. For paginated history with
        cost aggregates, use `/api/ai/generations`.
      operationId: OxenApiWeb.Controllers.QueueController.index
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
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueListResponse'
          description: Generation list
      callbacks: {}
components:
  schemas:
    QueueListResponse:
      description: >-
        Lean polling view of the workbench render queue. Active
        (`queued`/`processing`) rows by default; pass an explicit `status=`
        filter to include terminal rows. For paginated browse with cost
        aggregates, see `/api/ai/generations`.
      properties:
        count:
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
              enqueued_at:
                description: Unix timestamp
                type: integer
              error_message:
                nullable: true
                type: string
              error_provider:
                description: Upstream provider the failure came from
                nullable: true
                type: string
              error_provider_code:
                description: Provider's own error code, when it gave one
                nullable: true
                type: string
              error_retryable:
                description: Whether retrying the same request could plausibly succeed
                nullable: true
                type: boolean
              error_source:
                description: >-
                  Where a failure originated, so a provider refusal reads
                  differently from an Oxen fault
                enum:
                  - user
                  - provider_policy
                  - provider
                  - oxen
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
              retried_from_id:
                description: >-
                  Id of the generation this row is a kill & retry of, when
                  applicable
                format: uuid
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
      required:
        - count
        - generations
      title: QueueListResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.