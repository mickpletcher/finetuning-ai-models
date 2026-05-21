# finetuning-ai-models

A beginner's hands on guide to fine tuning AI models. From dataset prep to LoRA and QLoRA training, runnable notebooks, no paywalls, no PhD required.

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
[![Open in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/04-your-first-finetune/04-your-first-finetune.ipynb)
![PRs welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

## Start Here

If this is your first time working with model fine tuning, start with notebook `00` and move in order.
Each notebook builds on the one before it.
You do not need a machine learning background.
You do need basic Python knowledge and a way to run Jupyter notebooks.

If you only want the main hands on training notebook, jump to notebook `04`.
If you do that, read notebook `02` first so the dataset format makes sense.

## What You Will Learn

* What fine tuning is and when it makes sense.
* How to choose a base model for your task and hardware.
* How to format instruction datasets in Alpaca style JSONL.
* How LoRA works and why it lowers the barrier to entry.
* How to run a first adapter fine tune with PEFT and TRL.
* How QLoRA reduces memory pressure on GPU hardware.
* How to evaluate outputs instead of trusting loss alone.

## Who This Is For

This repo is for beginners who can already write basic Python but have never fine tuned a model before.
It fits software developers, hobbyists, and curious builders who want a practical path into model training without needing a research background.

You are a good fit if:

* You have used Python scripts or notebooks before.
* You have heard terms like model, token, or dataset but want them explained in plain English.
* You want an example that runs on free or low cost hardware.

## Before You Begin

You need these things first:

1. Python 3.10 or newer installed.
2. `pip` available in your terminal.
3. Jupyter installed through `requirements.txt`.
4. Enough disk space to download Python packages and a small Hugging Face model.
5. Patience for the first model download. It can take a few minutes.

If you do not know whether Python is installed, run:

```bash
python --version
```

If that fails on Windows, try:

```bash
py --version
```

## Quick Start

Follow these steps in order.

### Step 1: Clone the repo

```bash
git clone https://github.com/mickpletcher/finetuning-ai-models.git
cd finetuning-ai-models
```

### Step 2: Create a virtual environment

Windows PowerShell:

```powershell
py -3.10 -m venv .venv
.venv\Scripts\Activate.ps1
```

macOS or Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

### Step 3: Install the base packages

```bash
pip install -r requirements.txt
```

This installs the beginner path used by notebooks `00` through `03`, plus the evaluation notebook.

If you plan to run notebook `04` or `05`, install the training extras too:

```bash
pip install -r requirements-training.txt
```

That second file adds the training specific packages used for LoRA and QLoRA work.

If you plan to use the model family comparison notebook or the new Gemma, DeepSeek, Mistral, Qwen, Llama, or Kimi family tracks, install the model family stack too:

```bash
pip install -r requirements-model-families.txt
```

That file moves the `transformers` version forward for the newer family specific tokenizers and chat templates.

### Step 4: Start Jupyter

```bash
jupyter notebook
```

Your browser should open the Jupyter home page.
Open notebook `00` first.

## How To Work Through The Repo

Use this order:

1. `00` for the big picture.
2. `01` for picking a base model.
3. `02` for dataset prep.
4. `03` for LoRA concepts.
5. `04` for your first real fine tune.
6. `05` for the QLoRA path.
7. `06` for evaluation and model export.
8. `07` for side by side family comparison.
9. `08` through `13` for family specific full examples.

Do not worry if you do not understand every line of code on the first pass.
The goal is to finish one complete run, then go back and deepen your understanding.

## Hardware Requirements

You do not need a GPU to start learning.

* Notebooks `00` through `03` are CPU safe.
* Notebook `04` can open and run on CPU, but it does not create a real adapter unless you run it on CUDA.
* Notebook `05` needs CUDA for the 4 bit QLoRA training path.

If you do not have a local GPU, use the free Google Colab tier for notebook `04`.
That is the easiest way to run the main training example without buying hardware.

## What LoRA And QLoRA Mean

If the terms are new, here is the short version:

* LoRA trains a small adapter instead of changing every model weight.
* QLoRA does the same thing, but it also loads the base model in 4 bit form to save GPU memory.

That is why these methods matter for beginners.
They lower the hardware cost of learning.

## Curriculum

| Module | Title | What you do | Open in Colab |
| --- | --- | --- | --- |
| 00 | What is fine tuning? | Learn the difference between pretraining, prompting, RAG, and fine tuning | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/00-what-is-finetuning/00-what-is-finetuning.ipynb) |
| 01 | Choosing a base model | Compare model families, sizes, and licenses | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/01-choosing-a-base-model/01-choosing-a-base-model.ipynb) |
| 02 | Dataset preparation | Load JSONL data, inspect it, tokenize it, and split it for training | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/02-dataset-preparation/02-dataset-preparation.ipynb) |
| 03 | LoRA explained | See why LoRA matters and inspect trainable parameter counts | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/03-lora-explained/03-lora-explained.ipynb) |
| 04 | Your first finetune | Run a full LoRA adapter workflow and compare model outputs | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/04-your-first-finetune/04-your-first-finetune.ipynb) |
| 05 | QLoRA low resource | Repeat the workflow with 4 bit loading on CUDA | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/05-qlora-low-resource/05-qlora-low-resource.ipynb) |
| 06 | Evaluating your model | Review outputs, check metrics, and merge adapters for deployment | [Open](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/06-evaluating-your-model/06-evaluating-your-model.ipynb) |
| 07 | Model family comparison | Compare Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi side by side and inspect tokenizer differences | Pending |
| 08 | Gemma family full example | Run a Gemma specific fine tune workflow with family specific formatting notes | Pending |
| 09 | DeepSeek family full example | Run a DeepSeek family workflow using a smaller distilled checkpoint | Pending |
| 10 | Mistral family full example | Run a Mistral family workflow and compare its heavier hardware path | Pending |
| 11 | Qwen family full example | Run a Qwen family workflow with modern chat template handling | Pending |
| 12 | Llama family full example | Run a gated Llama family workflow with access and license checks | Pending |
| 13 | Kimi family full example | Compare Kimi K2 and run the teachable Moonshot family example | Pending |

