---
title: "Workspace"
source: https://docs.oxen.ai/python-api/workspace
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Workspace

# oxen.workspace

## Workspace Objects

```python theme={null}
class Workspace()
```

The Workspace class allows you to interact with an Oxen workspace
without downloading the data locally.

Workspaces can be created off a branch and is tied to the commit id of the branch
at the time of creation.

You can commit a Workspace back to the same branch if the branch has not
advanced, otherwise you will have to commit to a new branch and merge.

## Examples

### Adding Files to a Workspace

Create a workspace from a branch.

```python theme={null}
from oxen import RemoteRepo
from oxen import Workspace

# Connect to the remote repo
repo = RemoteRepo("ox/CatDogBBox")

# Create the workspace
workspace = Workspace(repo, "my-branch")

# Add a file to the workspace
failed_to_upload = workspace.add("my-image.png", raise_on_failure=False)
assert len(failed_to_upload) == 0

# Or raise an exception if any files fail to upload
workspace.add("my-image-final-final.png")

# Print the status of the workspace
status = workspace.status()
print(status.added_files())

# Commit the workspace
workspace.commit("Adding my images to the workspace.")
```

## \_\_init\_\_

```python theme={null}
def __init__(repo: "RemoteRepo",
             branch: str,
             workspace_id: Optional[str] = None,
             workspace_name: Optional[str] = None,
             path: Optional[str] = None) -> None
```

Create a new Workspace.

**Arguments**:

* `repo` - `PyRemoteRepo`
  The remote repo to create the workspace from.
* `branch` - `str`
  The branch name to create the workspace from. The workspace
  will be tied to the commit id of the branch at the time of creation.
* `workspace_id` - `Optional[str]`
  The workspace id to create the workspace from.
  If left empty, will create a unique workspace id.
* `workspace_name` - `Optional[str]`
  The name of the workspace. If left empty, the workspace will have no name.
* `path` - `Optional[str]`
  The path to the workspace. If left empty, the workspace will be created in the root of the remote repo.

## id

```python theme={null}
@property
def id()
```

Get the id of the workspace.

## name

```python theme={null}
@property
def name()
```

Get the name of the workspace.

## branch

```python theme={null}
@property
def branch()
```

Get the branch that the workspace is tied to.

## commit\_id

```python theme={null}
@property
def commit_id() -> str
```

Get the commit id of the workspace.

## created\_at

```python theme={null}
@property
def created_at() -> Optional[str]
```

Get the RFC 3339 time the workspace was created, or None for a workspace
created before the server recorded it.

## repo

```python theme={null}
@property
def repo() -> "RemoteRepo"
```

Get the remote repo that the workspace is tied to.

## status

```python theme={null}
def status(path: str = "")
```

Get the status of the workspace.

**Arguments**:

* `path` - `str`
  The path to check the status of.

## add

```python theme={null}
def add(src: str | Iterable[str] | Path | Iterable[Path],
        dst: str = "",
        raise_on_failure: bool = True) -> list[PyErrorFileInfo]
```

Add files to the workspace.

Accepts a single file, a single directory, or multiple of either.

Recursively walks directories to add all accessible files. Preserves
relative path to destination when adding multiple files from a directory.

**Arguments**:

* `src` - `str` | Iterable\[str] | Path | Iterable\[Path]
  The path(s) to the local file(s) to be staged.
* `dst` - `str`
  The path in the remote repo where the file(s) will be added.
* `raise_on_failure` - `bool`
  Whether to raise an exception if any files fail to upload.
  By default, raises an exception. Set to `False` to return
  a list of failed file paths instead.

**Returns**:

A list of `PyErrorFileInfo` for files that failed to upload.
An empty list means all files were uploaded successfully.
Each entry has `.hash`, `.path`, and `.error` attributes.

**Raises**:

ValueError if the provided input is not a valid filepath, an invalid
directory, or it points to an empty directory, or is a collection
of empty directories.

## add\_files

```python theme={null}
def add_files(base_dir: str | Path,
              paths: Iterable[str] | Iterable[Path],
              raise_on_failure: bool = True) -> list[PyErrorFileInfo]
```

A workspace add that preserves relative paths of files that share a common base.

Unlike `add`, which places files into a flat destination directory,
this method uses each file's path relative to the supplied base directory as
its staging path on the server.

The `base_dir` serves as a stand-in for the root of the remote repository. The key
use of `add_files` is to import a large file tree into an existing repository.

For example, a file at
`repo/data/images/cat.jpg` will be staged as `data/images/cat.jpg`.

**Arguments**:

* `base_dir` - `str` | `Path`
  The base directory: all added files share this as an ancestor.
* `paths` - `Iterable[str]` | `Iterable[Path]`
  The file paths to add. Can be absolute or relative to the
  base directory. Each path must point to an existing file.
* `raise_on_failure` - `bool`
  Whether to raise an exception if any files fail to upload.
  By default, raises an exception. Set to `False` to return
  a list of failed file paths instead.

**Returns**:

A list of `PyErrorFileInfo` for files that failed to upload.
An empty list means all files were uploaded successfully.
Each entry has `.hash`, `.path`, and `.error` attributes.

**Raises**:

* `PyOxenError` - If no valid file paths are provided.

## add\_bytes

```python theme={null}
def add_bytes(src: str, buf: bytes, dst: str = "") -> None
```

Adds from a memory buffer to the workspace

**Arguments**:

* `src` - `str`
  The relative path to be used as the entry's name in the workspace
* `buf` - `bytes`
  The memory buffer to be read from for this entry
* `dst` - `str`
  The path in the remote repo where the file will be added

## rm

```python theme={null}
def rm(path: str) -> None
```

Unstage a file that was previously added to the workspace.
Despite the name, this does not stage a deletion of a file in
the base repo. Prefer `unstage`, which does the same thing
through the non-deprecated endpoint.

**Arguments**:

* `path` - `str`
  The path to the staged file to unstage

## unstage

```python theme={null}
def unstage(path: str) -> None
```

Unstage a file that was previously added to the workspace,
without touching the base repo.

**Arguments**:

* `path` - `str`
  The path to the staged file to unstage

## commit

```python theme={null}
def commit(message: str, branch_name: Optional[str] = None) -> PyCommit
```

Commit the workspace to a branch

**Arguments**:

* `message` - `str`
  The message to commit with
* `branch_name` - `Optional[str]`
  The name of the branch to commit to. If left empty, will commit to the branch
  the workspace was created from.

## delete

```python theme={null}
def delete() -> None
```

Delete the workspace


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.