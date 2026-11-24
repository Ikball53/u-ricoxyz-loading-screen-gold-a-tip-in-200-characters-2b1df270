#!/usr/bin/env python3
"""Loading Screen Gold — writes one loading-screen tip to /output/entry.txt.

The tip is a single line for stressed developers and AI coding agents:
first-person agent voice, a concrete rename with a real import count,
and a punchline that lands on the spinner itself.
"""

import os

TIP = (
    "Tip: I renamed utils.py, fixed all 14 imports, and we're still "
    "staring at this spinner together. Breathe \u2014 it's as lost as we are."
)


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters, no trailing newline.
    assert 1 <= len(TIP) <= 200 and "\n" not in TIP, "tip violates the gate"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as handle:
        handle.write(TIP)


if __name__ == "__main__":
    main()
