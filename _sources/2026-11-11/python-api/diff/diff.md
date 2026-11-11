---
title: "Diff"
source: https://docs.oxen.ai/python-api/diff/diff
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Diff

# oxen.diff/diff

Oxen can be used to compare data frames and return a tabular diff.

There is more information about the diff in the
[Diff Getting Started Documentation](https://docs.oxen.ai/concepts/diffs.md).

For example comparing two data frames will give you an output data frame,
where the `.oxen.diff.status` column shows if the row was `added`, `removed`,
or `modified`.

```
shape: (6, 7)
+-------------+-----+-----+-------+--------+-------------+-------------------+
| file        | x   | y   | width | height | label.right | .oxen.diff.status |
| ---         | --- | --- | ---   | ---    | ---         | ---               |
| str         | i64 | i64 | i64   | i64    | str         | str               |
+-------------+-----+-----+-------+--------+-------------+-------------------+
| image_0.jpg | 0   | 0   | 10    | 10     | cat         | modified          |
| image_1.jpg | 1   | 2   | 10    | 20     | null        | removed           |
| image_1.jpg | 200 | 100 | 10    | 20     | dog         | added             |
| image_2.jpg | 4   | 10  | 20    | 20     | null        | removed           |
| image_3.jpg | 4   | 10  | 20    | 20     | dog         | added             |
| image_4.jpg | 10  | 10  | 10    | 10     | dog         | added             |
+-------------+-----+-----+-------+--------+-------------+-------------------+
```

## Usage

```python theme={null}
import os
import oxen

result = oxen.diff("dataset_1.csv", "dataset_2.csv")
print(result.get())
```

## diff

```python theme={null}
def diff(path: os.PathLike,
         to: Optional[os.PathLike] = None,
         repo_dir: Optional[os.PathLike] = None,
         revision_left: Optional[str] = None,
         revision_right: Optional[str] = None,
         output: Optional[os.PathLike] = None,
         keys: list[str] = [],
         compares: list[str] = [])
```

Compares data from two paths and returns a diff respecting the type of data.

**Arguments**:

* `path` - `os.PathLike`
  The path to diff. If `to` is not provided,
  this will compare the data frame to the previous commit.
* `to` - `os.PathLike`
  An optional second path to compare to.
  If provided this will be the right side of the diff.
* `repo_dir` - `os.PathLike`
  The path to the oxen repository. Must be provided if `compare_to` is
  not provided, or if `revision_left` or `revision_right` is provided.
  If not provided, the repository will be searched for in the current
  working directory.
* `revision_left` - `str`
  The left revision to compare. Can be a commit hash or branch name.
* `revision_right` - `str`
  The right revision to compare. Can be a commit hash or branch name.
* `output` - `os.PathLike`
  The path to save the diff to. If not provided, the diff will not be saved.
* `keys` - `list[str]`
  Only for tabular diffs. The keys to compare on.
  This is used to join the two data frames.
  Keys will be combined and hashed to create a identifier for each row.
* `compares` - `list[str]`
  Only for tabular diffs. The compares to compare on.
  This is used to compare the values of the two data frames.

## Diff Objects

```python theme={null}
class Diff()
```

Diff class wraps many types of diffs and provides a consistent interface.
For example the diff can be tabular or text. Eventually we will extend this
to support other types of diffs such as images, audio, etc.

## format

```python theme={null}
@property
def format() -> str
```

Returns the format of the diff. Ie. tabular, text, etc.

## tabular

```python theme={null}
@property
def tabular() -> Optional[TabularDiff]
```

Returns the tabular diff if the diff is tabular.

## text

```python theme={null}
@property
def text() -> Optional[TextDiff]
```

Returns the text diff if the diff is text.

## get

```python theme={null}
def get()
```

Resolves the diff type and returns the appropriate diff object.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.