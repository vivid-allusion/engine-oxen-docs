---
title: "Get diff tree"
source: https://docs.oxen.ai/http-api/compare/get-diff-tree
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get diff tree

> Get a tree structure of directories that have changed between two revisions.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/compare/{base_head}/tree
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
  /api/repos/{namespace}/{repo_name}/compare/{base_head}/tree:
    get:
      tags:
        - Compare
      summary: Get diff tree
      description: >-
        Get a tree structure of directories that have changed between two
        revisions.
      operationId: dir_tree
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: satellite-images
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: >-
            The base and head revisions separated by '..', or '...' to diff from
            the merge base
          example: main...feature/add-labels
          in: path
          name: base_head
          required: true
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/DirTreeDiffResponse'
          description: Directory diff tree found successfully
        '404':
          description: Repository or one of the revisions not found
components:
  schemas:
    DirTreeDiffResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            dirs:
              items:
                $ref: '#/components/schemas/DirDiffTreeSummary'
              type: array
          required:
            - dirs
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
    DirDiffTreeSummary:
      properties:
        can_display:
          type: boolean
        children:
          items:
            $ref: '#/components/schemas/DirDiffStatus'
          type: array
        name:
          type: string
        num_subdirs:
          minimum: 0
          type: integer
        status:
          $ref: '#/components/schemas/DiffEntryStatus'
      required:
        - name
        - status
        - num_subdirs
        - can_display
        - children
      type: object
    DirDiffStatus:
      properties:
        name:
          type: string
        status:
          $ref: '#/components/schemas/DiffEntryStatus'
      required:
        - name
        - status
      type: object
    DiffEntryStatus:
      enum:
        - added
        - modified
        - removed
      type: string
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.