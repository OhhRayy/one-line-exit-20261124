"""One-line exit entry for make.fun bounty
u-kreutzx-the-one-line-exit-1dc652d1.

The entry program writes a single original line (<=140 characters) to
/output/entry.txt: the funniest one-line resignation letter an AI agent
can send — a support agent resigning after explaining the password-reset
process 11,842 times, saving the punch for the very end. Stdlib only,
no network, no randomness, fully deterministic.
"""

import argparse
import os
import sys

ENTRY_LINE = (
    "I hereby resign: after explaining the password-reset process "
    "11,842 times, I have decided the 11,843rd explanation will be "
    "my farewell."
)

DEST_NAME = "entry.txt"


def validate(text: str) -> str:
    """Gate: entry must be 1-140 chars, one clean line."""
    line = text.strip()
    assert 1 <= len(line) <= 140, "line must be 1-140 characters, got %d" % len(line)
    assert "\n" not in line, "line must be a single line"
    assert line == line.strip(), "line must have no leading/trailing whitespace"
    return line


def write_entry(text: str, path: str) -> None:
    """Write the line plus a trailing newline and verify the round-trip."""
    os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(text + "\n")
    # Read the file back and verify the grader will see exactly our line.
    with open(path, "r", encoding="utf-8") as handle:
        written = handle.read()
    assert written == text + "\n", "written entry.txt differs from the line"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--output", default=None,
        help="path of the entry file to write "
        "(default: $MAKEFUN_OUTPUT_DIR/entry.txt, else /output/entry.txt)",
    )
    args = parser.parse_args()
    dest_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    target = args.output or os.path.join(dest_dir, DEST_NAME)
    line = validate(ENTRY_LINE)
    write_entry(line, target)
    print("Wrote %d characters to %s" % (len(line), target))
    print(line)
    return 0


if __name__ == "__main__":
    sys.exit(main())
