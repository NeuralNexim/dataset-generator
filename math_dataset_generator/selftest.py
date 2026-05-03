"""
Domain self-test runner.

Usage:
    python -m math_dataset_generator.selftest [--samples N] [--seed S]
"""

import argparse
import sys
import random as _random

from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.generator import generate_one_sample


_GREEN = "\033[32m"
_RED = "\033[31m"
_CYAN = "\033[36m"
_RESET = "\033[0m"


def run_domain_selftest(n_samples: int = 50, seed: int | None = None) -> dict[str, dict]:
    """Generate *n_samples* per domain and report pass/fail counts."""
    if seed is not None:
        _random.seed(seed)

    results: dict[str, dict] = {}
    for domain in DOMAIN_REGISTRY:
        passed = 0
        errors: list[str] = []
        for _ in range(n_samples):
            try:
                generate_one_sample(domain)
                passed += 1
            except Exception as exc:  # noqa: BLE001
                errors.append(str(exc))
        results[domain] = {
            "passed": passed,
            "failed": n_samples - passed,
            "errors": errors[:3],  # keep first 3 unique error messages
        }
    return results


def _print_report(results: dict[str, dict], n_samples: int) -> bool:
    """Print a formatted summary. Returns True if all domains passed."""
    all_ok = True
    print(f"{_CYAN}Domain Self-Test ({n_samples} samples each){_RESET}")
    print("-" * 60)
    for domain, res in results.items():
        passed = res["passed"]
        failed = res["failed"]
        if failed == 0:
            mark = f"{_GREEN}PASS{_RESET}"
        else:
            mark = f"{_RED}FAIL{_RESET}"
            all_ok = False
        print(f"  {mark}  {domain:20s}  {passed}/{n_samples} passed")
        for err in res["errors"]:
            print(f"         {_RED}! {err}{_RESET}")
    print("-" * 60)
    if all_ok:
        print(f"{_GREEN}All domains OK.{_RESET}")
    else:
        print(f"{_RED}Some domains FAILED.{_RESET}")
    return all_ok


def main() -> None:
    parser = argparse.ArgumentParser(description="Run domain self-tests.")
    parser.add_argument("--samples", type=int, default=50,
                        help="Number of samples per domain (default: 50).")
    parser.add_argument("--seed", type=int, default=None,
                        help="Random seed for reproducibility.")
    args = parser.parse_args()

    results = run_domain_selftest(n_samples=args.samples, seed=args.seed)
    ok = _print_report(results, args.samples)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()

