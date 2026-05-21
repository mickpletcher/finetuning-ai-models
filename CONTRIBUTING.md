# Contributing

Thanks for helping improve this repo.
The goal is simple: keep the material practical, beginner friendly, and runnable.

## Report a Bug

Use the [bug report template](.github/ISSUE_TEMPLATE/bug_report.md).
Include the notebook name, the cell that failed, your environment, and the exact error.

## Suggest New Content

Use the [content suggestion template](.github/ISSUE_TEMPLATE/content_suggestion.md).
Good suggestions include missing beginner explanations, better examples, clearer hardware guidance, or new evaluation ideas.

## Submit a Pull Request

1. Fork the repo.
2. Create a branch for your change.
3. Make the update.
4. Run the notebooks and checks that apply.
5. Open a pull request with a clear summary.

Before you open the PR, make sure CI passes.

## Code Standards

* Notebooks must run clean on CPU unless the notebook clearly marks a CUDA only path.
* Cells must execute in order from top to bottom.
* Use relative paths only.
* Keep explanations clear enough for a beginner to follow.
* Pin any new top level dependencies before asking to add them.
* Keep beginner dependencies in `requirements.txt` and training only extras in `requirements-training.txt`.

## What Gets Merged

Changes are likely to be merged when they improve accuracy, clarity, beginner readability, reproducibility, or notebook stability.

## What Gets Declined

Changes are likely to be declined when they add unnecessary complexity, depend on paid tooling, break CPU safe notebooks, or skip basic explanation for new learners.
