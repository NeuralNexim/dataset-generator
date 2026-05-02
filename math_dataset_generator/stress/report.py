import json
from dataclasses import dataclass, asdict
from typing import Dict, Any, List


@dataclass
class TestSummary:
    name: str
    iterations: int
    failures: int
    duration_sec: float


@dataclass
class StressReport:
    mode: str
    load: str
    workers: int
    summaries: List[TestSummary]


def write_report(path: str, report: StressReport) -> None:
    data = asdict(report)
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
