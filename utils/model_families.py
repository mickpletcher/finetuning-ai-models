from __future__ import annotations

from dataclasses import asdict, dataclass


@dataclass(frozen=True)
class ModelFamilyProfile:
    family: str
    example_model_id: str
    comparison_model_id: str
    notebook_slug: str
    prompt_strategy: str
    tokenizer_notes: str
    license_name: str
    gated_access: str
    full_example_hardware: str
    training_note: str
    trust_remote_code: bool = False
    use_system_prompt: bool = True


MODEL_FAMILIES = [
    ModelFamilyProfile(
        family="Gemma",
        example_model_id="google/gemma-2-2b-it",
        comparison_model_id="google/gemma-2-2b-it",
        notebook_slug="08-gemma-family-finetune",
        prompt_strategy="Use the tokenizer chat template. Keep turns short and instruction focused.",
        tokenizer_notes="Gemma instruct checkpoints expect role based chat formatting through tokenizer.apply_chat_template.",
        license_name="Gemma license",
        gated_access="Usually gated on Hugging Face. Accept the model terms and log in before download.",
        full_example_hardware="QLoRA on 2B class checkpoints is practical on roughly 12 to 16 GB VRAM. CPU only is for inspection, not real training.",
        training_note="Good first family for a real open weight instruct fine tune once access is approved.",
    ),
    ModelFamilyProfile(
        family="DeepSeek",
        example_model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        comparison_model_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-1.5B",
        notebook_slug="09-deepseek-family-finetune",
        prompt_strategy="Prefer the tokenizer chat template when available. Keep reasoning datasets narrow and consistent.",
        tokenizer_notes="DeepSeek checkpoints can differ by base family. Use the actual tokenizer for the chosen checkpoint instead of assuming one universal template.",
        license_name="MIT style or Apache style depending on checkpoint",
        gated_access="Most DeepSeek open checkpoints are not gated, but verify each model card before use.",
        full_example_hardware="1.5B class distilled checkpoints are the easiest entry point and fit a single consumer GPU for QLoRA.",
        training_note="Use smaller distilled checkpoints for learning. Do not start with the largest reasoning releases.",
    ),
    ModelFamilyProfile(
        family="Mistral",
        example_model_id="mistralai/Mistral-7B-Instruct-v0.3",
        comparison_model_id="mistralai/Mistral-7B-Instruct-v0.3",
        notebook_slug="10-mistral-family-finetune",
        prompt_strategy="Use the tokenizer chat template. Mistral instruct formatting and tokenizer handling changed across releases, so avoid manual prompt wrappers.",
        tokenizer_notes="Recent Mistral instruct models are best handled through the shipped tokenizer template rather than handwritten prompt strings.",
        license_name="Apache 2.0 for the mainstream open Mistral releases used here",
        gated_access="Usually open access on Hugging Face, but still verify the exact model card.",
        full_example_hardware="7B class Mistral fine tuning is a real GPU job. Expect roughly 16 to 24 GB VRAM for QLoRA and more for full precision LoRA.",
        training_note="Stronger general quality than the tiny teaching models, but no longer beginner cheap.",
    ),
    ModelFamilyProfile(
        family="Qwen",
        example_model_id="Qwen/Qwen2.5-1.5B-Instruct",
        comparison_model_id="Qwen/Qwen2.5-1.5B-Instruct",
        notebook_slug="11-qwen-family-finetune",
        prompt_strategy="Use the tokenizer chat template. Qwen instruct models are chat native and handle role formatted datasets well.",
        tokenizer_notes="Qwen chat formatting is clean and consistent in modern tokenizer templates, which makes it a good teaching family.",
        license_name="Apache 2.0 on common Qwen2.5 instruct checkpoints",
        gated_access="Usually open access on Hugging Face.",
        full_example_hardware="1.5B class Qwen models are practical for single GPU QLoRA and are one of the easier families to teach with.",
        training_note="Good balance of ease, quality, and open access.",
    ),
    ModelFamilyProfile(
        family="Llama",
        example_model_id="meta-llama/Llama-3.2-1B-Instruct",
        comparison_model_id="meta-llama/Llama-3.2-1B-Instruct",
        notebook_slug="12-llama-family-finetune",
        prompt_strategy="Use the tokenizer chat template and expect access controls. Keep your dataset style aligned to the instruct checkpoint behavior.",
        tokenizer_notes="Llama instruct checkpoints use a model specific chat template and should not be fine tuned with a generic Alpaca wrapper by default.",
        license_name="Llama community license",
        gated_access="Gated on Hugging Face. You need to request or accept access before download.",
        full_example_hardware="The 1B and 3B Llama 3.2 instruct models are reasonable teaching targets. Larger Llama checkpoints need much more VRAM.",
        training_note="Good family to teach gated access, license review, and prompt template discipline.",
    ),
    ModelFamilyProfile(
        family="Kimi",
        example_model_id="moonshotai/Moonlight-16B-A3B-Instruct",
        comparison_model_id="moonshotai/Kimi-K2-Instruct",
        notebook_slug="13-kimi-family-finetune",
        prompt_strategy="Use the tokenizer chat template and trust remote code when the model card requires it.",
        tokenizer_notes="For the Moonshot or Kimi family, tokenizer behavior varies across releases. Use the tokenizer directly and inspect the rendered chat template before training.",
        license_name="Model specific Moonshot license",
        gated_access="Access rules vary. Verify the exact model card before training or redistribution.",
        full_example_hardware="Kimi K2 scale models are not beginner local fine tune targets. This repo uses Moonlight-16B-A3B-Instruct as the teachable example from the same vendor family.",
        training_note="Treat Kimi K2 as compare only for most learners. Use the lighter Moonshot family checkpoint for the actual walkthrough.",
        trust_remote_code=True,
    ),
]


def get_model_family(name: str) -> ModelFamilyProfile:
    for profile in MODEL_FAMILIES:
        if profile.family.lower() == name.lower():
            return profile
    raise KeyError(f"Unknown model family: {name}")


def get_model_family_rows() -> list[dict[str, str | bool]]:
    return [asdict(profile) for profile in MODEL_FAMILIES]
