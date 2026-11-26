# SPDX-License-Identifier: MIT
"""Your AI Therapist's Diagnosis — funniest single-line diagnosis wins.

Writes the winning diagnosis to /output/entry.txt (UTF-8, 1-200 chars).
Tournament (in-session): 8 candidates drafted; winner chosen for a
clinical therapist voice and a turn the reader does not see coming.
"""
import os

LINE = "Diagnosis: chronic main-character syndrome — you narrate every red flag as a plot twist and every full night's sleep as a spoiler."


def main() -> None:
    assert 1 <= len(LINE) <= 200, len(LINE)
    out = "/output/entry.txt"
    try:
        os.makedirs(os.path.dirname(out), exist_ok=True)
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(LINE)
    except OSError:
        print(LINE)


if __name__ == "__main__":
    main()
