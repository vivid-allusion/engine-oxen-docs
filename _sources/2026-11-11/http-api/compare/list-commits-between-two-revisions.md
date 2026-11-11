---
title: "List commits between two revisions"
source: https://docs.oxen.ai/http-api/compare/list-commits-between-two-revisions
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List commits between two revisions

> List commits between a 'base' and 'head' commit. Two dots list what head added; three dots list the commits on either side but not both, each tagged with the side it came from.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/compare/{base_head}/commits
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
  /api/repos/{namespace}/{repo_name}/compare/{base_head}/commits:
    get:
      tags:
        - Compare
        - Commits
      summary: List commits between two revisions
      description: >-
        List commits between a 'base' and 'head' commit. Two dots list what head
        added; three dots list the commits on either side but not both, each
        tagged with the side it came from.
      operationId: commits
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: satellite-images
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: >-
            The base and head revisions separated by '..', or '...' for the
            commits on either side but not both
          example: main...feature/add-labels
          in: path
          name: base_head
          required: true
          schema:
            type: string
        - description: Page number for pagination (starts at 1)
          in: query
          name: page
          required: false
          schema:
            minimum: 0
            type: integer
        - description: Page size for pagination
          in: query
          name: page_size
          required: false
          schema:
            minimum: 0
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/CompareCommitsResponse'
          description: Commits found successfully
        '404':
          description: Repository or one of the revisions not found
components:
  schemas:
    CompareCommitsResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - $ref: '#/components/schemas/Pagination'
        - properties:
            compare:
              $ref: '#/components/schemas/CompareCommits'
          required:
            - compare
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
    CompareCommits:
      properties:
        base_commit:
          $ref: '#/components/schemas/Commit'
        commits:
          items:
            $ref: '#/components/schemas/CompareCommit'
          type: array
        head_commit:
          $ref: '#/components/schemas/Commit'
      required:
        - base_commit
        - head_commit
        - commits
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
    CompareCommit:
      allOf:
        - $ref: '#/components/schemas/Commit'
        - properties:
            side:
              $ref: '#/components/schemas/CommitSide'
          required:
            - side
          type: object
      description: >-
        A commit in a comparison, tagged with the side it came from. Every
        commit of a two-dot

        comparison is on the head side; a three-dot comparison reports commits
        from both.
    CommitSide:
      description: >-
        Which side of a comparison a commit came from, mirroring the markers
        git's

        `log --left-right base...head` prints.
      enum:
        - base
        - head
      type: string
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.