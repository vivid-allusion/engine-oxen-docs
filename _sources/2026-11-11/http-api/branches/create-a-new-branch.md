---
title: "Create a new branch"
source: https://docs.oxen.ai/http-api/branches/create-a-new-branch
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a new branch

> Create a new branch from another branch name or commit ID. Returns existing branch if name already exists.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/branches
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
  /api/repos/{namespace}/{repo_name}/branches:
    post:
      tags:
        - Branches
      summary: Create a new branch
      description: >-
        Create a new branch from another branch name or commit ID. Returns
        existing branch if name already exists.
      operationId: create
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
      requestBody:
        content:
          application/json:
            example:
              from_name: main
              new_name: development
            schema:
              $ref: '#/components/schemas/BranchNewFromBranchName'
        description: >-
          Branch creation details. Can be created from another branch or a
          commit ID.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BranchResponse'
          description: Branch created
        '400':
          description: Invalid request body
        '404':
          description: Repository or source branch/commit not found
components:
  schemas:
    BranchNewFromBranchName:
      properties:
        from_name:
          type: string
        new_name:
          type: string
      required:
        - new_name
        - from_name
      type: object
    BranchResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            branch:
              $ref: '#/components/schemas/Branch'
          required:
            - branch
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
    Branch:
      properties:
        commit_id:
          type: string
        name:
          type: string
      required:
        - name
        - commit_id
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.