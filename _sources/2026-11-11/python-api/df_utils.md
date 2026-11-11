---
title: "Df utils"
source: https://docs.oxen.ai/python-api/df_utils
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Df utils

# oxen.df\_utils

The `df_utils` module provides a consistent interface for loading data frames and saving them to disk.

Supported types: csv, parquet, json, jsonl, arrow

Example usage:

```python theme={null}
import os
from oxen import df_utils

# load a data frame
df = df_utils.load("path/to/data.csv")

# save a data frame
df_utils.save(df, "path/to/save.csv")
```

## load

```python theme={null}
def load(path: os.PathLike)
```

Reads a file into a data frame. The file format is inferred from the file extension.

Supported types: csv, parquet, json, jsonl, arrow

**Arguments**:

* `path` - `os.PathLike`
  The path to the file to read.

## save

```python theme={null}
def save(data_frame: DataFrame, path: os.PathLike)
```

Saves a data frame to a file. The file format is inferred from the file extension.

**Arguments**:

* `data_frame` - `DataFrame`
  The polars data frame to save.
* `path` - `os.PathLike`
  The path to save the data frame to.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.