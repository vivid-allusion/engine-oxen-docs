---
title: "Introduction"
source: https://docs.oxen.ai/python-api/index
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Introduction

> Learn how to get started with the oxenai Python package.

## Install

```bash theme={null}
pip install oxenai
```

## Clone Repository

Clone a repository from the [Oxen Hub](https://oxen.ai) or your own [oxen-server](https://docs.oxen.ai/getting-started/oxen-server.md). Detailed documentation for the [clone](https://docs.oxen.ai/python-api/clone.md) method can be found in the [Module Reference](#module-reference) below.

```python theme={null}
import oxen
oxen.clone("ox/SpanishToEnglish")
```

This will create a directory called `SpanishToEnglish` in your current working directory and download the latest version of the repository.

If you have not setup your API Key locally, you will get an error cloning data. View our [Authentication & Authorization documentation](https://docs.oxen.ai/getting-started/auth) to learn more.

## Initialize Local Repository

If you are creating a new repository from scratch, you can initialize it with the [init](https://docs.oxen.ai/python-api/init.md) method.

We will be using a fictional repository called `CatsVsDogs` for this example.

```python theme={null}
import oxen
import os

# Create an empty directory named CatsVsDogs
directory = "CatsVsDogs"
os.makedirs(directory)

# Initialize the Oxen Repository
repo = oxen.init(directory)
```

This will create a `.oxen` directory to keep track of changes as you make them.

## Load Existing Repository

Use the [repo](https://docs.oxen.ai/python-api/repo.md) class to interact with a repository that has already been initialized.

```python theme={null}
from oxen import Repo

# Load the repository from the CatsVsDogs directory
repo = Repo("CatsVsDogs")
# Check the status of the repository
print(repo.status())
```

## Add Files

Now let's create a README.md file and [add](https://docs.oxen.ai/python-api/repo.md#add) it to the local staging area. This will not commit the changes to the repository, but it will prepare them to be committed.

```python theme={null}
# ... continue from previous example

# Create a README.md file
filename = os.path.join(repo.path, "README.md")
with open(filename, "w") as f:
    f.write("# Cats vs. Dogs\n\nWhich is it? We will be using machine learning to find out!")

# Add the README.md file to the staging area
repo.add(filename)

# Confirm that the file has been staged
print(repo.status())
```

## Commit Changes

Now that we have added the README.md file to the staging area, we can commit the changes to the repository.

```python theme={null}
# ... continue from previous example

# Commit the changes to the repository
repo.commit("Adding README.md")
```

## Diff Changes

Oxen.ai has powerful diff tools built in that allow you to see the changes to files between commits, branches, and more.

```python theme={null}
result = oxen.diff("README.md")
print(result.get())
```

To learn more about diffs checkout the [diff](https://docs.oxen.ai/concepts/diffs.md) documentation or the [Python API Documentation](https://docs.oxen.ai/python-api/diff/diff.md).

## Push To Remote

It's one thing to version your data locally, but where the real power comes in is when you can share your data with others. Oxen repositories can be pushed to a remote repository hosted on [Oxen Hub](https://oxen.ai) or your own [oxen-server](https://docs.oxen.ai/getting-started/oxen-server.md).

There are a few steps when pushing to a remote for the first time.

1. [Create Remote](https://docs.oxen.ai/python-api/remote_repo.md#create_repo)
2. [Point Local to Remote](https://docs.oxen.ai/python-api/repo.md#set_remote)
3. [Push Changes](https://docs.oxen.ai/python-api/repo.md#push)

### Create Remote

Before you can push to a remote repository, you must create it. This can be done with the [create\_repo](https://docs.oxen.ai/python-api/remote_repo.md#create_repo) method.

```python theme={null}
from oxen.remote_repo import create_repo

# Create a remote repository
remote_name = "MyNamespace/CatsVsDogs"
remote_repo = create_repo(remote_name)
```

### Point Local to Remote

Now that we have created the remote repository, we need to point our local repository to sync to it. This can be done with the [set\_remote](https://docs.oxen.ai/python-api/repo.md#set_remote) method.

```python theme={null}
from oxen import Repo

# Load the local repository
repo = Repo("CatsVsDogs")

# Point the local repository to the remote
repo.set_remote("origin", remote_repo.url())
```

### Push Changes

Now that we have created the remote repository and pointed our local repository to it, we can [push](https://docs.oxen.ai/python-api/repo.md#push) our changes to the remote repository.

```python theme={null}
# Push the changes to the remote repository
repo.push()
```

### Full Push Example

The end to end workflow from scratch looks like this:

```python theme={null}
from oxen import Repo
from oxen.remote_repo import create_repo
from oxen.auth import config_auth

# 0. Load the local repository
repo = Repo("CatsVsDogs")

# 1. Configure Authentication
config_auth("YOUR_AUTH_TOKEN")

# 2. Create a remote repository
remote_name = "MyNamespace/CatsVsDogs"
repo = create_repo(remote_name)

# 3. Point the local repository to the remote
repo.set_remote("origin", repo.url)

# 4. Push the changes to the remote repository
repo.push()
```

## Pull Data

Now that we have pushed our changes to the remote repository, we can [pull](https://docs.oxen.ai/python-api/repo.md#pull) them down to another machine.

```python theme={null}
import oxen
import os

repo_path = "CatsVsDogs"
if os.path.exists(repo_path):
  # if you already have a local copy of the repository, you can load it
  repo = oxen.Repo(repo_path)
else:
  # if you don't have a local copy of the repository, you can clone it
  repo = oxen.clone("ox/CatsVsDogs")

# Pull the latest changes from the remote repository
repo.pull()
```

## OxenFS (fsspec Integration)

OxenFS allows you to conveniently read and write files through a Pythonic file interface.

```python theme={null}
import oxen

fs = oxen.OxenFS("openai", "gsm8k")
with fs.open("gsm8k_test.parquet") as f:
    content = f.read()
```

It also integrates directly with third-party libraries like Pandas like this:

```python theme={null}
df = pd.read_parquet("oxen://openai:gsm8k@main/gsm8k_test.parquet")
```

See the full documentation for [OxenFS](https://docs.oxen.ai/python-api/oxen_fs.md).

## Branching

Branching is a powerful feature of Oxen that allows you to create a named version of your data without affecting the original version. This is useful when you want to experiment with your changes affecting the original version.

### Create Branch

To create a new branch, use the [Repo.checkout](https://docs.oxen.ai/python-api/repo.md#checkout) method.

```python theme={null}
from oxen import Repo

repo = Repo("CatsVsDogs")
repo.checkout("add-dogs", create=True)
```

This both creates the branch and checks it out (the command line equivalent of `oxen checkout -b add-dogs`).

### List Branches

To list all of the branches in a repository, use the [Repo.branches](https://docs.oxen.ai/python-api/repo.md#branches) method.

```python theme={null}
from oxen import Repo

repo = Repo("CatsVsDogs")
print(repo.branches())
```

Output:

```
[Branch(name=add-dogs, commit_id=3168391af834ac18), Branch(name=main, commit_id=3168391af834ac18)]
```

As you can see there should be a `main` branch and a `add-dogs` branch, each tied to a commit id. The commit ids will be the same at this point, because the branches have not diverged in content.

## Module Reference

Detailed documentation for each Python module.

### Clone

[clone](https://docs.oxen.ai/python-api/clone.md) is used to download a repository to your local machine.

### Initialize Repository

[init](https://docs.oxen.ai/python-api/init.md) is used to initialize a new local repository.

### Configure User

[user](https://docs.oxen.ai/python-api/user) is used to configure the user for a local repository.

### Setup Auth

[auth](https://docs.oxen.ai/python-api/auth) is used to configure authentication for remote repositories.

### Repositories

The [Repositories](https://docs.oxen.ai/python-api/repositories.md) page has an overview of the two repository classes, and detailed documentation for each class can be found on their respective pages below.

* [Repo](https://docs.oxen.ai/python-api/repo.md) is used to interact with data locally.
* [RemoteRepo](https://docs.oxen.ai/python-api/remote_repo.md) is used to interact with a remote data without downloading all of it locally.

### OxenFS

[OxenFS](https://docs.oxen.ai/python-api/oxen_fs.md) is an [fsspec](https://filesystem-spec.readthedocs.io/en/latest/) backend that allows you to read and write files in your Oxen repo through a Pythonic file interface. It also provides a convenient integration point with third-party libraries.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.