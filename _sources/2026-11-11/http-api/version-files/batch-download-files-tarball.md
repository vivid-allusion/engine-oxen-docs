---
title: "Batch download files (Tarball)"
source: https://docs.oxen.ai/http-api/version-files/batch-download-files-tarball
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Batch download files (Tarball)

> Download multiple files as a gzipped tarball by providing their hashes.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json post /api/repos/{namespace}/{repo_name}/versions/batch-download
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
  /api/repos/{namespace}/{repo_name}/versions/batch-download:
    post:
      tags:
        - Version Files
      summary: Batch download files (Tarball)
      description: Download multiple files as a gzipped tarball by providing their hashes.
      operationId: batch_download
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
          application/gzip:
            schema:
              items:
                format: int32
                minimum: 0
                type: integer
              type: array
        description: >-
          Gzip compressed binary payload containing a line-delimited list of
          merkle hashes to download
        required: true
      responses:
        '200':
          content:
            application/gzip: {}
          description: Tarball of all requested files, gzipped.
components:
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.