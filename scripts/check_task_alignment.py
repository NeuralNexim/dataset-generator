#!/usr/bin/env python3
"""
check_task_alignment.py

Ensures that:
- The branch name corresponds to a TODO item.
- The commit message corresponds to the same TODO item.
- Only one TODO item is being implemented in this PR.

This prevents mixing multiple tasks in one PR and enforces
the workflow defined in the project.
"""

import sys
import re
from pathlib import Path
import subprocess

TODO = Path("TODO.md")

if not TODO.exists():
    print("TODO.md not found. Skipping task alignment check.")
    sys.exit(0)

todo_text = TODO.read_text(encoding="utf-8")

# Extract all TODO items (checked or unchecked)
ITEM_RE = re.compile(r"- 

\[[ xX]\]

 (.+)")
all_items = ITEM_RE.findall(todo_text)

# Normalize items for matching
normalized_items = {item.lower().strip(): item for item in all_items}

# Get branch name
branch = subprocess.check_output(
    ["git", "rev-parse", "--abbrev-ref", "HEAD"],
    text=True
).strip()

# Extract task name from branch: feature/<task-name>
BRANCH_RE = re.compile(r"^(feature|fix|docs)/(.+)$")
m = BRANCH_RE.match(branch)

if not m:
    print(f"❌ Branch '{branch}' does not follow feature/<task-name> format.")
    sys.exit(1)

branch_task_raw = m.group(2)
branch_task = branch_task_raw.replace("-", " ").lower().strip()

# Find matching TODO item
matched_item = None
for key, original in normalized_items.items():
    if branch_task in key:
        matched_item = original
        break

if not matched_item:
    print(f"❌ Branch name '{branch}' does not match any TODO item.")
    print("Make sure the branch name corresponds to a TODO task.")
    sys.exit(1)

print(f"✔ Branch matches TODO item: {matched_item}")

# Check commit message
commit_msg = subprocess.check_output(
    ["git", "log", "-1", "--pretty=%s"],
    text=True
).strip().lower()

if branch_task not in commit_msg:
    print("❌ Commit message does not reference the same TODO task.")
    print(f"Branch task: {branch_task_raw}")
    print(f"Commit message: {commit_msg}")
    sys.exit(1)

print("✔ Commit message matches branch task.")

# Ensure only one TODO item is being modified
modified_files = subprocess.check_output(
    ["git", "diff", "--name-only", "origin/main...HEAD"],
    text=True
).splitlines()

# If multiple TODO items appear in diff, fail
modified_todos = []
for key, original in normalized_items.items():
    if key != branch_task and key in "\n".join(modified_files).lower():
        modified_todos.append(original)

if modified_todos:
    print("❌ PR modifies multiple TODO items:")
    for item in modified_todos:
        print(f"  - {item}")
    print("Each PR must implement exactly one TODO item.")
    sys.exit(1)

print("✔ PR modifies only one TODO item.")
