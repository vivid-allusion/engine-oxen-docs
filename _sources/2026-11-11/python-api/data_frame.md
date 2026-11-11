---
title: "Data frame"
source: https://docs.oxen.ai/python-api/data_frame
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Data frame

# oxen.data\_frame

## DataFrame Objects

```python theme={null}
class DataFrame()
```

The DataFrame class allows you to perform CRUD operations on a remote data frame.

If you pass in a [Workspace](https://docs.oxen.ai/concepts/workspaces) or a [RemoteRepo](https://docs.oxen.ai/concepts/remote-repos) the data is indexed into DuckDB on an oxen-server without downloading the data locally.

## Examples

### CRUD Operations

Index a data frame in a workspace.

```python theme={null}
from oxen import DataFrame

# Connect to and index the data frame
# Note: This must be an existing file committed to the repo
#       indexing may take a while for large files
data_frame = DataFrame("datasets/SpamOrHam", "data.tsv")

# Add a row
row_id = data_frame.insert_row({"category": "spam", "message": "Hello, do I have an offer for you!"})

# Get a row by id
row = data_frame.get_row_by_id(row_id)
print(row)

# Update a row
row = data_frame.update_row(row_id, {"category": "ham"})
print(row)

# Delete a row
data_frame.delete_row(row_id)

# Commit the changes
data_frame.commit("Updating data.csv")
```

## \_\_init\_\_

```python theme={null}
def __init__(remote: Union[str, RemoteRepo, Workspace],
             path: str,
             host: str = "hub.oxen.ai",
             branch: Optional[str] = None,
             scheme: str = "https",
             workspace_name: Optional[str] = None)
```

Initialize the DataFrame class. Will index the data frame
into duckdb on init.

Will throw an error if the data frame does not exist.

**Arguments**:

* `remote` - `str`, `RemoteRepo`, or `Workspace`
  The workspace or remote repo the data frame is in.
* `path` - `str`
  The path of the data frame file in the repository.
* `host` - `str`
  The host of the oxen-server. Defaults to "hub.oxen.ai".
* `branch` - `Optional[str]`
  The branch of the remote repo. Defaults to None.
* `scheme` - `str`
  The scheme of the remote repo. Defaults to "https".

## workspace\_url

```python theme={null}
def workspace_url(host: str = "oxen.ai", scheme: str = "https") -> str
```

Get the url of the data frame.

## size

```python theme={null}
def size() -> tuple[int, int]
```

Get the size of the data frame. Returns a tuple of (rows, columns)

## page\_size

```python theme={null}
def page_size() -> int
```

Get the page size of the data frame for pagination in list() command.

**Returns**:

The page size of the data frame.

## total\_pages

```python theme={null}
def total_pages() -> int
```

Get the total number of pages in the data frame for pagination in list() command.

**Returns**:

The total number of pages in the data frame.

## list\_page

```python theme={null}
def list_page(page_num: int = 1) -> List[dict]
```

List the rows within the data frame.

**Arguments**:

* `page_num` - `int`
  The page number of the data frame to list. We default to page size of 100 for now.

**Returns**:

A list of rows from the data frame.

## insert\_row

```python theme={null}
def insert_row(data: dict, workspace: Optional[Workspace] = None)
```

Insert a single row of data into the data frame.

**Arguments**:

* `data` - `dict`
  A dictionary representing a single row of data.
  The keys must match a subset of the columns in the data frame.
  If a column is not present in the dictionary,
  it will be set to an empty value.

**Returns**:

The id of the row that was inserted.

## get\_columns

```python theme={null}
def get_columns() -> List[PyColumn]
```

Get the columns of the data frame.

## add\_column

```python theme={null}
def add_column(name: str, data_type: str)
```

Add a column to the data frame.

## where\_sql\_from\_dict

```python theme={null}
def where_sql_from_dict(attributes: dict, operator: str = "AND") -> str
```

Generate the SQL from the attributes.

## select\_sql\_from\_dict

```python theme={null}
def select_sql_from_dict(attributes: dict,
                         columns: Optional[List[str]] = None) -> str
```

Generate the SQL from the attributes.

## get\_embeddings

```python theme={null}
def get_embeddings(attributes: dict, column: str = "embedding") -> List[float]
```

Get the embedding from the data frame.

## is\_nearest\_neighbors\_enabled

```python theme={null}
def is_nearest_neighbors_enabled(column="embedding")
```

Check if the embeddings column is indexed in the data frame.

## enable\_nearest\_neighbors

```python theme={null}
def enable_nearest_neighbors(column: str = "embedding")
```

Index the embeddings in the data frame.

## query

```python theme={null}
def query(sql: Optional[str] = None,
          find_embedding_where: Optional[dict] = None,
          embedding: Optional[list[float]] = None,
          sort_by_similarity_to: Optional[str] = None,
          page_num: int = 1,
          page_size: int = 10)
```

Sort the data frame by the embedding.

## nearest\_neighbors\_search

```python theme={null}
def nearest_neighbors_search(find_embedding_where: dict,
                             sort_by_similarity_to: str = "embedding")
```

Get the nearest neighbors to the embedding.

## get\_by

```python theme={null}
def get_by(attributes: dict)
```

Get a single row of data by attributes.

## get\_row

```python theme={null}
def get_row(idx: int)
```

Get a single row of data by index.

**Arguments**:

* `idx` - `int`
  The index of the row to get.

**Returns**:

A dictionary representing the row.

## get\_row\_by\_id

```python theme={null}
def get_row_by_id(id: str)
```

Get a single row of data by id.

**Arguments**:

* `id` - `str`
  The id of the row to get.

**Returns**:

A dictionary representing the row.

## update\_row

```python theme={null}
def update_row(id: str, data: dict)
```

Update a single row of data by id.

**Arguments**:

* `id` - `str`
  The id of the row to update.
* `data` - `dict`
  A dictionary representing a single row of data.
  The keys must match a subset of the columns in the data frame.
  If a column is not present in the dictionary,
  it will be set to an empty value.

**Returns**:

The updated row as a dictionary.

## delete\_row

```python theme={null}
def delete_row(id: str)
```

Delete a single row of data by id.

**Arguments**:

* `id` - `str`
  The id of the row to delete.

## restore

```python theme={null}
def restore()
```

Discard all uncommitted edits to the data frame by re-indexing it
from the committed version

## commit

```python theme={null}
def commit(message: str, branch: Optional[str] = None)
```

Commit the current changes to the data frame.

**Arguments**:

* `message` - `str`
  The message to commit the changes.
* `branch` - `str`
  The branch to commit the changes to. Defaults to the current branch.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.