---
title: "Rename or describe a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/rename-or-describe-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename or describe a fine-tune job

> Change a fine-tune job's display name and description. Other fields in the body are ignored.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json patch /api/repos/{namespace}/{repo_name}/fine_tunes/{id}
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}:
    patch:
      tags:
        - fine_tunes
      summary: Rename or describe a fine-tune job
      description: >-
        Change a fine-tune job's display name and description. Other fields in
        the body are ignored.
      operationId: OxenApiWeb.Controllers.FineTuneController.update
      parameters:
        - description: Fine-tune ID
          example: ft_123
          in: path
          name: id
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              properties:
                description:
                  description: Description of the fine-tune job
                  type: string
                display_name:
                  description: Name shown for the fine-tune job
                  type: string
              type: object
        description: Fine-tune update request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FineTuneResponse'
          description: Updated fine-tune response
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
  schemas:
    FineTuneResponse:
      description: Standard wrapper for fine-tune responses.
      properties:
        fine_tune:
          anyOf:
            - $ref: '#/components/schemas/FineTune'
          description: Fine-tune job resource
        status:
          description: High-level status string (for example, 'success').
          type: string
        status_message:
          description: Human-readable status message (for example, 'resource_found').
          type: string
      title: FineTuneResponse
      type: object
    FineTune:
      description: >
        Fine-tune job resource.

        This is a simplified view meant for OpenAPI docs; extend as needed to
        match your views.
      properties:
        base_model:
          description: Canonical name of the base model
          type: string
        created_at:
          description: Creation time
          format: date_time
          type: string
        id:
          description: Fine-tune ID
          type: string
        name:
          description: Fine-tune name
          type: string
        status:
          description: Current status of the fine-tune
          type: string
        updated_at:
          description: Last update time
          format: date_time
          type: string
      title: FineTune
      type: object
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.