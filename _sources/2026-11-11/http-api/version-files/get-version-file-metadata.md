---
title: "Get version file metadata"
source: https://docs.oxen.ai/http-api/version-files/get-version-file-metadata
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get version file metadata

> Get metadata for a specific file version by its hash.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/versions/{version_id}/metadata
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
  /api/repos/{namespace}/{repo_name}/versions/{version_id}/metadata:
    get:
      tags:
        - Version Files
      summary: Get version file metadata
      description: Get metadata for a specific file version by its hash.
      operationId: metadata
      parameters:
        - description: The namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: The name of the repository
          example: ImageNet-1k
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: The hash ID of the file version
          example: 1eb45ac94f3eab120f3a
          in: path
          name: version_id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VersionFileResponse'
          description: File metadata found
        '404':
          description: Version file not found
components:
  schemas:
    VersionFileResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            version:
              $ref: '#/components/schemas/VersionFile'
          required:
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
    VersionFile:
      properties:
        hash:
          type: string
        size:
          format: int64
          minimum: 0
          type: integer
      required:
        - hash
        - size
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.