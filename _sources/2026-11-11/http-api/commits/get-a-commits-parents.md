---
title: "Get a commit's parents"
source: https://docs.oxen.ai/http-api/commits/get-a-commits-parents
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get a commit's parents

> Get the parent commits of a specific commit or the tip of a branch.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/commits/{commit_or_branch}/parents
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
  /api/repos/{namespace}/{repo_name}/commits/{commit_or_branch}/parents:
    get:
      tags:
        - Commits
      summary: Get a commit's parents
      description: Get the parent commits of a specific commit or the tip of a branch.
      operationId: parents
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
        - description: Commit ID or Branch name
          example: main
          in: path
          name: commit_or_branch
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListCommitResponse'
          description: List of parent commits
        '404':
          description: Commit or Branch not found
components:
  schemas:
    ListCommitResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            commits:
              items:
                $ref: '#/components/schemas/Commit'
              type: array
          required:
            - commits
          type: object
      example:
        commits:
          - author: ox
            email: ox@example.com
            id: a1b2c3d4e5f67890abcdef1234567890
            message: Refactor data loading pipeline.
            parent_ids:
              - f1e2d3c4b5a67890fedcba9876543210
            timestamp: '2025-01-01T10:00:00Z'
          - author: bessie
            email: bessie@example.com
            id: b0a9f8e7d6c543210fedcba987654321
            message: Update ImageNet-1k labels.
            parent_ids:
              - a1b2c3d4e5f67890abcdef1234567890
            timestamp: '2025-01-02T11:00:00Z'
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