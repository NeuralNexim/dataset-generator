#!/usr/bin/env python3
"""
check_no_large_files.py

Prevents large or unsafe files from being committed.

Checks for:
- Files larger than MAX_SIZE_MB (default: 1 MB)
- Forbidden binary extensions (zip, tar, pickle, npy, npz, pt, pth, onnx, etc.)
- Accidental dataset dumps
- Large logs or artifacts

This protects the repo from bloat and accidental leaks.
"""

import sys
from pathlib import Path

# Maximum allowed file size (in MB)
MAX_SIZE_MB = 1
MAX_BYTES = MAX_SIZE_MB * 1024 * 1024

# Forbidden file extensions
FORBIDDEN_EXT = {
    ".zip",
    ".tar",
    ".gz",
    ".bz2",
    ".pickle",
    ".pkl",
    ".npy",
    ".npz",
    ".pt",
    ".pth",
    ".onnx",
    ".bin",
    ".dat",
    ".h5",
    ".hdf5",
    ".sqlite",
    ".db",
    ".log",
}

ROOT = Path(".")

errors = []

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    # Skip virtual environments, build dirs, caches
    if any(skip in path.parts for skip in ("venv", "build", "__pycache__", ".git")):
        continue

    # 1. Check file size
    size = path.stat().st_size
    if size > MAX_BYTES:
        errors.append(
            f"Large file detected (> {MAX_SIZE_MB}MB): {path} ({size/1024/1024:.2f} MB)"
        )

    # 2. Check forbidden extensions
    if path.suffix.lower() in FORBIDDEN_EXT:
        errors.append(f"Forbidden binary file detected: {path}")

if errors:
    print("❌ Large or forbidden files detected:")
    for e in errors:
        print("  -", e)
    print("\nRemove or gitignore these files before merging.")
    sys.exit(1)

print("✔ No large or forbidden files found.")
