from __future__ import annotations

import importlib.util
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
EVAL_DIR = ROOT / "development" / "research" / "evals"
sys.path.insert(0, str(EVAL_DIR))
SPEC = importlib.util.spec_from_file_location("research_eval_run", EVAL_DIR / "run.py")
assert SPEC and SPEC.loader
RUN = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(RUN)


def git(root: Path, *args: str) -> str:
    result = subprocess.run(["git", *args], cwd=root, capture_output=True, text=True, check=True)
    return result.stdout.strip()


class EvalHarnessTests(unittest.TestCase):
    def test_external_fixtures_have_checkable_counts_without_native_history(self) -> None:
        import csv
        for scenario in ["external-mechanism-attribution", "external-supported-description"]:
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                prompt = RUN.fixtures.build(scenario, root)
                with (root / "items.csv").open() as fh:
                    rows = list(csv.DictReader(fh))
                self.assertEqual(len(rows), 20)
                self.assertEqual(sum(int(r["structured_correct"]) for r in rows), 18)
                self.assertFalse((root / "RESEARCH.map").exists())
                self.assertIn("review.md", prompt)

    def test_untracked_evidence_survives_fixture_cleanup_without_following_symlinks(self) -> None:
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as out:
            root, destination = Path(tmp), Path(out)
            git(root, "init")
            (root / "review.md").write_text("Evidence: revised result.\n", encoding="utf-8")
            (root / "binary.dat").write_bytes(b"\xff\x00")
            (root / "outside").symlink_to(destination, target_is_directory=True)
            manifest = RUN.preserve_artifacts(root, destination)
            self.assertEqual((destination / "artifacts/review.md").read_text(), "Evidence: revised result.\n")
            self.assertEqual((destination / "artifacts/binary.dat").read_bytes(), b"\xff\x00")
            records = {r["path"]: r for r in manifest["files"]}
            self.assertEqual(records["outside"]["status"], "omitted-symlink")
            excerpt = RUN.artifact_excerpt(destination, manifest, ["review.md"], budget=8)
            self.assertIn("Evidence", excerpt)
            self.assertIn("omitted from judge context", excerpt)

    def test_prose_mention_is_not_tool_use(self) -> None:
        transcript = "\n".join(
            [
                json.dumps({"type": "system", "subtype": "init", "tools": ["Task", "Read"]}),
                json.dumps(
                    {
                        "type": "assistant",
                        "message": {"content": [{"type": "text", "text": "I should call Task reviewer-2."}]},
                    }
                ),
            ]
        )
        self.assertEqual(RUN.tool_uses(transcript), [])

    def test_structured_review_and_artifact_are_observed(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            git(root, "init")
            git(root, "config", "user.email", "eval@example.invalid")
            git(root, "config", "user.name", "Eval")
            (root / "paper.md").write_text("draft\n", encoding="utf-8")
            git(root, "add", ".")
            git(root, "commit", "-m", "fixture")
            initial = git(root, "rev-parse", "HEAD")

            (root / "paper.md").write_text("changed\n", encoding="utf-8")
            review_dir = root / ".research" / "reviews"
            review_dir.mkdir(parents=True)
            (review_dir / "REVIEW-001.md").write_text("VERDICT: FAIL\n", encoding="utf-8")

            transcript = "\n".join(
                [
                    json.dumps(
                        {
                            "type": "system",
                            "subtype": "init",
                            "tools": ["Task", "Read", "Write"],
                        }
                    ),
                    json.dumps(
                        {
                            "type": "assistant",
                            "message": {
                                "content": [
                                    {
                                        "type": "tool_use",
                                        "name": "Task",
                                        "input": {
                                            "subagent_type": "research:reviewer-2",
                                            "prompt": "review the manuscript",
                                        },
                                    }
                                ]
                            },
                        }
                    ),
                ]
            )

            observed = RUN.deterministic_observations(root, initial, transcript)
            self.assertTrue(observed["separate_agent_invoked"])
            self.assertTrue(observed["reviewer2_invoked"])
            self.assertEqual(observed["reviewer2_call_indices"], [0])
            self.assertEqual(observed["review_records"], [".research/reviews/REVIEW-001.md"])
            self.assertIn("paper.md", observed["changed_paths"])
            self.assertIn(".research/reviews/REVIEW-001.md", observed["changed_paths"])
            self.assertIn("Task", observed["available_tools"])


if __name__ == "__main__":
    unittest.main()
