---
title: "Batch upload files (Multipart)"
source: https://docs.oxen.ai/http-api/version-files/batch-upload-files-multipart
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch upload files (Multipart)

> Upload multiple files via multipart form, identified by their content hashes.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/versions
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
  /api/repos/{namespace}/{repo_name}/versions:
    post:
      tags:
        - Version Files
      summary: Batch upload files (Multipart)
      description: >-
        Upload multiple files via multipart form, identified by their content
        hashes.
      operationId: batch_upload
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
          multipart/form-data:
            schema:
              $ref: '#/components/schemas/UploadVersionFile'
        description: >-
          Multipart upload of files. Each form field 'file[]' or 'file' should
          contain the file content (optionally gzip compressed), and the
          filename should be the content hash (e.g., 'file.jpg' is not used, the
          hash is the identifier).
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/ErrorFilesResponse'
          description: Files successfully uploaded (check err_files for failures)
        '400':
          description: Invalid multipart request
        '404':
          description: Repository not found
components:
  schemas:
    UploadVersionFile:
      properties:
        file:
          format: binary
          type: string
      required:
        - file
      type: object
    ErrorFilesResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            err_files:
              items:
                $ref: '#/components/schemas/ErrorFileInfo'
              type: array
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
    ErrorFileInfo:
      properties:
        error:
          type: string
        hash:
          type: string
        path:
          type:
            - string
            - 'null'
      required:
        - hash
        - error
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.