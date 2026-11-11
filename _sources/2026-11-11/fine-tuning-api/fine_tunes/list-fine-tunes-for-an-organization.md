---
title: "List fine-tunes for an organization"
source: https://docs.oxen.ai/fine-tuning-api/fine_tunes/list-fine-tunes-for-an-organization
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# List fine-tunes for an organization

> Return all fine-tune jobs in repositories belonging to the given organization. Requires the authenticated user to be a member of the organization.



## OpenAPI

````yaml https://hub.oxen.ai/api/_spec/oxen_hub_api.json get /api/orgs/{name}/fine_tunes
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
  /api/orgs/{name}/fine_tunes:
    get:
      tags:
        - fine_tunes
      summary: List fine-tunes for an organization
      description: >-
        Return all fine-tune jobs in repositories belonging to the given
        organization. Requires the authenticated user to be a member of the
        organization.
      operationId: OxenApiWeb.Controllers.FineTuneController.list_for_team
      parameters:
        - description: Organization name
          in: path
          name: name
          required: true
          schema:
            type: string
        - description: Page number (1-indexed)
          in: query
          name: page
          required: false
          schema:
            type: integer
        - description: Number of items per page
          in: query
          name: page_size
          required: false
          schema:
            type: integer
        - description: >-
            Search across fine-tune name, display name, base model, and
            repository (case-insensitive substring match). For example: 'qwen',
            'ox/Delorean', 'customer-support'.
          in: query
          name: search
          required: false
          schema:
            type: string
        - description: >-
            Filter by status. One of: created, tokenizing, enqueued, running,
            completed, stopped, errored, deployed
          in: query
          name: status
          required: false
          schema:
            type: string
        - description: Filter by creator username (exact match)
          in: query
          name: created_by
          required: false
          schema:
            type: string
        - description: 'Sort order by creation date: ''newest'' (default) or ''oldest'''
          in: query
          name: sort
          required: false
          schema:
            type: string
      responses:
        '200':
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/FineTuneListResponse'
          description: List fine-tunes response
        '401':
          content:
            application/json:
              schema:
                type: object
          description: Not authenticated or not a member
        '404':
          content:
            application/json:
              schema:
                type: object
          description: Organization not found
      callbacks: {}
      security:
        - authorization: []
components:
  schemas:
    FineTuneListResponse:
      description: Standard wrapper for fine-tune list responses.
      properties:
        fine_tunes:
          description: List of fine-tune job resources
          items:
            anyOf:
              - $ref: '#/components/schemas/FineTune'
          type: array
        status:
          description: High-level status string (for example, 'success').
          type: string
        status_message:
          description: Human-readable status message (for example, 'resource_found').
          type: string
      title: FineTuneListResponse
      type: object
    FineTune:
      description: >
        Fine-tune job resource.

        This is a simplified view meant for OpenAPI docs; extend as needed to
        match your views.
      properties:
        base_model:
          description: Canonical name of the base model
          type: string
        created_at:
          description: Creation time
          format: date_time
          type: string
        id:
          description: Fine-tune ID
          type: string
        name:
          description: Fine-tune name
          type: string
        status:
          description: Current status of the fine-tune
          type: string
        updated_at:
          description: Last update time
          format: date_time
          type: string
      title: FineTune
      type: object
  securitySchemes:
    authorization:
      scheme: bearer
      type: http

````

This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.