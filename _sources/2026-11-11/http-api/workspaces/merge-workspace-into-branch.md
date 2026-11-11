---
title: "Merge workspace into branch"
source: https://docs.oxen.ai/http-api/workspaces/merge-workspace-into-branch
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Merge workspace into branch

> Commit and merge workspace into the specified branch



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/merge/{branch}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/merge/{branch}:
    post:
      tags:
        - Workspaces
      summary: Merge workspace into branch
      description: Commit and merge workspace into the specified branch
      operationId: commit
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
        - description: ID of the workspace
          example: b3f27f05-0955-4076-805f-39575853b27b
          in: path
          name: workspace_id
          required: true
          schema:
            type: string
        - description: Target branch name to commit to
          example: main
          in: path
          name: branch
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              author: bessie
              email: bessie@oxen.ai
              message: Commit changes from bessie_workspace
            schema:
              $ref: '#/components/schemas/NewCommitBody'
        description: Commit details for the workspace merge.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CommitResponse'
          description: Workspace committed successfully
        '400':
          description: Invalid request body
        '404':
          description: Workspace or branch not found
        '409':
          description: >-
            Conflict — a staged file also changed on the target branch since the
            workspace's base commit
        '422':
          description: Unprocessable Entity — the commit failed for another reason
        '429':
          description: >-
            Too Many Requests: another commit already holds this commit's id, or
            another write moved the branch while this commit was being written,
            so retry after the Retry-After delay
components:
  schemas:
    NewCommitBody:
      description: NewCommitBody is used to parse the json into a Commit from the API
      properties:
        author:
          type: string
        email:
          type: string
        message:
          type: string
      required:
        - message
        - author
        - email
      type: object
    CommitResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            commit:
              $ref: '#/components/schemas/Commit'
          required:
            - commit
          type: object
      example:
        commit:
          author: ox
          email: ox@example.com
          id: a1b2c3d4e5f67890abcdef1234567890
          message: Refactor data loading pipeline.
          parent_ids:
            - f1e2d3c4b5a67890fedcba9876543210
          timestamp: '2025-01-01T10:00:00Z'
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
    Commit:
      example:
        author: ox
        email: ox@example.com
        id: a1b2c3d4e5f67890abcdef1234567890
        message: Refactor data loading pipeline.
        parent_ids:
          - f1e2d3c4b5a67890fedcba9876543210
        timestamp: '2025-01-01T10:00:00Z'
      properties:
        author:
          type: string
        email:
          type: string
        id:
          type: string
        message:
          type: string
        parent_ids:
          items:
            type: string
          type: array
        timestamp:
          format: date-time
          type: string
      required:
        - id
        - parent_ids
        - message
        - author
        - email
        - timestamp
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.