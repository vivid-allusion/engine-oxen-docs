---
title: "Unstage a file from the workspace"
source: https://docs.oxen.ai/http-api/workspace-files/unstage-a-file-from-the-workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Unstage a file from the workspace

> Unstage a file from workspace staging



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json delete /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/changes/{path}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/changes/{path}:
    delete:
      tags:
        - Workspace Files
      summary: Unstage a file from the workspace
      description: Unstage a file from workspace staging
      operationId: unstage
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
        - description: The path to the file to delete (unstage)
          example: images/train/dog_1.jpg
          in: path
          name: path
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: File marked for deletion
        '404':
          description: Workspace or File not found
components:
  schemas:
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