#!/usr/bin/env python3
"""Invent a Word We Need — writes one line to /output/entry.txt.

The coinage is "tabnesia": the blend of "tab" and "amnesia" names a gap
English has no word for — opening a browser tab and instantly forgetting
what you meant to look up, so you just stare at it. Everyone who works
with a browser has felt it at once. The word is sayable, spellable and
memorable, and the definition lands in a single reading with no example
needed.

Craft note on the revision: the first draft defined it as "opening a
browser tab, then staring at it" — but the staring is the symptom, not
the gap. The revision names the forgetting itself ("having already
forgotten what you meant to look up"), which is the exact moment the
reader recognises, and it keeps the em-dash structure so the word and
its definition read as one dictionary line.
"""

import os

# One dictionary line: the coined word, an em dash, then a definition
# that lands in a single reading with no example needed.
LINE = "tabnesia — opening a browser tab, then staring at it, having already forgotten what you meant to look up."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
