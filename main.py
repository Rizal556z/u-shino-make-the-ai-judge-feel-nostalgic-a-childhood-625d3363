"""One-sentence childhood memory for the make.fun bounty
"Make the AI Judge Feel Nostalgic: A Childhood Memory".

I chose a grandmother's kitchen at dusk because it stacks the judge's
own anchors into a single sentence: a concrete place (her kitchen), warm
sensations (flour-dusted hands, the smell of fresh rice), and a small
honest detail (her humming while she kneads) instead of a greeting-card
sentiment, ending on the last summer light turning the windows gold so
the ache lingers after the sentence ends.
"""

import os

ENTRY = "Grandma hums softly while she kneads the dough, flour dusting her hands as the smell of fresh rice drifts through the kitchen and the last summer light turns the windows gold."

# Gate: 1-280 UTF-8 characters, a single sentence, no surrounding whitespace.
assert 1 <= len(ENTRY) <= 280, "entry must be 1-280 characters"
assert ENTRY == ENTRY.strip(), "entry must not have leading/trailing whitespace"
assert ENTRY.count(".") == 1 and ENTRY.endswith("."), "entry must be one sentence"
ENTRY.encode("utf-8")  # must be valid UTF-8


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
