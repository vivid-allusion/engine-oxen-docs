---
title: "\ud83d\uddbc\ufe0f Image Generation"
source: https://docs.oxen.ai/examples/fine-tuning/image_generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🖼️ Image Generation

> How to fine-tune an image generation model in Oxen.ai

Oxen.ai allows you to fine-tune an image generation model to create higher quality images with consistent brand assets, characters, products, or your own style with no infrastructure setup required. Fine-tune your models with a few clicks, track results during training, and own all your weights to download and use anywhere.

## The Task

For this example, we are going to fine-tune [Qwen-Image](https://www.oxen.ai/ai/models/qwen-image) to be able to generate images of models wearing a specific outfit.

![Reference Image](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/nike-models.jpg?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=4e16cfce155497e02a899abc61eac50b)

## Dataset Format

When fine-tuning image generation models, you need a dataset that contains the images and descriptions of the images. The expected format is a csv, jsonl, or parquet file with a column that contains the *relative path* to the image in the repository, and a column that contains the description of the image.

![Dataset Format](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/dataset-format.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=b93a84825004497dd4d9355cca93b746)

We'll walk through the process of creating a dataset with the images and captions in the following sections.

## Creating a Repository

Oxen.ai repositories are used to store and version your data and models. We can create a new repository by clicking the "Create New Repository" button in your Oxen.ai dashboard.

![Create Repository](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-create-repo.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=cbead5abb62afddec659f6be79ab733b)

You will upload your dataset to the repository, and when the fine-tune is complete, the model weights will be saved to a branch in the repository. By versioning your data and models together, you can always track the data that was used to train the model.

## Uploading the Images

From your repository, you can click the "Add File" button to upload your dataset of images. If you upload a zip file, it will automatically be unpacked into the repository in the specified directory.

> [!NOTE]
>
> Note: When uploading your images, organize your files in a folder by specifying a "Target Directory" when uploading the files.

![Upload Dataset](https://mintcdn.com/oxenai/S-Fh7jS1NMc3HM8D/images/fine_tuning/fine-tune-images-zip.png?fit=max\&auto=format\&n=S-Fh7jS1NMc3HM8D\&q=85\&s=d0ee5b3a57771195b436e77e4ba286c7)

## Turn Your Images into a Dataset

In order to fine-tune in Oxen.ai, you need a csv, jsonl, or parquet file that contains the images and their captions.

With your images uploaded, you can convert the directory of images into a dataset that can be used for the fine-tune. Navigate to the directory of images and click the "Folder to Dataset" button.

![Folder to Dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-folder-to-dataset-button.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=3f4d92b2d7be7f969fac7a8eeada240d)

This will grab all of the relative paths from the folder and create a parquet file with a column called `file_path` that contains the relative path to the image.

![Folder to Dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-folder-to-dataset-conversion.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=7555f2755ff84d2129f37b1ac56cc8ca)

In order to view the images, you will need to enable image rendering on the `file_path` column. Click the "✏️" edit button above the dataset, then edit the column to enable image rendering. The video below shows the whole process.

<video controls>
  <source src="https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/data-frames/image_render.mp4?fit=max&auto=format&n=GvHCMKbbr_BpHEwk&q=85&s=4356f112c9f8d9d382f33cf0cbc98bd0" type="video/mp4" />

  Your browser does not support the video tag.
</video>

## Captioning The Images

In order for the fine-tune to learn a mapping from text to images, we'll need a prompt column that contains a description of each image. Oxen.ai makes it easy to run models on each row of the dataset in order to automatically generate captions.

Click the "Actions" button above the dataset, then select "Run Inference".

![Run Inference](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/data-frames/run-inference.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=f42221c35e4f359e4314635149f3ae37)

You will need to select a model that is able to go from "image" to "text" from the dropdown on the left.

![Run Inference](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/evaluations/image-to-text-captions.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=fef73087b872dfd66e8c1b07b2df9d71)

Now write a prompt that describes what you want in the caption and any formatting you want to apply.

```text theme={null}
Describe the model and the clothing that the model is wearing as if you are writing a prompt for an image generation model. The prompt should be one sentence in length and include the gender as "male" or "female". Also describe their hair color and skin tone (white, tan, black, latina, asian). Only describe the person and outfit.

The prompt should start with something like "A male Nike model wearing" or "A female Nike model wearing"

{file_path}
```

> [!NOTE]
>
> Note: You must supply the curly braces `{}` around the `file_path` column in the prompt to know what column to use for the image.

When you feel good about your prompt after looking at your samples click the "Next ->" button to decide where you want to save the results. By default, the results will create a new version of the existing file.

![Run Inference](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/evaluations/image-to-text-committing.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=abd8b32a42d2f5935955128274122b4e)

Now sit back and relax as the model captions your images 😌 ☕️.

![Run Inference](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/evaluations/image-to-text-progress.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=5106f69d6bf2b3c0261665b30ebde872)

## Kicking off the Fine-Tune

With our images captioned, now we can kick off the fine-tune! Click the "Actions" button and select "Fine-Tune a Model".

![Kick off Fine-Tune](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/fine-tune-a-model-button.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=04cdd8bf3e2d79b32798145b6142d4b6)

This will take you to the fine-tune page where you can select the model you want to fine-tune. Select the "Qwen-Image" model, and make sure the "Image" column is set to the `file_path` column, and the "Prompt" column is set to the `caption` column.

![Write Prompts](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/fine-tune-write-prompts.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=d79e55997ab168ff4fd90e5044cf5b2e)

To monitor the fine-tune, you can provide a few sample prompts that will be used to generate images during the fine-tune.

## Advanced Parameters

Click the "Advanced Parameters" button to see the advanced parameters for the fine-tune. You can set the learning rate, batch size, number of steps, and other parameters here.

One of the best parts of fine-tuning with Oxen.ai is that we track all your experiments for you, so that you can always refer back to the parameters that worked best for future fine-tunes.

![Fine-Tune Parameters](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/advanced-params.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=758abaa5ddedcd89f3af52ce387853a6)

Click the "Start Fine-Tune" button and you are off to the races!

## Monitoring the Fine-Tune

As the model is training, you can monitor the progress by clicking the "Samples" tab. This will show you the images that the model has generated so far.

![Monitor the Fine-Tune](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/monitor_the_fine_tune.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=080c1859268e32a5b3b23b1377da2b42)

## Deploying the Model

When the model has finished training, you can deploy it to a new model by clicking the "Deploy Model" button. The deployment will take a few minutes to complete.

![Deploy the Model](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/model-deploying.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=148e756942c87618ff3af90bca4e872b)

Once the model is deployed, you can use it in the playground or via the API.

```bash theme={null}
curl -X POST \
-H "Authorization: Bearer <YOUR_TOKEN>" \
-H "Content-Type: application/json" \
-d '{
  "model": "oxen:ox-brave-jade-gecko",
  "prompt": "A majestic ox standing in a field at sunset",
  "num_inference_steps": 28
}' https://hub.oxen.ai/api/ai/images/generate
```

## Using the Playground

Click the "Open Playground" button to use the model in the playground. This allows you to prompt the model with different images and prompts to see how it performs.

![Playground](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/playground.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=ed7e1ef8491cb510a71440f153209135)

The playground will save a history of your prompts and images so that you can refer back to them later.

## Exporting the Model

All of the model weights are stored back in your repository when the fine-tune is complete. Navigate to the fine-tune info tab, and you will see a link to the model weights. This is helpful if you want to download the weights to run in ComfyUI or your own infrastructure.

![Info Tab](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/info-tab.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=c372a783e519665988f17f6aa8d3fa7f)

This will take you to the file viewer where you can download the model `.safetensors` file.

![File Viewer](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/file-viewer.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=35df0436d0fec70b8d36fc41c4fc9838)

You can also automatically download the weights with the [oxen cli](https://docs.oxen.ai/getting-started/command-line/start_repository.md) or [python library](https://docs.oxen.ai/python-api.md).

```bash CLI theme={null}
oxen download user-name/repo-name path/to/model.safetensors --revision COMMIT_OR_BRANCH
```

```python Python theme={null}
from oxen import RemoteRepo
repo = RemoteRepo("user-name/repo-name")
repo.download("path/to/model.safetensors", revision="COMMIT_OR_BRANCH")
```

## Need Help Fine-Tuning?

If you need help fine-tuning your model, contact us at [hello@oxen.ai](mailto:hello@oxen.ai) and we are happy to help you get started.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.