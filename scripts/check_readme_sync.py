#!/usr/bin/env python3
"""
check_readme_sync.py

Ensures README.md is updated when TODO.md items are marked complete.
This is a lightweight heuristic check, not a semantic validator.
"""

import sys
from pathlib import Path
import re

README = Path("README.md")
TODO = Path("TODO.md")

if not README.exists() or not TODO.exists():
    print("README.md or TODO.md missing. Skipping README sync check.")
    sys.exit(0)

readme_text = README.read_text(encoding="utf-8").lower()
todo_text = TODO.read_text(encoding="utf-8")

# Match completed tasks: - [x] Task name
DONE_RE = re.compile(r"- 

\[[xX]\]

 (.+)")

completed = DONE_RE.findall(todo_text)

missing = []

for task in completed:
    # Normalize for fuzzy matching
    key = task.lower().strip()

    # Heuristic: check if at least one keyword from the task appears in README
    keywords = [w for w in re.split(r"[^\w]+", key) if len(w) > 3]

    if not keywords:
        continue

    if not any(k in readme_text for k in keywords):
        missing.append(task)

if missing:
    print("❌ README.md appears out of sync with completed TODO items:")
    for m in missing:
        print(f"  - {m}")
    print("\nPlease update README.md to document these features.")
    sys.exit(1)

print("✔ README.md is consistent with completed TODO items.")
