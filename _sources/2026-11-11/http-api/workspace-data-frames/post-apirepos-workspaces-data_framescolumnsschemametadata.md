---
title: "Post apirepos workspaces data framescolumnsschemametadata"
source: https://docs.oxen.ai/http-api/workspace-data-frames/post-apirepos-workspaces-data_framescolumnsschemametadata
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Post apirepos workspaces data framescolumnsschemametadata

> Set the metadata on a single column of a data frame, the HTTP equivalent of `oxen schemas add <path> -c <column> -m '{...}'`. Staged into the workspace, so no commit is required. Replaces that column's existing metadata wholesale.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/data_frames/columns/schema/metadata/{path}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/data_frames/columns/schema/metadata/{path}:
    post:
      tags:
        - Workspace Data Frames
      description: >-
        Set the metadata on a single column of a data frame, the HTTP equivalent
        of `oxen schemas add <path> -c <column> -m '{...}'`. Staged into the
        workspace, so no commit is required. Replaces that column's existing
        metadata wholesale.
      operationId: add_column_metadata
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
        - description: ID or name of the workspace
          example: b3f27f05-0955-4076-805f-39575853b27b
          in: path
          name: workspace_id
          required: true
          schema:
            type: string
        - description: Path to the data frame within the repository
          example: annotations/train.csv
          in: path
          name: path
          required: true
          schema:
            type: string
      requestBody:
        content:
          text/plain:
            example:
              column_name: file
              metadata:
                _oxen:
                  render:
                    func: image
            schema:
              type: string
        description: >-
          The column to annotate and the metadata to store on it.
          `_oxen.render.func` controls how oxen renders the column's values.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: Column metadata updated
        '400':
          description: >-
            Invalid request body, missing `column_name`, the path is not a
            tabular data frame, or the column does not exist in the schema
        '404':
          description: Repository, workspace, or data frame not found
        '409':
          description: The data frame is staged for removal in this workspace
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