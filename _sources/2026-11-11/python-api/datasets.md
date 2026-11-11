---
title: "Datasets"
source: https://docs.oxen.ai/python-api/datasets
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Datasets

# oxen.datasets

## load\_dataset

```python theme={null}
def load_dataset(repo_id: str,
                 path: str,
                 fmt: str = "hugging_face",
                 revision=None)
```

Load a dataset from an Oxen repository into memory using the HuggingFace datasets library.

**Arguments**:

* `repo_id` - `str`
  The namespace/repo\_name of the oxen repository to load the dataset from
* `path` - `str` | Sequence\[str]
  The path to the dataset we want to load
* `fmt` - `str`
  The format of the data files. Currently only "hugging\_face" is supported.
* `revision` - `str` | None
  The commit id or branch name of the version of the data to download

**Example**:

```python theme={null}
from oxen.datasets import load_dataset
dataset = load_dataset("datasets/gsm8k", "train.jsonl")
# use datasets functions as you normally would
dataset.shuffle()[:10]
```

## download

```python theme={null}
def download(repo_id: str,
             path: str,
             revision=None,
             dst=None,
             host="hub.oxen.ai",
             scheme="https")
```

Download files or directories from a remote Oxen repository.

**Arguments**:

* `repo_id` - `str`
  The namespace/repo\_name of the oxen repository to load the dataset from
* `path` - `str`
  The path to the data files
* `revision` - `str | None`
  The commit id or branch name of the version of the data to download
* `dst` - `str | None`
  The path to download the data to.
* `host` - `str`
  The host to download the data from.
* `scheme` - `str`
  The scheme to download the data with. (default: "https")

## upload

```python theme={null}
def upload(repo_id: str,
           path: str,
           message: str,
           branch: Optional[str] = None,
           dst: str = "")
```

Upload files or directories to a remote Oxen repository.

**Arguments**:

* `repo_id` - `str`
  The namespace/repo\_name of the oxen repository to upload the dataset to
* `path` - `str`
  The path to the data files
* `message` - `str`
  The commit message to use when uploading the data
* `branch` - `str | None`
  The branch to upload the data to. If None, the `main` branch is used.
* `dst` - `str | None`
  The directory to upload the data to.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.