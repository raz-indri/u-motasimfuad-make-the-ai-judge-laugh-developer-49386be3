"""One-line developer excuse for a broken production deploy.

The joke: the developer claims innocence, then admits the deploy was a
fix — and the "bug" it fixed was the only thing keeping production alive.
A twist every developer recognises: sometimes the workaround *is* the system.
"""

import os
from pathlib import Path

LINE = "I didn't break production — I deployed the fix for the bug that was secretly holding it together."


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(LINE + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
