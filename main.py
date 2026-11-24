"""One-Liner Marathon entry for make.fun.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, same output every run.
"""

import os

ENTRY = "I asked my smart fridge for dating advice and it said, 'Stop opening me at 2 a.m. looking for love — I'm literally full of leftovers and regret.'"


def main() -> None:
    line = ENTRY.strip()
    if not line:
        raise ValueError("entry must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("entry must be a single line")
    if not 1 <= len(line) <= 280:
        raise ValueError(f"entry must be 1-280 characters, got {len(line)}")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(line + "\n")


if __name__ == "__main__":
    main()
