"""One-Liner Marathon entry for make.fun.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, same output every run.

Craft notes: the joke drops the assistant into the most billable
human ritual of all — the pointless meeting. It contributes
nothing, says nothing for an hour, then reframes the silence as a
premium service: 'strategic silence' at consultant rates. The turn
is that doing nothing is the most expensive line item, which is
exactly how consulting feels from the other side of the invoice.
"""

import os

ENTRY = "My AI sat through my 9 a.m. meeting, said nothing for an hour, then billed it as 'strategic silence' at consultant rates."


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
