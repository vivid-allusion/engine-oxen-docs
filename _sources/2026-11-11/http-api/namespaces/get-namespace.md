---
title: "Get namespace"
source: https://docs.oxen.ai/http-api/namespaces/get-namespace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get namespace

> Get details of a specific namespace by name.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/namespaces/{namespace}
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
  /api/namespaces/{namespace}:
    get:
      tags:
        - Namespaces
      summary: Get namespace
      description: Get details of a specific namespace by name.
      operationId: show
      parameters:
        - description: Name of the namespace
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: >-
            The namespace's directory in the legacy layout, when it is not named
            for the namespace.
          in: path
          name: legacy_directory
          required: true
          schema:
            type:
              - string
              - 'null'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/NamespaceResponse'
          description: Namespace details
        '400':
          description: >-
            Missing namespace parameter, or a `legacy_directory` that is not a
            single path segment
        '404':
          description: Namespace not found
components:
  schemas:
    NamespaceResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            namespace:
              $ref: '#/components/schemas/Namespace'
          required:
            - namespace
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
    Namespace:
      properties:
        name:
          type: string
        storage_usage_gb:
          format: double
          type: number
      required:
        - name
        - storage_usage_gb
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.