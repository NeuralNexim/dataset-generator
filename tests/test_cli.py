import subprocess
import sys
import json


def test_cli_runs(tmp_path):
    output = tmp_path / "out.jsonl"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "math_dataset_generator.generate",
            "--domain",
            "arithmetic",
            "--count",
            "3",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    assert output.exists()

    lines = output.read_text().strip().split("\n")
    assert len(lines) == 3

    row = json.loads(lines[0])
    assert "input" in row
    assert "answer" in row


def test_cli_reasoning_depth_detailed(tmp_path):
    output = tmp_path / "out_detailed.jsonl"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "math_dataset_generator.generate",
            "--domain",
            "algebra",
            "--count",
            "1",
            "--difficulty",
            "hard",
            "--reasoning-depth",
            "detailed",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    row = json.loads(output.read_text().strip())
    assert "Step 1:" in row["reasoning"]


def test_cli_curriculum_domain_progressive(tmp_path):
    output = tmp_path / "out_curriculum_domain.jsonl"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "math_dataset_generator.generate",
            "--domain",
            "algebra",
            "--count",
            "6",
            "--seed",
            "5",
            "--curriculum",
            "domain_progressive",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    rows = [json.loads(line) for line in output.read_text().strip().split("\n")]
    assert rows[0]["difficulty"] == "easy"
    assert rows[-1]["difficulty"] == "olympiad"
    assert all("curriculum_stage" in row for row in rows)


def test_cli_curriculum_mixed_progressive(tmp_path):
    output = tmp_path / "out_curriculum_mixed.jsonl"

    result = subprocess.run(
        [
            sys.executable,
            "-m",
            "math_dataset_generator.generate",
            "--domain",
            "mixed",
            "--count",
            "8",
            "--seed",
            "7",
            "--curriculum",
            "mixed_progressive",
            "--output",
            str(output),
        ],
        capture_output=True,
        text=True,
        check=False,
    )

    assert result.returncode == 0
    rows = [json.loads(line) for line in output.read_text().strip().split("\n")]
    assert all(row["domain"] == "mixed" for row in rows)
    assert all("source_domain" in row for row in rows)
    assert all("curriculum_stage" in row for row in rows)
