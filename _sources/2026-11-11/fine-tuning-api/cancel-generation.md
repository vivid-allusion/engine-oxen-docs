---
title: "Cancel generation"
source: https://docs.oxen.ai/fine-tuning-api/cancel-generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Cancel generation

> Cancels a generation. The row is retained with status set to cancelled.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json delete /api/ai/queue/{generation_id}
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
  /api/ai/queue/{generation_id}:
    delete:
      tags: []
      summary: Cancel generation
      description: Cancels a generation. The row is retained with status set to cancelled.
      operationId: OxenApiWeb.Controllers.QueueController.delete
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
                $ref: '#/components/schemas/QueueDeleteResponse'
          description: Generation cancelled
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Generation not found
      callbacks: {}
components:
  schemas:
    QueueDeleteResponse:
      properties:
        generation_id:
          format: uuid
          type: string
        status:
          enum:
            - success
          type: string
      required:
        - status
        - generation_id
      title: QueueDeleteResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.