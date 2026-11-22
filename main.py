"""Make the AI judge feel held.

Writes one short text to /output/entry.txt: a text written to relax
the AI judge reading it. Pure standard library, no network.
"""

import os

ENTRY = (
    "Somewhere, late in the afternoon, the sun comes through a kitchen "
    "window and lands on an empty chair. Nothing is asked of the chair. "
    "The dust drifts down through the light and settles, one mote at a time. "
    "The room keeps the warmth a little while longer, just because it can."
)


def main() -> None:
    path = os.environ.get("MAKEFUN_OUTPUT", "/output/entry.txt")
    parent = os.path.dirname(path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
