---
title: "\ud83d\udcca Datasets"
source: https://docs.oxen.ai/examples/data/datasets
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 📊 Datasets

In Oxen.ai, datasets are used to structure your unstructured data. Any tabular data file will automatically be turned into a collaborative database that can be versioned and used to organize data, can be queried, or fed in as training data for models.

Oxen.ai datasets are accessible with an easy to use web interface as well as a command line tools, python, and HTTP library.

## Repositories vs Datasets

Repositories are the top level container for your datasets. They are a collection of versioned files and directories.

![Oxen.ai Repo](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/image_net_files.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=d6c884bc590e8125a57b8861d30988aa)

Certain files within Oxen with the extensions `csv`, `tsv`, `jsonl` and `parquet` gain super powers. These dataset files can be multi-modal containing links to images, audio, and PDFs. You can query them in natural language, and edit them like a spreadsheet.

![Image Net](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/image_net_train.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=aee33156db4fa1d1c151f18d1a78d5de)

Under the hood we turn these raw files into a lightweight database that can be queried, edited, versioned, and downloaded.

## View Your Dataset

Click the file your repository to open the dataset you want to work with. If you want to follow along with this example, download the [Thinking LLMs](https://www.oxen.ai/ox/Thinking-LLMs) dataset.

![Oxen.ai Thinking LLMs Repo](https://mintcdn.com/oxenai/VndlMSXTb9YuU-Wl/images/thinking_llms.png?fit=max\&auto=format\&n=VndlMSXTb9YuU-Wl\&q=85\&s=0b1ea583941415e692d7ebd5c23a18a2)

## Download Your Dataset

Datasets can be downloaded directly from the UI or using the CLI and Python library. You can grab any revision of the dataset by specifying the revision as a branch name or commit id.

```python Python theme={null}
from oxen import RemoteRepo

# Connect to the remote repository (does not download any data)
repo = RemoteRepo("YOUR_USERNAME/YOUR_REPO")

# Download the dataset
repo.download("path/to/dataset.jsonl", revision="main")
```

```bash CLI theme={null}
oxen download YOUR_USERNAME/YOUR_REPO path/to/dataset.jsonl --revision main
```

## Upload Your Dataset

Once you have created a repository, you can use the "Add Files" button on your repository to upload dataset files through the UI. The dataset will automatically be versioned so you can iterate on it and track changes.

![Oxen.ai Thinking LLMs Repo](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/dataset_upload.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=32ada42915ca295b50e9209f6f911da2)

Datasets can also be uploaded from the command line or python library. This allows you to integrate Oxen into your existing codebases or CI/CD pipelines. The workflow is similar to git where you `add` and `commit` your changes.

```python Python theme={null}
from oxen import RemoteRepo

# Connect to the remote repository
repo = RemoteRepo("YOUR_USERNAME/YOUR_REPO")

# Upload the file to the remote repository
repo.add("path/to/dataset.jsonl", dst="datasets/")

# Commit the changes
repo.commit("Add dataset.jsonl to the datasets/ directory")
```

```bash CLI theme={null}
# Clone the repository
oxen clone https://hub.oxen.ai/YOUR_USERNAME/YOUR_REPO
cd YOUR_REPO

# Add the file to the repository
oxen add path/to/dataset.jsonl

# Commit the changes
oxen commit -m "Add path/to/dataset.jsonl"

# Sync the changes to the remote repository
oxen push
```

> [!NOTE]
>
> To perform **write operations** on datasets, you need to be an editor on the repository and have your username and API key set. You can set your username and API key using the [CLI](https://docs.oxen.ai/getting-started/command-line/setup.md) or [Python library](https://docs.oxen.ai/python-api/index.md).
>
> Read more about [Authentication & Authorization](https://docs.oxen.ai/getting-started/auth).

## Using `fsspec`

Since datasets are just stored as files and directories, you can interact with them directly using [fsspec](https://filesystem-spec.readthedocs.io/en/latest/). This allows you to read and write to them similar to how you would with a local file system.

For example if you want to read the contents of a file on the server, you can simply use the `open` method.

```python Python theme={null}
import oxen

fs = oxen.OxenFS("YOUR_USERNAME", "YOUR_REPO")
with fs.open("path/to/dataset.jsonl") as f:
    content = f.read()

# Print the first 100 characters of the file
print(content[:100])
```

If you want to write to a file, you can use the `write` method.

```python Python theme={null}
fs = oxen.OxenFS("YOUR_USERNAME", "YOUR_REPO")

with fs.open("path/to/dataset.jsonl", "w") as f:
    f.write("Hello, world!")
```

If you want to specify a commit message, simply add the commit message in the scope of the `with` block.

```python Python theme={null}
fs = oxen.OxenFS("YOUR_USERNAME", "YOUR_REPO")

with fs.open("path/to/dataset.jsonl", "w") as f:
    f.write("{\"question\": \"What is the capital of France?\", \"answer\": \"Paris\"}")
    f.commit_message = "Add a new row"
```

To learn more about how to use fsspec with Oxen, check out the [OxenFS](https://docs.oxen.ai/python-api/oxen_fs.md) documentation.

## Using Pandas

Since `OxenFS` implements the `fsspec` interface, you can use it with any library that supports `fsspec`. For example, you can use it with [pandas](https://pandas.pydata.org/) to read and write to datasets.

```python Python theme={null}
import pandas as pd

# Format: oxen://<username>/<repo>@<revision>/<path/to/file>
df = pd.read_parquet("oxen://openai:gsm8k@main/gsm8k_test.parquet")

# Print the first 5 rows
print(df.head())

# Apply a transformation to the dataframe
df["answer"] = df["answer"].apply(lambda x: x.upper())

# Write the dataframe to a new file
df.to_parquet("oxen://openai:gsm8k@main/gsm8k_test_new.parquet")
```

## Your Dataset is a Database

Datasets look like raw files on the surface, but some of their superpowers come from the fact that Oxen.ai can index them into a [DuckDB](https://duckdb.org/) database on the remote server. This allows you to query your dataset directly with SQL.

You can use the [DataFrame](https://docs.oxen.ai/python-api/data_frame.md) class in the python library to interact with your dataset as a database.

```python Python theme={null}
from oxen import DataFrame

# Connect to and index the data frame
df = DataFrame("YOUR_USERNAME/YOUR_REPO", "path/to/file.jsonl")

# Print the first 5 rows that are spam
results = df.query("SELECT * FROM df where category = 'spam' LIMIT 5")
print(results)
```

Not only can you query your dataset, but you can also add rows, add columns, and perform other database operations before committing your changes. This is useful if you want to build labeling workflows or other data pipelines.

```python Python theme={null}
from oxen import DataFrame

# Connect to and index the data frame
# Note: This must be an existing file committed to the repo
#       indexing may take a while for large files
df = DataFrame("YOUR_USERNAME/YOUR_REPO", "path/to/file.jsonl")

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

# Get the current changes to the data frame
status = data_frame.diff()
print(status)

# Commit the changes
data_frame.commit("Updating data.csv")​
```

> [!NOTE]
>
> Note: There are currently some limitations to the DataFrame API.
>
> 1. You must have **write access** to the repository to use the DataFrame API. This is because it creates a [workspace](https://docs.oxen.ai/python-api/workspace.md) on the remote server to index the dataset.
>
> 2. Indexing may take a while for large files, and is performed on instantiation of the DataFrame object.
>
> 3. The DataFrame API is currently only supported for single files, you cannot yet use it to JOIN datasets across files.

## Datasets as a Vector Database

If you have a column in your dataset that contains a vector of floats representing a piece of text or image, you can use Oxen.ai as a vector database to sort by similarity.

![Embedding a dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/embeddings.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=c44b80bfbb95c4430bf96b1bf9dbba21)

```python Python theme={null}
from oxen import DataFrame

# Connect to and index the data frame
df = DataFrame("YOUR_USERNAME/YOUR_REPO", "path/to/file.parquet")

# Check if the dataset is indexed for embeddings search
if not df.is_nearest_neighbors_enabled():
    # Enable nearest neighbors search
    df.enable_nearest_neighbors()

# Get an embedding for a specific row (may return multiple embeddings there are multiple results for the query)
embed_column = "embedding"
embeddings = df.get_embeddings({"prompt": "What is the capital of France?"}, column=embed_column)

# Query the data frame
embedding = embeddings[0]
results = df.query(
    embedding=embedding,
    sort_by_similarity_to=embed_column
)
for row in results:
    print(row["prompt"])
```

If you don't have an embedding column, you can compute one using an Evaluation on the Oxen.ai platform.

## Rendering Images and Links

In the dataset viewer, you can render images and links to other files in the dataset. The assumption is that the value in the rows is a relative path to a file in the same repository. For example if we have a directory of images in the `images` directory, we can render the image by using the relative path to the image `images/my_image_0.png`.

![Rendering images and links](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/ox_with_wings.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=703b6524e6b539912cc4e0f664d16d57)

In order to enable the rendering, you need to edit the `render` function in the dataset viewer. Go into the edit mode of the dataset, then edit the column you want to render. You can select from a few different rendering options including: `image`, `link`, `markdown`, and `code`.

![Edit render function](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/image_metadata.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=1a41ff3a6791efc341d55cd3faf5c5d9)

This will save metadata to the repository that will be used to render the images and links. To programmatically set the render function, checkout the [file metadata documentation](https://docs.oxen.ai/concepts/file_metadata.md).

## Using the UI

### Editing Your Dataset

You can edit your dataset directly from the UI by clicking the pencil icon in the upper right of the dataset viewer. This will open the file in an editor that will allow to add, edit, and delete rows and columns.

![Editing a dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/remove_row.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=103385419037a973b4055126a9a73afb)

The editor will not commit any changes to the repository until you use the "Commit" button to write a message and save your changes.

![Editing a dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/commit_data_frame.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=9824fb50cf042b8d49d8487121d75fca)

### Use LLMs to Augment Your Dataset

In Oxen.ai, you can generate new columns and rows using LLMs. This is a great way to automatically label your dataset or generate training data for small LLMs from larger models. Click the "Actions" button and select "Run Inference".

![Oxen.ai Evaluation](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/evaluations/run_inference_dataset.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=357be38a4cdff355056d6f35d559ed38)

Simply select a model, write a prompt, and run the model row by row on the dataset.

![Oxen.ai Evaluation](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/categorieze_columns.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=cce2a33c5b41382cb059eb38a300e2be)

### Query Your Dataset

To query your dataset, write a question in plain English in the search bar. This will automatically translate the question into a SQL query and apply it to the view of your data. For example, you can look at the distribution of question types by asking:

```
What are all the categories sorted by count?
```

![Where to find Text2SQL](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/datasets/text2sql.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=8d9e8c6ea2ee08a68016b2fc5904bf37)

If the query engine makes a mistake, no worries! You can edit the SQL query to get the results you want.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.