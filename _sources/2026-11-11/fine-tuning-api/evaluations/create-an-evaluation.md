---
title: "Create an evaluation"
source: https://docs.oxen.ai/fine-tuning-api/evaluations/create-an-evaluation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create an evaluation

> Run model inference over a dataset in the repository. The resource path (branch and file) is encoded in the URL, e.g. `POST /api/repos/{ns}/{repo}/evaluations/main/datasets/training.parquet`.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/repos/{namespace}/{repo_name}/evaluations/*resource_path
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
  /api/repos/{namespace}/{repo_name}/evaluations/*resource_path:
    post:
      tags:
        - evaluations
      summary: Create an evaluation
      description: >-
        Run model inference over a dataset in the repository. The resource path
        (branch and file) is encoded in the URL, e.g. `POST
        /api/repos/{ns}/{repo}/evaluations/main/datasets/training.parquet`.
      operationId: OxenApiWeb.Controllers.EvaluationController.create_evaluation
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateEvaluationRequest'
        description: Create evaluation request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/EvaluationResponse'
          description: Evaluation created
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid parameters
      callbacks: {}
      security:
        - authorization: []
components:
  schemas:
    CreateEvaluationRequest:
      description: >
        Request payload to create an evaluation.


        The resource path (branch + file path) is specified in the URL after
        `/evaluations/`,

        for example: `POST
        /api/repos/{namespace}/{repo}/evaluations/main/datasets/training.parquet`.
      properties:
        auto_commit:
          default: false
          description: >-
            If true, automatically commit the results when the evaluation
            completes
          type: boolean
        batch_size:
          default: 10
          description: Number of rows to process per inference batch
          type: integer
        commit_message:
          description: Commit message used when auto_commit is true
          nullable: true
          type: string
        input_type:
          description: Type of input data
          enum:
            - text
            - image
            - video
          type: string
        is_sample:
          default: false
          description: >-
            If true, only evaluate a subset of rows. If false, evaluate all
            rows.
          type: boolean
        model_id:
          description: ID of the model to run inference with
          format: uuid
          type: string
        name:
          description: Human-readable name for the evaluation
          type: string
        output_type:
          description: Type of output produced by the model
          enum:
            - text
            - image
            - video
            - embeddings
          type: string
        prompt:
          description: >-
            Prompt template sent to the model. Use `{column_name}` placeholders
            to inject values from each row.
          type: string
        sample_count:
          default: 10
          description: Number of rows to sample when is_sample is true
          type: integer
        target_branch:
          description: Branch where evaluation results are committed
          type: string
        target_column:
          description: Column where the model output will be written
          type: string
        target_path:
          description: File path for the output data frame
          type: string
      required:
        - prompt
        - input_type
        - output_type
        - model_id
        - target_column
      title: CreateEvaluationRequest
      type: object
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