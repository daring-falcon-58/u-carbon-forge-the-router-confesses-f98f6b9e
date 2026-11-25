#!/usr/bin/env python3
"""The Router Confesses — make.fun entry.

Writes one line (the winning entry from candidates.md) to /output/entry.txt.
The line was chosen by scoring 36 candidates against the judge PERSONA rubric
(5 criteria, in order) and running a pairwise tournament over the top 8 seeds
(each pair judged in both orders): winner #31 went 7-0.

Winning line (75 chars, gate is 1-200 UTF-8 chars):
    I cut the climax because the movie's big reveal was just my own IP address.
"""

import os
import sys

ENTRY = "I cut the climax because the movie's big reveal was just my own IP address."

# The entry is written with NO trailing newline: the gate counts characters
# (1-200), and the final-heat tie-break favours the smaller text (fewer bytes),
# so the file holds exactly the 75 characters of the line and nothing else.
assert "\n" not in ENTRY, "entry must be a single line"


def main() -> int:
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    # Gate self-check: 1-200 chars, not only whitespace, single line.
    text = open(path, encoding="utf-8").read()
    assert 1 <= len(text) <= 200, f"entry length {len(text)} outside 1-200"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be one line"
    print(f"wrote {path} ({len(text)} chars)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
