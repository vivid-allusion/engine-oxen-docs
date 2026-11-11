---
title: "Get file from workspace"
source: https://docs.oxen.ai/http-api/workspace-files/get-file-from-workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get file from workspace

> Get a file from a workspace.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/files/{path}
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
    get:
      tags:
        - Workspace Files
      summary: Get file from workspace
      description: Get a file from a workspace.
      operationId: get
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
        - description: The path to the file in the workspace
          example: images/train/dog_1.jpg
          in: path
          name: path
          required: true
          schema:
            type: string
        - description: Width for image resize or video thumbnail
          example: 320
          in: query
          name: width
          required: false
          schema:
            format: int32
            minimum: 0
            type: integer
        - description: Height for image resize or video thumbnail
          example: 240
          in: query
          name: height
          required: false
          schema:
            format: int32
            minimum: 0
            type: integer
        - description: Timestamp in seconds to extract video thumbnail from
          example: 1
          in: query
          name: timestamp
          required: false
          schema:
            format: double
            type: number
        - description: >-
            Set to true to generate a video thumbnail instead of returning the
            full video
          example: true
          in: query
          name: thumbnail
          required: false
          schema:
            type: boolean
      responses:
        '200':
          content:
            application/octet-stream:
              schema:
                items:
                  format: int32
                  minimum: 0
                  type: integer
                type: array
          description: >-
            File content returned as a stream. Content-Type varies: matches the
            file's MIME type for regular files and image resizes, or
            'image/jpeg' for video thumbnails
          headers:
            oxen-revision-id:
              description: The commit ID of the file version
              schema:
                type: string
        '400':
          description: Invalid parameters
        '404':
          description: Workspace or File not found
components:
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.