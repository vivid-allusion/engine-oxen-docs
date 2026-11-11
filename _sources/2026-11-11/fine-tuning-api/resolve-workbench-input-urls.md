---
title: "Resolve workbench input URLs"
source: https://docs.oxen.ai/fine-tuning-api/resolve-workbench-input-urls
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Resolve workbench input URLs

> Turns input URLs a client saved earlier into URLs that load now. A branch or workspace URL into `oxen/context/` or `oxen/outputs/` that the v3 workbench migration left dead is re-pointed at a commit from before the migration that holds the file. Each URL is checked against the caller's read access on its own repo; a URL into a repo the caller cannot read comes back `unknown` without being looked up.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json post /api/repos/{namespace}/{repo_name}/workbench/references/resolve
openapi: 3.0.0
info:
  title: oxen
  version: v282
servers:
  - url: https://hub.oxen.ai
    variables: {}
security: []
tags: []
paths:
  /api/repos/{namespace}/{repo_name}/workbench/references/resolve:
    post:
      tags: []
      summary: Resolve workbench input URLs
      description: >-
        Turns input URLs a client saved earlier into URLs that load now. A
        branch or workspace URL into `oxen/context/` or `oxen/outputs/` that the
        v3 workbench migration left dead is re-pointed at a commit from before
        the migration that holds the file. Each URL is checked against the
        caller's read access on its own repo; a URL into a repo the caller
        cannot read comes back `unknown` without being looked up.
      operationId: OxenApiWeb.Controllers.WorkbenchReferenceController.resolve
      parameters:
        - description: ''
          in: path
          name: namespace
          required: true
          schema:
            type: string
        - description: ''
          in: path
          name: repo_name
          required: true
          schema:
            type: string
      requestBody:
        content:
          application/json:
            schema:
              $ref: '#/components/schemas/WorkbenchReferencesResolveRequest'
        description: URLs to resolve
        required: false
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/WorkbenchReferencesResolveResponse'
          description: One result per URL, in order
        '400':
          content:
            application/json:
              schema:
                type: object
          description: '`urls` is missing or not an array of strings'
        '422':
          content:
            application/json:
              schema:
                type: object
          description: More than 100 URLs
      callbacks: {}
components:
  schemas:
    WorkbenchReferencesResolveRequest:
      properties:
        urls:
          description: Input URLs to resolve, such as those a saved form draft holds.
          items:
            type: string
          maxItems: 100
          type: array
      required:
        - urls
      title: WorkbenchReferencesResolveRequest
      type: object
    WorkbenchReferencesResolveResponse:
      properties:
        references:
          description: One entry per requested URL, in request order.
          items:
            properties:
              pinned_url:
                description: >-
                  The URL to store in place of `url`, pinned to a commit that
                  holds the file and unsigned, in the form of `url` (a relative
                  URL stays relative). Present for a `live` branch URL, a `live`
                  workspace URL whose file the workspace has not changed, and a
                  `recovered` URL. Null for a file only staged in a workspace,
                  which only a commit can pin, for a URL already pinned, and for
                  every other status.
                nullable: true
                type: string
              resolved_url:
                description: >-
                  `live`: the URL presigned. `recovered`: the URL pinned to that
                  commit, presigned. `missing`: null. `unknown` and `skipped`:
                  the URL unchanged.
                nullable: true
                type: string
              status:
                description: >-
                  `live`: the file is where the URL names it. `recovered`: it is
                  not, and a commit from before the v3 workbench migration holds
                  it. `missing`: no such file. `unknown`: the lookup failed, the
                  caller cannot read the repo the URL names, or the file was not
                  found while a migration is running on that repo. `skipped`:
                  not a hub file URL.
                enum:
                  - live
                  - recovered
                  - missing
                  - unknown
                  - skipped
                type: string
              url:
                description: The URL as requested.
                type: string
            required:
              - url
              - status
              - resolved_url
              - pinned_url
            type: object
          type: array
        status:
          enum:
            - success
          type: string
      required:
        - status
        - references
      title: WorkbenchReferencesResolveResponse
      type: object

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.