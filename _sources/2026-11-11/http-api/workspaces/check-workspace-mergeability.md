---
title: "Check workspace mergeability"
source: https://docs.oxen.ai/http-api/workspaces/check-workspace-mergeability
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Check workspace mergeability

> Checks if a workspace can be committed and merged onto a branch



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/merge/{branch}
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
    get:
      tags:
        - Workspaces
      summary: Check workspace mergeability
      description: Checks if a workspace can be committed and merged onto a branch
      operationId: mergeability
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
        - description: Target branch name to merge into
          example: main
          in: path
          name: branch
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MergeableResponse'
          description: Mergeability status found
        '404':
          description: Workspace or target branch not found
components:
  schemas:
    MergeableResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - $ref: '#/components/schemas/Mergeable'
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
    Mergeable:
      properties:
        commits:
          items:
            $ref: '#/components/schemas/Commit'
          type: array
        conflicts:
          items:
            $ref: '#/components/schemas/MergeConflictFile'
          type: array
        is_mergeable:
          type: boolean
      required:
        - is_mergeable
        - conflicts
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
    MergeConflictFile:
      properties:
        path:
          type: string
      required:
        - path
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.