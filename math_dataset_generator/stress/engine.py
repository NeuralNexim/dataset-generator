from typing import Dict, Any, List
from multiprocessing import Pool

from .load_levels import resolve_load, get_stress_domains, get_stress_languages
from .workers import resolve_workers
from .tests_roundtrip import run_roundtrip_tests
from .tests_noise import run_noise_tests
from .tests_templates import run_template_tests
from .tests_domains import run_domain_tests
from .tests_perf import run_perf_tests
from .report import StressReport, TestSummary


def _color(text: str, code: str) -> str:
    return f"\033[{code}m{text}\033[0m"


def _green(text: str) -> str:
    return _color(text, "32")


def _red(text: str) -> str:
    return _color(text, "31")


def _yellow(text: str) -> str:
    return _color(text, "33")


def _cyan(text: str) -> str:
    return _color(text, "36")


def run_stress_tests(
    *,
    do_roundtrip: bool,
    do_noise: bool,
    do_domains: bool,
    do_templates: bool,
    do_perf: bool,
    mode: str,
    load: str,
    iterations_override: int | None,
    workers: int | None,
    report_path: str | None,
    generate_one,
) -> None:
    iters = resolve_load(load, iterations_override)
    domains = get_stress_domains()
    languages = get_stress_languages()
    worker_count = resolve_workers(workers)

    tasks: List[tuple[str, Dict[str, Any]]] = []

    if do_roundtrip:
        tasks.append(
            ("roundtrip", {"iterations": iters["roundtrip"], "languages": languages})
        )
    if do_noise:
        tasks.append(("noise", {"iterations": iters["noise"]}))
    if do_templates:
        tasks.append(("templates", {"iterations": iters["templates"]}))
    if do_domains:
        tasks.append(
            (
                "domains",
                {
                    "iterations": iters["domains"],
                    "domains": domains,
                    "generate_one": generate_one,
                },
            )
        )
    if do_perf:
        tasks.append(
            (
                "perf",
                {
                    "iterations": iters["perf"],
                    "domains": domains,
                    "generate_one": generate_one,
                },
            )
        )

    if not tasks:
        print(_yellow("No tests selected; nothing to run."))
        return

    print(_cyan(f"Mode: {mode}, Load: {load}, Workers: {worker_count}"))

    results: List[Dict[str, Any]] = []

    if mode == "sequential":
        for name, kwargs in tasks:
            res = _run_single(name, kwargs)
            results.append(res)
    else:
        # parallel or hybrid → for now treat both as parallel at test level
        with Pool(processes=worker_count) as pool:
            async_results = [
                pool.apply_async(_run_single, (name, kwargs)) for name, kwargs in tasks
            ]
            for ar in async_results:
                results.append(ar.get())

    _print_summary(results)

    if report_path:
        _write_report(report_path, mode, load, worker_count, results)


def _run_single(name: str, kwargs: Dict[str, Any]) -> Dict[str, Any]:
    if name == "roundtrip":
        return run_roundtrip_tests(**kwargs)
    if name == "noise":
        return run_noise_tests(**kwargs)
    if name == "templates":
        return run_template_tests(**kwargs)
    if name == "domains":
        return run_domain_tests(**kwargs)
    if name == "perf":
        return run_perf_tests(**kwargs)
    raise ValueError(f"Unknown test name: {name}")


def _print_summary(results: List[Dict[str, Any]]) -> None:
    print(_cyan("\nStress Test Summary"))
    for res in results:
        name = res["name"]
        iters = res["iterations"]
        failures = res.get("failures", 0)
        duration = res["duration_sec"]
        line = f"{name:10s} | iters={iters:8d} | failures={failures:5d} | time={duration:7.3f}s"
        if res.get("throughput_per_sec") is not None:
            line += f" | {res['throughput_per_sec']:.1f} samples/s"
        if failures == 0:
            print(_green(line))
        else:
            print(_red(line))
        # Per-domain breakdown for perf test
        if name == "perf" and res.get("per_domain"):
            for domain, stats in res["per_domain"].items():
                print(
                    f"  {domain:20s} mean={stats['mean_ms']:6.2f}ms  "
                    f"p95={stats['p95_ms']:6.2f}ms  "
                    f"min={stats['min_ms']:6.2f}ms  max={stats['max_ms']:6.2f}ms"
                )


def _write_report(
    path: str,
    mode: str,
    load: str,
    workers: int,
    results: List[Dict[str, Any]],
) -> None:
    summaries: List[TestSummary] = []
    for res in results:
        summaries.append(
            TestSummary(
                name=res["name"],
                iterations=res["iterations"],
                failures=res.get("failures", 0),
                duration_sec=res["duration_sec"],
            )
        )
    report = StressReport(mode=mode, load=load, workers=workers, summaries=summaries)
    from .report import write_report

    write_report(path, report)
    print(_yellow(f"Report written to {path}"))
