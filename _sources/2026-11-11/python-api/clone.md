---
title: "Clone"
source: https://docs.oxen.ai/python-api/clone
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Clone

# oxen.clone

## clone

```python theme={null}
def clone(repo_id: str,
          path: Optional[str] = None,
          host: str = "hub.oxen.ai",
          branch: str = "main",
          scheme: str = "https",
          filters: Optional[str | list[str]] = None,
          all=False)
```

Clone a repository

**Arguments**:

* `repo_id` - `str`
  Name of the repository in the format 'namespace/repo\_name'.
  For example 'ox/chatbot'
* `path` - `Optional[str]`
  The path to clone the repo to. Defaults to the name of the repository.
* `host` - `str`
  The host to connect to. Defaults to 'hub.oxen.ai'
* `branch` - `str`
  The branch name id to clone. Defaults to 'main'
* `scheme` - `str`
  The scheme to use. Defaults to 'https'
* `all` - `bool`
  Whether to clone the full commit history or not. Default: False
* `filters` - `str | list[str] | None`
  Filter down the set of directories you want to clone. Useful if
  you have a large repository and only want to make changes to a
  specific subset of files. Default: None

**Returns**:

[Repo](https://docs.oxen.ai/python-api/repo.md)
A Repo object that can be used to interact with the cloned repo.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.