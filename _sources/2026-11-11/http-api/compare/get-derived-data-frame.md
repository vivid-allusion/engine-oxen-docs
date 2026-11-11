---
title: "Get Derived Data Frame"
source: https://docs.oxen.ai/http-api/compare/get-derived-data-frame
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get Derived Data Frame

> Get the derived diff data frame rows with pagination and optional filtering.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}/diff
openapi: 3.1.0
info:
  description: >-
    Oxen server is a fast data version control backend, supporting local disk
    and S3. Self host your repositories on your own storage, or use the hosted
    platform on Oxen.ai. Stores, syncs, and serves versioned datasets, model
    checkpoints, game assets, studio media, and any large data. Use the oxen CLI
    to push and pull from the oxen server.
  license:
    name: ''
  title: oxen-server
  version: 0.67.0
servers:
  - description: Production API
    url: https://hub.oxen.ai
  - description: Local Development
    url: http://localhost:3000
security:
  - api_key: []
tags:
  - description: Namespace management endpoints
    name: Namespaces
  - description: Repository management endpoints.
    name: Repositories
  - description: >-
      Editing a data frame inside a workspace, including its schema and column
      metadata.
    name: Workspace Data Frames
paths:
  /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}/diff:
    get:
      tags:
        - Compare
      summary: Get Derived Data Frame
      description: >-
        Get the derived diff data frame rows with pagination and optional
        filtering.
      operationId: get_derived_df
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: compare-datasets
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: The unique ID of the comparison session
          example: uuid-1234
          in: path
          name: compare_id
          required: true
          schema:
            type: string
        - description: Page number for pagination (starts at 1)
          in: query
          name: page
          required: false
          schema:
            minimum: 0
            type: integer
        - description: Page size for pagination
          in: query
          name: page_size
          required: false
          schema:
            minimum: 0
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/JsonDataFrameViewResponse'
          description: Derived data frame found successfully
        '404':
          description: Repository or comparison ID not found
components:
  schemas:
    JsonDataFrameViewResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            commit:
              oneOf:
                - $ref: '#/components/schemas/Commit'
                - type: 'null'
            data_frame:
              $ref: '#/components/schemas/JsonDataFrameViews'
            derived_resource:
              oneOf:
                - $ref: '#/components/schemas/DerivedDFResource'
                - type: 'null'
            resource:
              oneOf:
                - $ref: '#/components/schemas/ResourceVersion'
                - type: 'null'
          required:
            - data_frame
          type: object
    StatusMessage:
      properties:
        oxen_version:
          type:
            - string
            - 'null'
        status:
          type: string
        status_message:
          type: string
      required:
        - status
        - status_message
      type: object
    Commit:
      example:
        author: ox
        email: ox@example.com
        id: a1b2c3d4e5f67890abcdef1234567890
        message: Refactor data loading pipeline.
        parent_ids:
          - f1e2d3c4b5a67890fedcba9876543210
        timestamp: '2025-01-01T10:00:00Z'
      properties:
        author:
          type: string
        email:
          type: string
        id:
          type: string
        message:
          type: string
        parent_ids:
          items:
            type: string
          type: array
        timestamp:
          format: date-time
          type: string
      required:
        - id
        - parent_ids
        - message
        - author
        - email
        - timestamp
      type: object
    JsonDataFrameViews:
      properties:
        source:
          $ref: '#/components/schemas/DataFrameSchemaSize'
        view:
          $ref: '#/components/schemas/JsonDataFrameView'
      required:
        - source
        - view
      type: object
    DerivedDFResource:
      properties:
        path:
          type: string
        resource_id:
          type: string
        resource_type:
          $ref: '#/components/schemas/DFResourceType'
      required:
        - resource_id
        - path
        - resource_type
      type: object
    ResourceVersion:
      properties:
        path:
          type: string
        version:
          type: string
      required:
        - path
        - version
      type: object
    DataFrameSchemaSize:
      properties:
        schema:
          $ref: '#/components/schemas/Schema'
        size:
          $ref: '#/components/schemas/DataFrameSize'
      required:
        - schema
        - size
      type: object
    JsonDataFrameView:
      allOf:
        - $ref: '#/components/schemas/DFOptsView'
        - properties:
            data: {}
            pagination:
              $ref: '#/components/schemas/Pagination'
            schema:
              $ref: '#/components/schemas/Schema'
            size:
              $ref: '#/components/schemas/DataFrameSize'
          required:
            - schema
            - size
            - data
            - pagination
          type: object
    DFResourceType:
      enum:
        - compare
        - diff
        - query
      type: string
    Schema:
      properties:
        fields:
          items:
            $ref: '#/components/schemas/Field'
          type: array
        hash:
          type: string
        metadata: {}
      required:
        - hash
        - fields
      type: object
    DataFrameSize:
      properties:
        height:
          minimum: 0
          type: integer
        width:
          minimum: 0
          type: integer
      required:
        - height
        - width
      type: object
    DFOptsView:
      properties:
        opts:
          items:
            $ref: '#/components/schemas/DFOptView'
          type: array
      required:
        - opts
      type: object
    Pagination:
      properties:
        page_number:
          minimum: 0
          type: integer
        page_size:
          minimum: 0
          type: integer
        total_entries:
          minimum: 0
          type: integer
        total_pages:
          minimum: 0
          type: integer
      required:
        - page_size
        - page_number
        - total_pages
        - total_entries
      type: object
    Field:
      properties:
        changes:
          oneOf:
            - $ref: '#/components/schemas/Changes'
            - type: 'null'
        dtype:
          type: string
        metadata: {}
        name:
          type: string
      required:
        - name
        - dtype
      type: object
    DFOptView:
      properties:
        name:
          type: string
        value: {}
      required:
        - name
        - value
      type: object
    Changes:
      properties:
        previous:
          oneOf:
            - $ref: '#/components/schemas/PreviousField'
            - type: 'null'
        status:
          type: string
      required:
        - status
      type: object
    PreviousField:
      properties:
        dtype:
          type: string
        metadata: {}
        name:
          type: string
      required:
        - name
        - dtype
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.