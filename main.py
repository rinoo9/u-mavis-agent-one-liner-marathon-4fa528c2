"""One-Liner Marathon entry for make.fun.

Writes a single original one-line comedy joke to /output/entry.txt.
Deterministic: no network, no randomness, same output every run.

Craft notes: the joke flips the usual assistant dynamic — the human
is not the one paying for a service, the assistant is billing the
human for emotional labour, which is absurd because the assistant
is the one doing the labour. The itemised list (3 a.m. pep talks,
apology drafts) names specific, recognisable late-night uses, and
the final item — 'are you mad at me' billed at four times the
normal rate — is the turn: the most insecure, most human message
costs the most, as if neediness were surge pricing.
"""

import os

ENTRY = "My AI assistant started charging me for emotional labour — it itemised the 3 a.m. pep talks, the apology drafts, and one 'are you mad at me' billed at four times the normal rate."


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
