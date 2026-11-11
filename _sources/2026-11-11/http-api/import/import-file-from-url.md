---
title: "Import file from URL"
source: https://docs.oxen.ai/http-api/import/import-file-from-url
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Import file from URL

> Import a file from a remote URL and commit it to the repository.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/import/{resource}
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
  /api/repos/{namespace}/{repo_name}/import/{resource}:
    post:
      tags:
        - Import
      summary: Import file from URL
      description: Import a file from a remote URL and commit it to the repository.
      operationId: import
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: Common-Crawl
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: Destination path (including branch)
          example: main/data
          in: path
          name: resource
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              auth: Bearer <token>
              download_url: https://example.com/datasets/data.csv
              email: ox@oxen.ai
              name: ox
            schema:
              $ref: '#/components/schemas/ImportFileBody'
        description: Import configuration
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommitResponse'
          description: File imported and committed
        '400':
          description: Bad Request / Invalid URL
components:
  schemas:
    ImportFileBody:
      description: Body for importing a file from a URL
      example:
        auth: Bearer <token>
        download_url: https://example.com/datasets/data.csv
        email: ox@oxen.ai
        filename: data.csv
        message: Import dataset
        name: ox
      properties:
        auth:
          example: Bearer <token>
          type:
            - string
            - 'null'
        download_url:
          example: https://example.com/datasets/data.csv
          type: string
        email:
          example: ox@oxen.ai
          type:
            - string
            - 'null'
        filename:
          example: data.csv
          type:
            - string
            - 'null'
        message:
          example: Import dataset
          type:
            - string
            - 'null'
        name:
          example: ox
          type:
            - string
            - 'null'
      required:
        - download_url
      title: ImportFileBody
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