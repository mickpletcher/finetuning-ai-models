# Model Families

This repo now teaches six unique open model families:

1. Gemma
2. DeepSeek
3. Mistral
4. Qwen
5. Llama
6. Kimi

Gemma appeared twice in the request, so the curriculum uses one Gemma track.

The goal of this document is simple:

* compare the families side by side
* show where prompt formatting differs
* call out license and access rules
* set realistic hardware expectations
* map each family to one runnable teaching notebook

All access and license notes below should be rechecked against the current model card before you train or redistribute anything.

## Side By Side Comparison

| Family | Teaching checkpoint in this repo | Compare only checkpoint | Prompt formatting rule | Access pattern | Hardware reality |
| --- | --- | --- | --- | --- | --- |
| Gemma | `google/gemma-2-2b-it` | same as teaching checkpoint | Use `tokenizer.apply_chat_template(...)` | Usually gated on Hugging Face | Good beginner QLoRA target once access is approved |
| DeepSeek | `deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B` | same as teaching checkpoint | Use the actual tokenizer template for the chosen checkpoint | Often open, but check each model card | Distilled 1.5B class models are practical for a single GPU |
| Mistral | `mistralai/Mistral-7B-Instruct-v0.3` | same as teaching checkpoint | Use the tokenizer template, not a hand rolled wrapper | Usually open | Strong model, but no longer cheap to fine tune |
| Qwen | `Qwen/Qwen2.5-1.5B-Instruct` | same as teaching checkpoint | Use the tokenizer template | Usually open | Good balance of quality and accessibility |
| Llama | `meta-llama/Llama-3.2-1B-Instruct` | same as teaching checkpoint | Use the tokenizer template and respect license controls | Gated on Hugging Face | Good teaching target at 1B or 3B |
| Kimi | `moonshotai/Moonlight-16B-A3B-Instruct` | `moonshotai/Kimi-K2-Instruct` | Use the tokenizer template and follow model card guidance | Varies by release | The flagship Kimi family is not a beginner local fine tune target |

## Why The Kimi Track Uses Moonlight

The Kimi family is included because it matters in current open model discussions.

The problem is scale.

The largest Kimi branded checkpoints are not practical first fine tune targets for a normal local setup.
This repo uses `moonshotai/Moonlight-16B-A3B-Instruct` for the full walkthrough because it comes from the same vendor family and is much easier to reason about as a teaching example.

The comparison notebook still includes `moonshotai/Kimi-K2-Instruct` so you can see how the flagship family sits beside the others.

## Prompt Formatting And Tokenizer Differences

Do not assume one prompt wrapper works everywhere.

That is one of the fastest ways to get weak fine tune results.

### Gemma

* Treat the tokenizer chat template as the source of truth.
* Do not assume an Alpaca style `### Instruction` wrapper is the best training format for instruct checkpoints.

### DeepSeek

* DeepSeek prompt conventions differ by checkpoint family.
* Some DeepSeek models inherit behavior from Qwen style chat formatting.
* Others use a different layout.
* Use the exact tokenizer and inspect the rendered template before you build the dataset.

### Mistral

* Mistral instruct formatting changed across generations.
* Use the model tokenizer rather than copying old blog post wrappers.
* If your tokenizer package is too old, formatting can drift from the model card.

### Qwen

* Qwen is one of the cleaner families for tokenizer-driven chat formatting.
* It is a strong teaching family because the modern tokenizer support is straightforward.

### Llama

* Llama instruct models are strict about their chat template.
* Access control is part of the workflow, not an afterthought.
* This family is good for learning both formatting discipline and license discipline.

### Kimi

* Treat the tokenizer as the source of truth.
* Some Moonshot family releases may require `trust_remote_code=True`.
* Inspect the rendered prompt before you commit to a dataset format.

## Licenses And Gated Models

This is the practical view, not legal advice.

### Gemma

* License family: Gemma specific license
* Common workflow issue: gated access on Hugging Face
* What to check first: allowed commercial use, redistribution rules, and access approval steps

