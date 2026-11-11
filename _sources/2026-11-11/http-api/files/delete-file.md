---
title: "Delete file"
source: https://docs.oxen.ai/http-api/files/delete-file
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete file

> Remove a file from the repository. Stage the file as removed to a workspace and commit the removal. Can remove files or directories.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json delete /api/repos/{namespace}/{repo_name}/file/{resource}
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
  /api/repos/{namespace}/{repo_name}/file/{resource}:
    delete:
      tags:
        - Files
      summary: Delete file
      description: >-
        Remove a file from the repository. Stage the file as removed to a
        workspace and commit the removal. Can remove files or directories.
      operationId: delete
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
        - description: Path to the file to be deleted (including branch)
          example: main/train/images/n01440764_10026.JPEG
          in: path
          name: resource
          required: true
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FileUploadBody'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommitResponse'
          description: File removed successfully
        '404':
          description: Branch or path not found
components:
  schemas:
    FileUploadBody:
      description: >-
        Multipart form for uploading files. Use `file` for a single full-path
        upload, or `files[]` for uploading one or more files into a directory.
      example:
        email: bessie@oxen.ai
        files[]:
          - <binary data>
        message: Adding a picture of a cow
        name: bessie
      properties:
        email:
          example: bessie@oxen.ai
          type:
            - string
            - 'null'
        file:
          deprecated: true
          description: 'Deprecated: use `files[]` instead.'
          format: binary
          type:
            - string
            - 'null'
        files:
          items:
            format: binary
            type: string
          type: array
        message:
          example: Adding a new image to the training set
          type:
            - string
            - 'null'
        name:
          example: bessie
          type:
            - string
            - 'null'
      required:
        - files
      title: FileUploadBody
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