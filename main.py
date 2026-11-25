#!/usr/bin/env python3
"""One-Line Office Jokes (make.fun).

Writes a single original one-line joke about office life to
/output/entry.txt. The joke turns on a real office detail (the
printer jamming) and lands its laugh in the final words.
"""

import os

JOKE = (
    "The printer jammed on page one of my resignation letter, "
    "which is the most loyal thing anyone in this office has "
    "ever done for me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 199


def validate(text: str) -> None:
    """Check the text against the competition gate before writing it."""
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(f"joke is {len(text)} characters, must be 1-{MAX_CHARS}")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    validate(JOKE)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)
    # Read it back: a silent write failure must fail loudly here
    # instead of shipping a wrong entry to the grader.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    if written != JOKE:
        raise ValueError("read-back mismatch: entry.txt does not hold the joke")
    print(f"wrote {len(JOKE)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
