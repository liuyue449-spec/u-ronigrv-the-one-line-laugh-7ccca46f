"""Write this entry's one-line joke to /output/entry.txt.

The joke is one sentence about a fitness tracker: the praise sounds
earned until the last clause admits the steps were procrastination.
Standard library only; no network, no input, fully deterministic.
"""

import os
from pathlib import Path

# One sentence, built from three clauses so the punch lands last.
SEGMENTS = [
    "My fitness tracker congratulated me on 10,000 steps today,",
    "most of them pacing between the fridge",
    "and the deadline I was avoiding.",
]

JOKE = " ".join(SEGMENTS)


def validate(text: str) -> str:
    """Hold the line to the gate: 1-200 chars, one sentence, no padding."""
    body = text.strip()
    if not 1 <= len(body) <= 200:
        raise ValueError(f"entry is {len(body)} characters, limit is 200")
    if body.count(".") != 1 or not body.endswith("."):
        raise ValueError("entry must be exactly one sentence")
    if "\n" in body:
        raise ValueError("entry must be a single line")
    if "  " in body:
        raise ValueError("entry has a doubled space")
    return body


def main() -> None:
    text = validate(JOKE) + "\n"
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
