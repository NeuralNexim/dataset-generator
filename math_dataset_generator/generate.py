import argparse
import json
from math_dataset_generator.generator import generate_one_sample
from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.utils.logger import configure_logging


def main():
    parser = argparse.ArgumentParser(description="Generate dataset samples.")
    parser.add_argument(
        "--domain",
        type=str,
        required=True,
        help=f"Domain to generate. Options: {list(DOMAIN_REGISTRY.keys())}",
    )
    parser.add_argument(
        "--count", type=int, default=1, help="Number of samples to generate."
    )
    parser.add_argument(
        "--output",
        type=str,
        default=None,
        help="Output JSONL file. If omitted, prints to stdout.",
    )
    parser.add_argument(
        "--seed",
        type=int,
        default=None,
        help="Random seed for reproducible output.",
    )
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Enable DEBUG-level logging.",
    )

    args = parser.parse_args()
    configure_logging(debug=args.debug)

    if args.domain not in DOMAIN_REGISTRY:
        raise ValueError(f"Unknown domain: {args.domain}")

    import random

    if args.seed is not None:
        random.seed(args.seed)

    if args.output:
        with open(args.output, "w", encoding="utf8") as f:
            for _ in range(args.count):
                sample = generate_one_sample(args.domain)
                f.write(json.dumps(sample, ensure_ascii=False) + "\n")
        print(f"Wrote {args.count} samples to {args.output}")
    else:
        for _ in range(args.count):
            sample = generate_one_sample(args.domain)
            print(json.dumps(sample, ensure_ascii=False))


if __name__ == "__main__":
    main()