## Common Questions

### Do I need to understand deep math first?

No.
This repo explains the ideas in plain language first.

### Do I need to pay for a GPU?

No.
You can learn most of the workflow on CPU and use free Colab for the main training notebook.

### Do I need my own dataset right away?

No.
The repo includes a sample dataset in [`datasets/sample_dataset.jsonl`](datasets/sample_dataset.jsonl).
Use that first.
Once the workflow works, swap in your own data.

### Where do the training outputs go?

Notebook `04` saves adapter output under `output/lora-adapter` at the repo root.
Notebook `05` saves QLoRA output under `output/qlora-adapter` at the repo root.
Notebook `02` writes prepared dataset splits under `output/prepared_data`.
These paths are ignored by git because model artifacts can get large.

### Can this repo teach model families like Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi?

Yes.
Use [`MODEL_FAMILIES.md`](MODEL_FAMILIES.md) and notebook `07` first.
That gives you the side by side comparison, access notes, license notes, prompt formatting differences, tokenizer differences, and hardware guidance.
Then move into notebooks `08` through `13` for one full example per family.

## Repo Structure

```text
finetuning-ai-models/
├── README.md
├── CHANGELOG.md
├── LICENSE
├── .gitignore
├── requirements.txt
├── requirements-training.txt
├── requirements-model-families.txt
├── CONTRIBUTING.md
├── MODEL_FAMILIES.md
├── .github/
│   ├── workflows/
│   │   ├── notebook-ci.yml
│   │   └── broken-links.yml
│   └── ISSUE_TEMPLATE/
│       ├── bug_report.md
│       └── content_suggestion.md
├── 00-what-is-finetuning/
│   └── 00-what-is-finetuning.ipynb
├── 01-choosing-a-base-model/
│   └── 01-choosing-a-base-model.ipynb
├── 02-dataset-preparation/
│   └── 02-dataset-preparation.ipynb
├── 03-lora-explained/
│   └── 03-lora-explained.ipynb
├── 04-your-first-finetune/
│   └── 04-your-first-finetune.ipynb
├── 05-qlora-low-resource/
│   └── 05-qlora-low-resource.ipynb
├── 06-evaluating-your-model/
│   └── 06-evaluating-your-model.ipynb
├── 07-model-family-comparison/
│   └── 07-model-family-comparison.ipynb
├── 08-gemma-family-finetune/
│   └── 08-gemma-family-finetune.ipynb
├── 09-deepseek-family-finetune/
│   └── 09-deepseek-family-finetune.ipynb
├── 10-mistral-family-finetune/
│   └── 10-mistral-family-finetune.ipynb
├── 11-qwen-family-finetune/
│   └── 11-qwen-family-finetune.ipynb
├── 12-llama-family-finetune/
│   └── 12-llama-family-finetune.ipynb
├── 13-kimi-family-finetune/
│   └── 13-kimi-family-finetune.ipynb
├── datasets/
│   ├── README.md
│   └── sample_dataset.jsonl
└── utils/
    ├── __init__.py
    ├── helpers.py
    └── model_families.py
```

## Files You Should Know About

* [`datasets/sample_dataset.jsonl`](datasets/sample_dataset.jsonl) is the sample training dataset.
* [`datasets/README.md`](datasets/README.md) explains the expected dataset format.
* [`utils/helpers.py`](utils/helpers.py) holds shared helper functions used by the notebooks.
* [`requirements-training.txt`](requirements-training.txt) adds the optional packages for notebooks `04` and `05`.
* [`requirements-model-families.txt`](requirements-model-families.txt) adds the newer package set used by the family comparison and family specific notebooks.
* [`MODEL_FAMILIES.md`](MODEL_FAMILIES.md) compares Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi side by side.
* [`CHANGELOG.md`](CHANGELOG.md) tracks repo changes.
* [`CONTRIBUTING.md`](CONTRIBUTING.md) explains how to submit improvements.

## Contributing

Contributions are welcome if they keep the repo clear, practical, and runnable for beginners.
Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md) for the record of scaffold work and later updates.

## License

MIT. See [`LICENSE`](LICENSE).
