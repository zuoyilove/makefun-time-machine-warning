#!/usr/bin/env python3
"""Funniest Time Machine Warning Label.

Writes a single warning label for a time machine to /output/entry.txt.
The label is a straight-faced safety notice whose punchline lands on the
last few words: a real hazard of time travel (meeting your own past self)
turned into the joke.
"""

from pathlib import Path

LABEL = (
    "WARNING: Do not wave at your past self. "
    "He is armed, bitter, and already blames you for this trip."
)

MAX_CHARS = 120
OUT_PATH = Path("/output/entry.txt")


def validate(text: str) -> str:
    stripped = text.strip()
    assert stripped, "label must not be blank"
    assert "\n" not in stripped, "label must be a single line"
    assert len(stripped) <= MAX_CHARS, f"label is {len(stripped)} chars, over {MAX_CHARS}"
    return stripped


def main() -> None:
    label = validate(LABEL)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(label + "\n", encoding="utf-8")
    print(f"wrote {len(label)} chars to {OUT_PATH}")


if __name__ == "__main__":
    main()
