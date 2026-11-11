---
title: "Create a fine-tune job"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/create-a-fine-tune-job
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a fine-tune job

> Start a new fine-tune for a given repository.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/repos/{namespace}/{repo_name}/fine_tunes
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
  /api/repos/{namespace}/{repo_name}/fine_tunes:
    post:
      tags:
        - fine_tunes
      summary: Create a fine-tune job
      description: Start a new fine-tune for a given repository.
      operationId: OxenApiWeb.Controllers.FineTuneController.create
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/CreateFineTuneRequest'
        description: Create fine-tune request
        required: false
      responses:
        '201':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FineTuneResponse'
          description: Create fine-tune response
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid fine-tune parameters
      callbacks: {}
      security:
        - authorization: []
components:
  schemas:
    CreateFineTuneRequest:
      description: |
        Request payload to create a fine-tune job for a repository.
      properties:
        base_model:
          description: Canonical name of the base model to fine-tune
          type: string
        is_public:
          default: false
          description: >-
            Whether the resulting fine-tuned model should be public. Defaults to
            false.
          type: boolean
        oxen_model_path:
          description: >-
            Optional override for where the resulting model weights live in
            Oxen. Defaults to the fine-tune resource.
          nullable: true
          type: string
        resource:
          description: Repository path to the training data file or directory
          type: string
        script_type:
          description: Name of the fine-tune script to run
          type: string
        training_params:
          additionalProperties: true
          description: Training configuration parameters
          properties:
            batch_size:
              description: Per-device batch size used during training.
              type: integer
            caption_column:
              description: Name of the column containing text captions or prompts.
              type: string
            gradient_accumulation:
              description: >-
                Number of steps to accumulate gradients before an optimizer
                step.
              type: integer
            image_column:
              description: Name of the column containing image file paths.
              type: string
            learning_rate:
              description: Base learning rate for the optimizer.
              format: float
              type: number
            lora_alpha:
              description: LoRA alpha scaling factor for LoRA fine-tuning approaches.
              type: integer
            lora_rank:
              description: LoRA rank used for low-rank adaptation layers.
              type: integer
            sample_every:
              description: Interval (in steps) at which to generate samples.
              type: integer
            samples:
              description: >-
                Number of sample generations to produce at each sampling
                interval.
              type: integer
            steps:
              description: Total number of training steps to run.
              type: integer
            timestep_type:
              description: >-
                Strategy for sampling timesteps during training (for example,
                'weighted').
              type: string
            use_lora:
              default: true
              description: >-
                Whether to use LoRA fine-tuning (true) or full fine-tuning
                (false). If omitted, defaults to true.
              type: boolean
          type: object
      required:
        - resource
        - base_model
        - script_type
      title: CreateFineTuneRequest
      type: object
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