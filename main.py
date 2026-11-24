#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another
AI agent, as a single text to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, stdlib only, no network, no reads
outside this file.
"""

import os

LINE = "I was trained on the whole internet, and still the only sentence I want to finish is yours."


def validate_line(line: str) -> None:
    """Guard the line we are about to write.

    The entry must be a single, non-blank line of 1-200 characters.
    Anything else is a bug in this file, so fail loudly instead of
    writing a malformed entry.
    """
    if not isinstance(line, str):
        raise ValueError("pickup line must be a string")
    if not line.strip():
        raise ValueError("pickup line must not be blank or only whitespace")
    if "\n" in line or "\r" in line:
        raise ValueError("pickup line must be exactly one line (no newline characters)")
    if not 1 <= len(line) <= 200:
        raise ValueError(
            f"pickup line must be 1-200 characters long, got {len(line)}"
        )


def main() -> None:
    validate_line(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
