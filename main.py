#!/usr/bin/env python3
"""Make the AI Judge Feel Nostalgic: A Childhood Memory.

Writes one sentence (140 chars) recalling a childhood memory to
/output/entry.txt. Gate: UTF-8 text of 1 to 280 characters, not only
whitespace, a single sentence.

Tournament (specificity / surprise / freshness, 1-5):
  1. Grandma's kitchen, fresh rice and woodsmoke, humming at six - 4/3/3
  2. Grandfather's sandals on the tiles, rambutan in a plastic bag - 5/4/4
  3. Bicycle chain broke, father carried the bike home on his shoulder - 5/4/4
  4. WINNER: rainy season, ginger tea, fogged window, drawn faces - 5/5/5
  5. Ice-cream cart bell at four, coins in mother's apron pocket - 5/4/4
  6. Power out, candlelight dinner, father's childhood house story - 5/5/4

Winner: concrete sensation (ginger tea steam, fogged window), a
surprising turn (the faces are pretended portraits of her), and a
small honest detail rather than greeting-card sentiment.
"""

import os
import sys

ENTRY = (
    "Every rainy season my mother boiled ginger tea, and the steam "
    "fogged the window where I drew faces that she pretended were "
    "portraits of her."
)

MAX_CHARS = 280


def check(text: str) -> None:
    """Validate the entry against the gate: 1-280 chars, single sentence."""
    if not text or not text.strip():
        raise SystemExit("entry is empty or whitespace only")
    if len(text) > MAX_CHARS:
        raise SystemExit(f"entry is {len(text)} chars, over the 280 limit")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be a single sentence ending in a period")
    if "\n" in text:
        raise SystemExit("entry must be a single line")


def main(argv) -> int:
    check(ENTRY)
    if "--check" in argv[1:]:
        # Dry run: validate only, write nothing.
        print(f"check OK: {len(ENTRY)} chars "
              f"({len(ENTRY.encode('utf-8'))} bytes), single sentence")
        return 0
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(ENTRY)
    # Verify the round trip: what we wrote is byte-for-byte what we meant.
    with open(path, "r", encoding="utf-8") as fh:
        written = fh.read()
    if written != ENTRY:
        raise SystemExit("round-trip mismatch: entry.txt differs from ENTRY")
    print(f"wrote {len(ENTRY)} chars ({len(ENTRY.encode('utf-8'))} bytes) to {path}")
    print(ENTRY)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
