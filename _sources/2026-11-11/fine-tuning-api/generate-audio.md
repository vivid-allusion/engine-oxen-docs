---
title: "Generate audio"
source: https://docs.oxen.ai/fine-tuning-api/generate-audio
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate audio

> Creates audio (e.g. speech) from a text prompt.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/audio/generate
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
  /api/ai/audio/generate:
    post:
      tags: []
      summary: Generate audio
      description: Creates audio (e.g. speech) from a text prompt.
      operationId: OxenApiWeb.Controllers.ModelController.generate_audio
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/AudioGenerateRequest'
        description: Audio generation request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/AudioGenerateResponse'
          description: Generated audio
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    AudioGenerateRequest:
      properties:
        audio_urls:
          description: Reference audio URLs for voice cloning
          items:
            type: string
          nullable: true
          type: array
        image_url:
          description: Reference image URL
          nullable: true
          type: string
        model:
          type: string
        output_format:
          description: wav, mp3, pcm, or ogg_opus
          nullable: true
          type: string
        pitch:
          nullable: true
          type: integer
        prompt:
          description: Text prompt or text to synthesize
          type: string
        response_format:
          description: url (default) or b64_json
          nullable: true
          type: string
        sample_rate:
          description: Output sample rate in Hz
          nullable: true
          type: integer
        save_to_workbench:
          description: Persist the generated audio to the workbench (default true)
          nullable: true
          type: boolean
        speed:
          nullable: true
          type: number
        voice:
          description: Preset voice name or cloned voice ID
          nullable: true
          type: string
        volume:
          nullable: true
          type: number
      required:
        - model
        - prompt
      title: AudioGenerateRequest
      type: object
    AudioGenerateResponse:
      properties:
        audios:
          items:
            properties:
              url:
                type: string
            type: object
          type: array
        created:
          type: integer
        model:
          type: string
      title: AudioGenerateResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.