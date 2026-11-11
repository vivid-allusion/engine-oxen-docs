---
title: "\ud83d\udc68\u200d\ud83c\udfa8 Image Editing"
source: https://docs.oxen.ai/examples/fine-tuning/image_editing
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 👨‍🎨 Image Editing

> How to fine-tune an image editing model in Oxen.ai

Oxen.ai allows you to get higher quality image edits with consistent brand assets, characters, products, or your own style with no infrastructure setup required. Fine-tune your models with a few clicks, track results during training, and own all your weights to download and use anywhere.

## The Task

For this example, we are going to fine-tune Qwen-Image-Edit to be able to turn a photo of a Yeti Mug from a product catalogue into a photo of the mug being used in the wild. The input images will be the mug we want in the scene on a black background (left) and the output will be the mug in a beautiful scene (right).

![Reference Image](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/yeti_reference_image.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=33d39ce977ffc9b563afa559512aa378)

The prompt that generated the image on the right was *"a red headed woman sipping from the mug outdoors"*. Notice we did not have to say "yeti mug", but instead we teach the model that "mug" in our context should always be the mug from the reference image.

## Creating a Repository

Oxen.ai repositories are used to store and [version](https://docs.oxen.ai/examples/data/versioning.md) your data and models. We can create a new repository by clicking the "Create New Repository" button in your Oxen.ai dashboard.

![Create Repository](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-create-repo.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=cbead5abb62afddec659f6be79ab733b)

You will upload your dataset to the repository, and when the fine-tune is complete, the model weights will be saved to the repository on a branch. By versioning your data and models together, you can always track the data that was used to train the model.

## Uploading the Dataset

From your repository, you can click the "Add File" button to upload your dataset. The upload supports unpacking zip files if you want to upload a directory of images.

![Upload Dataset](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/fine-tune-upload-file.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=a16ad9326ccb4cb037c4f551c17b4d3d)

For image editing models, you will need three things:

1. Input images
2. Reference images
3. Prompts for the edits or changes we want to make

Start by collecting the input images, reference images, and uploading them to the repository. You will also need a csv file that will contain the prompts for the edits or changes we want to make.

## Formatting the Dataset

When you upload tabular data files (like CSV, JSONL, or Parquet) to Oxen.ai, they get superpowers. For example, you can enable image rendering on your image columns to show as thumbnails in the dataset. To view the images, click the "✏️" edit button above the dataset, then edit the column to enable image rendering. The video below shows the whole process.

<video controls>
  <source src="https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/data-frames/image_render.mp4?fit=max&auto=format&n=GvHCMKbbr_BpHEwk&q=85&s=4356f112c9f8d9d382f33cf0cbc98bd0" type="video/mp4" />

  Your browser does not support the video tag.
</video>

This lets you view images, reference images, and prompts all in one place.

![Yeti Images Dataset](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/yeti_data_frame.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=0b00e8b50e0c4d35e93cda12141387f1)

In this case we have one column called `image` that represents the output we want, and a column called `control_image` that represents the reference image that we want to feed as input. There is a third column for the `prompt` that describes the edits or changes we want to make.

The image column needs to contain the **relative path** to the image from the root of the repository. For example, if the image is in the `images` folder, the path should be `images/image_0.png`.

## Kicking off the Fine-Tune

The other superpower your csv file gets is that you can kick off a fine-tune from the dataset page. Click the "Actions" button and select "Fine-Tune a Model".

![Kick off Fine-Tune](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/yeti_fine_tune_a_model_button.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=d522f2b83fee2b18dc24c07a7cfe90b0)

This will take you to the fine-tune page where you can select the model you want to fine-tune. Select the "Qwen-Image-Edit" model, and make sure the "Control Image" column is set to `control_image` column, the "Image" column is set to `image` column, and the "Prompt" column is set to `prompt` column.

![Kick off Fine-Tune](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/select_model.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=578786c7c05486ccf740b835ca101c6c)

You can also upload some test images and prompts that will be used as samples during the fine-tune.

## Advanced Parameters

Click the "Advanced Parameters" button to see the advanced parameters for the fine-tune. You can set the learning rate, batch size, number of steps, and other parameters here.

![Fine-Tune Parameters](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/advanced_parameters.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=f17670997a118f9685200aa738370872)

One of the best parts of fine-tuning with Oxen.ai is that we track all your experiments for you, so that you can always refer back to the parameters that worked best for future fine-tunes.

## Monitoring the Fine-Tune

While the model is training, you can monitor the progress by clicking the "Samples" tab. This will show you the images that the model has generated so far.

![Monitor the Fine-Tune](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/monitor_the_fine_tune.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=98e50cd771b3df367b57bc842e0c45ec)

## Deploying the Model

When the model has finished training, you can deploy it to a new model by clicking the "Deploy Model" button.

![Deploy the Model](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/deploy-model-button.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=9ca044b4bbeeeb35df5e01bbf5d1ae35)

Once the model is deployed, you can use it in the playground or via the API.

```bash theme={null}
curl -X POST \
    -H "Authorization: Bearer <YOUR_TOKEN>" \
    -H "Content-Type: application/json" \
    -d '{
    "model": "oxen:ox-busy-scarlet-beaver",
    "input_image": "https://hub.oxen.ai/api/repos/ox/Oxen-Character-Simple-Vector-Graphic/file/main/images/reference/bloxy_white_bg.png",
    "prompt": "Add a funny hat to the ox",
    "num_inference_steps": 20
    }' https://hub.oxen.ai/api/ai/images/edit
```

## Using the Playground

Click the "Open Playground" button to use the model in the playground. This allows you to prompt the model with different images and prompts to see how it performs.

![Before and After](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-edit/playground.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=f17056baa6124af4e4ac71b0a6bd71a8)

The playground will save a history of your prompts and images so that you can refer back to them later.

## Exporting the Model

All of the model weights are stored back in your repository when the fine-tune is complete. Navigate to the fine-tune info tab, and you will see a link to the model weights. This is helpful if you want to download the weights to run in ComfyUI or your own infrastructure.

![Info Tab](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/image-generation/info-tab.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=c372a783e519665988f17f6aa8d3fa7f)

This will take you to the file viewer where you can download the model safetensors.

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