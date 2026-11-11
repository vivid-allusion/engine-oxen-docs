---
title: "Merge branches"
source: https://docs.oxen.ai/http-api/merge/merge-branches
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Merge branches

> Merge the head branch into the base branch, creating a merge commit.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/merge/{base_head}
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
  /api/repos/{namespace}/{repo_name}/merge/{base_head}:
    post:
      tags:
        - Merge
      summary: Merge branches
      description: Merge the head branch into the base branch, creating a merge commit.
      operationId: merge
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
        - description: The base and head revisions separated by '..'
          example: main..feature/add-labels
          in: path
          name: base_head
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              email: bessie@oxen.ai
              name: bessie
            schema:
              properties:
                email:
                  type: string
                name:
                  type: string
              required:
                - email
                - name
              type: object
        description: >-
          Author for the merge commit (the user initiating the merge). Required:
          name and email must both be present and non-empty.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MergeSuccessResponse'
          description: Branches merged successfully
        '400':
          description: Missing merge author (name and email)
        '404':
          description: Repository or one of the revisions not found
        '409':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/StatusMessage'
          description: Merge conflict
components:
  schemas:
    MergeSuccessResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            commits:
              $ref: '#/components/schemas/MergeResult'
          required:
            - commits
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
    MergeResult:
      properties:
        base:
          $ref: '#/components/schemas/Commit'
        head:
          $ref: '#/components/schemas/Commit'
        merge:
          $ref: '#/components/schemas/Commit'
      required:
        - head
        - base
        - merge
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