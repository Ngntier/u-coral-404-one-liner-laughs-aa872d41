"""One-Liner Laughs entry: write a single original joke to entry.txt.

The joke is a fixed string written deterministically to the output
directory given by MAKEFUN_OUTPUT_DIR (default /output). No network,
no randomness, no input read: the program always emits the same line.
"""

import os

JOKE = (
    "I asked my smart fridge for a midnight snack and it sighed, opened "
    "the door, and said, 'We both know you're not hungry \u2014 you're just "
    "avoiding a deadline.'"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE + "\n")


if __name__ == "__main__":
    main()
