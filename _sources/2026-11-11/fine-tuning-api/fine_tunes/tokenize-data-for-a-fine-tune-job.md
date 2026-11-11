---
title: "Tokenize data for a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/tokenize-data-for-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Tokenize data for a fine-tune job

> Trigger tokenization for a fine-tune that is in created state.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/tokenize
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/tokenize:
    post:
      tags:
        - fine_tunes
      summary: Tokenize data for a fine-tune job
      description: Trigger tokenization for a fine-tune that is in created state.
      operationId: OxenApiWeb.Controllers.FineTuneController.tokenize
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
                description: Wrapped fine-tune object
                type: object
          description: Tokenize fine-tune response
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