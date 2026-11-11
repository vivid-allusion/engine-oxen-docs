---
title: "Repo"
source: https://docs.oxen.ai/python-api/repo
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Repo

# oxen.repo

## Repo Objects

```python theme={null}
class Repo()
```

The Repo class that allows you to interact with your local oxen repo.

## Examples

### Init, Add, Commit and Push

Adding and committing a file to a remote workspace.

```python theme={null}
import os
from oxen import Repo

# Initialize the Oxen Repository in a CatsAndDogs directory
directory = "CatsAndDogs"
repo = Repo(directory)
repo.init()
repo.add("images")
repo.commit("Adding all the images")
# Replace <namespace> and <repo_name> with your values
repo.set_remote("origin", "https://hub.oxen.ai/<namespace>/<repo_name>")
repo.push()
```

## \_\_init\_\_

```python theme={null}
def __init__(path: str = "", mkdir=False)
```

Create a new Repo object. Use .init() to initialize a new oxen repository,
or pass the path to an existing one.

**Arguments**:

* `path` - `str`
  Path to the main working directory of your oxen repo.
* `mkdir` - `bool`
  Whether to create the directory if one doesn't exist. Default: False

## init

```python theme={null}
def init()
```

Initializes a new oxen repository at the path specified in the constructor.
Will create a .oxen folder to store all the versions and metadata.

## clone

```python theme={null}
def clone(url: str,
          branch: str = "main",
          all=False,
          filters: Optional[str | list[str]] = None)
```

Clone repository from a remote url.

**Arguments**:

* `url` - `str`
  The url of the remote repository. ex) [https://hub.oxen.ai/ox/chatbot](https://hub.oxen.ai/ox/chatbot)
* `branch` - `str`
  The name of the branch to clone. Default: main
* `all` - `bool`
  Whether to clone the full commit history or not. Default: False
* `filters` - `str | list[str] | None`
  Filter down the set of directories you want to clone. Useful if
  you have a large repository and only want to make changes to a
  specific subset of files. Default: None

## branches

```python theme={null}
def branches()
```

List all branches for a repo

## branch

```python theme={null}
def branch(name: str, delete=False)
```

## branch\_exists

```python theme={null}
def branch_exists(name: str)
```

## checkout

```python theme={null}
def checkout(revision: str, create=False)
```

Checkout a branch or commit id.

**Arguments**:

* `revision` - `str`
  The name of the branch or commit id to checkout.
* `create` - `bool`
  Whether to create a new branch if it doesn't exist. Default: False

## add

```python theme={null}
def add(path: str)
```

Stage a file or directory to be committed.

## add\_schema\_metadata

```python theme={null}
def add_schema_metadata(path: str, column_name: str, metadata: str)
```

Add schema to the local repository

## rm

```python theme={null}
def rm(path: str, recursive=False, staged=False)
```

Delete a file or directory from the working tree and stage the removal.

The next commit records the path as removed. The path must already be
committed. To bring the file back, use `oxen restore --staged <path>` to
unstage the removal and then `oxen restore <path>`.

With `staged=True` the working-tree copy is left in place. A committed
path is staged for removal and shows as untracked afterward, and a path
that has never been committed has what is staged for it unstaged.

**Arguments**:

* `path` - `str`
  The path to the file or directory to remove.
* `recursive` - `bool`
  Whether to remove the file or directory recursively. Default: False
* `staged` - `bool`
  Whether to stage the removal and leave the working-tree
  copy in place. Default: False

## restore

```python theme={null}
def restore(path: str, staged=False, source=None)
```

Restore a file or directory to a previous state.

By default the working copy is written back from the commit. With
`staged=True` the staged entry is discarded instead and the working copy
is left alone, so undoing an `rm` takes both, staged first.

**Arguments**:

* `path` - `str`
  The path to the file or directory to restore.
* `staged` - `bool`
  Discard the staged entry rather than the working copy. Default: False
* `source` - `str`
  Commit id or branch name to take the contents from, when
  restoring the working copy. Defaults to HEAD, and has no effect
  with `staged=True`.

## clean

```python theme={null}
def clean(paths=None, force=False)
```

Remove untracked files and directories from the working tree.

Without `force=True` this is a dry-run — the returned object lists what
*would* be removed but nothing is deleted. Pass `force=True` to actually
delete.

Matches the `oxen clean` CLI: tracked files, `.oxen/`, and
`.oxenignore`-matched files are never touched.

**Arguments**:

* `paths` - `list[str] | None`
  Optional list of paths to scope the cleanup. `None` (the default)
  means the whole working tree.
* `force` - `bool`
  Actually remove. Without this the call is a dry-run. Default: False

**Returns**:

A `CleanResult` with `.files`, `.dirs`, `.total_bytes`, and `.applied`
attributes.

## status

```python theme={null}
def status()
```

Check the status of the repo. Returns a StagedData object.

## commit

```python theme={null}
def commit(message: str)
```

Commit the staged data in a repo with a message.

**Arguments**:

* `message` - `str`
  The commit message.

## log

```python theme={null}
def log()
```

Get the commit history for a repo.

## set\_remote

```python theme={null}
def set_remote(name: str, url: str)
```

Map a name to a remote url.

Reads the repository at `url` and records its identifier alongside the name and
url, so the remote has to be reachable and the repository has to exist.

**Arguments**:

* `name` - `str`
  The name of the remote. Ex) origin
* `url` - `str`
  The url you want to map the name to. Ex) [https://hub.oxen.ai/ox/chatbot](https://hub.oxen.ai/ox/chatbot)

**Raises**:

* `PyOxenError` - If the repository at `url` cannot be read, or if `name` is
  already attached to a different repository.

## push

```python theme={null}
def push(remote_name: str = "origin",
         branch: str = "main",
         delete: bool = False)
```

Push data to a remote repo from a local repo.

**Arguments**:

* `remote_name` - `str`
  The name of the remote to push to.
* `branch` - `str`
  The name of the branch to push to.

## pull

```python theme={null}
def pull(remote_name: str = "origin", branch: str = "main", all=False)
```

Pull data from a remote repo to a local repo.

**Arguments**:

* `remote_name` - `str`
  The name of the remote to pull from.
* `branch` - `str`
  The name of the branch to pull from.
* `all` - `bool`
  Whether to pull all data from branch history or not. Default: False

## path

```python theme={null}
@property
def path()
```

Returns the path to the repo.

## current\_branch

```python theme={null}
@property
def current_branch()
```

Returns the current branch.

## merge

```python theme={null}
def merge(branch: str)
```

Merge a branch into the current branch.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.