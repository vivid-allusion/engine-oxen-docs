---
title: "Get repository stats"
source: https://docs.oxen.ai/http-api/repositories/get-repository-stats
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get repository stats

> Get the total number of files, the total size of the files, and the number of different file types.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/stats
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
  /api/repos/{namespace}/{repo_name}/stats:
    get:
      tags:
        - Repositories
      summary: Get repository stats
      description: >-
        Get the total number of files, the total size of the files, and the
        number of different file types.
      operationId: stats
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
                $ref: '#/components/schemas/RepositoryStatsResponse'
          description: Repository statistics
        '404':
          description: Repository not found
components:
  schemas:
    RepositoryStatsResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            repository:
              $ref: '#/components/schemas/RepositoryStatsView'
          required:
            - repository
          type: object
      example:
        repository:
          data_size: 1074288000
          data_types:
            - data_size: 524288000
              data_type: image
              file_count: 500
            - data_size: 550000000
              data_type: tabular
              file_count: 5
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
    RepositoryStatsView:
      example:
        data_size: 1074288000
        data_types:
          - data_size: 524288000
            data_type: image
            file_count: 500
          - data_size: 550000000
            data_type: tabular
            file_count: 5
      properties:
        data_size:
          format: int64
          minimum: 0
          type: integer
        data_types:
          items:
            $ref: '#/components/schemas/DataTypeView'
          type: array
      required:
        - data_size
        - data_types
      type: object
    DataTypeView:
      example:
        data_size: 524288000
        data_type: image
        file_count: 500
      properties:
        data_size:
          format: int64
          minimum: 0
          type: integer
        data_type:
          $ref: '#/components/schemas/EntryDataType'
        file_count:
          minimum: 0
          type: integer
      required:
        - data_type
        - data_size
        - file_count
      type: object
    EntryDataType:
      enum:
        - dir
        - text
        - image
        - video
        - audio
        - tabular
        - binary
      type: string
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.