---
title: "Generate video"
source: https://docs.oxen.ai/fine-tuning-api/generate-video
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate video

> Creates a video from a text prompt.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/videos/generate
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
  /api/ai/videos/generate:
    post:
      tags: []
      summary: Generate video
      description: Creates a video from a text prompt.
      operationId: OxenApiWeb.Controllers.ModelController.generate_video
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/VideoGenerateRequest'
        description: Video generation request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VideoGenerateResponse'
          description: Generated videos
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    VideoGenerateRequest:
      description: >-
        `prompt` is required unless `draft_task_id` renders the final video from
        a draft, which reuses the draft's prompt, media, and settings.
      properties:
        aspect_ratio:
          nullable: true
          type: string
        draft:
          description: >-
            Seedance 2.5: render a quick 480p draft whose `draft_task_id` can
            render the final video.
          nullable: true
          type: boolean
        draft_task_id:
          description: >-
            Seedance 2.5: render the final 1080p video from this draft. No
            prompt is needed.
          nullable: true
          type: string
        duration:
          description: Duration in seconds
          nullable: true
          type: integer
        model:
          type: string
        prompt:
          description: Text prompt describing the desired video
          nullable: true
          type: string
        seed:
          nullable: true
          type: integer
      required:
        - model
      title: VideoGenerateRequest
      type: object
    VideoGenerateResponse:
      properties:
        created:
          type: integer
        model:
          type: string
        videos:
          items:
            additionalProperties: true
            description: >-
              The stored media's `url`, with whatever else the model returned
              beside it: a Seedance 2.5 draft (`draft: true`) returns
              `draft_task_id` and `draft_expires_at`. Pass `draft_task_id` back
              as the request param of the same name to render the final video,
              with `resolution` set to `1080p` (the default) or `4k`.
            properties:
              draft_expires_at:
                nullable: true
                type: string
              draft_task_id:
                nullable: true
                type: string
              text:
                description: >-
                  A text result's text (a transcript); the full JSON result is
                  the file at `url`.
                nullable: true
                type: string
              url:
                type: string
            type: object
          type: array
      title: VideoGenerateResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.