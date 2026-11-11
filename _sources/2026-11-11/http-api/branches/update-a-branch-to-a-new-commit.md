---
title: "Update a branch to a new commit"
source: https://docs.oxen.ai/http-api/branches/update-a-branch-to-a-new-commit
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Update a branch to a new commit

> Update a branch to point to a different commit ID.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json put /api/repos/{namespace}/{repo_name}/branches/{branch_name}
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
  /api/repos/{namespace}/{repo_name}/branches/{branch_name}:
    put:
      tags:
        - Branches
      summary: Update a branch to a new commit
      description: Update a branch to point to a different commit ID.
      operationId: update
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
        - description: Name of the branch to update
          example: main
          in: path
          name: branch_name
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              commit_id: 84c76a5b2e9a2637f9091991475c404d
            schema:
              $ref: '#/components/schemas/BranchUpdate'
        description: The commit ID to update the branch head to.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/BranchResponse'
          description: Branch updated
        '400':
          description: Bad Request
        '404':
          description: Branch or Commit not found
components:
  schemas:
    BranchUpdate:
      properties:
        commit_id:
          type: string
      required:
        - commit_id
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