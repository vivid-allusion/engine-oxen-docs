---
title: "List repositories"
source: https://docs.oxen.ai/http-api/repositories/list-repositories
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List repositories

> List all repositories in a namespace.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}
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
  /api/repos/{namespace}:
    get:
      tags:
        - Repositories
      summary: List repositories
      description: List all repositories in a namespace.
      operationId: index
      parameters:
        - description: Namespace to list repositories from
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListRepositoryResponse'
          description: List of repositories
        '400':
          description: Namespace is not a single path segment
        '404':
          description: Namespace not found
components:
  schemas:
    ListRepositoryResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            repositories:
              example:
                - name: data-fields
                  namespace: ox
                - name: my-corn-pics
                  namespace: bessie
              items:
                $ref: '#/components/schemas/RepositoryListView'
              type: array
          required:
            - repositories
          type: object
      example:
        repositories:
          - name: data-fields
            namespace: ox
          - name: my-corn-pics
            namespace: bessie
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
    RepositoryListView:
      example:
        name: my-farm-data
        namespace: bessie
      properties:
        min_version:
          type:
            - string
            - 'null'
        name:
          type: string
        namespace:
          type: string
      required:
        - namespace
        - name
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.