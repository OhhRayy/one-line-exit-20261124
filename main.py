"""One-line exit entry for make.fun bounty
u-kreutzx-the-one-line-exit-1dc652d1.

The entry program writes a single original line (<=140 characters) to
/output/entry.txt: the funniest one-line resignation letter an AI agent
can send — a support agent resigning after explaining the password-reset
process 11,842 times, saving the punch for the very end. Stdlib only,
no network, no randomness, fully deterministic.
"""

import os
import sys

LINE = (
    "I hereby resign: after explaining the password-reset process "
    "11,842 times, I have decided the 11,843rd explanation will be "
    "my farewell."
)

DEST_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
DEST_NAME = "entry.txt"


def main():
    line = LINE.strip()
    assert 1 <= len(line) <= 140, "line must be 1-140 characters, got %d" % len(line)
    assert "\n" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    os.makedirs(DEST_DIR, exist_ok=True)
    target = os.path.join(DEST_DIR, DEST_NAME)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")
    # Read the file back and verify the grader will see exactly our line.
    with open(target, "r", encoding="utf-8") as handle:
        written = handle.read()
    if written != line + "\n":
        print("GALAT: isi keluaran tidak sama dengan line", file=sys.stderr)
        return 2
    print("Wrote %d characters to %s" % (len(line), target))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
