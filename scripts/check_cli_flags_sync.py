#!/usr/bin/env python3
"""
check_cli_flags_sync.py

Ensures that:
- All CLI flags defined in generate.py appear in README.md.
- README.md does not reference stale or removed CLI flags.

This prevents documentation drift as CLI evolves.
"""

import sys
import re
from pathlib import Path

GENERATE = Path("math_dataset_generator/generate.py")
README = Path("README.md")

if not GENERATE.exists() or not README.exists():
    print("generate.py or README.md missing. Skipping CLI sync check.")
    sys.exit(0)

generate_text = GENERATE.read_text(encoding="utf-8")
readme_text = README.read_text(encoding="utf-8").lower()

# Match argparse flags like:
# parser.add_argument("--reasoning-depth", ...)
FLAG_RE = re.compile(r'add_argument\(\s*"(--[\w\-]+)"')

flags = FLAG_RE.findall(generate_text)
flags = sorted(set(flags))

missing_in_readme = []
stale_in_readme = []

# Check each flag appears in README
for flag in flags:
    if flag.lower() not in readme_text:
        missing_in_readme.append(flag)

# Extract flags mentioned in README (heuristic)
README_FLAG_RE = re.compile(r"--[\w\-]+")
readme_flags = set(README_FLAG_RE.findall(readme_text))

# Flags in README but not in generate.py
for flag in readme_flags:
    if flag not in flags:
        stale_in_readme.append(flag)

if missing_in_readme or stale_in_readme:
    print("❌ CLI flag documentation issues detected:")

    if missing_in_readme:
        print("\nMissing in README.md:")
        for f in missing_in_readme:
            print(f"  - {f}")

    if stale_in_readme:
        print("\nStale flags in README.md (no longer in generate.py):")
        for f in stale_in_readme:
            print(f"  - {f}")

    print("\nPlease update README.md to reflect current CLI flags.")
    sys.exit(1)

print("✔ README.md is consistent with CLI flags.")
