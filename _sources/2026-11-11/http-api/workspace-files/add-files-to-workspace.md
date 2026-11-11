---
title: "Add files to workspace"
source: https://docs.oxen.ai/http-api/workspace-files/add-files-to-workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Add files to workspace

> Upload and stage files to a workspace. Accept a multipart with either gzipped or uncompressed file parts. Use the filename from the file part and compute the file hash from the content.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/files/{path}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/files/{path}:
    post:
      tags:
        - Workspace Files
      summary: Add files to workspace
      description: >-
        Upload and stage files to a workspace. Accept a multipart with either
        gzipped or uncompressed file parts. Use the filename from the file part
        and compute the file hash from the content.
      operationId: add
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
        - description: The UUID of the workspace
          example: 580c0587-c157-417b-9118-8686d63d2745
          in: path
          name: workspace_id
          required: true
          schema:
            type: string
        - description: The target path to upload the file to
          example: data/train
          in: path
          name: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/FileUpload'
        description: >-
          Multipart upload of file. Each file should be sent as a separate file
          part
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilePathsResponse'
          description: File successfully uploaded to workspace
        '400':
          description: Invalid upload request
        '404':
          description: Workspace not found
components:
  schemas:
    FileUpload:
      properties:
        file:
          format: binary
          type: string
      required:
        - file
      type: object
    FilePathsResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            paths:
              items:
                type: string
              type: array
          required:
            - paths
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
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.