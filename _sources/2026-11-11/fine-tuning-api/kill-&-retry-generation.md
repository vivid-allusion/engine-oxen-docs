---
title: "Kill & retry generation"
source: https://docs.oxen.ai/fine-tuning-api/kill-&-retry-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Kill & retry generation

> Cancels a generation (and any live job backing it), then enqueues a fresh generation with the same parameters. The original row is retained with status cancelled and the new row links back to it via `retried_from_id`. A generation that already succeeded cannot be retried.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/queue/{generation_id}/retry
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
  /api/ai/queue/{generation_id}/retry:
    post:
      tags: []
      summary: Kill & retry generation
      description: >-
        Cancels a generation (and any live job backing it), then enqueues a
        fresh generation with the same parameters. The original row is retained
        with status cancelled and the new row links back to it via
        `retried_from_id`. A generation that already succeeded cannot be
        retried.
      operationId: OxenApiWeb.Controllers.QueueController.retry
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
                $ref: '#/components/schemas/QueueRetryResponse'
          description: Retry enqueued
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Generation not found
        '409':
          content:
            application/json:
              schema:
                type: object
          description: Generation already succeeded
      callbacks: {}
components:
  schemas:
    QueueRetryResponse:
      description: >-
        Result of a kill & retry: `generation_id` is the freshly enqueued
        generation, `retried_from_id` the cancelled original.
      properties:
        generation_id:
          format: uuid
          type: string
        retried_from_id:
          format: uuid
          type: string
        status:
          enum:
            - success
          type: string
      required:
        - status
        - generation_id
        - retried_from_id
      title: QueueRetryResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.