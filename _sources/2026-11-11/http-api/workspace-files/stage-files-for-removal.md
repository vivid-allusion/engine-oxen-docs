---
title: "Stage files for removal"
source: https://docs.oxen.ai/http-api/workspace-files/stage-files-for-removal
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Stage files for removal

> Stage files for removal from the repository. Accepts both files and directories.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json delete /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/files
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/files:
    delete:
      tags:
        - Workspace Files
      summary: Stage files for removal
      description: >-
        Stage files for removal from the repository. Accepts both files and
        directories.
      operationId: rm_files
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
      requestBody:
        content:
          application/json:
            example:
              - images/train/dog_1.jpg
              - annotations/incorrect.xml
            schema:
              items:
                type: string
              type: array
        description: List of paths to stage for removal
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilePathsResponse'
          description: Files successfully removed
        '206':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FilePathsResponse'
          description: >-
            Some files could not be found/removed (returns paths of files not
            found)
        '404':
          description: Workspace not found
components:
  schemas:
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