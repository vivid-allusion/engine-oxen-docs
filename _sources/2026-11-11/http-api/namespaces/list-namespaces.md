---
title: "List namespaces"
source: https://docs.oxen.ai/http-api/namespaces/list-namespaces
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List namespaces

> List all namespaces on the server.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/namespaces
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
  /api/namespaces:
    get:
      tags:
        - Namespaces
      summary: List namespaces
      description: List all namespaces on the server.
      operationId: index
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListNamespacesResponse'
          description: List of namespaces
components:
  schemas:
    ListNamespacesResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            namespaces:
              items:
                $ref: '#/components/schemas/NamespaceView'
              type: array
          required:
            - namespaces
          type: object
      example:
        namespaces:
          - name: my_namespace
          - name: oxen
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
    NamespaceView:
      properties:
        namespace:
          type: string
      required:
        - namespace
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.