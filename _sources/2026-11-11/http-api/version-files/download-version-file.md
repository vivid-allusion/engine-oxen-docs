---
title: "Download version file"
source: https://docs.oxen.ai/http-api/version-files/download-version-file
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Download version file

> Download a file by its resource path, with optional image resizing.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/versions/{resource}
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
  /api/repos/{namespace}/{repo_name}/versions/{resource}:
    get:
      tags:
        - Version Files
      summary: Download version file
      description: Download a file by its resource path, with optional image resizing.
      operationId: download
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
        - description: >-
            The resource identifier (e.g., 'main/path/to/file.ext' or a commit
            ID/branch name followed by the file path)
          example: main/images/dog_1.jpg
          in: path
          name: resource
          required: true
          schema:
            type: string
        - in: path
          name: width
          required: true
          schema:
            format: int32
            minimum: 0
            type:
              - integer
              - 'null'
        - in: path
          name: height
          required: true
          schema:
            format: int32
            minimum: 0
            type:
              - integer
              - 'null'
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
            File content returned as a stream. Content-Type matches the file's
            MIME type (e.g., image/jpeg), or the resized image's MIME type.
          headers:
            oxen-revision-id:
              description: The commit ID of the file version
              schema:
                type: string
        '404':
          description: Repository, commit, or file not found
components:
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.