---
title: "List the values each filter column takes"
source: https://docs.oxen.ai/fine-tuning-api/list-the-values-each-filter-column-takes
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List the values each filter column takes

> Distinct values for each requested filter column, so a client can populate filter dropdowns with choices that actually match rows. Scope params (`namespace`, `user_id`) apply; the list endpoint's own filter params do not, so a selected value never narrows its own column.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/ai/generations/_filters
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
  /api/ai/generations/_filters:
    get:
      tags: []
      summary: List the values each filter column takes
      description: >-
        Distinct values for each requested filter column, so a client can
        populate filter dropdowns with choices that actually match rows. Scope
        params (`namespace`, `user_id`) apply; the list endpoint's own filter
        params do not, so a selected value never narrows its own column.
      operationId: OxenApiWeb.Controllers.GenerationsController.list_filter_values
      parameters:
        - description: >-
            Comma-separated filter columns. Allowed: `repo`, `folder`, `model`,
            `media_type`, `status`, `user_id` — the same keys the list endpoint
            filters on.
          in: query
          name: columns
          required: true
          schema:
            type: string
        - description: ''
          in: query
          name: namespace
          required: false
          schema:
            type: string
        - description: ''
          in: query
          name: user_id
          required: false
          schema:
            format: uuid
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/GenerationsFilterValuesResponse'
          description: Filter values
        '400':
          content:
            application/json:
              schema:
                type: object
          description: Missing, empty, or unknown columns
      callbacks: {}
components:
  schemas:
    GenerationsFilterValuesResponse:
      description: >-
        Distinct values for each requested filter column, keyed by the column
        name the caller passes back to the list endpoint. `truncated` says the
        column has more values than the response carries.
      properties:
        filters:
          additionalProperties:
            properties:
              truncated:
                type: boolean
              values:
                items:
                  type: string
                type: array
            required:
              - values
              - truncated
            type: object
          type: object
        status:
          example: success
          type: string
        status_message:
          example: resource_found
          type: string
      required:
        - status
        - status_message
        - filters
      title: GenerationsFilterValuesResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.