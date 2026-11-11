---
title: "Begin a version file upload"
source: https://docs.oxen.ai/http-api/version-files/begin-a-version-file-upload
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Begin a version file upload

> Begin uploading a large file in parts. A file may be at most 1 TiB, a provisional limit. The response's `file` is `awaiting_parts`, with the upload id, the size of every part but the last, the number of parts, and how many parts the upload accepts at once, starting at the first part not yet hashed. When the request gives a destination, a workspace and a path, the file is staged there once its last part arrives. When the store already has the file, `file` is `already_stored`: no parts are needed, and the file is staged at the destination, if one was given. A client whose upload completed without a response, or failed to stage, begins it again.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/versions/uploads
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
  /api/repos/{namespace}/{repo_name}/versions/uploads:
    post:
      tags:
        - Version Files
      summary: Begin a version file upload
      description: >-
        Begin uploading a large file in parts. A file may be at most 1 TiB, a
        provisional limit. The response's `file` is `awaiting_parts`, with the
        upload id, the size of every part but the last, the number of parts, and
        how many parts the upload accepts at once, starting at the first part
        not yet hashed. When the request gives a destination, a workspace and a
        path, the file is staged there once its last part arrives. When the
        store already has the file, `file` is `already_stored`: no parts are
        needed, and the file is staged at the destination, if one was given. A
        client whose upload completed without a response, or failed to stage,
        begins it again.
      operationId: begin
      parameters:
        - description: The namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: The name of the repository
          example: ImageNet-1k
          in: path
          name: repo_name
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/BeginVersionUploadRequest'
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VersionUploadResponse'
          description: Upload begun, or the file already stored
        '400':
          description: Invalid hash, size, or destination
        '404':
          description: Repository or workspace not found
        '429':
          description: Repository busy with maintenance
components:
  schemas:
    BeginVersionUploadRequest:
      description: >-
        Body of `POST /versions/uploads`: the file's hash and size, and where to
        stage it once it

        completes.
      properties:
        destination:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceDestination'
            - type: 'null'
        hash:
          type: string
        size:
          format: int64
          minimum: 0
          type: integer
      required:
        - hash
        - size
      type: object
    VersionUploadResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - $ref: '#/components/schemas/VersionUploadStart'
      description: The answer to `POST /versions/uploads`.
    WorkspaceDestination:
      description: The workspace and path to stage an uploaded file at.
      properties:
        path:
          type: string
        workspace_id:
          type: string
      required:
        - workspace_id
        - path
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
    VersionUploadStart:
      description: >-
        Where a file stands once its upload starts, in the response's `file`
        field.
      oneOf:
        - description: >-
            Send parts 1 through `num_parts` to `upload_id`, each `part_size`
            bytes but the last.
          properties:
            file:
              enum:
                - awaiting_parts
              type: string
            num_parts:
              format: int64
              minimum: 0
              type: integer
            part_size:
              format: int64
              minimum: 0
              type: integer
            part_window:
              description: >-
                How many consecutive parts the upload accepts at once, starting
                at the first part not

                yet hashed. A part past them gets 429, so a client sending parts
                in order keeps at most

                this many in flight.
              format: int64
              minimum: 0
              type: integer
            upload_id:
              type: string
          required:
            - upload_id
            - part_size
            - num_parts
            - part_window
            - file
          type: object
        - description: >-
            The store already had the file, so it needs no parts, and it is
            staged at the destination,

            if one was given.
          properties:
            file:
              enum:
                - already_stored
              type: string
          required:
            - file
          type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.