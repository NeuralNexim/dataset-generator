import argparse
from math_dataset_generator.generator import generate_from_cli

import sys

if sys.version_info < (3, 13):
    raise RuntimeError("Python 3.13 or higher is required for this project.")


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Math Dataset Generator — multi-domain reasoning datasets."
    )

    parser.add_argument(
        "--domain",
        type=str,
        required=True,
        help="Domain name (e.g., arithmetic, algebra, geometry, word_numbers, ...)",
    )

    parser.add_argument(
        "--n",
        type=int,
        required=True,
        help="Number of samples to generate.",
    )

    parser.add_argument(
        "--difficulty",
        type=str,
        default="auto",
        choices=["easy", "medium", "hard", "auto"],
        help="Difficulty level.",
    )

    parser.add_argument(
        "--noise",
        type=str,
        default="none",
        choices=["none", "light", "medium", "heavy"],
        help="Noise injection level.",
    )

    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Optional random seed for reproducibility.",
    )

    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Optional JSONL output file path.",
    )

    parser.add_argument(
        "--no-reasoning",
        action="store_true",
        help="Disable reasoning steps.",
    )

    parser.add_argument(
        "--no-expression",
        action="store_true",
        help="Disable symbolic expression generation.",
    )

    return parser


def main():
    parser = build_parser()
    args = parser.parse_args()
    generate_from_cli(args)


if __name__ == "__main__":
    main()
