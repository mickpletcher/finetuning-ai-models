# Changelog

## 2026 05 13

### Added

* Root project files for a runnable tutorial repo, including `.gitignore`, `LICENSE`, `requirements.txt`, and `CONTRIBUTING.md`.
* Seven tutorial notebooks that cover fine tuning basics, model selection, dataset prep, LoRA, QLoRA, training, and evaluation.
* `datasets/README.md` and `datasets/sample_dataset.jsonl` with a 20 row machine learning Q and A sample dataset in Alpaca format.
* `utils/helpers.py` and `utils/__init__.py` for shared notebook helper functions.
* GitHub Actions workflows for notebook execution and broken link checks.
* GitHub issue templates for bug reports and content suggestions.

### Changed

* Rewrote `README.md` into a first run guide with beginner focused setup steps, plain language explanations, hardware guidance, common questions, and direct links to important files.
* Added `CHANGELOG.md` to the documented repo structure and linked it from `README.md`.

### Notes

* CPU safe notebook execution is set up in CI for notebooks `00` through `03`.
* Notebook `04` keeps the main LoRA training walkthrough and supports CPU setup with a GPU path for practical training.
* Notebook `05` clearly skips the QLoRA training path on CPU because CUDA is required for that workflow.

## 2026 05 21

### Changed

* Unified notebook artifact paths through shared helpers so notebooks `02`, `04`, `05`, and `06` all read and write from the same repo root `output/` tree.
* Updated notebook `04` so CPU mode no longer saves a fake adapter and the comparison cell now checks for a real trained adapter before loading it.
* Updated notebook `05` to prepare the quantized model for k bit training before applying LoRA.
* Split beginner dependencies from optional training extras by moving `trl`, `accelerate`, and `bitsandbytes` into `requirements-training.txt`.
* Fixed the broken links workflow so real link failures now trigger the issue creation and failure path.
* Added `MODEL_FAMILIES.md`, a shared model registry in `utils/model_families.py`, notebook `07` for side by side model family comparison, and notebooks `08` through `13` for Gemma, DeepSeek, Mistral, Qwen, Llama, and Kimi family specific full examples.
* Added `requirements-model-families.txt` so the newer family specific notebooks can use a newer `transformers` version without changing the original beginner notebook stack.
