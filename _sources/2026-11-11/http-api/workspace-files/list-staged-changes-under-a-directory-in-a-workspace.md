---
title: "List staged changes under a directory in a workspace"
source: https://docs.oxen.ai/http-api/workspace-files/list-staged-changes-under-a-directory-in-a-workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List staged changes under a directory in a workspace

> List the staged changes (added, modified, and removed files) under a directory in a workspace. The added, modified, and removed lists are each paginated independently, with the same page and page_size applied to each list.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/changes/{path}
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
  /api/repos/{namespace}/{repo_name}/workspaces/{workspace_id}/changes/{path}:
    get:
      tags:
        - Workspace Files
      summary: List staged changes under a directory in a workspace
      description: >-
        List the staged changes (added, modified, and removed files) under a
        directory in a workspace. The added, modified, and removed lists are
        each paginated independently, with the same page and page_size applied
        to each list.
      operationId: list
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
        - description: The UUID of the workspace
          example: 580c0587-c157-417b-9118-8686d63d2745
          in: path
          name: workspace_id
          required: true
          schema:
            type: string
        - description: The directory to list staged changes under
          example: images/train
          in: path
          name: path
          required: true
          schema:
            type: string
        - description: Page number for pagination (default 1)
          in: query
          name: page
          required: false
          schema:
            minimum: 0
            type: integer
        - description: Number of entries per page (default 100, must be at least 1)
          in: query
          name: page_size
          required: false
          schema:
            minimum: 0
            type: integer
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/RemoteStagedStatusResponse'
          description: Staged changes under the directory
        '400':
          description: Invalid page_size
        '404':
          description: Workspace not found
