---
title: "\ud83d\udcac Text Generation"
source: https://docs.oxen.ai/examples/fine-tuning/text_generation
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 💬 Text Generation

> How to fine-tune an LLM for text generation.

This tutorial will show you how to fine-tune an LLM for text generation. Text generation is useful for tasks like classification like sentiment analysis where you have a single input and output you want the model to learn. Small language models are great for tasks like this because they are fast and cheap to fine-tune and run.

> [!NOTE]
>
> If your application needs to maintain a history of chat messages\[] as context for the model, you should follow the [Chat Completions](https://docs.oxen.ai/examples/fine-tuning/chat_completions.md) tutorial.

## Upload Your Dataset

For this example, we are teaching the model to classify financial sentiment from text. You can follow along with the [Tutorials/FinancialSentiment](https://www.oxen.ai/Tutorials/FinancialSentiment/file/main/train_financial_sentiment.parquet) dataset containing 2000 rows of text and their corresponding sentiment labels. The dataset has one column for the prompt and one for the sentiment label (positive, negative, or neutral).

Oxen supports datasets in a variety of formats, including jsonl, csv, and parquet.

![datasets-page](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/dataset.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=5949056a41f5792fc7efd0202f21ef2e)

## Fine-Tuning The Model

Once you have uploaded your dataset, click the "Actions" button and select "Fine-tune a model".

![Fine-tune button](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/fine-tune-action.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=5bf327ea7907420ad999dd785b7fd26a)

Next select your base model, the prompt source, the response source, whether you'd like to use LoRA or not, and if you want advanced control over the fine-tune. For this example, we are using the [Qwen3-0.6B](https://www.oxen.ai/ai/models/qwen-qwen3-0-6b) model, which is small and fast to fine-tune.

![Fine-tune first page](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/fine-tune-qwen3-0.6b.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=cbe2c244786eb8f7e1f50686e90647c2)

For our Advance Options, you can have control over hyper-parameters and model specifications like learning rate, batch size, and number of epochs.

![Advanced options photo](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/text-generation/advanced-settings.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=8a0a3996beca03cac5751cba14d48e32)

## Monitoring the Fine-Tune

While we're fine-tuning your model, you'll be able to see the configuration, logs, and metrics of the fine-tuning.

![Metrics example](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-loss.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=26e6cda451537e564a657297b4db04ca)

## Deploying the Model

Once your fine-tuning is complete, go to the info page and click "Deploy". Oxen.ai will spin up a dedicated endpoint for your model to access via a chat interface or through the API.

![Deploy example](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/deploy-button.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=d1f43c68f0c5f86109e1e45f37f2726d)

After the model is deployed, you can click the "Chat with this model" button to open a chat interface.

![fine-tuned chatbot](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/chat-button.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=8a5e87f0b12ff424907da8baca4e5027)

This will bring up a chat interface where you can test your model to see how it performs.

![fine-tuned chatbot](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/chat-interface.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=c22dd33f7b048e19d57aca272b2b0fbf)

## Model API

You can integrate it into your application using the API. The API is OpenAI compatible, so you can use any OpenAI client library to interact with it. The base URL for the API is `https://hub.oxen.ai/api/ai`.

```bash theme={null}
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
-H "Authorization: Bearer $API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "your-model-id",
  "messages": [{"role": "user", "content": "The company went bankrupt last week."}]
}'
```

Make sure to replace `your-model-id` with the ID of your fine-tuned model.

## Next Steps

Feel free to join our [Discord](https://discord.com/invite/s3tBEn7Ptg) and ask us or the community any questions you have, we have a community of developers and machine learning experts who are happy to help you out.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.