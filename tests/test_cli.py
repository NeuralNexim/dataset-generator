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
