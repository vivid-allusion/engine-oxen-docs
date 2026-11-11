---
title: "Deploy a checkpoint from a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/deploy-a-checkpoint-from-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Deploy a checkpoint from a fine-tune job

> Deploy a specific training checkpoint to make it available for inference. Pass `retry=true` to tear down any existing deployment for this checkpoint before creating a new one.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/checkpoints/{step}/deploy
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
  /api/repos/{namespace}/{repo_name}/fine_tunes/{id}/checkpoints/{step}/deploy:
    post:
      tags:
        - fine_tunes
      summary: Deploy a checkpoint from a fine-tune job
      description: >-
        Deploy a specific training checkpoint to make it available for
        inference. Pass `retry=true` to tear down any existing deployment for
        this checkpoint before creating a new one.
      operationId: OxenApiWeb.Controllers.FineTuneController.create_checkpoint_deployment
      parameters:
        - description: Fine-tune ID
          example: ft_123
          in: path
          name: id
          required: true
          schema:
            type: string
        - description: Checkpoint step number
          example: 100
          in: path
          name: step
          required: true
          schema:
            type: integer
        - description: >-
            If true, cleanup the existing deployment and model for this
            checkpoint before creating a new one.
          in: query
          name: retry
          required: false
          schema:
            type: boolean
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateCheckpointDeploymentRequest'
        description: Deployment configuration
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CheckpointDeploymentResponse'
          description: Deployment created response
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
    CreateCheckpointDeploymentRequest:
      description: Request payload to deploy a specific checkpoint from a fine-tune job.
      properties:
        deployment_type:
          default: normal
          description: >-
            Deployment type: 'fast' for faster inference instances, 'normal' for
            standard instances.
          enum:
            - fast
            - normal
          type: string
      title: CreateCheckpointDeploymentRequest
      type: object
    CheckpointDeploymentResponse:
      description: Standard wrapper for checkpoint deployment responses.
      properties:
        deployment_id:
          description: ID of the created Baseten deployment.
          type: string
        fine_tune:
          anyOf:
            - $ref: '#/components/schemas/FineTuneRun'
          description: Fine-tune job the deployed checkpoint belongs to.
        model:
          additionalProperties: true
          description: Model record created for this checkpoint deployment.
          type: object
        status:
          description: High-level status string (for example, 'success').
          type: string
        status_message:
          description: Human-readable status message (for example, 'resource_found').
          type: string
      title: CheckpointDeploymentResponse
      type: object
    FineTuneRun:
      additionalProperties: true
      description: Fine-tune job payload as returned by the /run API.
      properties:
        base_model:
          description: Canonical name of the base model, e.g. 'Qwen/Qwen3-0.6B'
          type: string
        created_by:
          description: User who created the fine-tune job
          properties:
            id:
              description: User ID
              type: string
            image:
              description: Avatar image URL
              nullable: true
              type: string
            name:
              description: Display name
              nullable: true
              type: string
            username:
              description: Username
              type: string
          type: object
        credits_used:
          description: Credits used so far for this fine-tune
          type: string
        deployed_model:
          additionalProperties: true
          description: Deployment information for the resulting model, if deployed
          nullable: true
          type: object
        description:
          description: Optional description of the fine-tune
          nullable: true
          type: string
        display_name:
          description: Optional display name for the fine-tune
          nullable: true
          type: string
        error:
          description: Error message if the fine-tune failed
          nullable: true
          type: string
        fine_tune_script:
          description: Fine-tune script configuration used for this run
          properties:
            description:
              description: Description of what the script does
              type: string
            display_name:
              description: Human-friendly name for the script
              type: string
            docker_image_name:
              description: Docker image used to run the script
              type: string
            fine_tune_schema:
              additionalProperties: true
              description: Fine-tune configuration schema used by the script
              properties:
                description:
                  description: Schema description
                  type: string
                id:
                  description: Fine-tune schema ID
                  type: string
                name:
                  description: Schema name
                  type: string
                schema:
                  additionalProperties: true
                  description: JSON schema describing training params UI
                  properties:
                    additionalProperties:
                      type: boolean
                    basic:
                      items:
                        type: string
                      type: array
                    properties:
                      additionalProperties: true
                      description: Per-parameter schema; structure is flexible
                      type: object
                    required:
                      items:
                        type: string
                      type: array
                    type:
                      type: string
                  type: object
              type: object
            id:
              description: Fine-tune script ID
              type: string
            name:
              description: Fine-tune script name
              type: string
            script_type:
              description: Type of script (for example, 'text_generation')
              type: string
          type: object
        finished_at:
          description: Time when training finished
          format: date_time
          nullable: true
          type: string
        gpu_count:
          description: Number of GPUs requested for the job
          type: integer
        gpu_model:
          description: GPU model requested for the job (for example, 'A10G')
          type: string
        id:
          description: Fine-tune ID
          type: string
        inserted_at:
          description: Creation timestamp
          format: date_time
          type: string
        last_credit_check:
          description: Last time credits were checked for this job
          format: date_time
          nullable: true
          type: string
        name:
          description: Fine-tune name
          type: string
        output_resource:
          additionalProperties: true
          description: Optional output resource produced by this fine-tune
          nullable: true
          type: object
        queue_position:
          description: Queue position if the job is queued
          nullable: true
          type: integer
        rate_per_second:
          description: Billing rate per second for this fine-tune
          type: string
        repository_id:
          description: ID of the repository this fine-tune belongs to
          type: string
        resource:
          description: Training data resource used for this fine-tune
          properties:
            path:
              description: Path to the resource inside the repository
              type: string
            version:
              description: Commit or version identifier
              type: string
          type: object
        source_model:
          additionalProperties: true
          description: Base model that is being fine-tuned
          type: object
        started_at:
          description: Time when training actually started
          format: date_time
          nullable: true
          type: string
        status:
          description: Current status of the fine-tune
          type: string
        total_token_count:
          default: 0
          description: Total number of tokens processed
          type: integer
        training_params:
          description: Training parameters used for this fine-tune run
          properties:
            answer_column:
              description: Column containing assistant responses
              type: string
            batch_size:
              description: Per-device batch size used during training
              type: integer
            enable_thinking:
              description: Whether to enable thinking tokens during training
              type: boolean
            epochs:
              description: Number of epochs to train for
              type: integer
            grad_accum:
              description: Gradient accumulation steps
              type: integer
            learning_rate:
              description: Base learning rate for the optimizer
              format: float
              type: number
            logging_steps:
              description: Interval (in steps) at which logs are written
              type: integer
            lora_alpha:
              description: LoRA alpha scaling factor
              type: integer
            lora_rank:
              description: LoRA rank for low-rank adapters
              type: integer
            neftune_noise_alpha:
              description: NEFTune noise alpha
              format: float
              type: number
            question_column:
              description: Column containing user prompts
              type: string
            save_steps_ratio:
              description: Ratio of steps at which to save checkpoints
              format: float
              type: number
            save_strategy:
              description: Save strategy, e.g. 'epoch'
              type: string
            seq_length:
              description: Sequence length used during training
              type: integer
            use_lora:
              description: Whether LoRA is enabled for this run
              type: boolean
          type: object
        updated_at:
          description: Last update timestamp
          format: date_time
          type: string
        use_lora:
          description: Whether LoRA fine-tuning is enabled
          type: boolean
      title: FineTuneRun
      type: object
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.