---
title: "Remote repo"
source: https://docs.oxen.ai/python-api/remote_repo
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Remote repo

# oxen.remote\_repo

## get\_repo

```python theme={null}
def get_repo(name: str, host: str = "hub.oxen.ai", scheme: str = "https")
```

Get a RemoteRepo object for the specified name. For example 'ox/CatDogBBox'.

**Arguments**:

* `name` - `str`
  Name of the repository in the format 'namespace/repo\_name'.
* `host` - `str`
  The host to connect to. Defaults to 'hub.oxen.ai'

**Returns**:

[RemoteRepo](https://docs.oxen.ai/python-api/remote_repo.md)

## create\_repo

```python theme={null}
def create_repo(name: str,
                description="",
                is_public: bool = True,
                host: str = "hub.oxen.ai",
                scheme: str = "https",
                files: List[Tuple[str, str]] = [])
```

Create a new repository on the remote server.

**Arguments**:

* `name` - `str`
  Name of the repository in the format 'namespace/repo\_name'.
* `description` - `str`
  Description of the repository.
  Only applicable to [OxenHub](https://oxen.ai).
* `is_public` - `bool`
  Whether the repository is public or private.
  Only applicable to [OxenHub](https://oxen.ai).
* `host` - `str`
  The host to connect to. Defaults to 'hub.oxen.ai'
* `scheme` - `str`
  The scheme to use for the remote url. Default: 'https'
* `files` - `List[Tuple[str, str]]`
  A list of tuples containing the path to the file and the contents
  of the file that you would like to seed the repository with.

**Returns**:

[RemoteRepo](https://docs.oxen.ai/python-api/remote_repo.md)

## RemoteRepo Objects

```python theme={null}
class RemoteRepo()
```

The RemoteRepo class allows you to interact with an Oxen repository
without downloading the data locally.

## Examples

### Add & Commit Files

Adding and committing a file to a remote workspace.

```python theme={null}
from oxen import RemoteRepo

repo = RemoteRepo("ox/CatDogBBox")
repo.add("/path/to/image.png")
status = repo.status()
print(status.added_files())
repo.commit("Adding my image to the remote workspace.")
```

### Downloading Specific Files

Grab a specific file revision and load it into pandas.

```python theme={null}
from oxen import RemoteRepo
import pandas as pd

# Connect to the remote repo
repo = RemoteRepo("ox/CatDogBBox")
# Specify the version of the file you want to download
branch = repo.get_branch("my-pets")
# Download takes a file or directory a commit id
repo.download("annotations", revision=branch.commit_id)
# Once you have the data locally, use whatever library you want to explore the data
df = pd.read_csv("annotations/train.csv")
print(df.head())
```

## \_\_init\_\_

```python theme={null}
def __init__(repo_id: str,
             host: str = "hub.oxen.ai",
             revision: str = "main",
             scheme: str = "https")
```

Create a new RemoteRepo object to interact with.

**Arguments**:

* `repo_id` - `str`
  Name of the repository in the format 'namespace/repo\_name'.
  For example 'ox/chatbot'
* `host` - `str`
  The host to connect to. Defaults to 'hub.oxen.ai'
* `revision` - `str`
  The branch name or commit id to checkout. Defaults to 'main'
* `scheme` - `str`
  The scheme to use for the remote url. Default: 'https'

## create

```python theme={null}
def create(empty: bool = False, is_public: bool = False)
```

Will create the repo on the remote server.

**Arguments**:

* `empty` - `bool`
  Whether to create an empty repo or not. Default: False
* `is_public` - `bool`
  Whether the repository is public or private. Default: False

## exists

```python theme={null}
def exists() -> bool
```

Checks if this remote repo exists on the server.

## delete

```python theme={null}
def delete()
```

Delete this remote repo from the server.

## checkout

```python theme={null}
def checkout(revision: str, create=False)
```

Switches the remote repo to the specified revision.

**Arguments**:

* `revision` - `str`
  The name of the branch or commit id to checkout.
* `create` - `bool`
  Whether to create a new branch if it doesn't exist. Default: False

## ls

```python theme={null}
def ls(directory: Optional[str] = None,
       page_num: int = 1,
       page_size: int = 100)
```

Lists the contents of a directory in the remote repo.

**Arguments**:

* `directory` - `str`
  The directory to list. If None, will list the root directory.
* `page_num` - `int`
  The page number to return. Default: 1
* `page_size` - `int`
  The number of items to return per page. Default: 100

## scan

```python theme={null}
def scan(directory: Optional[str] = None, page_size: int = 100)
```

Generator over the contents of a directory in the remote repo

**Arguments**:

* `directory` - `str`
  The directory to list. If None, will list the root directory
* `page_size` - `int`
  The number of items to return per page. Default: 100

## download

```python theme={null}
def download(src: str,
             dst: Optional[str] = None,
             revision: Optional[str] = None)
```

Download a file or directory from the remote repo.

**Arguments**:

* `src` - `str`
  The path to the remote file
* `dst` - `str | None`
  The path to the local file. If None, will download to
  the same path as `src`
* `revision` - `str | None`
  The branch or commit id to download. Defaults to `self.revision`

## download\_zip

```python theme={null}
def download_zip(src: str,
                 dst: Optional[str] = None,
                 revision: Optional[str] = None)
```

Download the contents of a directory as a zip file

**Arguments**:

* `src` - `str`
  The path to the remote dir to download files from. This must be a directory
* `dst` - `str | None`
  The path to the local file. If None, will download to `{src}.zip`
* `revision` - `str | None`
  The branch or commit id to download. Defaults to `self.revision`

## get\_file

```python theme={null}
def get_file(src: str, revision: Optional[str] = None)
```

Get a file from the remote repo.

**Arguments**:

* `src` - `str`
  The path to the remote file
* `revision` - `str | None`
  The branch or commit id to download. Defaults to `self.revision`

## create\_workspace

```python theme={null}
def create_workspace(branch: Optional[str] = None,
                     workspace_name: Optional[str] = None)
```

Create a new workspace in the remote repo. If the workspace already exists, it will just be returned.

**Arguments**:

* `branch` - `str | None`
  The branch to create the workspace on. Defaults to `self.revision`
* `workspace_name` - `str | None`
  The named workspace to use when adding the file. If None, will create a temporary workspace

**Returns**:

[Workspace](https://docs.oxen.ai/python-api/workspace.md)

## delete\_workspace

```python theme={null}
def delete_workspace()
```

Delete the current workspace in the remote repo.

## add

```python theme={null}
def add(src: str,
        dst: Optional[str] = "",
        branch: Optional[str] = None,
        workspace_name: Optional[str] = None)
```

Stage a file to a workspace in the remote repo.

**Arguments**:

* `src` - `str`
  The path to the local file to upload
* `dst` - `str | None`
  The directory to upload the file to. If None, will upload to the root directory.
* `branch` - `str | None`
  The branch to upload the file to. Defaults to `self.revision`
* `workspace_name` - `str | None`
  The named workspace to use when adding the file. If None, will create a temporary workspace

**Returns**:

[Workspace](https://docs.oxen.ai/python-api/workspace.md)

## status

```python theme={null}
def status()
```

Get the status of the workspace.

## commit

```python theme={null}
def commit(message: str, branch: Optional[str] = None)
```

Commit the workspace to the remote repo.

**Arguments**:

* `message` - `str`
  The message to commit with
* `branch` - `str | None`
  The branch to commit to. Defaults to the branch the workspace was created on.

## delete\_file

```python theme={null}
def delete_file(path: str,
                commit_message: Optional[str] = None,
                branch: Optional[str] = None)
```

Delete from the remote repo. This can be used with a committed file or dir

**Arguments**:

* `path` - `str`
  The path to the remote file to remove
* `commit_message` - `str` | None
  The message to commit with. Defaults to "Removed '{path}'"
* `branch` - `str | None`
  The branch to remove the file from. Defaults to `self.revision`

## upload

```python theme={null}
def upload(src: str,
           commit_message: str,
           file_name: Optional[str] = None,
           dst_dir: Optional[str] = "",
           branch: Optional[str] = None)
```

Upload a file to the remote repo.

**Arguments**:

* `src` - `str`
  The path to the local file to upload
* `commit_message` - `str`
  The message to commit with. Defaults to "Uploaded '{src}'"
* `file_name` - `str | None`
  The name of the file to upload. If None, will use the name of the file in `src`
* `dst_dir` - `str | None`
  The directory to upload the file to. If None, will upload to the root directory.
* `branch` - `str | None`
  The branch to upload the file to. Defaults to `self.revision`

## metadata

```python theme={null}
def metadata(path: str)
```

Get the metadata for a file in the remote repo.

## file\_exists

```python theme={null}
def file_exists(path: str, revision: Optional[str] = None)
```

Check if a file exists in the remote repo.

**Arguments**:

* `path` - `str`
  The path to the file to check
* `revision` - `str`
  The revision to check against, defaults to `self.revision`

## file\_has\_changes

```python theme={null}
def file_has_changes(local_path: str,
                     remote_path: str = None,
                     revision: str = None)
```

Check if a local file has changed compared to a remote revision

**Arguments**:

* `local_path` - `str`
  The local path to the file to check
* `remote_path` - `str`
  The remote path to the file to check, will default to `local_path` if not provided
* `revision` - `str`
  The revision to check against, defaults to `self.revision`

## log

```python theme={null}
def log(revision: Optional[str] = None,
        path: Optional[str] = None,
        page_num: int = 1,
        page_size: int = 10)
```

Get the commit history for a remote repo

**Arguments**:

* `revision` - `str | None`
  The revision to get the commit history for. Defaults to `self.revision`
* `path` - `str | None`
  The path to the file to get the commit history for. Defaults to
  None, which will return the commit history for the entire repo
* `page_num` - `int`
  The page number to return. Defaults to 1
* `page_size` - `int`
  The number of items to return per page. Defaults to 10

**Returns**:

One page of commits, newest first. `has_more` says whether a later page exists.
`pagination` carries the totals for a revision's history, and is `None` for a path's
history, which is not counted.

## branch\_exists

```python theme={null}
def branch_exists(name: str) -> bool
```

Check if a branch exists in the remote repo.

**Arguments**:

* `name` - `str`
  The name of the branch to check

## branch

```python theme={null}
def branch()
```

Get the current branch for a remote repo

## branches

```python theme={null}
def branches()
```

List all branches for a remote repo

## list\_workspaces

```python theme={null}
def list_workspaces()
```

List all workspaces for a remote repo

## get\_branch

```python theme={null}
def get_branch(branch: str)
```

Return a branch by name on this repo, if exists

**Arguments**:

* `branch` - `str`
  The name of the branch to return

## create\_branch

```python theme={null}
def create_branch(branch: str)
```

Return a branch by name on this repo,
creating it from the currently checked out branch if it doesn't exist

**Arguments**:

* `branch` - `str`
  The name to assign to the created branch

## delete\_branch

```python theme={null}
def delete_branch(branch: str)
```

Delete a branch from the remote repo.

**Arguments**:

* `branch` - `str`
  The name of the branch to delete

## create\_checkout\_branch

```python theme={null}
def create_checkout_branch(branch: str)
```

Create a new branch from the currently checked out branch,
and switch to it

**Arguments**:

* `branch` - `str`
  The name to assign to the created branch

## merge

```python theme={null}
def merge(base_branch: str, head_branch: str)
```

Merge the head branch into the base branch on the remote repo.

**Arguments**:

* `base_branch` - `str`
  The base branch to merge into
* `head_branch` - `str`
  The head branch to merge

## mergeable

```python theme={null}
def mergeable(base_branch: str, head_branch: str)
```

Check if a branch is mergeable into another branch.

**Arguments**:

* `base_branch` - str
  The target branch to merge into
* `head_branch` - str
  The source branch to merge from

## diff

```python theme={null}
def diff(base: str | PyCommit, head: str | PyCommit, path: str)
```

Get the diff between two refs on the remote repo.

**Arguments**:

* `base` - `str`
  The base ref to diff (branch or commit)
* `head` - `str`
  The head ref to diff (branch or commit)
* `path` - `str`
  The path to the file to diff

## namespace

```python theme={null}
@property
def namespace() -> str
```

The namespace for the repo.

## name

```python theme={null}
@property
def name() -> str
```

The name of the repo.

## identifier

```python theme={null}
@property
def identifier()
```

The namespace/name of the repo.

## url

```python theme={null}
@property
def url() -> str
```

The remote url for the repo.

## revision

```python theme={null}
@property
def revision() -> str
```

The branch or commit id for the repo

## repo\_uuid

```python theme={null}
@property
def repo_uuid() -> Optional[str]
```

The identifier the server addresses this repo by, or None from a server
that reports no identity. Raises if the repo does not exist yet.

## storage\_backend

```python theme={null}
@property
def storage_backend() -> str
```

Where the server keeps this repo's version files, "local" or "s3".
Raises if the repo does not exist yet.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.