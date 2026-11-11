---
title: "Get repository size"
source: https://docs.oxen.ai/http-api/repositories/get-repository-size
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get repository size

> Get the cached size of the repository in bytes.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/size
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
  /api/repos/{namespace}/{repo_name}/size:
    get:
      tags:
        - Repositories
      summary: Get repository size
      description: Get the cached size of the repository in bytes.
      operationId: get_size
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
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RepoSizeFile'
          description: Repository size in bytes
        '404':
          description: Repository not found
components:
  schemas:
    RepoSizeFile:
      description: >-
        A repository's size in bytes together with the state of the calculation
        behind it. The figure is

        the last one a pass completed, or zero when none has.
      properties:
        size:
          format: int64
          minimum: 0
          type: integer
        status:
          $ref: '#/components/schemas/SizeStatus'
      required:
        - status
        - size
      type: object
    SizeStatus:
      enum:
        - pending
        - done
        - error
      type: string
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.