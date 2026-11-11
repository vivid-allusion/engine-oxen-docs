---
title: "Update tabular data frame diff"
source: https://docs.oxen.ai/http-api/data-frames/update-tabular-data-frame-diff
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update tabular data frame diff

> Update an existing cached tabular diff comparison with new configuration.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json put /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}
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
  /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}:
    put:
      tags:
        - Data Frames
      summary: Update tabular data frame diff
      description: >-
        Update an existing cached tabular diff comparison with new
        configuration.
      operationId: update_df_diff
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
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/TabularCompareBody'
        description: Updated tabular comparison configuration
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompareTabularResponse'
          description: Data frame diff updated and cached successfully
        '400':
          description: Bad Request
        '404':
          description: Comparison ID, Repository, revision, or file not found
components:
  schemas:
    TabularCompareBody:
      properties:
        compare:
          items:
            $ref: '#/components/schemas/TabularCompareTargetBody'
          type: array
        compare_id:
          type: string
        display:
          items:
            $ref: '#/components/schemas/TabularCompareTargetBody'
          type: array
        keys:
          items:
            $ref: '#/components/schemas/TabularCompareFieldBody'
          type: array
        left:
          $ref: '#/components/schemas/TabularCompareResourceBody'
        right:
          $ref: '#/components/schemas/TabularCompareResourceBody'
      required:
        - compare_id
        - left
        - right
        - keys
        - compare
        - display
      type: object
    CompareTabularResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            dfs:
              $ref: '#/components/schemas/CompareTabular'
            messages:
              items:
                $ref: '#/components/schemas/OxenMessage'
              type: array
          required:
            - dfs
            - messages
          type: object
    TabularCompareTargetBody:
      properties:
        compare_method:
          type:
            - string
            - 'null'
        left:
          type:
            - string
            - 'null'
        right:
          type:
            - string
            - 'null'
      type: object
    TabularCompareFieldBody:
      properties:
        alias_as:
          type:
            - string
            - 'null'
        compare_method:
          type:
            - string
            - 'null'
        left:
          type: string
        right:
          type: string
      required:
        - left
        - right
      type: object
    TabularCompareResourceBody:
      properties:
        path:
          type: string
        version:
          type: string
      required:
        - path
        - version
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
    CompareTabular:
      properties:
        display:
          items:
            $ref: '#/components/schemas/TabularCompareTargetBody'
          type:
            - array
            - 'null'
        dupes:
          $ref: '#/components/schemas/CompareDupes'
        keys:
          items:
            $ref: '#/components/schemas/TabularCompareFieldBody'
          type:
            - array
            - 'null'
        schema_diff:
          oneOf:
            - $ref: '#/components/schemas/CompareSchemaDiff'
            - type: 'null'
        source_schemas:
          $ref: '#/components/schemas/CompareSourceSchemas'
        summary:
          oneOf:
            - $ref: '#/components/schemas/CompareSummary'
            - type: 'null'
        targets:
          items:
            $ref: '#/components/schemas/TabularCompareTargetBody'
          type:
            - array
            - 'null'
      required:
        - dupes
        - source_schemas
      type: object
    OxenMessage:
      properties:
        description:
          type: string
        level:
          $ref: '#/components/schemas/MessageLevel'
        title:
          type: string
      required:
        - level
        - title
        - description
      type: object
    CompareDupes:
      properties:
        left:
          format: int64
          minimum: 0
          type: integer
        right:
          format: int64
          minimum: 0
          type: integer
      required:
        - left
        - right
      type: object
    CompareSchemaDiff:
      properties:
        added_cols:
          items:
            $ref: '#/components/schemas/CompareSchemaColumn'
          type: array
        removed_cols:
          items:
            $ref: '#/components/schemas/CompareSchemaColumn'
          type: array
      required:
        - added_cols
        - removed_cols
      type: object
    CompareSourceSchemas:
      properties:
        left:
          $ref: '#/components/schemas/Schema'
        right:
          $ref: '#/components/schemas/Schema'
      required:
        - left
        - right
      type: object
    CompareSummary:
      properties:
        modifications:
          $ref: '#/components/schemas/CompareTabularMods'
        schema:
          $ref: '#/components/schemas/Schema'
      required:
        - modifications
        - schema
      type: object
    MessageLevel:
      enum:
        - Info
        - Warning
        - Error
      type: string
    CompareSchemaColumn:
      properties:
        dtype:
          type: string
        key:
          type: string
        name:
          type: string
      required:
        - name
        - key
        - dtype
      type: object
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
    CompareTabularMods:
      properties:
        added_rows:
          minimum: 0
          type: integer
        modified_rows:
          minimum: 0
          type: integer
        removed_rows:
          minimum: 0
          type: integer
      required:
        - added_rows
        - removed_rows
        - modified_rows
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