---
title: "Delete DF Diff"
source: https://docs.oxen.ai/http-api/data-frames/delete-df-diff
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Delete DF Diff

> Delete a cached tabular diff comparison by its ID.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json delete /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}
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
  /api/repos/{namespace}/{repo_name}/compare/data_frames/{compare_id}:
    delete:
      tags:
        - Data Frames
      summary: Delete DF Diff
      description: Delete a cached tabular diff comparison by its ID.
      operationId: delete_df_diff
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: compare-datasets
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: The unique ID of the comparison session to delete
          example: uuid-1234
          in: path
          name: compare_id
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: Data frame diff deleted successfully
        '404':
          description: Repository or comparison ID not found
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