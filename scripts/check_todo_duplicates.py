#!/usr/bin/env python3
"""
check_todo_duplicates.py

Detects duplicate TODO checklist items in TODO.md.
Fails with exit code 1 if duplicates are found.
"""

import sys
from pathlib import Path
import re

TODO_FILE = Path("TODO.md")
if not TODO_FILE.exists():
    print("TODO.md not found. Skipping duplicate check.")
    sys.exit(0)

content = TODO_FILE.read_text(encoding="utf-8")

# Match checklist items like:
# - [ ] Task name
# - [x] Task name
CHECKBOX_RE = re.compile(r"- 

\[[ xX]\]

 (.+)")

items = CHECKBOX_RE.findall(content)

seen = set()
duplicates = []

for item in items:
    normalized = item.strip().lower()
    if normalized in seen:
        duplicates.append(item)
    else:
        seen.add(normalized)

if duplicates:
    print("❌ Duplicate TODO items detected:")
    for d in duplicates:
        print(f"  - {d}")
    sys.exit(1)

print("✔ No duplicate TODO items found.")
