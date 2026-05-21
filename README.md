# finetuning-ai-models

Learn how to fine tune open source AI models without starting from research papers.

This repo is built for beginners.
It explains the terms, shows the notebook workflow, and gives you family specific examples for Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi.

![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
[![Open Notebook 04 in Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/mickpletcher/finetuning-ai-models/blob/main/04-your-first-finetune/04-your-first-finetune.ipynb)

## What This Repo Helps You Learn

This repo teaches the practical fine tuning workflow:

* what fine tuning is
* when to fine tune instead of prompt engineer
* how to format a small instruction dataset
* how LoRA and QLoRA reduce hardware cost
* how model families differ in prompt formatting and tokenization
* how to compare open models side by side
* how to run a full example notebook for each supported model family

This repo does not turn you into an ML researcher.
It gives you a working mental model and a repeatable starter workflow.

## Who This Is For

Use this repo if:

* you know basic Python
* you have never fine tuned a model before
* you want examples that explain the why, not just the code
* you want to learn open models such as Gemma, Mistral, Qwen, Llama, DeepSeek, and Kimi family models

Do not use this as your first Python project.
You should already know how to open a terminal, create a virtual environment, and run a notebook.

## What You Need Before You Start

Minimum setup:

1. Python `3.10` or newer
2. `pip`
3. enough disk space for Python packages and model downloads
4. a Hugging Face account if you want gated families such as Gemma or Llama

Helpful but optional:

* an NVIDIA GPU for real training runs
* Google Colab if you do not have a local GPU

If you are not sure whether Python is installed, run:

```powershell
py --version
```

If that does not work, try:

```bash
python --version
```

## Start Here

If you are new, do not jump straight to the family notebooks.

Use this order:

1. Notebook `00` to understand what fine tuning is
2. Notebook `01` to understand model size, license, and hardware tradeoffs
3. Notebook `02` to understand dataset format
4. Notebook `03` to understand LoRA
5. Notebook `04` to see a first end to end LoRA workflow
6. Notebook `05` to understand QLoRA
7. Notebook `06` to evaluate and merge outputs
8. Notebook `07` to compare model families side by side
9. Notebooks `08` through `13` for one family specific example each

If you only want the shortest useful beginner path, do:

1. Notebook `00`
2. Notebook `02`
3. Notebook `04`
4. Notebook `06`

## Setup

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

### Step 3: Pick the right dependency set

There are three install paths.
Pick the smallest one that matches what you want to do.

#### Option A: Beginner path

Use this if you only want the core learning notebooks.

```bash
pip install -r requirements.txt
```

This covers notebooks `00` through `03` and the evaluation concepts in notebook `06`.

#### Option B: Training path

Use this if you want the original LoRA and QLoRA training notebooks too.

```bash
pip install -r requirements.txt
pip install -r requirements-training.txt
```

This adds the training stack used by notebooks `04` and `05`.

#### Option C: Model family path

Use this if you want the side by side comparison notebook and the family specific notebooks for Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi.

```bash
pip install -r requirements-model-families.txt
```

This path uses a newer `transformers` version because the newer model families depend on newer tokenizer and chat template behavior.

### Step 4: Start Jupyter

```bash
jupyter notebook
```

Your browser should open the notebook home page.
If it does not, copy the URL from the terminal and paste it into your browser.

## CPU Versus GPU

This matters.

What works on CPU:

* notebooks `00` through `03`
* reading notebook `04`
* reading notebook `05`
* notebook `07` if tokenizer access works

What does not become a real fine tune on CPU:

* notebook `04` training
* notebook `05` QLoRA training
* most of the family specific training notebooks

Plain version:

* CPU is fine for learning concepts
* CUDA GPU is needed for real training
* Colab is the easiest low-cost way to run the training notebooks if you do not have local hardware

## Beginner Workflow

If you have never done this before, use this exact workflow:

1. Open notebook `00` and read it top to bottom.
2. Open notebook `02` and look at the sample dataset.
3. Read [`datasets/README.md`](datasets/README.md).
4. Run notebook `04` on Colab or a CUDA machine.
5. Run notebook `06` to see how evaluation and merging work.
6. Open [`MODEL_FAMILIES.md`](MODEL_FAMILIES.md).
7. Run notebook `07` to compare the supported families.
8. Pick one family notebook from `08` through `13`.

## Model Families In This Repo

This repo now teaches these model families:

* Gemma
* DeepSeek
* Mistral
* Qwen
* Llama
* Kimi

Use [`MODEL_FAMILIES.md`](MODEL_FAMILIES.md) first.
That file explains:

* the teaching checkpoint used for each family
* prompt formatting differences
* tokenizer differences
* license and gating notes
* hardware expectations

Important note about Kimi:

The repo compares `Kimi-K2-Instruct`, but the runnable family example uses `Moonlight-16B-A3B-Instruct`.
That is intentional.
K2 scale models are not normal beginner local fine tune targets.

## Notebook Guide

| Notebook | Purpose | What to expect |
| --- | --- | --- |
| `00` | Intro to fine tuning | Concept notebook, CPU safe |
| `01` | Base model selection | Compare size, license, and hardware tradeoffs |
| `02` | Dataset preparation | Learn JSONL formatting and train-validation splits |
| `03` | LoRA explained | Learn why adapters matter |
| `04` | First LoRA fine tune | Real training path on CUDA, inspection only on CPU |
| `05` | QLoRA low resource | CUDA path for 4 bit training |
| `06` | Evaluation | Review outputs, merge adapters, and inspect results |
| `07` | Family comparison | Compare tokenizers, prompt templates, and access notes |
| `08` | Gemma family | Gemma specific full example |
| `09` | DeepSeek family | DeepSeek family full example |
| `10` | Mistral family | Mistral family full example |
| `11` | Qwen family | Qwen family full example |
| `12` | Llama family | Llama family full example |
| `13` | Kimi family | Kimi comparison plus Moonshot family training example |

## Where Files Get Written

Generated output goes into the repo root `output/` folder.
That folder is ignored by Git.

Main paths:

* `output/prepared_data` from notebook `02`
* `output/lora-adapter` from notebook `04`
* `output/qlora-adapter` from notebook `05`
* family specific adapter folders from notebooks `08` through `13`
* `output/merged-model` from notebook `06`

## Common Questions

### Do I need advanced math first?

No.
You need enough patience to learn the workflow and enough Python to follow the notebooks.

### Do I need a paid GPU?

No.
You can learn the ideas on CPU and use Colab for the training path.

### Do I need my own dataset?

No.
Start with [`datasets/sample_dataset.jsonl`](datasets/sample_dataset.jsonl).
Once the workflow makes sense, replace it with your own data.

### Do I need Hugging Face access?

Sometimes.
Gemma and Llama teaching checkpoints can require accepted access terms on Hugging Face.
Always check the model card before you try to train.

### Why are there multiple requirements files?

Because one giant install is a bad beginner experience.

`requirements.txt` is the lighter learning path.
`requirements-training.txt` adds the older training stack.
`requirements-model-families.txt` supports the newer family specific tokenizer behavior.

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
├── 00-what-is-finetuning/
├── 01-choosing-a-base-model/
├── 02-dataset-preparation/
├── 03-lora-explained/
├── 04-your-first-finetune/
├── 05-qlora-low-resource/
├── 06-evaluating-your-model/
├── 07-model-family-comparison/
├── 08-gemma-family-finetune/
├── 09-deepseek-family-finetune/
├── 10-mistral-family-finetune/
├── 11-qwen-family-finetune/
├── 12-llama-family-finetune/
├── 13-kimi-family-finetune/
├── datasets/
└── utils/
```

## Most Important Files

* [`datasets/sample_dataset.jsonl`](datasets/sample_dataset.jsonl)
* [`datasets/README.md`](datasets/README.md)
* [`MODEL_FAMILIES.md`](MODEL_FAMILIES.md)
* [`requirements.txt`](requirements.txt)
* [`requirements-training.txt`](requirements-training.txt)
* [`requirements-model-families.txt`](requirements-model-families.txt)
* [`CHANGELOG.md`](CHANGELOG.md)
* [`CONTRIBUTING.md`](CONTRIBUTING.md)

## Contributing

If you improve beginner clarity, dataset examples, or notebook reliability, that is useful.
Read [`CONTRIBUTING.md`](CONTRIBUTING.md) before opening a pull request.

## Changelog

See [`CHANGELOG.md`](CHANGELOG.md).

## License

MIT.
See [`LICENSE`](LICENSE).
