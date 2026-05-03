from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class CurriculumStage:
    name: str
    until: float
    difficulty: str
    reasoning_depth: str | None = None
    domain_weights: dict[str, int] | None = None


SCHEDULES: dict[str, list[CurriculumStage]] = {
    "domain_progressive": [
        CurriculumStage("foundation", 0.25, "easy", "brief"),
        CurriculumStage("core", 0.60, "medium", "standard"),
        CurriculumStage("advanced", 0.85, "hard", "detailed"),
        CurriculumStage("mastery", 1.00, "olympiad", "full"),
    ],
    "mixed_progressive": [
        CurriculumStage(
            "foundation",
            0.30,
            "easy",
            "brief",
            {
                "arithmetic": 5,
                "word_numbers": 4,
                "story_single": 4,
                "units_rates": 3,
                "geometry": 2,
            },
        ),
        CurriculumStage(
            "core",
            0.65,
            "medium",
            "standard",
            {
                "arithmetic": 3,
                "algebra": 3,
                "proportional": 3,
                "functions": 3,
                "story_multi": 3,
                "probability": 2,
                "sequences": 2,
            },
        ),
        CurriculumStage(
            "advanced",
            0.88,
            "hard",
            "detailed",
            {
                "algebra": 3,
                "multi_step_algebra": 4,
                "logic_puzzles": 3,
                "number_theory": 3,
                "combinatorics": 3,
                "calculus": 2,
            },
        ),
        CurriculumStage(
            "mastery",
            1.00,
            "olympiad",
            "full",
            {
                "multi_step_algebra": 4,
                "combinatorics": 3,
                "number_theory": 3,
                "calculus": 3,
                "matrices": 2,
                "diagram_word_problems": 2,
                "logic_puzzles": 2,
            },
        ),
    ],
}


def resolve_curriculum_stage(
    schedule_name: str, index: int, total: int
) -> CurriculumStage:
    if schedule_name not in SCHEDULES:
        raise ValueError(
            f"Unknown curriculum schedule: {schedule_name}. Available: {list(SCHEDULES.keys())}"
        )
    if total < 1:
        raise ValueError("total must be >= 1")
    if index < 0 or index >= total:
        raise ValueError("index out of range for curriculum stage resolution")

    progress = (index + 1) / total
    for stage in SCHEDULES[schedule_name]:
        if progress <= stage.until:
            return stage
    return SCHEDULES[schedule_name][-1]
