---
title: "Create data frame from directory"
source: https://docs.oxen.ai/http-api/data-frames/create-data-frame-from-directory
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create data frame from directory

> Create a data frame by scanning directory contents and commit it to a branch.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/data_frames/from_directory/{resource}
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
  /api/repos/{namespace}/{repo_name}/data_frames/from_directory/{resource}:
    post:
      tags:
        - Data Frames
      summary: Create data frame from directory
      description: >-
        Create a data frame by scanning directory contents and commit it to a
        branch.
      operationId: from_directory
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: CattleData
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: Directory path to read from (including branch/commit info)
          example: main/data/images
          in: path
          name: resource
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              commit_message: Generated image index
              extra_columns:
                - size
                - extension
              output_path: data/image_index.csv
              recursive: true
              user_email: bessie@oxen.ai
              user_name: Bessie
            schema:
              $ref: '#/components/schemas/FromDirectoryRequest'
        description: >-
          Options for creating a data frame from a directory, including output
          path, columns, and commit message.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommitResponse'
          description: Data frame created and committed
        '400':
          description: Invalid request body or resource path
        '404':
          description: Repository or resource not found
components:
  schemas:
    FromDirectoryRequest:
      properties:
        commit_message:
          type:
            - string
            - 'null'
        extra_columns:
          items:
            $ref: '#/components/schemas/NewColumn'
          type:
            - array
            - 'null'
        output_path:
          type:
            - string
            - 'null'
        recursive:
          type:
            - boolean
            - 'null'
        user_email:
          type:
            - string
            - 'null'
        user_name:
          type:
            - string
            - 'null'
      type: object
    CommitResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            commit:
              $ref: '#/components/schemas/Commit'
          required:
            - commit
          type: object
      example:
        commit:
          author: ox
          email: ox@example.com
          id: a1b2c3d4e5f67890abcdef1234567890
          message: Refactor data loading pipeline.
          parent_ids:
            - f1e2d3c4b5a67890fedcba9876543210
          timestamp: '2025-01-01T10:00:00Z'
        status: success
        status_message: resource_found
    NewColumn:
      properties:
        data_type:
          type: string
        name:
          type: string
      required:
        - name
        - data_type
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
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.