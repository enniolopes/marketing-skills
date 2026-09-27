import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
SCRIPT = REPO_ROOT / "systems" / "research" / "skills" / "research-graph" / "scripts" / "graph.py"
spec = importlib.util.spec_from_file_location("research_graph", SCRIPT)
graph = importlib.util.module_from_spec(spec)
sys.modules["research_graph"] = graph
spec.loader.exec_module(graph)

MAP = """# RESEARCH.map

## Layout
- protocol: protocol.md
- decisions: decisions.md
- aggregates: aggregates/
- documents: paper/
- notebooks: notebooks/
- references: references.bib
- floor: 5

## Question
Q → `protocol.md#question`
Problem: SHOWN → `problem-brief.md`
Registration: https://example.org/reg, 2026-09-14

## Hypotheses
| Id | Prediction | Refutation | State | Pointer |
|---|---|---|---|---|
| H1 | p | r | — | `protocol.md#h1` |

## Gates
| Phase | State | Blocked by | Evidence |
|---|---|---|---|
| 1 Problem | pending | | |
| 2 Literature | pending | | |
| 3 Protocol | pending | | |
| 4 Data | pending | | |
| 5 Analysis | pending | | |
| 6 Writing | pending | | |
| 7 Review | pending | | |
| 8 Publication | pending | | |

## Deferred

## Last session
- 2026-09-14: fixture.
- Next: test graph.
"""

PLAN = """# Analysis plan
Freeze: frozen

## H1
Estimand: E1
Primary test: T1
Mode: confirmatory
Generated from: DATA1

### Assumptions
| ID | Assumption | Check | Failure action |
|---|---|---|---|
| A1 | assumption | K1 | T2 |
"""


class ResearchGraphTests(unittest.TestCase):
    def test_dependency_queries_follow_inputs_assumptions_and_keep_other_support(self):
        triples = [
            ("RUN-1", "uses", "DATA1"), ("T1", "requires", "A1"),
            ("A1", "checked_by", "K1"), ("T1", "executed_as", "RUN-1"),
            ("RUN-1", "produces", "R1"), ("R1", "supports", "I1"),
            ("I1", "supports", "C1"), ("R2", "supports", "I1"),
            ("T1", "fallback_to", "T2"), ("T2", "executed_as", "RUN-2"),
            ("RUN-2", "produces", "R3"), ("R3", "supports", "I3"),
            ("I3", "supports", "C3"),
        ]
        raw = {"edges": [{"from": a, "relation": r, "to": b} for a, r, b in triples]}
        projected = graph.dependency_graph(raw)
        for changed in ["DATA1", "A1", "K1"]:
            consequences = "\n".join(graph.walk(projected, changed, reverse=False))
            self.assertIn("C1", consequences)
            self.assertNotIn("C3", consequences)
            self.assertNotIn("R2", consequences)
        trace = "\n".join(graph.walk(projected, "C1", reverse=True))
        self.assertIn("DATA1", trace)
        self.assertIn("K1", trace)
        self.assertIn("R2", trace)
        self.assertEqual(raw["edges"][0]["relation"], "uses")

    def test_walk_does_not_silently_truncate_and_terminates_cycles(self):
        edges = [{"from": f"N{i}", "relation": "supports", "to": f"N{i+1}"} for i in range(12)]
        edges.append({"from": "N12", "relation": "supports", "to": "N0"})
        lines = graph.walk({"edges": edges}, "N0", reverse=False)
        self.assertEqual(len(lines), 13)
        self.assertIn("N12", "\n".join(lines))

    def test_build_is_deterministic_and_contains_lineage(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "aggregates").mkdir()
            (root / "paper").mkdir()
            (root / "notebooks").mkdir()
            (root / ".research" / "runs").mkdir(parents=True)
            (root / "RESEARCH.map").write_text(MAP, encoding="utf-8")
            (root / "analysis-plan.md").write_text(PLAN, encoding="utf-8")
            (root / "protocol.md").write_text("# Protocol\n## question\nQ\n## h1\nH1\n", encoding="utf-8")
            (root / "decisions.md").write_text("# Decisions\n", encoding="utf-8")
            (root / "problem-brief.md").write_text("# Brief\n", encoding="utf-8")
            (root / "references.bib").write_text("@article{x, title={X}, doi={10.1/x}}\n", encoding="utf-8")
            (root / "data.csv").write_text("x\n1\n", encoding="utf-8")
            (root / "aggregates" / "result.csv").write_text("estimate\n1\n", encoding="utf-8")
            manifest = {
                "id": "RUN-001",
                "mode": "confirmatory",
                "commit": "abcdef1",
                "protocol_freeze": "abcdef1",
                "analysis_plan_freeze": "abcdef1",
                "hypothesis": "H1",
                "estimand": "E1",
                "test": "T1",
                "inputs": [{"id": "DATA1", "path": "data.csv", "role": "confirmatory"}],
                "outputs": [{"result": "R1", "artifact": "aggregates/result.csv"}],
            }
            (root / ".research" / "runs" / "RUN-001.json").write_text(json.dumps(manifest), encoding="utf-8")
            (root / "paper" / "results.md").write_text(
                "Result. <!-- claim:C1 inference:I1 result:R1 decides:H1 -->\n",
                encoding="utf-8",
            )

            first = graph.build(root / "RESEARCH.map")
            second = graph.build(root / "RESEARCH.map")
            self.assertEqual(first, second)
            nodes = {node["id"]: node for node in first["nodes"]}
            for node_id in ["H1", "E1", "T1", "A1", "K1", "DATA1", "RUN-001", "R1", "I1", "C1"]:
                self.assertIn(node_id, nodes)
            edges = {(edge["from"], edge["relation"], edge["to"]) for edge in first["edges"]}
            self.assertIn(("H1", "generated_from", "DATA1"), edges)
            self.assertIn(("RUN-001", "uses", "DATA1"), edges)
            self.assertIn(("RUN-001", "produces", "R1"), edges)
            self.assertIn(("R1", "supports", "I1"), edges)
            self.assertIn(("I1", "supports", "C1"), edges)
            self.assertNotIn(("H1", "derived_from", "I1"), edges)
            trace = "\n".join(graph.walk(graph.dependency_graph(first), "C1", reverse=True))
            for node_id in ["DATA1", "H1", "E1", "K1"]:
                self.assertIn(node_id, trace)


if __name__ == "__main__":
    unittest.main()
