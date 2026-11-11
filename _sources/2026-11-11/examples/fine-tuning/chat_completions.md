---
title: "\ud83e\udd16 Chat Completions"
source: https://docs.oxen.ai/examples/fine-tuning/chat_completions
---

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.oxen.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 🤖 Chat Completions

> How to fine-tune an LLM on a conversation of messages.

This tutorial will show you how to fine-tune an LLM on a history of messages. If you have traces from a chat application or have curated a dataset, you can use them to fine-tune a model to be more accurate, faster, or tailored to your use-case. Often a small, specialized model can outperform a larger, more general model for a specific use-case when it comes to latency, accuracy, and cost.

## Upload Your Dataset

For this example, we are teaching the model to answer questions based on context that is supplied in the system prompt. You can follow along with the [Tutorials/CoQA](https://www.oxen.ai/Tutorials/CoQA/file/main/train_coqa.jsonl) dataset containing over 7,000 rows of chat messages. Each row of the dataset contains a conversation between a user and an assistant.

![dataset](https://mintcdn.com/oxenai/cXqZfdhecMqwRHTK/images/fine_tuning/chat-completions/dataset.png?fit=max\&auto=format\&n=cXqZfdhecMqwRHTK\&q=85\&s=c76ac6d3ccb4d76968fd0b41a1059514)

This particular dataset focuses on multi-turn conversations. Each example starts by grounding some context taken from a news article or a Wikipedia article. The user then asks a question about the context, and the assistant answers the question. There are multiple back and forth exchanges between the user and the assistant, each question building on the previous one. Here's a few examples from the paper to give you an idea of the task.

![coqa-questions](https://mintcdn.com/oxenai/cXqZfdhecMqwRHTK/images/fine_tuning/chat-completions/coqa-questions.png?fit=max\&auto=format\&n=cXqZfdhecMqwRHTK\&q=85\&s=2df684971a51d39f6f6132f03652859e)

Notice that you would not be able to answer the second question without the first question being answered first.

## Dataset Format

Oxen.ai supports datasets in a variety of file formats, including jsonl, csv, and parquet. The only requirement is that you have a column where each row is a list of messages. Each message is an dictionary with a `role` and `content` key. The `role` can be "system", "user", or "assistant". The `content` is the message content.

```json theme={null}
{
  "conversations": [
    {
      "messages": [
        {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
        {"role": "user", "content": "What is the easiest way to fine-tune a model?"},
        {"role": "assistant", "content": "Oxen.ai allows you to fine-tune a model with a few clicks. Just upload your dataset, select your base model, and click 'Fine-tune'."},
        {"role": "user", "content": "What modalities does Oxen.ai support?"},
        {"role": "assistant", "content": "Oxen.ai supports text, image, and video generation."}
      ]
    }
  ]
}
```

## Fine-Tuning The Model

Once you have uploaded your dataset, click the "Actions" button and select "Fine-tune a model".

![Fine-tune button](https://mintcdn.com/oxenai/cXqZfdhecMqwRHTK/images/fine_tuning/chat-completions/fine-tune-action.png?fit=max\&auto=format\&n=cXqZfdhecMqwRHTK\&q=85\&s=aa5810f8a78b96fc8896d3c0e89f7150)

Next select your base model, the messages source, whether you'd like to use LoRA or not. We recommend starting with a smaller model like [Qwen3-0.6B](https://www.oxen.ai/ai/models/qwen-qwen3-0-6b) for faster iteration, or a larger model like [Llama 3.1 8B](https://www.oxen.ai/ai/models/meta-llama-3-1-8b-instruct) for better performance on complex conversations.

![Fine-tune first page](https://mintcdn.com/oxenai/ccInAwcxb-C1RCGU/images/fine_tuning/text-generation/fine-tune-qwen3-0.6b.png?fit=max\&auto=format\&n=ccInAwcxb-C1RCGU\&q=85\&s=cbe2c244786eb8f7e1f50686e90647c2)

For our Advance Options, you can have control over hyper-parameters and model specifications like learning rate, batch size, and number of epochs. These settings can help you optimize for your specific use case, whether you prioritize training speed, model accuracy, or computational efficiency.

![Advanced options photo](https://mintcdn.com/oxenai/T4_0EQB1ENVXiGMM/images/fine_tuning/text-generation/advanced-settings.png?fit=max\&auto=format\&n=T4_0EQB1ENVXiGMM\&q=85\&s=8a0a3996beca03cac5751cba14d48e32)

## Monitoring the Fine-Tune

While we're fine-tuning your model, you'll be able to see the configuration, logs, and metrics of the fine-tuning. This helps you track the model's progress and identify if you need to adjust any hyperparameters or stop training early if the model has converged.

![Metrics example](https://mintcdn.com/oxenai/GvHCMKbbr_BpHEwk/images/fine_tuning/fine-tune-loss.png?fit=max\&auto=format\&n=GvHCMKbbr_BpHEwk\&q=85\&s=26e6cda451537e564a657297b4db04ca)

## Deploying the Model

Once your fine-tuning is complete, go to the info page and click "Deploy". Oxen.ai will spin up a dedicated endpoint for your model to access via a chat interface or through the API. After the model is deployed, you can click the "Chat with this model" button to open a chat interface where you can test multi-turn conversations.

![fine-tuned chatbot](https://mintcdn.com/oxenai/cXqZfdhecMqwRHTK/images/fine_tuning/chat-completions/chat-button.png?fit=max\&auto=format\&n=cXqZfdhecMqwRHTK\&q=85\&s=e05961cd61b0b6326c51fbbeb8447751)

This will bring up a chat interface where you can test your model with back-and-forth conversations to see how it maintains context across multiple turns.

![fine-tuned chatbot](https://mintcdn.com/oxenai/cXqZfdhecMqwRHTK/images/fine_tuning/chat-completions/chat-interface.png?fit=max\&auto=format\&n=cXqZfdhecMqwRHTK\&q=85\&s=a888a54820a8f12a0944dc86f3738cd6)

## Model API

You can integrate it into your application using the API. The API is OpenAI compatible, so you can use any OpenAI client library to interact with it. The base URL for the API is `https://hub.oxen.ai/api`.

For chat completions, you'll send a list of messages that includes the conversation history. Each message should have a `role` (either "user", "assistant", or "system") and `content`.

```bash theme={null}
curl -X POST https://hub.oxen.ai/api/ai/chat/completions \
-H "Authorization: Bearer $API_KEY" \
-H "Content-Type: application/json" \
-d '{
  "model": "your-model-id",
  "messages": [
    {"role": "system", "content": "You are a helpful assistant that answers questions based on the provided context."},
    {"role": "user", "content": "What is the capital of France?"},
    {"role": "assistant", "content": "The capital of France is Paris."},
    {"role": "user", "content": "What is its population?"}
  ]
}'
```

Make sure to replace `your-model-id` with the ID of your fine-tuned model. The model will use the entire conversation history to generate contextually appropriate responses.

## Next Steps

Feel free to join our [Discord](https://discord.com/invite/s3tBEn7Ptg) and ask us or the community any questions you have, we have a community of developers and machine learning experts who are happy to help you out.


This documentation is built and hosted on [Mintlify](https://mintlify.com), a developer documentation platform.