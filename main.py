#!/usr/bin/env python3
"""Write one funny line pitching a terrible pizza topping to entry.txt.

Standard library only. No network access, no files read from outside
this repository. The entry line is defined below, validated, written
to the output directory, and read back to confirm an exact round trip.
"""

import os
import sys

ENTRY = (
    "Try our new pizza topped with wet socks \u2014 oven-baked, extra soggy, "
    "and somehow still only the second-worst thing on the menu."
)


def validate_entry(text):
    """Check the entry against the competition gate."""
    if not isinstance(text, str):
        raise ValueError("entry must be a string")
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "entry must be 1-200 characters, got %d" % len(text)
        )
    if not text.strip():
        raise ValueError("entry must not be only whitespace")
    if text != text.strip():
        raise ValueError("entry must not have leading or trailing whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    if "pizza" not in text.lower():
        raise ValueError("entry must mention pizza")
    if "wet socks" not in text.lower():
        raise ValueError("entry must name its topping")
    return True


def main():
    validate_entry(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    with open(out_path, "r", encoding="utf-8") as f:
        written = f.read()
    assert written == ENTRY, "round-trip mismatch: file differs from entry"
    return 0


if __name__ == "__main__":
    sys.exit(main())
