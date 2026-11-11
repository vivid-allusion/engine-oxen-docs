---
title: "List all branches"
source: https://docs.oxen.ai/http-api/branches/list-all-branches
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all branches

> List all branches in the repository with their current commit information.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/branches
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
    get:
      tags:
        - Branches
      summary: List all branches
      description: >-
        List all branches in the repository with their current commit
        information.
      operationId: index
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
              example:
                branches:
                  - commit:
                      author: Bessie Oxington
                      email: hello@oxen.ai
                      id: 592d564750031fa1431000472c2d721d
                      message: update README
                      timestamp: '2024-11-25T21:11:12Z'
                    commit_id: 592d564750031fa1431000472c2d721d
                    name: main
                  - commit:
                      author: Daisy Oxington
                      email: daisy@oxen.ai
                      id: abc1234567890def1234567890fedcba
                      message: added new validation data
                      timestamp: '2024-11-25T20:00:00Z'
                    commit_id: abc1234567890def1234567890fedcba
                    name: development
                oxen_version: 0.22.2
                status: success
                status_message: resource_found
              schema:
                $ref: '#/components/schemas/ListBranchesResponse'
          description: List of branches
        '404':
          description: Repository not found
components:
  schemas:
    ListBranchesResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            branches:
              items:
                $ref: '#/components/schemas/Branch'
              type: array
          required:
            - branches
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