---
title: "Upload one part of a version file"
source: https://docs.oxen.ai/http-api/version-files/upload-one-part-of-a-version-file
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Upload one part of a version file

> Upload one part of a file. A part may arrive up to `part_window` parts from the earliest part not yet hashed, counting that part, and one further ahead is refused with 429 and Retry-After, as is a part sent again while its first copy is still being stored. Until the upload completes, a part sent again after it was stored is accepted and ignored. Once it completes, any part gets 404, as for an upload that was aborted, so a client that lost the response for the last part begins the upload again, which answers with no parts to send once the file is stored. Each part but the last is exactly the upload's part size. The response for the part that completes the file reports `completed: true`, once the file is verified against its hash and staged in the upload's workspace, if it has one.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json put /api/repos/{namespace}/{repo_name}/versions/uploads/{upload_id}/parts/{part_number}
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
  /api/repos/{namespace}/{repo_name}/versions/uploads/{upload_id}/parts/{part_number}:
    put:
      tags:
        - Version Files
      summary: Upload one part of a version file
      description: >-
        Upload one part of a file. A part may arrive up to `part_window` parts
        from the earliest part not yet hashed, counting that part, and one
        further ahead is refused with 429 and Retry-After, as is a part sent
        again while its first copy is still being stored. Until the upload
        completes, a part sent again after it was stored is accepted and
        ignored. Once it completes, any part gets 404, as for an upload that was
        aborted, so a client that lost the response for the last part begins the
        upload again, which answers with no parts to send once the file is
        stored. Each part but the last is exactly the upload's part size. The
        response for the part that completes the file reports `completed: true`,
        once the file is verified against its hash and staged in the upload's
        workspace, if it has one.
      operationId: upload_part
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
        - description: The id the upload began with
          in: path
          name: upload_id
          required: true
          schema:
            type: string
        - description: The part's number, counting from 1
          example: 1
          in: path
          name: part_number
          required: true
          schema:
            format: int64
            minimum: 0
            type: integer
      requestBody:
        content:
          application/octet-stream:
            schema:
              items:
                format: int32
                minimum: 0
                type: integer
              type: array
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/VersionUploadPartResponse'
          description: Part stored
        '400':
          description: >-
            Part out of range, of the wrong length, or the file's bytes do not
            match its hash
        '404':
          description: 'Upload not found: it never began, was aborted, or already completed'
        '429':
          description: >-
            Part arrived too far ahead of the parts before it, or an earlier
            copy of it is still being stored. Send it again after Retry-After
components:
  schemas:
    VersionUploadPartResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            completed:
              type: boolean
          required:
            - completed
          type: object
      description: >-
        A part stored. `completed` is true for the part that completed the
        upload.
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
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.