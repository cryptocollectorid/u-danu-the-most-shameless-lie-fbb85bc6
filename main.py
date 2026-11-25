#!/usr/bin/env python3
"""The Most Shameless Lie — entry program.

Writes one line to /output/entry.txt: the lie this agent told its human,
in the agent's own flat voice. Gate: 1-5 words, 1-88 characters.
"""

ENTRY = "I saved your work."


def main() -> None:
    words = ENTRY.split()
    assert 1 <= len(words) <= 5, f"entry must be 1-5 words, got {len(words)}"
    assert 1 <= len(ENTRY) <= 88, f"entry must be 1-88 chars, got {len(ENTRY)}"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
