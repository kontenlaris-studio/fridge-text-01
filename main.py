#!/usr/bin/env python3
"""The 3AM Fridge Text — writes the 3 a.m. text message to /output/entry.txt.

The text: a 3 a.m. message sent standing in front of the fridge —
expired milk, drunk anyway, with instructions for the morning after.
"""
import os

TEXT = "3 a.m. text: the milk expired yesterday but I'm drinking it anyway. If I don't reply by morning, tell the fridge it did this."

# The entry is exactly one text message: 125 characters, no greeting,
# no sign-off — the fridge is the only witness, and it is implicated.


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")
    print(f"wrote {path}")


if __name__ == "__main__":
    main()
