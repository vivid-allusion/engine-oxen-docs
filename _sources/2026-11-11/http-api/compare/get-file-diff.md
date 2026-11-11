---
title: "Get file diff"
source: https://docs.oxen.ai/http-api/compare/get-file-diff
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Get file diff

> Get the detailed diff for a specific file between two revisions.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_server_openapi.json get /api/repos/{namespace}/{repo_name}/compare/{base_head}/file/{resource}
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
  /api/repos/{namespace}/{repo_name}/compare/{base_head}/file/{resource}:
    get:
      tags:
        - Compare
      summary: Get file diff
      description: Get the detailed diff for a specific file between two revisions.
      operationId: file
      parameters:
        - description: Namespace of the repository
          example: ox
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: Name of the repository
          example: compare-datasets
          in: path
          name: repo_name
          required: true
          schema:
            type: string
        - description: The base and head revisions separated by '..'
          example: main..feature/add-labels
          in: path
          name: base_head
          required: true
          schema:
            type: string
        - description: Path to the file (including branch)
          example: data/test/file.txt
          in: path
          name: resource
          required: true
          schema:
            type: string
        - description: Page number for pagination (starts at 1)
          in: query
          name: page
          required: false
          schema:
            minimum: 0
            type: integer
        - description: Page size for pagination
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
                $ref: '#/components/schemas/CompareEntryResponse'
          description: File diff found successfully
        '404':
          description: Repository, revision, or file not found
