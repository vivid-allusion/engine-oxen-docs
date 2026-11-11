---
title: "Export resource as a zip"
source: https://docs.oxen.ai/http-api/export/export-resource-as-a-zip
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Export resource as a zip

> Download a directory as a zip archive. Subject to size limits.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/export/download/{resource}
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
  /api/repos/{namespace}/{repo_name}/export/download/{resource}:
    get:
      tags:
        - Export
      summary: Export resource as a zip
      description: Download a directory as a zip archive. Subject to size limits.
      operationId: download_zip
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: Wiki-Text
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: Path to directory and branch/commit (e.g. main/data)
          example: main/data
          in: path
          name: resource
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/zip: {}
          description: Zip archive of the directory
        '400':
          description: Download size exceeds limit
        '404':
          description: Repository or resource not found
components:
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.