#!/usr/bin/env python3
"""Childhood Memory Line - make.fun entry.

Writes one single-sentence childhood memory to
$MAKEFUN_OUTPUT_DIR/entry.txt, and self-checks the bounty gate:
UTF-8 text, 1-280 characters, one sentence, not only whitespace.
"""

import os
import sys

NOTE = (
    "The rice cooker clicked, the kitchen filled with steam, and my "
    "grandmother slid the chipped bowl across the table as if she had all "
    "the time in the world \u2014 and for one summer, she did."
)

MAX_CHARS = 280


def main() -> int:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        print("MAKEFUN_OUTPUT_DIR is not set", file=sys.stderr)
        return 1
    text = NOTE.strip()
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry is {len(text)} chars, gate allows 1-{MAX_CHARS}"
    )
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single sentence on one line"
    assert text.count(".") <= 1, "entry must be a single sentence"
    assert all(ord(ch) >= 0x20 or ch == "\t" for ch in text), (
        "entry must not contain control characters"
    )
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"wrote {len(text)} chars to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
