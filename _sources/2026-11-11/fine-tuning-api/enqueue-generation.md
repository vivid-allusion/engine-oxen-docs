---
title: "Enqueue generation"
source: https://docs.oxen.ai/fine-tuning-api/enqueue-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Enqueue generation

> Enqueues an async image or video generation job.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/queue
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
    post:
      tags: []
      summary: Enqueue generation
      description: Enqueues an async image or video generation job.
      operationId: OxenApiWeb.Controllers.QueueController.create
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/QueueCreateRequest'
        description: Queue request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/QueueCreateResponse'
          description: Generation enqueued
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    QueueCreateRequest:
      description: >-
        Enqueue an async image or video generation job. `prompt` is required
        unless `draft_task_id` renders the final video from a Seedance draft,
        which reuses the draft's prompt, media, and settings.
      properties:
        aspect_ratio:
          nullable: true
          type: string
        draft:
          description: >-
            Seedance 2.5: render a quick 480p draft whose `draft_task_id` can
            render the final video.
          nullable: true
          type: boolean
        draft_task_id:
          description: >-
            Seedance 2.5: render the final 1080p video from this draft. No
            prompt is needed.
          nullable: true
          type: string
        duration:
          nullable: true
          type: integer
        model:
          description: Model ID to use
          type: string
        num_generations:
          default: 1
          maximum: 12
          minimum: 1
          type: integer
        prompt:
          description: Text prompt for generation
          nullable: true
          type: string
        seed:
          nullable: true
          type: integer
        target_directory:
          nullable: true
          type: string
        target_namespace:
          description: Namespace to store results. Defaults to current user.
          nullable: true
          type: string
        target_repo:
          nullable: true
          type: string
        workbench_session_id:
          description: >-
            Workbench session (tab) this generation belongs to. Must name an
            existing, non-deleted session on the target repository that the
            caller may use.
          format: uuid
          nullable: true
          type: string
      required:
        - model
      title: QueueCreateRequest
      type: object
    QueueCreateResponse:
      properties:
        generations:
          items:
            properties:
              generation_id:
                format: uuid
                type: string
              status:
                enum:
                  - queued
                type: string
            required:
              - generation_id
              - status
            type: object
          type: array
      required:
        - generations
      title: QueueCreateResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.