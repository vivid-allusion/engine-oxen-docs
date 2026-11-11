---
title: "Get logs for a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/get-logs-for-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get logs for a fine-tune job

> Fetch aggregated logs for a specific fine-tune run.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/logs
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/logs:
    get:
      tags:
        - fine_tunes
      summary: Get logs for a fine-tune job
      description: Fetch aggregated logs for a specific fine-tune run.
      operationId: OxenApiWeb.Controllers.FineTuneController.logs
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
                description: Fine-tune log payload
                type: object
          description: Fine-tune logs response
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