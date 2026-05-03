import argparse
import json
from math_dataset_generator.generator import generate_dataset
from math_dataset_generator.domains import DOMAIN_REGISTRY
from math_dataset_generator.utils.curriculum_schedules import SCHEDULES
from math_dataset_generator.validation import DIFFICULTY_LEVELS
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
    parser.add_argument(
        "--difficulty",
        choices=list(DIFFICULTY_LEVELS),
        default="medium",
        help="Difficulty tier: easy, medium, hard, or olympiad. Default: medium.",
    )
    parser.add_argument(
        "--reasoning-depth",
        choices=["auto", "brief", "standard", "detailed", "full"],
        default="auto",
        help=(
            "Reasoning verbosity: auto maps to difficulty "
            "(easy->brief, medium->standard, hard->detailed, olympiad->full)."
        ),
    )
    parser.add_argument(
        "--curriculum",
        dest="curriculum_schedule",
        choices=list(SCHEDULES.keys()),
        default=None,
        help=(
            "Optional curriculum schedule for staged export. "
            f"Options: {list(SCHEDULES.keys())}."
        ),
    )

    args = parser.parse_args()
    configure_logging(debug=args.debug)

    if args.domain not in DOMAIN_REGISTRY:
        raise ValueError(f"Unknown domain: {args.domain}")

    rows = generate_dataset(
        domain=args.domain,
        n=args.count,
        seed=args.seed,
        difficulty=args.difficulty,
        reasoning_depth=args.reasoning_depth,
        curriculum_schedule=args.curriculum_schedule,
    )

    if args.output:
        with open(args.output, "w", encoding="utf8") as f:
            for sample in rows:
                f.write(json.dumps(sample, ensure_ascii=False) + "\n")
        print(f"Wrote {args.count} samples to {args.output}")
    else:
        for sample in rows:
            print(json.dumps(sample, ensure_ascii=False))


if __name__ == "__main__":
    main()
