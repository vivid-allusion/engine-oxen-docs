---
title: "Get evaluation status"
source: https://docs.oxen.ai/fine-tuning-api/evaluations/get-evaluation-status
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get evaluation status

> Fetch a single evaluation by ID. Use this to poll for progress (`evaluation.progress.processed` / `evaluation.progress.total`) and completion (`evaluation.status`).



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/repos/{namespace}/{repo_name}/evaluations/{evaluation_id}
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
  /api/repos/{namespace}/{repo_name}/evaluations/{evaluation_id}:
    get:
      tags:
        - evaluations
      summary: Get evaluation status
      description: >-
        Fetch a single evaluation by ID. Use this to poll for progress
        (`evaluation.progress.processed` / `evaluation.progress.total`) and
        completion (`evaluation.status`).
      operationId: OxenApiWeb.Controllers.EvaluationController.get_evaluation
      parameters:
        - description: Evaluation ID
          example: d0c8585d-1234-5678-abcd-ef0123456789
          in: path
          name: evaluation_id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationResponse'
          description: Evaluation details
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Evaluation not found
      callbacks: {}
      security:
        - authorization: []
components:
  schemas:
    EvaluationResponse:
      description: Standard response wrapper for a single evaluation.
      properties:
        evaluation:
          anyOf:
            - $ref: '#/components/schemas/Evaluation'
          description: Evaluation resource
        status:
          description: High-level status string (for example, 'success').
          type: string
        status_message:
          description: Human-readable status message (for example, 'resource_found').
          type: string
      title: EvaluationResponse
      type: object
    Evaluation:
      description: >-
        An evaluation resource representing a model inference run over a
        dataset.
      properties:
        cancelled_at:
          format: date_time
          nullable: true
          type: string
        completed_at:
          format: date_time
          nullable: true
          type: string
        completion_tokens_used:
          description: Completion tokens consumed
          type: integer
        created_by:
          description: User who created the evaluation
          nullable: true
          properties:
            id:
              type: string
            image:
              nullable: true
              type: string
            name:
              nullable: true
              type: string
            username:
              type: string
          type: object
        credits_used:
          description: Credits consumed
          format: float
          type: number
        error_message:
          description: Error details if status is errored
          nullable: true
          type: string
        id:
          description: Evaluation ID
          format: uuid
          type: string
        input_type:
          enum:
            - text
            - image
            - video
          type: string
        inserted_at:
          format: date_time
          type: string
        is_sample:
          type: boolean
        model:
          additionalProperties: true
          description: Model used for this evaluation
          nullable: true
          type: object
        name:
          description: Evaluation name
          nullable: true
          type: string
        output_type:
          enum:
            - text
            - image
            - video
            - embeddings
          type: string
        progress:
          description: Processing progress
          properties:
            processed:
              description: Number of rows processed so far
              type: integer
            total:
              description: Total number of rows to process
              type: integer
          type: object
        prompt:
          description: Prompt template used for inference
          type: string
        prompt_tokens_used:
          description: Prompt tokens consumed
          type: integer
        repository_id:
          type: string
        resource:
          description: Source data resource
          nullable: true
          properties:
            path:
              description: Path inside the repository
              type: string
            version:
              description: Commit ID or version
              type: string
          type: object
        sample_count:
          type: integer
        started_at:
          format: date_time
          nullable: true
          type: string
        status:
          description: Current status
          enum:
            - queued
            - running
            - committing
            - completed
            - errored
            - cancelled
          type: string
        target_branch:
          nullable: true
          type: string
        target_column:
          nullable: true
          type: string
        target_path:
          nullable: true
          type: string
        tokens_used:
          description: Total tokens (prompt + completion)
          type: integer
      title: Evaluation
      type: object
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.