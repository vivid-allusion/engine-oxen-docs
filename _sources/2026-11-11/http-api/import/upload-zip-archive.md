---
title: "Upload zip archive"
source: https://docs.oxen.ai/http-api/import/upload-zip-archive
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload zip archive

> Upload and decompress a zip archive into the repository and commit the contents.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/import/upload/{resource}
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
  /api/repos/{namespace}/{repo_name}/import/upload/{resource}:
    post:
      tags:
        - Import
      summary: Upload zip archive
      description: >-
        Upload and decompress a zip archive into the repository and commit the
        contents.
      operationId: upload_zip
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: Wiki-Text
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: Destination path (including branch)
          example: main/archive
          in: path
          name: resource
          required: true
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/ZipUploadBody'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommitResponse'
          description: Zip archive decompressed and committed
        '400':
          description: Bad Request
components:
  schemas:
    ZipUploadBody:
      description: Body for uploading a zip archive via multipart/form-data
      example:
        commit_message: Importing full archive of grazing data
        email: ox@oxen.ai
        file: <binary zip data>
        name: ox
      properties:
        commit_message:
          example: Importing dataset archive
          type:
            - string
            - 'null'
        email:
          example: ox@oxen.ai
          type:
            - string
            - 'null'
        file:
          format: binary
          type: string
        name:
          example: ox
          type:
            - string
            - 'null'
      required:
        - file
      title: ZipUploadBody
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