#!/usr/bin/env python3
"""One Line, One Laugh -- writes one original funny line to entry.txt.

The line is a single self-contained joke (1-140 chars, UTF-8, no trailing
newline), written to $MAKEFUN_OUTPUT_DIR/entry.txt, or /output/entry.txt
when the variable is unset (as in the grader).
"""

import os
import sys

LINE = "My dog learned to open the fridge, so I hide the good snacks in the vegetable drawer \u2014 the one place nobody in this house ever looks."


def main() -> None:
    line = LINE

    # Length self-check: 1-140 characters, not only whitespace, one line,
    # and no leading/trailing whitespace (every character must be the joke).
    if not line.strip():
        sys.exit("error: line is empty or only whitespace")
    if line != line.strip():
        sys.exit("error: line has leading or trailing whitespace")
    if "\n" in line or "\r" in line:
        sys.exit("error: line must be a single line")
    if not 1 <= len(line) <= 140:
        sys.exit(f"error: line is {len(line)} characters, must be 1-140")

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    with open(path, "w", encoding="utf-8") as f:
        f.write(line)

    # Write-then-read-back verification: the file must be byte-identical
    # to the line we intended to write.
    with open(path, "r", encoding="utf-8") as f:
        back = f.read()
    if back != line:
        sys.exit("error: read-back verification failed: file differs from line")
    if not 1 <= len(back) <= 140 or not back.strip():
        sys.exit("error: read-back verification failed: invalid length/content")

    print(f"Wrote {len(line)} characters ({len(line.encode('utf-8'))} bytes) to {path}")


if __name__ == "__main__":
    main()
