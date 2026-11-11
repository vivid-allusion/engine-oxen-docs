---
title: "List checkpoints for a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/list-checkpoints-for-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List checkpoints for a fine-tune job

> Retrieve all saved checkpoints for a fine-tune training run. Returns an empty list if the model branch has not been created yet (e.g. before training has produced checkpoints).



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/checkpoints
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/checkpoints:
    get:
      tags:
        - fine_tunes
      summary: List checkpoints for a fine-tune job
      description: >-
        Retrieve all saved checkpoints for a fine-tune training run. Returns an
        empty list if the model branch has not been created yet (e.g. before
        training has produced checkpoints).
      operationId: OxenApiWeb.Controllers.FineTuneController.checkpoints
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
                $ref: '#/components/schemas/CheckpointListResponse'
          description: Checkpoints list
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
    CheckpointListResponse:
      description: Standard wrapper for the list-checkpoints response.
      properties:
        branch:
          description: Oxen branch where the model and its checkpoints are stored.
          type: string
        checkpoints:
          description: >-
            Checkpoints saved during the fine-tune run, sorted by step
            ascending.
          items:
            $ref: '#/components/schemas/Checkpoint'
          type: array
        fine_tune_id:
          description: ID of the fine-tune job these checkpoints belong to.
          type: string
        status:
          description: High-level status string (for example, 'success').
          type: string
        status_message:
          description: Human-readable status message (for example, 'resource_found').
          type: string
        total_checkpoints:
          description: Total number of checkpoints returned.
          type: integer
      title: CheckpointListResponse
      type: object
    Checkpoint:
      description: >
        A single training checkpoint produced by a fine-tune run. Each
        checkpoint

        corresponds to a step directory in the model's Oxen branch and may carry

        metrics, inference samples, and (if previously deployed) deployment
        status.
      properties:
        created_at:
          description: Timestamp of the commit that produced this checkpoint.
          format: date_time
          nullable: true
          type: string
        deployment_status:
          description: >-
            Current Baseten deployment status for this checkpoint, if it has
            been deployed.
          nullable: true
          type: string
        inference_samples:
          description: Sample generations produced at this checkpoint, if any.
          items:
            additionalProperties: true
            type: object
          type: array
        metrics:
          additionalProperties: true
          description: >-
            Training metrics recorded at this step (when training logs are
            available).
          properties:
            epoch:
              format: float
              nullable: true
              type: number
            grad_norm:
              format: float
              nullable: true
              type: number
            learning_rate:
              format: float
              nullable: true
              type: number
            loss:
              format: float
              nullable: true
              type: number
            mean_token_accuracy:
              format: float
              nullable: true
              type: number
          type: object
        model_id:
          description: >-
            ID of the deployed Model row backing this checkpoint, if it has been
            deployed.
          nullable: true
          type: string
        model_name:
          description: >-
            Canonical model name used when this checkpoint is deployed (e.g.
            '<fine_tune_name>-step-<step>').
          type: string
        path:
          description: Path within the model branch where the checkpoint is stored.
          type: string
        size_bytes:
          description: Total size in bytes of the checkpoint directory.
          nullable: true
          type: integer
        step:
          description: Training step number this checkpoint was saved at.
          type: integer
      title: Checkpoint
      type: object
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.