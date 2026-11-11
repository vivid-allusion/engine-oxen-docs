---
title: "Estimate a generation's cost"
source: https://docs.oxen.ai/fine-tuning-api/estimate-a-generations-cost
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Estimate a generation's cost

> Estimates what a generation with these parameters would cost, from the same pricing that bills it. `kind` is `exact`, `range` (the parameters leave the length or size open), `rate` (billed by usage only known after the run; see `rates`) or `unknown`. The final charge is always computed from the run's actual usage.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/ai/models/{id}/estimate
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
  /api/ai/models/{id}/estimate:
    post:
      tags: []
      summary: Estimate a generation's cost
      description: >-
        Estimates what a generation with these parameters would cost, from the
        same pricing that bills it. `kind` is `exact`, `range` (the parameters
        leave the length or size open), `rate` (billed by usage only known after
        the run; see `rates`) or `unknown`. The final charge is always computed
        from the run's actual usage.
      operationId: OxenApiWeb.Controllers.ModelsController.estimate
      parameters:
        - description: Model ID (UUID) or name
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
                input_image_height:
                  description: Height in pixels of the input image
                  maximum: 65535
                  minimum: 1
                  type: integer
                input_image_width:
                  description: >-
                    Width in pixels of the input image; with input_image_height,
                    prices an image model billed by output size exactly
                  maximum: 65535
                  minimum: 1
                  type: integer
                input_video_seconds:
                  description: >-
                    Length of the longest input video; prices a video edit,
                    which runs at that length
                  minimum: 0
                  type: number
                num_generations:
                  default: 1
                  maximum: 100
                  minimum: 1
                  type: integer
                params:
                  description: The model's request parameters, per its json_request_schema
                  type: object
              type: object
        description: Estimate request
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                properties:
                  estimate:
                    properties:
                      kind:
                        enum:
                          - exact
                          - range
                          - rate
                          - unknown
                        type: string
                      label:
                        type: string
                      max_usd:
                        nullable: true
                        type: string
                      min_usd:
                        nullable: true
                        type: string
                      note:
                        type: string
                      rates:
                        items:
                          properties:
                            per:
                              description: >-
                                The unit: second, credit, 1M input tokens, 1M
                                output tokens
                              type: string
                            usd:
                              description: Dollars per unit, as a decimal string
                              type: string
                          type: object
                        type: array
                    type: object
                  model:
                    type: string
                type: object
          description: Cost estimate
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Invalid request
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Model not found
      callbacks: {}

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.