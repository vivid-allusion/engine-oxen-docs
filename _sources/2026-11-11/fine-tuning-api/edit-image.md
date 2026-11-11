---
title: "Edit image"
source: https://docs.oxen.ai/fine-tuning-api/edit-image
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Edit image

> Edits an image given a prompt and source image.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/images/edit
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
  /api/ai/images/edit:
    post:
      tags: []
      summary: Edit image
      description: Edits an image given a prompt and source image.
      operationId: OxenApiWeb.Controllers.ModelController.edit_image
      parameters: []
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/ImageEditRequest'
        description: Image edit request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ImageGenerateResponse'
          description: Edited images
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
      callbacks: {}
components:
  schemas:
    ImageEditRequest:
      properties:
        image:
          description: URL of the source image
          type: string
        mask:
          description: URL of the mask image
          nullable: true
          type: string
        model:
          type: string
        'n':
          default: 1
          type: integer
        prompt:
          description: Text instruction for the edit
          type: string
        size:
          nullable: true
          type: string
      required:
        - model
        - prompt
        - image
      title: ImageEditRequest
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