### DeepSeek

* License family: varies by checkpoint
* Common workflow issue: people assume every DeepSeek release uses the same terms
* What to check first: the exact model card for the exact checkpoint you plan to tune

### Mistral

* License family: Apache 2.0 on the mainstream open instruct releases used here
* Common workflow issue: mixing tokenizer assumptions across versions
* What to check first: checkpoint version and tokenizer requirements

### Qwen

* License family: Apache 2.0 on the Qwen2.5 instruct checkpoints used here
* Common workflow issue: people assume open access means zero usage constraints
* What to check first: the official model card and any updated usage notes

### Llama

* License family: Llama community license
* Common workflow issue: gated access and redistribution misunderstandings
* What to check first: approved access, redistribution rules, and downstream deployment terms

### Kimi

* License family: model specific Moonshot license
* Common workflow issue: using the biggest headline model without checking whether local fine tuning is even realistic
* What to check first: license, access rules, and whether the checkpoint needs custom code support

## Hardware Guidance By Family

These are rough training expectations for the teaching checkpoints in this repo.
They are not hard guarantees.
Real memory use depends on sequence length, batch size, optimizer state, quantization path, and framework versions.

| Family | Teaching checkpoint size class | Practical path | Notes |
| --- | --- | --- | --- |
| Gemma | 2B | QLoRA on a single consumer GPU | Good first gated family |
| DeepSeek | 1.5B distilled | QLoRA on a single consumer GPU | Easier than the flagship reasoning models |
| Mistral | 7B | QLoRA on a stronger consumer GPU | Much heavier than the 1B to 2B teaching families |
| Qwen | 1.5B | QLoRA on a single consumer GPU | One of the easiest full examples in this repo |
| Llama | 1B | QLoRA or small LoRA run | Larger Llama variants scale up fast |
| Kimi | 16B A3B teaching example | Strong GPU or hosted environment | Flagship Kimi K2 belongs in compare only mode for most learners |

## Family Notebooks

Use the comparison notebook first:

* [`07-model-family-comparison/07-model-family-comparison.ipynb`](07-model-family-comparison/07-model-family-comparison.ipynb)

Then use one full example notebook per family:

* [`08-gemma-family-finetune/08-gemma-family-finetune.ipynb`](08-gemma-family-finetune/08-gemma-family-finetune.ipynb)
* [`09-deepseek-family-finetune/09-deepseek-family-finetune.ipynb`](09-deepseek-family-finetune/09-deepseek-family-finetune.ipynb)
* [`10-mistral-family-finetune/10-mistral-family-finetune.ipynb`](10-mistral-family-finetune/10-mistral-family-finetune.ipynb)
* [`11-qwen-family-finetune/11-qwen-family-finetune.ipynb`](11-qwen-family-finetune/11-qwen-family-finetune.ipynb)
* [`12-llama-family-finetune/12-llama-family-finetune.ipynb`](12-llama-family-finetune/12-llama-family-finetune.ipynb)
* [`13-kimi-family-finetune/13-kimi-family-finetune.ipynb`](13-kimi-family-finetune/13-kimi-family-finetune.ipynb)

## Official Model Cards

These are the starting points to verify current access rules and licenses:

* [Gemma 2 2B IT](https://huggingface.co/google/gemma-2-2b-it)
* [DeepSeek R1 Distill Qwen 1.5B](https://huggingface.co/deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B)
* [Mistral 7B Instruct v0.3](https://huggingface.co/mistralai/Mistral-7B-Instruct-v0.3)
* [Qwen2.5 1.5B Instruct](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct)
* [Llama 3.2 1B Instruct](https://huggingface.co/meta-llama/Llama-3.2-1B-Instruct)
* [Moonlight 16B A3B Instruct](https://huggingface.co/moonshotai/Moonlight-16B-A3B-Instruct)
* [Kimi K2 Instruct](https://huggingface.co/moonshotai/Kimi-K2-Instruct)
