---
title: "Oxen fs"
source: https://docs.oxen.ai/python-api/oxen_fs
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Oxen fs

# oxen.oxen\_fs

## OxenFS Objects

```python theme={null}
class OxenFS(fsspec.AbstractFileSystem)
```

OxenFS is a filesystem interface for Oxen repositories that implements the
[fsspec](https://filesystem-spec.readthedocs.io/en/latest/) protocol. This
allows you to interact with Oxen repositories using familiar filesystem
operations and integrate with other compatible libraries like Pandas.

## Basic Usage

### Creating a Filesystem Instance

```python theme={null}
import oxen

# For Oxen Hub repositories
fs = oxen.OxenFS("ox", "Flowers")

# For local oxen-server
fs = oxen.OxenFS("ox", "test-repo", host="localhost:3000", scheme="http")
```

### Reading Files

```python theme={null}
with fs.open("data/train.csv") as f:
    content = f.read()
```

### Writing Files

You must have write access to the repository to write files. See:
[https://docs.oxen.ai/getting-started/auth#public-vs-private-repositories](https://docs.oxen.ai/getting-started/auth#public-vs-private-repositories)

OxenFS will automatically commit the file to the repository when the
context is exited (or the file is closed some other way). New
directories are automatically created as needed.

```python theme={null}
# Write with custom commit message
with fs.open("data/test.txt", mode="wb", commit_message="Added test.txt") as f:
    f.write("Hello, world!")

# You can also set/update the commit message inside the context
with fs.open("data/test.txt", mode="wb") as f:
    f.commit_message = "Updated test.txt"
    f.write("Hello, world again!")
```

## Writing file objects

If you're integrating Oxen in a situation where you already have a file object,
you can save it to your repo by using `shutil.copyfileobj` like this:

```python theme={null}
import shutil

file_object_from_somewhere = open("data.csv")

with fs.open("train/data.csv", mode="wb") as output_file:
    output_file.commit_message = "Copy from a file object"
    shutil.copyfileobj(file_object_from_somewhere, output_file)
```

## Integration with Third Party Libraries (Pandas, etc.)

OxenFS works seamlessly with Pandas and other fsspec-compatible libraries using
the URL format: `oxen://namespace:repo@revision/path/to/file`

### Reading Data

These will work with Pandas `{to,from}_{csv,parquet,json,etc.}` functions.

```python theme={null}
import pandas as pd

# Read parquet directly from Oxen repository
df = pd.read_parquet("oxen://openai:gsm8k@main/gsm8k_test.parquet")
```

### Writing Data

```python theme={null}
# Write DataFrame directly to Oxen repository
df.to_csv("oxen://ox:my-repo@main/data/test.csv", index=False)
```

## Notes

* Only binary read ("rb") and write ("wb") modes are currently supported
  * But writing will automatically encode strings to bytes
* Does not yet support streaming files. All operations use temporary local files.

## \_\_init\_\_

```python theme={null}
def __init__(namespace: str,
             repo: str,
             host: str = "hub.oxen.ai",
             revision: str = "main",
             scheme: str = "https",
             **kwargs)
```

Initialize the OxenFS instance.

**Arguments**:

* `namespace` - `str`
  The namespace of the repository.
* `repo` - `str`
  The name of the repository.
* `host` - `str`
  The host to connect to. Defaults to 'hub.oxen.ai'
* `revision` - `str`
  The branch name or commit id to checkout. Defaults to 'main'
* `scheme` - `str`
  The scheme to use for the remote url. Default: 'https'

## ls

```python theme={null}
def ls(path: str = "", detail: bool = False)
```

List the contents of a directory.

**Arguments**:

* `path` - `str`
  The path to list the contents of.
* `detail` - `bool`
  If True, return a list of dictionaries with detailed metadata.
  Otherwise, return a list of strings with the filenames.

## OxenFSFileWriter Objects

```python theme={null}
class OxenFSFileWriter()
```

A file writer for the OxenFS backend.

This is normally called through `OxenFS.open()` or `fsspec.open()`.

## write

```python theme={null}
def write(data: str | bytes)
```

Write string or binary data to the file.

## flush

```python theme={null}
def flush()
```

Flush the file to disk.

## tell

```python theme={null}
def tell()
```

Return the current position of the file.

## seek

```python theme={null}
def seek(offset: int, whence: int = os.SEEK_SET)
```

Seek to a specific position in the file.

## commit

```python theme={null}
def commit(commit_message: Optional[str] = None)
```

Commit the file to the remote repo.

## close

```python theme={null}
def close()
```

Close the file writer. This will commit the file to the remote repo.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.