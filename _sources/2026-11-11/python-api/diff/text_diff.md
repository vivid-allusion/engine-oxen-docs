---
title: "Text diff"
source: https://docs.oxen.ai/python-api/diff/text_diff
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Text diff

# oxen.diff/text\_diff

## TextDiff Objects

```python theme={null}
class TextDiff()
```

A class representing a text diff.

## num\_added

```python theme={null}
@property
def num_added() -> int
```

Returns the number of added lines in the diff.

## num\_removed

```python theme={null}
@property
def num_removed() -> int
```

Returns the number of removed lines in the diff.

## lines

```python theme={null}
@property
def lines() -> list[LineDiff]
```

Returns the contents of the diff as a polars data frame.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.