components:
  schemas:
    RemoteStagedStatusResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            staged:
              $ref: '#/components/schemas/RemoteStagedStatus'
          required:
            - staged
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
    RemoteStagedStatus:
      properties:
        added_dirs:
          $ref: '#/components/schemas/SummarizedStagedDirStats'
        added_files:
          $ref: '#/components/schemas/PaginatedDirEntries'
        modified_files:
          $ref: '#/components/schemas/PaginatedDirEntries'
        removed_files:
          $ref: '#/components/schemas/PaginatedDirEntries'
      required:
        - added_dirs
        - added_files
        - modified_files
        - removed_files
      type: object
    SummarizedStagedDirStats:
      description: >-
        This is a representation of directories that are staged and we want a
        top level summary of counts

        For example:
          annotations/
            train/
              annotations.csv
              one_shot.csv
              unstaged.csv
            test/
              annotations.csv

        Would have:
            annotations/train/ -> num_staged: 2, total: 3
            annotations/test/ -> num_staged: 1, total: 1

        Rolled up to:
            annotations/ -> num_staged: 3, total: 4
      properties:
        num_files_staged:
          minimum: 0
          type: integer
        paths:
          additionalProperties:
            items:
              $ref: '#/components/schemas/StagedDirStats'
            type: array
          propertyNames:
            type: string
          type: object
        total_files:
          minimum: 0
          type: integer
      required:
        - num_files_staged
        - total_files
        - paths
      type: object
    PaginatedDirEntries:
      properties:
        dir:
          oneOf:
            - $ref: '#/components/schemas/EMetadataEntry'
            - type: 'null'
        entries:
          items:
            $ref: '#/components/schemas/EMetadataEntry'
          type: array
        metadata:
          oneOf:
            - $ref: '#/components/schemas/MetadataDir'
            - type: 'null'
        page_number:
          minimum: 0
          type: integer
        page_size:
          minimum: 0
          type: integer
        resource:
          oneOf:
            - $ref: '#/components/schemas/ResourceVersion'
            - type: 'null'
        total_entries:
          minimum: 0
          type: integer
        total_pages:
          minimum: 0
          type: integer
      required:
        - entries
        - page_size
        - page_number
        - total_pages
        - total_entries
      type: object
    StagedDirStats:
      properties:
        num_files_staged:
          minimum: 0
          type: integer
        path:
          type: string
        status:
          $ref: '#/components/schemas/StagedEntryStatus'
        total_files:
          minimum: 0
          type: integer
      required:
        - path
        - num_files_staged
        - total_files
        - status
      type: object
    EMetadataEntry:
      oneOf:
        - $ref: '#/components/schemas/MetadataEntry'
        - $ref: '#/components/schemas/WorkspaceMetadataEntry'
    MetadataDir:
      properties:
        dir:
          $ref: '#/components/schemas/MetadataDirImpl'
      required:
        - dir
      type: object
    ResourceVersion:
      properties:
        path:
          type: string
        version:
          type: string
      required:
        - path
        - version
      type: object
    StagedEntryStatus:
      enum:
        - Added
        - Modified
        - Removed
        - Unmodified
      type: string
    MetadataEntry:
      additionalProperties: false
      description: >-
        `deny_unknown_fields` is the discriminator for the untagged
        `EMetadataEntry` enum:

        payloads with a `changes` field (i.e. `WorkspaceMetadataEntry`) fail to
        deserialize here

        and fall through to the workspace variant.
      properties:
        children:
          items:
            $ref: '#/components/schemas/MetadataEntry'
          type:
            - array
            - 'null'
        data_type:
          $ref: '#/components/schemas/EntryDataType'
        extension:
          type: string
        filename:
          type: string
        hash:
          type: string
        is_dir:
          type: boolean
        is_queryable:
          type:
            - boolean
            - 'null'
        latest_commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
        metadata:
          oneOf:
            - $ref: '#/components/schemas/GenericMetadata'
            - type: 'null'
        mime_type:
          type: string
        resource:
          oneOf:
            - $ref: '#/components/schemas/ParsedResourceView'
            - type: 'null'
        size:
          format: int64
          minimum: 0
          type: integer
      required:
        - filename
        - hash
        - is_dir
        - size
        - data_type
        - mime_type
        - extension
      type: object
    WorkspaceMetadataEntry:
      properties:
        changes:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceChanges'
            - type: 'null'
        children:
          items:
            $ref: '#/components/schemas/WorkspaceMetadataEntry'
          type:
            - array
            - 'null'
        data_type:
          $ref: '#/components/schemas/EntryDataType'
        extension:
          type: string
        filename:
          type: string
        hash:
          type: string
        is_dir:
          type: boolean
        is_queryable:
          type:
            - boolean
            - 'null'
        latest_commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
        metadata:
          oneOf:
            - $ref: '#/components/schemas/GenericMetadata'
            - type: 'null'
        mime_type:
          type: string
        resource:
          oneOf:
            - $ref: '#/components/schemas/ParsedResourceView'
            - type: 'null'
        size:
          format: int64
          minimum: 0
          type: integer
      required:
        - filename
        - hash
        - is_dir
        - size
        - data_type
        - mime_type
        - extension
      type: object
    MetadataDirImpl:
      properties:
        data_types:
          items:
            $ref: '#/components/schemas/DataTypeCount'
          type: array
      required:
        - data_types
      type: object
    EntryDataType:
      enum:
        - dir
        - text
        - image
        - video
        - audio
        - tabular
        - binary
      type: string
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
    GenericMetadata:
      oneOf:
        - $ref: '#/components/schemas/MetadataDir'
        - $ref: '#/components/schemas/MetadataText'
        - $ref: '#/components/schemas/MetadataImage'
        - $ref: '#/components/schemas/MetadataVideo'
        - $ref: '#/components/schemas/MetadataAudio'
        - $ref: '#/components/schemas/MetadataTabular'
    ParsedResourceView:
      description: External (view) model that is returned to the client with fewer fields.
      properties:
        branch:
          oneOf:
            - $ref: '#/components/schemas/Branch'
            - type: 'null'
        commit:
          oneOf:
            - $ref: '#/components/schemas/Commit'
            - type: 'null'
        path:
          type: string
        resource:
          type: string
        version:
          type: string
        workspace:
          oneOf:
            - $ref: '#/components/schemas/WorkspaceView'
            - type: 'null'
      required:
        - path
        - version
        - resource
      type: object
    WorkspaceChanges:
      properties:
        status:
          $ref: '#/components/schemas/StagedEntryStatus'
      required:
        - status
      type: object
    DataTypeCount:
      properties:
        count:
          minimum: 0
          type: integer
        data_type:
          type: string
      required:
        - count
        - data_type
      type: object
    MetadataText:
      properties:
        text:
          $ref: '#/components/schemas/MetadataTextImpl'
      required:
        - text
      type: object
    MetadataImage:
      properties:
        image:
          $ref: '#/components/schemas/MetadataImageImpl'
      required:
        - image
      type: object
    MetadataVideo:
      properties:
        video:
          $ref: '#/components/schemas/MetadataVideoImpl'
      required:
        - video
      type: object
    MetadataAudio:
      properties:
        audio:
          $ref: '#/components/schemas/MetadataAudioImpl'
      required:
        - audio
      type: object
    MetadataTabular:
      properties:
        tabular:
          $ref: '#/components/schemas/MetadataTabularImpl'
      required:
        - tabular
      type: object
    Branch:
      properties:
        commit_id:
          type: string
        name:
          type: string
      required:
        - name
        - commit_id
      type: object
    WorkspaceView:
      description: >-
        Used to send workspace state across the wire. The `Workspace`'s other
        fields (like

        `LocalRepository`) would bloat the response and leak internal state.
      properties:
        commit:
          $ref: '#/components/schemas/Commit'
        created_at:
          description: >-
            `None` for a workspace created before the server recorded creation
            time.
          format: date-time
          type:
            - string
            - 'null'
        id:
          type: string
        name:
          type:
            - string
            - 'null'
      required:
        - id
        - commit
      type: object
    MetadataTextImpl:
      properties:
        num_chars:
          minimum: 0
          type: integer
        num_lines:
          minimum: 0
          type: integer
      required:
        - num_lines
        - num_chars
      type: object
    MetadataImageImpl:
      properties:
        color_space:
          oneOf:
            - $ref: '#/components/schemas/ImgColorSpace'
            - type: 'null'
        height:
          format: int32
          minimum: 0
          type: integer
        width:
          format: int32
          minimum: 0
          type: integer
      required:
        - width
        - height
      type: object
    MetadataVideoImpl:
      properties:
        height:
          minimum: 0
          type: integer
        num_seconds:
          format: double
          type: number
        width:
          minimum: 0
          type: integer
      required:
        - num_seconds
        - width
        - height
      type: object
    MetadataAudioImpl:
      properties:
        num_channels:
          minimum: 0
          type: integer
        num_seconds:
          format: double
          type: number
        sample_rate:
          minimum: 0
          type: integer
      required:
        - num_seconds
        - num_channels
        - sample_rate
      type: object
    MetadataTabularImpl:
      properties:
        height:
          minimum: 0
          type: integer
        schema:
          $ref: '#/components/schemas/Schema'
        width:
          minimum: 0
          type: integer
      required:
        - width
        - height
        - schema
      type: object
    ImgColorSpace:
      enum:
        - RGB
        - RGBA
        - Grayscale
        - GrayscaleAlpha
        - Rgb16
        - Rgba16
        - Grayscale16
        - GrayscaleAlpha16
        - Rgb32F
        - Rgba32F
        - Unknown
      type: string
    Schema:
      properties:
        fields:
          items:
            $ref: '#/components/schemas/Field'
          type: array
        hash:
          type: string
        metadata: {}
      required:
        - hash
        - fields
      type: object
    Field:
      properties:
        changes:
          oneOf:
            - $ref: '#/components/schemas/Changes'
            - type: 'null'
        dtype:
          type: string
        metadata: {}
        name:
          type: string
      required:
        - name
        - dtype
      type: object
    Changes:
      properties:
        previous:
          oneOf:
            - $ref: '#/components/schemas/PreviousField'
            - type: 'null'
        status:
          type: string
      required:
        - status
      type: object
    PreviousField:
      properties:
        dtype:
          type: string
        metadata: {}
        name:
          type: string
      required:
        - name
        - dtype
      type: object
  securitySchemes:
    api_key:
      bearerFormat: JWT
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.