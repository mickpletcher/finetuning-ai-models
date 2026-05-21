# Resources

Use this file when you want the official references behind the ideas in this repo.

This is not meant to replace the notebooks.
It is the follow up reading list once you want the original docs, model cards, and papers.

## Start Here

If you are new, read these first:

* [Hugging Face Transformers documentation](https://huggingface.co/docs/transformers/index)
* [Hugging Face PEFT documentation](https://huggingface.co/docs/peft/index)
* [Hugging Face Datasets documentation](https://huggingface.co/docs/datasets/index)
* [Hugging Face task guide for causal language modeling](https://huggingface.co/docs/transformers/tasks/language_modeling)

## Core Papers

These are the key papers behind the training methods used in this repo.

### LoRA

* [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)

Why it matters:

* explains why adapter training can work without updating every model weight
* gives the idea behind rank, adapter matrices, and parameter-efficient fine tuning

### QLoRA

* [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)

Why it matters:

* explains 4 bit loading for fine tuning
* explains why QLoRA made larger models practical on smaller GPUs

## Official Libraries Used In This Repo

* [Transformers GitHub repo](https://github.com/huggingface/transformers)
* [PEFT GitHub repo](https://github.com/huggingface/peft)
* [TRL GitHub repo](https://github.com/huggingface/trl)
* [Datasets GitHub repo](https://github.com/huggingface/datasets)
* [bitsandbytes GitHub repo](https://github.com/bitsandbytes-foundation/bitsandbytes)

## Recommended Reading

These are useful once the beginner notebooks make sense.

### Model Selection

* [Hugging Face model hub](https://huggingface.co/models)
* [Open LLM leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)

### Tokenizers And Prompt Templates

* [Transformers tokenizer documentation](https://huggingface.co/docs/transformers/main_classes/tokenizer)
* [Chat templating documentation](https://huggingface.co/docs/transformers/chat_templating)

### Training And Evaluation

* [Trainer documentation](https://huggingface.co/docs/transformers/main_classes/trainer)
* [Evaluate documentation](https://huggingface.co/docs/evaluate/index)

### Licensing And Model Access

* [Gemma model page](https://huggingface.co/google/gemma-2-2b-it)
* [Llama model page](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
* [Qwen model page](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
* [Mistral model page](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
* [DeepSeek model page](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
* [Moonlight model page](https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct)

## Practical Advice

Use the docs for facts.
Use the notebooks in this repo for the learning path.

If you hit a conflict between a notebook and the current official docs, trust the official docs first and then update the notebook.
