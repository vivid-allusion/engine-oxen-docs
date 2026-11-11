---
title: "\ud83c\udf3f Branches & Merging"
source: https://docs.oxen.ai/getting-started/command-line/branches
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🌿 Branches & Merging

> Create branches, switch between them, and merge work together.

Branches let you take a snapshot of your data, experiment freely, and merge the results back without affecting the original. The commands map closely to git.

## Create a Branch

Create a new branch and check it out in one step with `oxen checkout -b`.

```bash theme={null}
oxen checkout -b feature
```

## List Branches

To list the branches in your repository (highlighting the one you're on), use `oxen branch`.

```bash theme={null}
oxen branch
```

To see branches that exist on the remotes, add `--remote`.

```bash theme={null}
oxen branch --remote
```

To delete a branch, use `oxen branch --delete`. This fails if the branch has changes that haven't been merged.

```bash theme={null}
oxen branch --delete feature
```

Use `-D` to force-delete a branch.

```bash theme={null}
oxen branch -D feature
```

## Switch Between Branches

Use `oxen checkout` to switch branches. This restores the working directory to the HEAD commit of the branch you're checking out.

```bash theme={null}
oxen checkout main
```

You can also check out a specific commit.

```bash theme={null}
oxen checkout COMMIT_ID
```

## Merge Branches

Merge another branch into your current branch with `oxen merge`. This creates a merge commit, or fails if there are conflicts to resolve.

```bash theme={null}
oxen merge TARGET_BRANCH
```

If you're collaborating, you may instead want to open a merge request through the [Oxen.ai web UI](https://oxen.ai).

![Oxen.ai merge request](https://mintcdn.com/oxenai/Bb9kRFujEIMk3du0/images/merge_request.png?fit=max\&auto=format\&n=Bb9kRFujEIMk3du0\&q=85\&s=8c74209d788e4848b7b63de2a4cab792)


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.