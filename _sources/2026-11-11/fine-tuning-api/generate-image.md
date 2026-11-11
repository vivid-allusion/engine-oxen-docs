---
title: "Generate image"
source: https://docs.oxen.ai/fine-tuning-api/generate-image
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Generate image

> Creates an image from a text prompt.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/images/generate
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
  /api/ai/images/generate:
    post:
      tags: []
      summary: Generate image
      description: Creates an image from a text prompt.
      operationId: OxenApiWeb.Controllers.ModelController.generate_image
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImageGenerateRequest'
        description: Image generation request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageGenerateResponse'
          description: Generated images
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    ImageGenerateRequest:
      properties:
        model:
          description: Model ID to use for image generation
          type: string
        'n':
          default: 1
          description: Number of images to generate
          type: integer
        prompt:
          description: Text prompt describing the desired image
          type: string
        seed:
          nullable: true
          type: integer
        size:
          description: Image size
          nullable: true
          type: string
      required:
        - model
        - prompt
      title: ImageGenerateRequest
      type: object
    ImageGenerateResponse:
      properties:
        created:
          type: integer
        images:
          items:
            properties:
              revised_prompt:
                nullable: true
                type: string
              url:
                type: string
            type: object
          type: array
        model:
          type: string
      title: ImageGenerateResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.