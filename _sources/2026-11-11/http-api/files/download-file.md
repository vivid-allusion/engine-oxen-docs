---
title: "Download File"
source: https://docs.oxen.ai/http-api/files/download-file
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Download File

> Download a file from the repository. Supports image resizing and video thumbnail generation via query parameters.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/file/{resource}
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
    get:
      tags:
        - Files
      summary: Download File
      description: >-
        Download a file from the repository. Supports image resizing and video
        thumbnail generation via query parameters.
      operationId: get
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: Voice-Data
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: Path to the file (including branch/commit info)
          example: main/audio/moo.wav
          in: path
          name: resource
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
        - description: 'Timestamp in seconds to extract video thumbnail from (default: 1.0)'
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
          description: File content stream
        '404':
          description: File not found
components:
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.