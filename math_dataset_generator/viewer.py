"""
Dataset Viewer CLI
Allows inspection, filtering, and sampling of JSONL datasets.
"""

import argparse
import json
import random
from typing import List, Dict, Any


def view_sample(rows: List[Dict[str, Any]], n: int):
    for row in random.sample(rows, min(n, len(rows))):
        print("\n--- SAMPLE ---")
        print(f"Domain: {row.get('domain')}")
        print(f"Difficulty: {row.get('difficulty')}")
        print(f"Input: {row.get('input')}")
        print(f"Answer: {row.get('answer')}")
        if "reasoning" in row:
            print(f"Reasoning: {row['reasoning']}")
        print(f"Metadata: {row.get('metadata')}")


def show_stats(rows: List[Dict[str, Any]]):
    from collections import Counter

    domains = Counter(row["domain"] for row in rows)
    difficulties = Counter(row["difficulty"] for row in rows)

    print("\n=== DATASET STATS ===")
    print("Total rows:", len(rows))
    print("\nDomains:")
    for k, v in domains.items():
        print(f"  {k}: {v}")
    print("\nDifficulties:")
    for k, v in difficulties.items():
        print(f"  {k}: {v}")


def build_parser():
    parser = argparse.ArgumentParser(description="Dataset Viewer CLI")

    parser.add_argument("--file", required=True, help="Path to JSONL dataset")
    parser.add_argument("--stats", action="store_true", help="Show dataset statistics")
    parser.add_argument("--sample", type=int, help="Show N random samples")
    parser.add_argument("--filter-domain", type=str, help="Filter by domain")
    parser.add_argument("--filter-difficulty", type=str, help="Filter by difficulty")

    return parser


def load_jsonl(path: str):
    import os

    if not os.path.exists(path):
        print(f"\n❌ Dataset file not found: {path}")
        print("💡 Generate one first using:")
        print(
            "   python -m math_dataset_generator.main --domain arithmetic --n 100 --output output/arithmetic.jsonl\n"
        )
        return None

    try:
        with open(path, "r", encoding="utf-8") as f:
            lines = f.read().strip().split("\n")
            if not lines or lines == [""]:
                print(f"\n⚠️ The dataset file exists but is empty: {path}")
                return []
            return [json.loads(line) for line in lines]
    except json.JSONDecodeError as e:
        print(f"\n❌ Invalid JSONL format in file: {path}")
        print(f"   Error: {e}")
        print("💡 Ensure the dataset was generated using the official generator.\n")
        return None
    except Exception as e:
        print(f"\n❌ Could not read dataset file: {path}")
        print(f"   Error: {e}\n")
        return None


def main():
    parser = build_parser()
    args = parser.parse_args()

    rows = load_jsonl(args.file)
    if rows is None:
        return
    if rows == []:
        print("⚠️ No rows to display.\n")
        return

    # Filtering
    if args.filter_domain:
        rows = [r for r in rows if r.get("domain") == args.filter_domain]

    if args.filter_difficulty:
        rows = [r for r in rows if r.get("difficulty") == args.filter_difficulty]

    if args.stats:
        show_stats(rows)

    if args.sample:
        view_sample(rows, args.sample)


if __name__ == "__main__":
    main()
