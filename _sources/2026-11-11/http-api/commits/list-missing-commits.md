---
title: "List missing commits"
source: https://docs.oxen.ai/http-api/commits/list-missing-commits
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List missing commits

> From a list of commit hashes, list the ones not present on the server



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/commits/missing
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
  /api/repos/{namespace}/{repo_name}/commits/missing:
    get:
      tags:
        - Commits
      summary: List missing commits
      description: From a list of commit hashes, list the ones not present on the server
      operationId: list_missing
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
      requestBody:
        content:
          application/json:
            example:
              hashes:
                - abc1234567890def1234567890fedcba
                - 84c76a5b2e9a2637f9091991475c404d
            schema:
              $ref: '#/components/schemas/MerkleHashes'
        description: List of commit hashes present on the client.
        required: true
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/MerkleHashesResponse'
          description: List of commit hashes missing on the server
        '400':
          description: Invalid JSON body
        '404':
          description: Repository not found
components:
  schemas:
    MerkleHashes:
      properties:
        hashes:
          items:
            $ref: '#/components/schemas/MerkleHash'
          type: array
          uniqueItems: true
      required:
        - hashes
      type: object
    MerkleHashesResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            hashes:
              items:
                $ref: '#/components/schemas/MerkleHash'
              type: array
              uniqueItems: true
          required:
            - hashes
          type: object
    MerkleHash:
      type: string
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