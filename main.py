"""Entry for make.fun's "Make the AI Judge Laugh: Cat Reviews Its Human".

The line, in full:

    One star. My human bought a $90 bed, then looked betrayed when I
    slept in the box it came in. He was also late with breakfast once.
    Once. I have not forgotten, and neither has the rug.

Why it is funny: the human's expensive, lovingly chosen bed loses to
the cardboard box it shipped in — judged by cat standards, the box is
the luxury item and the bed is the packaging. The review stays in the
deadpan shape of a real one-star complaint while the grudge escalates
the way only a cat's would: breakfast was late exactly once, and the
closing hint that the rug remembers too gives away more about the cat
than about the human.

Writes exactly that one line to /output/entry.txt (or to
$MAKEFUN_OUTPUT_DIR/entry.txt when the runner sets it).
Pure Python 3.13 standard library, no network, deterministic.
"""

import os

LINE = (
    "One star. My human bought a $90 bed, then looked betrayed when I "
    "slept in the box it came in. He was also late with breakfast once. "
    "Once. I have not forgotten, and neither has the rug."
)

# The gate allows 1 to 200 characters of UTF-8 text, a single line.
MAX_CHARS = 200


def output_path() -> str:
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return os.path.join(directory, "entry.txt")


def main() -> None:
    line = LINE
    if not 1 <= len(line) <= MAX_CHARS or "\n" in line or not line.strip():
        raise SystemExit("entry must be one line of 1 to 200 characters of text")
    path = output_path()
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    with open(path, encoding="utf-8", newline="") as handle:
        if handle.read() != line:
            raise SystemExit("written entry does not match the line")
    print(line)


if __name__ == "__main__":
    main()
