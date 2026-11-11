---
title: "\ud83d\udd04 Sync with a Remote"
source: https://docs.oxen.ai/getting-started/command-line/sync_remote
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🔄 Sync with a Remote

> Push, pull, and fetch changes between your local repository and a remote.

Once your repository has a remote configured (see [Start a Repository](https://docs.oxen.ai/getting-started/command-line/start_repository.md#configure-a-remote)), you can push your work and pull collaborators' changes.

## Push Changes

Once you've committed changes locally, push them to a remote with `oxen push`.

```bash theme={null}
oxen push origin main
```

If you don't supply a remote name or branch, they default to `origin` and the current branch.

```bash theme={null}
oxen push
```

### Resume a Push

If a push is cancelled partway through, use `--missing-files` to resume and upload only the files the remote is missing.

```bash theme={null}
oxen push --missing-files
```

This is a fast repair. It uploads content the remote doesn't have, but it does not detect corrupted files. To find and fix corruption too, use `--revalidate`.

### Revalidate a Remote

`--revalidate` runs a full integrity check on the remote. It removes corrupted files from the remote and then pushes all missing files. This is the right option to use if you suspect there are any corrupted files on the remote.

```bash theme={null}
oxen push --revalidate
```

## Pull Changes

To pull the latest commits for a branch — downloading their files and Merkle trees, then checking out the latest commit — use `oxen pull`.

```bash theme={null}
oxen pull origin main
```

If no arguments are provided, the remote defaults to `origin` and the branch defaults to the current branch.

```bash theme={null}
oxen pull
```

As with `clone`, you can pull all branches with `--all`.

```bash theme={null}
oxen pull --all
```

## Fetch Changes

To fetch the latest changes without checking them out in the working directory, use `oxen fetch`.

```bash theme={null}
oxen fetch
```

This is useful when you want to inspect what's new on the remote before deciding whether to merge or check it out.

## View Configured Remotes

`oxen remote` lists the remotes configured for your repository.

```bash theme={null}
oxen remote
```

Output:

```
origin
```

Use `--verbose` to also see each remote's URL.

```bash theme={null}
oxen remote --verbose
```

Output:

```
origin      https://hub.oxen.ai/ox/CatDogBBox
local_dev   http://localhost:3000/ox/CatDogBBox
```

To add or change a remote's URL, see [Configure a Remote](https://docs.oxen.ai/getting-started/command-line/start_repository.md#configure-a-remote) on the Start a Repository page.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.