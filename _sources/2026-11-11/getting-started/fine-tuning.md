---
title: "Fine-Tuning Models on Oxen.ai"
source: https://docs.oxen.ai/getting-started/fine-tuning
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Fine-Tuning Models on Oxen.ai

> Oxen.ai allows you to fine-tune text, image, and video models with a few clicks.

Simply [upload your data](https://docs.oxen.ai/examples/data/datasets.md), and we will provision GPU infrastructure and run the fine-tune. When it's done, Oxen.ai will save the fine-tuned model weights directly to your repository, and we spin down the GPU for you. No worrying about run away costs or having to manage your own infrastructure.

Once the fine-tuning process is complete, you can deploy your model to a dedicated endpoint and use the [inference endpoints](https://docs.oxen.ai/getting-started/inference.md) to integrate it into your application.

![Fine-Tuning Ox](https://mintcdn.com/oxenai/Zz1r0EaHSepwL757/images/fine_tuning/bloxy-fine-tuning.png?fit=max\&auto=format\&n=Zz1r0EaHSepwL757\&q=85\&s=cb47bd2f4dc5e993aad4b7138132a4ab)

Oxen.ai automatically [versions](https://docs.oxen.ai/examples/data/versioning.md) and manages the raw model weights and datasets, so that you can always track the data that was used to train the model, or download the model to run locally.

## Why Fine-Tune?

Fine-tuning is a great tool to reach for when basic prompting and context engineering fall short. You may need to fine-tune when:

* **Quality** is critical and the model isn't consistently producing correct outputs.
* **Proprietary Data** gives you a unique advantage that generic models can't capture.
* **Latency**  is a deal breaker and you need real-time responses.
* **Throughput** limitations are bottlenecking your application's scalability.
* **Ownership** of the model is important and you want to control your own destiny.
* **Cost** if a foundation model is too expensive for your use case or you want to deploy a smaller model to the edge.

With Oxen.ai, we make it easy to automate the fine-tuning process of LLMs on your own data.

## Modalities

Oxen.ai supports many data types and tasks for fine-tuning.

> [card] [Text Generation](https://docs.oxen.ai/examples/fine-tuning/text_generation.md)
>
> Fine-tune a model to take a user input as text and generate a single response as text.

> [card] [Chat Completions](https://docs.oxen.ai/examples/fine-tuning/chat_completions.md)
>
> Fine-tune a model on chat messages to have a conversation with a user.

> [card] [Image Generation](https://docs.oxen.ai/examples/fine-tuning/image_generation.md)
>
> Fine-tune a model to go from text descriptions to images.

> [card] [Image Editing](https://docs.oxen.ai/examples/fine-tuning/image_editing.md)
>
> Fine-tune a model to take a prompt and a reference image and generate a new image.

> [card] [Video Generation](https://docs.oxen.ai/examples/fine-tuning/video_generation.md)
>
> Fine-tune a model to take in a prompt and generate a video.

## Start by Uploading a Dataset

To get started, you'll need to create a new repository on Oxen.ai. Once you've created a repository, you can upload your data. The dataset can be in any tabular format including `csv`, `jsonl`, or `parquet`.

![Fine-Tuning Dataset Upload](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/fine-tune-upload-file.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=a16ad9326ccb4cb037c4f551c17b4d3d)

Once you have your dataset uploaded, you can query, explore, and make sure that the data is high quality before kicking off the fine-tuning process. Your model will only be as good as the data you train it on.

![Fine-Tuning Dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-dataset.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=75d3369875023b8cf44f387e13494568)

When you feel confident that your dataset is ready, use the "Actions" button to select the model you want to fine-tune.

![Fine-Tuning Dataset](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-actions.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=20f6f40b3c070acb3f86b3213a069c07)

## Selecting a Model

This will take you to a form where you can select the model you want to fine-tune and the columns you want to use for the fine-tuning process. We support fine-tuning for [text generation](https://docs.oxen.ai/examples/fine-tuning/text_generation.md), [image generation](https://docs.oxen.ai/examples/fine-tuning/image_generation.md), [image editing](https://docs.oxen.ai/examples/fine-tuning/image_editing.md), and [video generation](https://docs.oxen.ai/examples/fine-tuning/video_generation.md) with a variety of models.

![Fine-Tuning Model Selection](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/fine-tune-model-selection.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=8656b3e176e96a202ec6be8249bb6af9)

> [!NOTE]
>
> If you want support for any specific models, data formats, training methods contact us at [hello@oxen.ai](mailto:hello@oxen.ai) and we are happy to help you get started. We are actively working on support for new models and distributed training.

## Monitoring the Fine-Tune

Once you have started the fine-tuning process, you can monitor its progress. The dashboard will show you loss over time and token accuracy processed.

![Fine-Tuning Monitoring](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-loss.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=26e6cda451537e564a657297b4db04ca)

If you are fine-tuning an [image](https://docs.oxen.ai/examples/fine-tuning/image_generation.md) or [video](https://docs.oxen.ai/examples/fine-tuning/video_generation.md) generation model, you can view the generated images or videos in the "Samples" tab to get a feel for the model's performance.

![Fine-Tuning Samples](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/fine-tune-samples.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=6075fc9546d7f2749c94c6f35d2811f0)

Click on the "Info" tab to see the fine-tuning configuration and all the hyper-parameters used. This will include a link to the [dataset version](https://docs.oxen.ai/examples/data/versioning.md) you used and the raw model weights for downloading and running locally.

![Fine-Tuning Samples](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-info-tab.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=1e76a98705f6aaef58cdcb33dc5f432d)

## Deploying the Model

Once the model is fine-tuned, you can deploy it to a dedicated endpoint or in the playground.

This will give you a `/ai/chat/completions` api and a playground that you can use to test out the model.

Start by using the "playgroud" button.

![Fine-Tuning Configuration](https://mintcdn.com/oxenai/D1rpfmXbqvsK8ph0/images/fine_tuning/fine-tune-deploy-model.png?fit=max\&auto=format\&n=D1rpfmXbqvsK8ph0\&q=85\&s=b59d83bcd8ced343d7703cf5ce99460d)

if the model is not loaded you'll see an "inactive" button on the top right of the playgroud.

![Fine-Tuning Configuration](https://mintcdn.com/oxenai/D1rpfmXbqvsK8ph0/images/fine_tuning/fine-tune-deploy-model-inactive.png?fit=max\&auto=format\&n=D1rpfmXbqvsK8ph0\&q=85\&s=a563335e4901ccb4c9e8d4b3c8fd7563)

use the activate button to load the model.

![Fine-Tuning Configuration](https://mintcdn.com/oxenai/D1rpfmXbqvsK8ph0/images/fine_tuning/fine-tune-deploy-model-active.png?fit=max\&auto=format\&n=D1rpfmXbqvsK8ph0\&q=85\&s=b3c8b6bd53bce7f066a5ecf4a7dafc0b)

To use the API Swap out the model name with the name of the model you want to use.

```bash theme={null}
curl https://hub.oxen.ai/api/ai/chat/completions -H "Content-Type: application/json" -d '{
    "model":"oxen:my-model-name",
    "messages": [{"role": "user", "content": "What is the best name for a friendly ox?"}],
}'
```

## Using the Model

Once the model is deployed, you can also chat with it using the Oxen.ai chat interface at the playgroud. Learn more about the [chat interface here](https://docs.oxen.ai/getting-started/inference.md).

![Chatting with the Model](https://mintcdn.com/oxenai/s_o9ZlhOEkYJf27_/images/chat/chat_window_powerful_coffee_chimpanzee.png?fit=max\&auto=format\&n=s_o9ZlhOEkYJf27_\&q=85\&s=da4770552d70fc735792f5e0acdf6620)

For image and video generation, you can use the [playground](https://oxen.ai/ai/models) to generate images and videos.

![Chatting with the Model](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/model-playground.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=f8ce52e6962271cb0e9edc7f5158c0b6)

## Downloading the Model

If you want access to the raw model weights, you can download them from the repository using the Oxen.ai [Python Library](https://docs.oxen.ai/python-api.md) or the [CLI](https://docs.oxen.ai/getting-started/command-line/start_repository.md).

Follow the instructions for [installing oxen](https://docs.oxen.ai/getting-started/install.md) if you haven't already.

```bash CLI theme={null}
oxen download my-username/my-repo models/ox-artistic-cyan-elephant/model.safetensors --revision models/ox-artistic-cyan-elephant
```

```python Python theme={null}
from oxen import RemoteRepo

repo = RemoteRepo("my-username/my-repo")

repo.download("models/ox-artistic-cyan-elephant/model.safetensors", revision="models/ox-artistic-cyan-elephant")
```

![Fine-Tuning Configuration](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/fine-tune-model-weights.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=b9e508d20cfdd8425d93d142dc80b554)

## Need Custom Infrastructure?

If you need custom or private deployments in your own VPC or want to train a larger model on distributed infrastructure, contact us at [hello@oxen.ai](mailto:hello@oxen.ai) and we can give you a custom deployment.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.