#!/usr/bin/env python3
"""
check_no_debug_code.py

Ensures no debug code is committed to the repository.

Checks for:
- print() statements outside logging
- pdb.set_trace()
- import pdb
- breakpoint()
- commented-out debug blocks
- temporary debug logging

This keeps the codebase production-clean.
"""

import sys
import re
from pathlib import Path

ROOT = Path("math_dataset_generator")

# Patterns to detect debug code
PATTERNS = {
    "print() statement": re.compile(r"\bprint\("),
    "pdb.set_trace()": re.compile(r"\bpdb\.set_trace\("),
    "import pdb": re.compile(r"\bimport pdb\b"),
    "breakpoint()": re.compile(r"\bbreakpoint\("),
    "debug comment": re.compile(r"#\s*(debug|dbg|todo-debug)", re.IGNORECASE),
    "temporary logging": re.compile(r"logger\.debug\(", re.IGNORECASE),
}

errors = []

# Scan all .py files
for py_file in ROOT.rglob("*.py"):
    text = py_file.read_text(encoding="utf-8")

    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(text):
            line_no = text.count("\n", 0, match.start()) + 1
            errors.append(f"{py_file}:{line_no} — {label}")

if errors:
    print("❌ Debug code detected in repository:")
    for e in errors:
        print("  -", e)
    print("\nRemove debug code before merging.")
    sys.exit(1)

print("✔ No debug code found.")
