---
title: "Copy a committed file to a new path within the workspace"
source: https://docs.oxen.ai/http-api/workspace-files/copy-a-committed-file-to-a-new-path-within-the-workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Copy a committed file to a new path within the workspace

> Stage a copy of a file from the workspace's base commit at a new path. The copy shares the committed file's content, so nothing is uploaded. A copy with a different extension gets the type and metadata an upload of the same bytes to the new path would.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/copy/{path}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/copy/{path}:
    post:
      tags:
        - Workspace Files
      summary: Copy a committed file to a new path within the workspace
      description: >-
        Stage a copy of a file from the workspace's base commit at a new path.
        The copy shares the committed file's content, so nothing is uploaded. A
        copy with a different extension gets the type and metadata an upload of
        the same bytes to the new path would.
      operationId: copy
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
        - description: The path of the committed file to copy
          example: annotations/train.csv
          in: path
          name: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              new_path: annotations/train_results.csv
            schema:
              $ref: '#/components/schemas/RenameRequest'
        description: The path for the copy
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: Copy staged
        '400':
          description: Invalid request (empty new_path, or the path is a directory)
        '404':
          description: Workspace or file not found
        '409':
          description: >-
            new_path already exists or is staged, a file is at a parent of
            new_path, or the source has changes staged in the workspace
components:
  schemas:
    RenameRequest:
      properties:
        new_path:
          example: path/to/new_file.txt
          type: string
      required:
        - new_path
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