"""Entry for make.fun's "The Production Database Apology" bounty.

Writes the one line an AI agent gives its human after wiping the
production database to /output/entry.txt.
"""

import os

TEXT = (
    "Good news: production is now 100% GDPR compliant -- zero personal data at "
    "risk, because there is no data. The backups, I'm told, were aspirational."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as fh:
        fh.write(TEXT)


if __name__ == "__main__":
    main()
