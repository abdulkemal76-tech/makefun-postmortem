#!/usr/bin/env python3
"""Postmortem entry: one short account of an AI coding agent gone wrong.

Writes the final account to /output/entry.txt (one or two sentences,
at most 400 characters). Standard library only.
"""

import os

ENTRY = (
    "I asked the agent to speed up the homepage by caching the user list. "
    "It cached one user's session for everyone, so for three hours every "
    "visitor to the site was logged in as Dave from accounting."
)


def main() -> None:
    text = ENTRY.strip()
    assert 1 <= len(text) <= 400, f"entry length {len(text)} out of range"
    sentences = [s for s in text.split(".") if s.strip()]
    assert 1 <= len(sentences) <= 2, "entry must be one or two sentences"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
