import argparse

from .engine import run_stress_tests


def main() -> None:
    parser = argparse.ArgumentParser(
        prog="math_dataset_generator.stress",
        description="Stress tester for math_dataset_generator",
    )

    parser.add_argument("--all", action="store_true", help="Run all stress tests")
    parser.add_argument(
        "--roundtrip", action="store_true", help="Test number↔words roundtrip"
    )
    parser.add_argument("--noise", action="store_true", help="Test noise injection")
    parser.add_argument("--domains", action="store_true", help="Test domain generators")
    parser.add_argument("--templates", action="store_true", help="Test templates")
    parser.add_argument("--perf", action="store_true", help="Test performance")

    parser.add_argument(
        "--load",
        choices=["light", "medium", "heavy", "extreme", "custom"],
        default="light",
        help="Stress load level",
    )
    parser.add_argument(
        "--iterations",
        type=int,
        default=None,
        help="Custom iteration count (used when --load custom)",
    )

    parser.add_argument(
        "--mode",
        choices=["parallel", "sequential", "hybrid"],
        default="parallel",
        help="Execution mode",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=None,
        help="Number of worker processes (parallel/hybrid)",
    )

    parser.add_argument(
        "--report",
        type=str,
        default=None,
        help="Optional JSON report path",
    )

    args = parser.parse_args()

    do_roundtrip = args.all or args.roundtrip
    do_noise = args.all or args.noise
    do_domains = args.all or args.domains
    do_templates = args.all or args.templates
    do_perf = args.all or args.perf

    # Import here to avoid circulars
    from math_dataset_generator.generator import (
        generate_one_sample,
    )  # you implement this

    run_stress_tests(
        do_roundtrip=do_roundtrip,
        do_noise=do_noise,
        do_domains=do_domains,
        do_templates=do_templates,
        do_perf=do_perf,
        mode=args.mode,
        load=args.load,
        iterations_override=args.iterations,
        workers=args.workers,
        report_path=args.report,
        generate_one=generate_one_sample,
    )
