---
title: "Create repository"
source: https://docs.oxen.ai/http-api/repositories/create-repository
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Create repository

> Create a new repository, optionally with initial files via JSON or multipart form.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos
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
  /api/repos:
    post:
      tags:
        - Repositories
      summary: Create repository
      description: >-
        Create a new repository, optionally with initial files via JSON or
        multipart form.
      operationId: create
      requestBody:
        content:
          application/json:
            example:
              description: A repository for image classification
              name: Cat-Dog-Classifier
              namespace: ox
              user:
                email: bessie@oxen.ai
                name: bessie
            schema:
              $ref: '#/components/schemas/RepoNew'
        description: Repository creation payload (JSON or Multipart)
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RepositoryCreationResponse'
          description: Repository created
        '400':
          description: Invalid payload
        '409':
          description: Repository already exists
components:
  schemas:
    RepoNew:
      description: >
        Only used between client and server for creating a new remote
        repository.
      properties:
        description:
          type:
            - string
            - 'null'
        files:
          items:
            $ref: '#/components/schemas/FileNew'
          type:
            - array
            - 'null'
        host:
          type:
            - string
            - 'null'
        is_public:
          type:
            - boolean
            - 'null'
        name:
          description: >-
            The name of the repository. When cloned locally, this is the name of
            the directory.

            This name uniquely identifies it in the namespace.
          type: string
        namespace:
          description: >-
            The namespace that the repository lives in: dictates
            application-level repository ownership.

            A namespace can be e.g. a user, a team, or an entire organization.
            Namespaces must be unique.
          type: string
        namespace_name:
          description: >-
            What the namespace is called, where `namespace` addresses it by UUID
            instead. Recorded as a

            hint beside the identity, ignored by a server that owns its own
            namespaces, and refused when

            it is not a valid namespace name.
          type:
            - string
            - 'null'
        repo_name:
          description: >-
            What the repository is called, where `name` addresses it by UUID
            instead. Recorded as a hint

            beside the identity, ignored by a server that owns its own
            namespaces, and refused when it

            is not a valid repository name.
          type:
            - string
            - 'null'
        repo_uuid:
          description: >-
            The immutable UUID to address the new repo's storage by. Supplied by
            an external control

            plane that owns repository identity; `None` leaves the choice to the
            server.
          format: uuid
          type:
            - string
            - 'null'
        root_commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
        scheme:
          type:
            - string
            - 'null'
        storage_kind:
          oneOf:
            - $ref: '#/components/schemas/StorageKind'
              description: >-
                Which storage backend the server should use for this repo (e.g.
                "local", "s3").
            - type: 'null'
      required:
        - namespace
        - name
      type: object
    RepositoryCreationResponse:
      example:
        repository:
          latest_commit:
            author: ox
            email: ox@example.com
            id: a1b2c3d4e5f678902e41
            message: Initial dataset import.
            parent_ids:
              - f1e2d3c4b5a67890fedc
            timestamp: '2025-01-01T10:00:00Z'
          name: ImageNet-1k
          namespace: ox
        status: success
        status_message: resource_created
      properties:
        repository:
          $ref: '#/components/schemas/RepositoryCreationView'
        status:
          type: string
        status_message:
          type: string
      required:
        - status
        - status_message
        - repository
      type: object
    FileNew:
      properties:
        contents:
          $ref: '#/components/schemas/FileContents'
        path:
          type: string
        user:
          $ref: '#/components/schemas/User'
      required:
        - path
        - contents
        - user
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
    StorageKind:
      description: >-
        Storage backend kind. Serializes as `"local"` / `"s3"` on the wire and
        on disk.
      enum:
        - local
        - s3
      type: string
    RepositoryCreationView:
      example:
        latest_commit:
          author: ox
          email: ox@example.com
          id: a1b2c3d4e5f67890abcdef1234567890
          message: Initial dataset import.
          parent_ids:
            - f1e2d3c4b5a67890fedcba9876543210
          timestamp: '2025-01-01T10:00:00Z'
        name: ImageNet-1k
        namespace: ox
        storage_kind: s3
      properties:
        latest_commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
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
        - storage_kind
      type: object
    FileContents:
      oneOf:
        - properties:
            Text:
              type: string
          required:
            - Text
          type: object
        - properties:
            Binary:
              items:
                format: int32
                minimum: 0
                type: integer
              type: array
          required:
            - Binary
          type: object
    User:
      properties:
        email:
          type: string
        name:
          type: string
      required:
        - email
        - name
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.