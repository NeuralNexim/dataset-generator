#!/usr/bin/env python3
"""
check_changelog_update.py

Ensures that:
- CHANGELOG.md contains an entry for the current version.
- The version in CHANGELOG.md matches __version__.
- The changelog entry contains at least one bullet point.
- No empty or placeholder sections exist.

This enforces proper release documentation.
"""

import sys
import re
from pathlib import Path

CHANGELOG = Path("CHANGELOG.md")
VERSION_FILE = Path("math_dataset_generator/__init__.py")

if not CHANGELOG.exists() or not VERSION_FILE.exists():
    print("CHANGELOG.md or __init__.py missing. Skipping changelog check.")
    sys.exit(0)

# Extract version from __init__.py
version_text = VERSION_FILE.read_text(encoding="utf-8")
VERSION_RE = re.compile(r'__version__\s*=\s*"(\d+\.\d+\.\d+)"')
m = VERSION_RE.search(version_text)

if not m:
    print("❌ Could not find __version__ in __init__.py")
    sys.exit(1)

current_version = m.group(1)

# Read changelog
changelog = CHANGELOG.read_text(encoding="utf-8")

# Match version headers like: ## 1.2.3
HEADER_RE = re.compile(r"^##\s+(\d+\.\d+\.\d+)", re.MULTILINE)
headers = HEADER_RE.findall(changelog)

if current_version not in headers:
    print(f"❌ CHANGELOG.md missing entry for version {current_version}")
    sys.exit(1)

# Extract the section for the current version
pattern = rf"## {re.escape(current_version)}(.*?)(?=^## |\Z)"
section_re = re.compile(pattern, re.DOTALL | re.MULTILINE)
section_match = section_re.search(changelog)

if not section_match:
    print(f"❌ Could not extract changelog section for version {current_version}")
    sys.exit(1)

section = section_match.group(1).strip()

# Ensure at least one bullet point exists
if not re.search(r"^- ", section, re.MULTILINE):
    print(f"❌ CHANGELOG.md entry for version {current_version} has no bullet points")
    sys.exit(1)

# Prevent placeholder text
if "todo" in section.lower() or "tbd" in section.lower():
    print(
        f"❌ CHANGELOG.md entry for version {current_version} contains placeholder text"
    )
    sys.exit(1)

print("✔ CHANGELOG.md is consistent with version bump.")
