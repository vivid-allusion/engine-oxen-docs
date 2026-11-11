---
title: "Upload data chunk"
source: https://docs.oxen.ai/http-api/commits/upload-data-chunk
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload data chunk

> Upload one chunk of a gzipped archive of commit history, unpacked once every chunk has arrived and the whole payload matches its hash.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/commits/upload_chunk
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
  /api/repos/{namespace}/{repo_name}/commits/upload_chunk:
    post:
      tags:
        - Commits
      summary: Upload data chunk
      description: >-
        Upload one chunk of a gzipped archive of commit history, unpacked once
        every chunk has arrived and the whole payload matches its hash.
      operationId: upload_chunk
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
        - example: a2c3d4e5f67890b1c2d3e4f5a6b7c8d9
          in: path
          name: hash
          required: true
          schema:
            type: string
        - example: 1
          in: path
          name: chunk_num
          required: true
          schema:
            minimum: 0
            type: integer
        - example: 10
          in: path
          name: total_chunks
          required: true
          schema:
            minimum: 0
            type: integer
        - example: 100000000
          in: path
          name: total_size
          required: true
          schema:
            minimum: 0
            type: integer
      requestBody:
        content:
          application/octet-stream:
            schema:
              items:
                format: int32
                minimum: 0
                type: integer
              type: array
        description: Chunk of data (binary bytes)
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: Chunk uploaded successfully
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