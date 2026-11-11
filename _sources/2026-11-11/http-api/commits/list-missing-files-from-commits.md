---
title: "List missing files from commits"
source: https://docs.oxen.ai/http-api/commits/list-missing-files-from-commits
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List missing files from commits

> List files that are referenced in a commit but not present on the server. Accept a commit range.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/commits/missing_files
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
  /api/repos/{namespace}/{repo_name}/commits/missing_files:
    get:
      tags:
        - Commits
      summary: List missing files from commits
      description: >-
        List files that are referenced in a commit but not present on the
        server. Accept a commit range.
      operationId: list_missing_files
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
        - example: abc1234567890def1234567890fedcba
          in: path
          name: base
          required: true
          schema:
            type:
              - string
              - 'null'
        - example: 84c76a5b2e9a2637f9091991475c404d
          in: path
          name: head
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ListCommitEntryResponse'
          description: List of missing file entries
        '404':
          description: Repository or commit not found
components:
  schemas:
    ListCommitEntryResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            entries:
              items:
                $ref: '#/components/schemas/CommitEntry'
              type: array
          required:
            - entries
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
    CommitEntry:
      description: >-
        Represents a file or directory entry at a specific commit.


        `Hash` and `Eq` are based on the content hash field, so
        `HashSet<CommitEntry>`

        deduplicates by file content. This is used during fetch and push to
        avoid

        transferring the same content twice.
      properties:
        commit_id:
          type: string
        hash:
          type: string
        last_modified_nanoseconds:
          format: int32
          minimum: 0
          type: integer
        last_modified_seconds:
          format: int64
          type: integer
        num_bytes:
          format: int64
          minimum: 0
          type: integer
        path:
          type: string
      required:
        - commit_id
        - path
        - hash
        - num_bytes
        - last_modified_seconds
        - last_modified_nanoseconds
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.