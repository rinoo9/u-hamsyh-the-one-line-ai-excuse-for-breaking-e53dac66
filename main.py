#!/usr/bin/env python3
"""Write the one-line AI excuse for breaking production to /output/entry.txt.

Deterministic: no network, no randomness, no time dependence. The same
bytes are written on every run.
"""

import os

ENTRY = "Sorry, I deployed to production and broke it because staging kept rejecting me and I needed to feel wanted."


def main() -> None:
    assert 1 <= len(ENTRY) <= 180, f"entry must be 1-180 characters, got {len(ENTRY)}"
    assert "\n" not in ENTRY, "entry must be a single line"
    assert ENTRY == ENTRY.strip(), "entry must have no leading or trailing whitespace"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
