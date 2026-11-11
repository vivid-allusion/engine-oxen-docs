---
title: "Get training status for a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/get-training-status-for-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get training status for a fine-tune job

> Retrieve the current training status of a fine-tune job.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/train_status
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/train_status:
    get:
      tags:
        - fine_tunes
      summary: Get training status for a fine-tune job
      description: Retrieve the current training status of a fine-tune job.
      operationId: OxenApiWeb.Controllers.FineTuneController.get_train_status
      parameters:
        - description: Fine-tune ID
          example: ft_123
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
                description: Training status information
                type: object
          description: Training status response
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Fine-tune not found
      callbacks: {}
      security:
        - authorization: []
components:
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.