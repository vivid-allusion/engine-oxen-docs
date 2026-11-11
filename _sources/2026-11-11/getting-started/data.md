---
title: "Repositories on Oxen.ai"
source: https://docs.oxen.ai/getting-started/data
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Repositories on Oxen.ai

> Oxen.ai allows you to version and store your data in repositories. Think of it like git for large data.

When using models on Oxen.ai, by default we store the model inputs, outputs, and metadata in a repository. Every piece of data is versioned so you can trace the provenance of your data and models.

In order to version data at scale, we built an [open source version control system](https://github.com/Oxen-AI/Oxen) that can scale to monorepos with millions of files and terabytes of data.

## Key Concepts

* **[Repository](https://docs.oxen.ai/examples/data/versioning.md)**: A collection of files and folders that is versioned together.
* **Commit**: A snapshot of a repository at a given time.
* **Branch**: A named pointer to a commit.
* **[Dataset](https://docs.oxen.ai/examples/data/datasets.md)**: A tabular file within an oxen repository that can be indexed and searched. ie csv, jsonl, parquet, etc.
* **[Workspace](https://docs.oxen.ai/examples/data/workspaces.md)**: The equivalent of a working directory on the remote server where files can be added in an uncommitted state.

Follow along with the [Version Control](https://docs.oxen.ai/examples/data/versioning.md) guide to learn how to version your data.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.