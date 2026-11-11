---
title: "List all commits"
source: https://docs.oxen.ai/http-api/commits/list-all-commits
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List all commits

> List all commits in a repository



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/commits/all
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
  /api/repos/{namespace}/{repo_name}/commits/all:
    get:
      tags:
        - Commits
      summary: List all commits
      description: List all commits in a repository
      operationId: list_all
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
        - in: path
          name: page
          required: true
          schema:
            minimum: 0
            type:
              - integer
              - 'null'
        - in: path
          name: page_size
          required: true
          schema:
            minimum: 0
            type:
              - integer
              - 'null'
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/PaginatedCommits'
          description: Paginated list of all commits
        '404':
          description: Repository not found
components:
  schemas:
    PaginatedCommits:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - $ref: '#/components/schemas/Pagination'
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
        page_number: 1
        page_size: 10
        status: success
        status_message: resource_found
        total_entries: 45
        total_pages: 5
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
    Pagination:
      properties:
        page_number:
          minimum: 0
          type: integer
        page_size:
          minimum: 0
          type: integer
        total_entries:
          minimum: 0
          type: integer
        total_pages:
          minimum: 0
          type: integer
      required:
        - page_size
        - page_number
        - total_pages
        - total_entries
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