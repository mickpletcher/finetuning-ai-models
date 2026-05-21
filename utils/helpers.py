from __future__ import annotations

import json
from pathlib import Path

import torch


ALPACA_TEMPLATE = """### Instruction:
{instruction}

### Input:
{input_text}

### Response:
{output}"""


REPO_ROOT = Path(__file__).resolve().parent.parent
DATASETS_DIR = REPO_ROOT / "datasets"
OUTPUT_DIR = REPO_ROOT / "output"
PREPARED_DATA_DIR = OUTPUT_DIR / "prepared_data"
LORA_ADAPTER_DIR = OUTPUT_DIR / "lora-adapter"
QLORA_ADAPTER_DIR = OUTPUT_DIR / "qlora-adapter"
MERGED_MODEL_DIR = OUTPUT_DIR / "merged-model"
CHECKPOINTS_DIR = OUTPUT_DIR / "checkpoints"
QLORA_CHECKPOINTS_DIR = OUTPUT_DIR / "qlora-checkpoints"


def get_device() -> str:
    """Return the best available device for model work."""
    return "cuda" if torch.cuda.is_available() else "cpu"


def print_trainable_parameters(model) -> None:
    """Print trainable and total parameter counts for a model."""
    trainable_params = 0
    total_params = 0
    for parameter in model.parameters():
        total_params += parameter.numel()
        if parameter.requires_grad:
            trainable_params += parameter.numel()

    percentage = 100 * trainable_params / total_params if total_params else 0
    print(
        f"trainable params: {trainable_params:,} | total params: {total_params:,} | trainable%: {percentage:.2f}"
    )


def format_alpaca(instruction: str, input_text: str, output: str) -> str:
    """Format one record using the common Alpaca prompt layout."""
    return ALPACA_TEMPLATE.format(
        instruction=instruction.strip(),
        input_text=input_text.strip(),
        output=output.strip(),
    )


def load_jsonl(path: str | Path) -> list[dict]:
    """Load a JSONL file and return its rows as dictionaries."""
    records = []
    with Path(path).open("r", encoding="utf-8") as handle:
        for line in handle:
            line = line.strip()
            if not line:
                continue
            records.append(json.loads(line))
    return records
