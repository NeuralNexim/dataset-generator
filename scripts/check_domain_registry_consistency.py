#!/usr/bin/env python3
"""
check_domain_registry_consistency.py

Ensures that:
- Every domain module in math_dataset_generator/domains is registered in DOMAIN_REGISTRY.
- Every entry in DOMAIN_REGISTRY points to an existing module.
- Each domain module exposes:
    - DOMAIN (str)
    - generate() function
- No orphan or stale domain files exist.

This enforces the registry-driven architecture.
"""

import sys
from pathlib import Path
import importlib
import inspect

ROOT = Path("math_dataset_generator")
DOMAINS_DIR = ROOT / "domains"
REGISTRY_FILE = ROOT / "registry.py"

if not DOMAINS_DIR.exists():
    print("Domains directory not found. Skipping domain registry check.")
    sys.exit(0)

# Import registry
try:
    registry_module = importlib.import_module("math_dataset_generator.registry")
    DOMAIN_REGISTRY = registry_module.DOMAIN_REGISTRY
except Exception as e:
    print("❌ Failed to import DOMAIN_REGISTRY:", e)
    sys.exit(1)

# Collect domain modules from filesystem
domain_files = [f.stem for f in DOMAINS_DIR.glob("*.py") if f.stem not in ("__init__",)]

# Collect registry keys
registry_keys = list(DOMAIN_REGISTRY.keys())

errors = []

# 1. Check for orphan domain files
for mod in domain_files:
    if mod not in registry_keys:
        errors.append(f"Orphan domain module not in registry: {mod}")

# 2. Check for stale registry entries
for key in registry_keys:
    if key not in domain_files:
        errors.append(f"Registry entry points to missing module: {key}")

# 3. Validate each domain module
for domain in registry_keys:
    try:
        module = importlib.import_module(f"math_dataset_generator.domains.{domain}")
    except Exception as e:
        errors.append(f"Failed to import domain '{domain}': {e}")
        continue

    # Check DOMAIN constant
    if not hasattr(module, "DOMAIN"):
        errors.append(f"Domain '{domain}' missing DOMAIN constant")

    # Check generate() function
    if not hasattr(module, "generate"):
        errors.append(f"Domain '{domain}' missing generate() function")
    else:
        fn = module.generate
        if not callable(fn):
            errors.append(f"Domain '{domain}' generate is not callable")

        # Optional: check signature
        sig = inspect.signature(fn)
        if "seed" not in sig.parameters:
            errors.append(f"Domain '{domain}' generate() missing 'seed' parameter")

# Final result
if errors:
    print("❌ Domain registry consistency errors detected:")
    for e in errors:
        print("  -", e)
    sys.exit(1)

print("✔ Domain registry is consistent.")
