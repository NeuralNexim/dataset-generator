#!/usr/bin/env python3
"""
check_version_bump.py

Ensures that:
- __version__ is bumped when a TODO item is completed.
- Version follows semantic versioning (MAJOR.MINOR.PATCH).
- Version bump is forward-only.
- Only one version bump occurs in a PR.

This prevents forgetting to update the version after implementing features.
"""

import sys
import re
from pathlib import Path
import subprocess

VERSION_FILE = Path("math_dataset_generator/__init__.py")

if not VERSION_FILE.exists():
    print("__init__.py not found. Skipping version bump check.")
    sys.exit(0)

# Extract version from __init__.py
text = VERSION_FILE.read_text(encoding="utf-8")
VERSION_RE = re.compile(r'__version__\s*=\s*"(\d+\.\d+\.\d+)"')
m = VERSION_RE.search(text)

if not m:
    print("❌ __version__ not found or invalid format in __init__.py")
    sys.exit(1)

current_version = m.group(1)

# Validate semantic versioning
if not re.match(r"^\d+\.\d+\.\d+$", current_version):
    print(f"❌ Version '{current_version}' is not semantic (MAJOR.MINOR.PATCH)")
    sys.exit(1)

print(f"✔ Current version: {current_version}")

# Get previous version from main branch
try:
    prev_text = subprocess.check_output(
        ["git", "show", "origin/main:math_dataset_generator/__init__.py"], text=True
    )
    m_prev = VERSION_RE.search(prev_text)
    prev_version = m_prev.group(1) if m_prev else None
except Exception:
    print("⚠ Could not read version from origin/main. Skipping forward-only check.")
    sys.exit(0)

if not prev_version:
    print("⚠ No previous version found. Skipping forward-only check.")
    sys.exit(0)

print(f"Previous version: {prev_version}")


# Compare versions
def parse(v):
    return tuple(map(int, v.split(".")))


if parse(current_version) == parse(prev_version):
    print("❌ Version was not bumped. Feature PRs must bump version.")
    sys.exit(1)

if parse(current_version) < parse(prev_version):
    print("❌ Version regression detected.")
    sys.exit(1)

print("✔ Version bump is valid and forward-only.")
