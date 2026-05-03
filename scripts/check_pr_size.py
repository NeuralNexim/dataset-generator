#!/usr/bin/env python3
"""
check_pr_size.py

Ensures that pull requests remain small and focused.

Rules enforced:
- Maximum total changed lines (additions + deletions).
- Maximum number of changed files.
- Warns (or fails) if PR is too large.

This prevents "mega PRs" and keeps the workflow clean.
"""

import sys
import subprocess

# Thresholds (tune these as needed)
MAX_LINES = 500
MAX_FILES = 25

# Get diff stats against main
try:
    diff_output = subprocess.check_output(
        ["git", "diff", "--stat", "origin/main...HEAD"], text=True
    )
except Exception as e:
    print("⚠ Could not compute diff against origin/main:", e)
    sys.exit(0)

# Count changed files
file_count = diff_output.count("|")

# Extract total line changes
# Example summary line: " 12 files changed, 345 insertions(+), 120 deletions(-)"
summary_line = diff_output.strip().split("\n")[-1]

import re

m = re.search(
    r"(\d+)\s+files? changed.*?(\d+)\s+insertions.*?(\d+)\s+deletions", summary_line
)

if not m:
    print("⚠ Could not parse diff summary. Skipping PR size check.")
    sys.exit(0)

files_changed = int(m.group(1))
insertions = int(m.group(2))
deletions = int(m.group(3))
total_lines = insertions + deletions

errors = []

if files_changed > MAX_FILES:
    errors.append(f"Too many files changed: {files_changed} (max {MAX_FILES})")

if total_lines > MAX_LINES:
    errors.append(f"Too many total line changes: {total_lines} (max {MAX_LINES})")

if errors:
    print("❌ Pull request is too large:")
    for e in errors:
        print("  -", e)
    print("\nPlease split this PR into smaller, focused changes.")
    sys.exit(1)

print(f"✔ PR size OK: {files_changed} files, {total_lines} lines changed.")
