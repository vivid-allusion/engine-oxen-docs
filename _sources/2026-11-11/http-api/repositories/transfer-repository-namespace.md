---
title: "Transfer repository namespace"
source: https://docs.oxen.ai/http-api/repositories/transfer-repository-namespace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Transfer repository namespace

> Transfer a repository to a different namespace.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json patch /api/repos/{namespace}/{repo_name}/transfer
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
  /api/repos/{namespace}/{repo_name}/transfer:
    patch:
      tags:
        - Repositories
      summary: Transfer repository namespace
      description: Transfer a repository to a different namespace.
      operationId: transfer_namespace
      parameters:
        - description: Current namespace of the repository
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
              namespace: new_org
            schema:
              $ref: '#/components/schemas/TransferNamespaceRequest'
        description: Target namespace to transfer the repository to.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RepositoryResponse'
          description: Repository transferred successfully
        '400':
          description: Invalid body or target namespace
        '404':
          description: Repository not found
components:
  schemas:
    TransferNamespaceRequest:
      description: The namespace a repository is being transferred into.
      properties:
        namespace:
          description: >-
            The destination namespace, as addressed on disk. A UUID where a
            control plane owns

            namespaces, and the namespace's name where the server owns its own.
          type: string
        namespace_name:
          description: >-
            What the destination namespace is called, where `namespace`
            addresses it by UUID instead.

            Recorded as the repository's namespace hint, and refused when it is
            not a valid namespace

            name. A server that owns its own namespaces takes the name from the
            `namespace` position and

            ignores this.
          type:
            - string
            - 'null'
      required:
        - namespace
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