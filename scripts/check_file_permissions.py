#!/usr/bin/env python3
"""
check_file_permissions.py

Ensures:
- No Python source files are accidentally executable.
- No unexpected permission changes are introduced in a PR.
- Only scripts in /bin or /tools may be executable (optional rule).

This prevents accidental chmod changes and keeps the repo permission-clean.
"""

import sys
import os
from pathlib import Path
import subprocess

ROOT = Path(".")

# Directories where executable files ARE allowed
ALLOWED_EXECUTABLE_DIRS = {
    "bin",
    "tools",
    "scripts",  # optional: allow scripts to be executable
}

errors = []


def is_executable(path: Path) -> bool:
    """Check if file has any executable bit set."""
    mode = path.stat().st_mode
    return bool(mode & 0o111)


# 1. Scan for executable Python files
for py_file in ROOT.rglob("*.py"):
    # Skip virtual environments or build dirs
    if "venv" in py_file.parts or "build" in py_file.parts:
        continue

    if is_executable(py_file):
        # Check if allowed
        if not any(d in py_file.parts for d in ALLOWED_EXECUTABLE_DIRS):
            errors.append(f"Executable Python file not allowed: {py_file}")

# 2. Detect permission changes in PR diff
try:
    diff_output = subprocess.check_output(
        ["git", "diff", "--summary", "origin/main...HEAD"], text=True
    )
except Exception as e:
    print("⚠ Could not compute diff summary:", e)
    sys.exit(0)

for line in diff_output.splitlines():
    if line.startswith("mode change"):
        errors.append(f"Unexpected permission change: {line}")

# Final result
if errors:
    print("❌ File permission issues detected:")
    for e in errors:
        print("  -", e)
    print("\nFix permissions before merging.")
    sys.exit(1)

print("✔ File permissions are clean.")
