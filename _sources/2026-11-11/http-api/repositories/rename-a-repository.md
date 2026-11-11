---
title: "Rename a repository"
source: https://docs.oxen.ai/http-api/repositories/rename-a-repository
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Rename a repository

> Record a new name for a repository whose directory does not carry its name. Only a server whose repository UUIDs are assigned by an auth provider accepts it.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json patch /api/repos/{namespace}/{repo_name}/rename
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
  /api/repos/{namespace}/{repo_name}/rename:
    patch:
      tags:
        - Repositories
      summary: Rename a repository
      description: >-
        Record a new name for a repository whose directory does not carry its
        name. Only a server whose repository UUIDs are assigned by an auth
        provider accepts it.
      operationId: rename
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: Cat-Dog-Classifier
          in: path
          name: repo_name
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            example:
              repo_name: Cat-Dog-Detector
            schema:
              $ref: '#/components/schemas/RenameRepoRequest'
        description: The repository's new name.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RepositoryResponse'
          description: Repository renamed
        '400':
          description: Invalid body or name, or a server whose directories carry names
        '404':
          description: Repository not found
        '409':
          description: Another repository in the namespace holds the name
components:
  schemas:
    RenameRepoRequest:
      description: The name a repository is being renamed to.
      properties:
        repo_name:
          description: >-
            What the repository is called from now on, recorded as its name
            hint. Refused when it is not

            a valid repository name.
          type: string
      required:
        - repo_name
      type: object
    RepositoryResponse:
      example:
        repository:
          is_empty: false
          name: ImageNet-1k
          namespace: ox
        status: success
        status_message: resource_found
      properties:
        repository:
          $ref: '#/components/schemas/RepositoryView'
        status:
          type: string
        status_message:
          type: string
      required:
        - status
        - status_message
        - repository
      type: object
    RepositoryView:
      example:
        is_empty: false
        name: ImageNet-1k
        namespace: ox
        storage_kind: s3
      properties:
        is_empty:
          type: boolean
        min_version:
          type:
            - string
            - 'null'
        name:
          type: string
        namespace:
          type: string
        repo_uuid:
          description: >-
            The immutable UUID this repo's storage is addressed by. `None` for a
            repository whose

            identity backfill has not run.
          format: uuid
          type:
            - string
            - 'null'
        storage_kind:
          $ref: '#/components/schemas/StorageKind'
      required:
        - namespace
        - name
        - is_empty
        - storage_kind
      type: object
    StorageKind:
      description: >-
        Storage backend kind. Serializes as `"local"` / `"s3"` on the wire and
        on disk.
      enum:
        - local
        - s3
      type: string
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.