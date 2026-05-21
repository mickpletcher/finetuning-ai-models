# Datasets

This folder holds training data used by the notebooks.

## Expected format

The sample file uses Alpaca style JSONL. Each line is one JSON object with these keys:

```json
{"instruction": "...", "input": "", "output": "..."}
```

Use `instruction` for the task, `input` for optional extra context, and `output` for the target answer.

## Notes

Keep examples consistent.
Keep answers in the tone and format you want the model to learn.
Use UTF 8 text and one JSON object per line.
