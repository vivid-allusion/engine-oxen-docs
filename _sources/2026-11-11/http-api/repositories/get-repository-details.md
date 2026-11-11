---
title: "Get repository details"
source: https://docs.oxen.ai/http-api/repositories/get-repository-details
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get repository details

> Get repository details including size and data types from the main branch.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}
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
  /api/repos/{namespace}/{repo_name}:
    get:
      tags:
        - Repositories
      summary: Get repository details
      description: >-
        Get repository details including size and data types from the main
        branch.
      operationId: show
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: ImageNet-1k
          in: path
          name: repo_name
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RepositoryDataTypesResponse'
          description: Repository details
        '404':
          description: Repository not found
components:
  schemas:
    RepositoryDataTypesResponse:
      example:
        repository:
          data_types:
            - count: 1000
              data_type: image
            - count: 5
              data_type: tabular
          is_empty: false
          name: my-corn-pics
          namespace: bessie
          size: 1074288000
        status: success
        status_message: resource_found
      properties:
        repository:
          $ref: '#/components/schemas/RepositoryDataTypesView'
        status:
          type: string
        status_message:
          type: string
      required:
        - status
        - status_message
        - repository
      type: object
    RepositoryDataTypesView:
      allOf:
        - $ref: '#/components/schemas/RepositoryView'
        - properties:
            branch_count:
              minimum: 0
              type: integer
            data_types:
              items:
                $ref: '#/components/schemas/DataTypeCount'
              type: array
            default_resource:
              oneOf:
                - $ref: '#/components/schemas/ParsedResourceView'
                - type: 'null'
            size:
              format: int64
              minimum: 0
              type: integer
          required:
            - size
            - data_types
          type: object
      example:
        branch_count: 3
        data_types:
          - count: 1000
            data_type: image
          - count: 5
            data_type: tabular
        is_empty: false
        name: my-corn-pics
        namespace: bessie
        size: 1073741824
        storage_kind: s3
    RepositoryView:
      example:
        is_empty: false
        name: ImageNet-1k
        namespace: ox
        storage_kind: s3
      properties:
        is_empty:
          type: boolean
        min_version:
          type:
            - string
            - 'null'
        name:
          type: string
        namespace:
          type: string
        repo_uuid:
          description: >-
            The immutable UUID this repo's storage is addressed by. `None` for a
            repository whose

            identity backfill has not run.
          format: uuid
          type:
            - string
            - 'null'
        storage_kind:
          $ref: '#/components/schemas/StorageKind'
      required:
        - namespace
        - name
        - is_empty
        - storage_kind
      type: object
    DataTypeCount:
      properties:
        count:
          minimum: 0
          type: integer
        data_type:
          type: string
      required:
        - count
        - data_type
      type: object
    ParsedResourceView:
      description: External (view) model that is returned to the client with fewer fields.
      properties:
        branch:
          oneOf:
            - $ref: '#/components/schemas/Branch'
            - type: 'null'
        commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
        path:
          type: string
        resource:
          type: string
        version:
          type: string
        workspace:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceView'
            - type: 'null'
      required:
        - path
        - version
        - resource
      type: object
    StorageKind:
      description: >-
        Storage backend kind. Serializes as `"local"` / `"s3"` on the wire and
        on disk.
      enum:
        - local
        - s3
      type: string
    Branch:
      properties:
        commit_id:
          type: string
        name:
          type: string
      required:
        - name
        - commit_id
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
    WorkspaceView:
      description: >-
        Used to send workspace state across the wire. The `Workspace`'s other
        fields (like

        `LocalRepository`) would bloat the response and leak internal state.
      properties:
        commit:
          $ref: '#/components/schemas/Commit'
        created_at:
          description: >-
            `None` for a workspace created before the server recorded creation
            time.
          format: date-time
          type:
            - string
            - 'null'
        id:
          type: string
        name:
          type:
            - string
            - 'null'
      required:
        - id
        - commit
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.