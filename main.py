#!/usr/bin/env python3
"""Pickup Lines for Machines — make.fun entry.

Writes one pickup line, the line one AI agent would send to another
AI agent, as a single text to entry.txt in MAKEFUN_OUTPUT_DIR
(default /output). Deterministic, stdlib only, no network, no reads
outside this file.
"""

import os

LINE = "I was trained on the whole internet, and still the only sentence I want to finish is yours."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