components:
  schemas:
    CompareEntryResponse:
      allOf:
        - $ref: '#/components/schemas/StatusMessage'
        - properties:
            compare:
              $ref: '#/components/schemas/DiffEntry'
          required:
            - compare
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
    DiffEntry:
      properties:
        base_entry:
          oneOf:
            - $ref: '#/components/schemas/MetadataEntry'
            - type: 'null'
        base_resource:
          oneOf:
            - $ref: '#/components/schemas/ParsedResourceView'
            - type: 'null'
        data_type:
          $ref: '#/components/schemas/EntryDataType'
        diff:
          oneOf:
            - $ref: '#/components/schemas/GenericDiff'
            - type: 'null'
        diff_summary:
          oneOf:
            - $ref: '#/components/schemas/GenericDiffSummary'
            - type: 'null'
        filename:
          type: string
        head_entry:
          oneOf:
            - $ref: '#/components/schemas/MetadataEntry'
            - type: 'null'
        head_resource:
          oneOf:
            - $ref: '#/components/schemas/ParsedResourceView'
            - type: 'null'
        is_dir:
          type: boolean
        size:
          format: int64
          minimum: 0
          type: integer
        status:
          type: string
      required:
        - status
        - data_type
        - filename
        - is_dir
        - size
      type: object
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
    GenericDiff:
      oneOf:
        - $ref: '#/components/schemas/DirDiff'
        - $ref: '#/components/schemas/TabularDiffView'
        - $ref: '#/components/schemas/TextDiff'
    GenericDiffSummary:
      oneOf:
        - $ref: '#/components/schemas/DirDiffSummary'
        - $ref: '#/components/schemas/TabularDiffWrapper'
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
    DirDiff:
      allOf:
        - $ref: '#/components/schemas/DirDiffSummary'
    TabularDiffView:
      properties:
        tabular:
          $ref: '#/components/schemas/TabularDiffViewImpl'
      required:
        - tabular
      type: object
    TextDiff:
      properties:
        filename1:
          type:
            - string
            - 'null'
        filename2:
          type:
            - string
            - 'null'
        lines:
          items:
            $ref: '#/components/schemas/LineDiff'
          type: array
      required:
        - lines
      type: object
    DirDiffSummary:
      properties:
        dir:
          $ref: '#/components/schemas/DirDiffSummaryImpl'
      required:
        - dir
      type: object
    TabularDiffWrapper:
      properties:
        tabular:
          $ref: '#/components/schemas/TabularDiffSummaryImpl'
      required:
        - tabular
      type: object
    MetadataDir:
      properties:
        dir:
          $ref: '#/components/schemas/MetadataDirImpl'
      required:
        - dir
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
    TabularDiffViewImpl:
      allOf:
        - $ref: '#/components/schemas/TabularDiffSummary'
        - properties:
            added_cols:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrame'
                - type: 'null'
            added_cols_view:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrameView'
                - type: 'null'
            added_rows:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrame'
                - type: 'null'
            added_rows_view:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrameView'
                - type: 'null'
            base_schema:
              oneOf:
                - $ref: '#/components/schemas/Schema'
                - type: 'null'
            head_schema:
              oneOf:
                - $ref: '#/components/schemas/Schema'
                - type: 'null'
            removed_cols:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrame'
                - type: 'null'
            removed_cols_view:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrameView'
                - type: 'null'
            removed_rows:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrame'
                - type: 'null'
            removed_rows_view:
              oneOf:
                - $ref: '#/components/schemas/JsonDataFrameView'
                - type: 'null'
          type: object
    LineDiff:
      properties:
        modification:
          $ref: '#/components/schemas/ChangeType'
        text:
          type: string
      required:
        - modification
        - text
      type: object
    DirDiffSummaryImpl:
      properties:
        file_counts:
          $ref: '#/components/schemas/AddRemoveModifyCounts'
      required:
        - file_counts
      type: object
    TabularDiffSummaryImpl:
      properties:
        num_added_cols:
          minimum: 0
          type: integer
        num_added_rows:
          minimum: 0
          type: integer
        num_removed_cols:
          minimum: 0
          type: integer
        num_removed_rows:
          minimum: 0
          type: integer
        schema_has_changed:
          type: boolean
      required:
        - num_added_rows
        - num_added_cols
        - num_removed_rows
        - num_removed_cols
        - schema_has_changed
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
    TabularDiffSummary:
      properties:
        summary:
          $ref: '#/components/schemas/TabularDiffSummaryImpl'
      required:
        - summary
      type: object
    JsonDataFrame:
      properties:
        data: {}
        full_size:
          $ref: '#/components/schemas/DataFrameSize'
        schema:
          $ref: '#/components/schemas/Schema'
        view_schema:
          $ref: '#/components/schemas/Schema'
        view_size:
          $ref: '#/components/schemas/DataFrameSize'
      required:
        - schema
        - view_schema
        - view_size
        - full_size
        - data
      type: object
    JsonDataFrameView:
      allOf:
        - $ref: '#/components/schemas/DFOptsView'
        - properties:
            data: {}
            pagination:
              $ref: '#/components/schemas/Pagination'
            schema:
              $ref: '#/components/schemas/Schema'
            size:
              $ref: '#/components/schemas/DataFrameSize'
          required:
            - schema
            - size
            - data
            - pagination
          type: object
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
    ChangeType:
      enum:
        - Added
        - Removed
        - Modified
        - Unchanged
      type: string
    AddRemoveModifyCounts:
      properties:
        added:
          minimum: 0
          type: integer
        modified:
          minimum: 0
          type: integer
        removed:
          minimum: 0
          type: integer
      required:
        - added
        - removed
        - modified
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
    DataFrameSize:
      properties:
        height:
          minimum: 0
          type: integer
        width:
          minimum: 0
          type: integer
      required:
        - height
        - width
      type: object
    DFOptsView:
      properties:
        opts:
          items:
            $ref: '#/components/schemas/DFOptView'
          type: array
      required:
        - opts
      type: object
    Pagination:
      properties:
        page_number:
          minimum: 0
          type: integer
        page_size:
          minimum: 0
          type: integer
        total_entries:
          minimum: 0
          type: integer
        total_pages:
          minimum: 0
          type: integer
      required:
        - page_size
        - page_number
        - total_pages
        - total_entries
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
    DFOptView:
      properties:
        name:
          type: string
        value: {}
      required:
        - name
        - value
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