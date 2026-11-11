"""Mechanical integrity of landing-page eval data, not behavioral quality."""

import copy
import json
from pathlib import Path
import re
import unittest


CASES_PATH = Path(__file__).resolve().parents[1] / "evals" / "cases.json"
GROUPS = ("regressions", "creative_briefs", "activation")


def validate_cases(raw):
    """Parse schema-v2 eval JSON or raise ValueError identifying the defect."""
    try:
        data = json.loads(raw)
    except json.JSONDecodeError as exc:
        raise ValueError(f"cases.json: invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("cases.json: root must be an object")
    expected = {"version", "skill", "rule", *GROUPS}
    if set(data) != expected:
        raise ValueError(
            f"cases.json: root fields: missing {sorted(expected - set(data))}; "
            f"unexpected {sorted(set(data) - expected)}"
        )
    if type(data["version"]) is not int or data["version"] != 2:
        raise ValueError("cases.json: version must be integer 2")
    if data["skill"] != "landing-page":
        raise ValueError("cases.json: skill must be 'landing-page'")
    if not isinstance(data["rule"], str) or not data["rule"].strip():
        raise ValueError("cases.json: rule must be a nonempty string")

    seen = set()
    for group in GROUPS:
        if not isinstance(data[group], list) or not data[group]:
            raise ValueError(f"cases.json: {group} must be a nonempty list")
        for index, case in enumerate(data[group]):
            location = f"cases.json: {group}[{index}]"
            if not isinstance(case, dict):
                raise ValueError(f"{location} must be an object")
            required = {"id", "brief"} if group == "creative_briefs" else {"id", "prompt", "judge"}
            allowed = required if group == "creative_briefs" else required | {"setup"}
            if not required <= set(case) <= allowed:
                raise ValueError(
                    f"{location}: missing fields {sorted(required - set(case))}; "
                    f"unexpected fields {sorted(set(case) - allowed)}"
                )
            case_id = case["id"]
            if not isinstance(case_id, str) or not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", case_id):
                raise ValueError(f"{location}: id must be a lowercase kebab-case string")
            if case_id in seen:
                raise ValueError(f"{location}: duplicate id {case_id!r}")
            seen.add(case_id)
            for key in ("brief", "prompt", "setup"):
                if key in case and (not isinstance(case[key], str) or not case[key].strip()):
                    raise ValueError(f"{location}: {key} must be a nonempty string")
            if "judge" in case:
                if not isinstance(case["judge"], list) or not case["judge"]:
                    raise ValueError(f"{location}: judge must be a nonempty list")
                for judge_index, judge in enumerate(case["judge"]):
                    if not isinstance(judge, str) or not judge.strip():
                        raise ValueError(f"{location}: judge[{judge_index}] must be a nonempty string")
    return data


class EvalContractTests(unittest.TestCase):
    def setUp(self):
        self.valid = {
            "version": 2,
            "skill": "landing-page",
            "rule": "Judge observable outcomes.",
            "regressions": [{"id": "regression-one", "prompt": "A prompt.", "judge": ["A criterion."]}],
            "creative_briefs": [{"id": "creative-one", "brief": "A brief."}],
            "activation": [{"id": "activation-one", "prompt": "A prompt.", "judge": ["A criterion."]}],
        }

    def test_repository_cases_follow_contract(self):
        validate_cases(CASES_PATH.read_text(encoding="utf-8"))

    def test_optional_setup_is_valid_in_prompt_groups(self):
        for group in ("regressions", "activation"):
            self.valid[group][0]["setup"] = "Relevant context."
        self.assertEqual(validate_cases(json.dumps(self.valid)), self.valid)

    def test_malformed_cases_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "invalid JSON"):
            validate_cases("{")
        for root in ([], None, "text"):
            with self.subTest(root=root), self.assertRaisesRegex(ValueError, "root must be an object"):
                validate_cases(json.dumps(root))

        mutations = [
            ("wrong-version", ("version",), 3, "version"),
            ("boolean-version", ("version",), True, "version"),
            ("float-version", ("version",), 2.0, "version"),
            ("wrong-skill", ("skill",), "other", "skill"),
            ("empty-rule", ("rule",), "  ", "rule"),
            ("nontext-rule", ("rule",), [], "rule"),
            ("extra-root-field", ("extra",), "value", "root fields"),
            ("duplicate-id", ("activation", 0, "id"), "regression-one", "duplicate id"),
            ("invalid-id", ("regressions", 0, "id"), "Bad_ID", "kebab-case"),
            ("nontext-id", ("regressions", 0, "id"), 1, "kebab-case"),
            ("empty-judge", ("regressions", 0, "judge"), [], "judge"),
            ("nonlist-judge", ("regressions", 0, "judge"), "criterion", "judge"),
            ("blank-criterion", ("regressions", 0, "judge"), [" "], "judge\\[0\\]"),
            ("nontext-criterion", ("regressions", 0, "judge"), [None], "judge\\[0\\]"),
            ("blank-prompt", ("activation", 0, "prompt"), "\n", "prompt"),
            ("nontext-prompt", ("activation", 0, "prompt"), False, "prompt"),
            ("blank-brief", ("creative_briefs", 0, "brief"), "", "brief"),
            ("nontext-brief", ("creative_briefs", 0, "brief"), [], "brief"),
            ("blank-setup", ("regressions", 0, "setup"), " ", "setup"),
            ("nontext-setup", ("regressions", 0, "setup"), {}, "setup"),
            ("unexpected-case-field", ("regressions", 0, "extra"), "x", "unexpected fields"),
            ("judge-in-creative-brief", ("creative_briefs", 0, "judge"), ["x"], "unexpected fields"),
        ]
        for group in GROUPS:
            mutations.extend([
                (f"empty-{group}", (group,), [], group),
                (f"nonlist-{group}", (group,), {}, group),
                (f"nonobject-{group}-case", (group, 0), "text", "must be an object"),
            ])
        for label, path, value, message in mutations:
            data = copy.deepcopy(self.valid)
            target = data
            for key in path[:-1]:
                target = target[key]
            target[path[-1]] = value
            with self.subTest(case=label), self.assertRaisesRegex(ValueError, message):
                validate_cases(json.dumps(data))

        for path in (("activation",), ("version",), ("regressions", 0, "judge"),
                     ("creative_briefs", 0, "brief"), ("activation", 0, "prompt"),
                     ("regressions", 0, "id")):
            data = copy.deepcopy(self.valid)
            target = data
            for key in path[:-1]:
                target = target[key]
            del target[path[-1]]
            with self.subTest(missing=path), self.assertRaisesRegex(ValueError, "missing"):
                validate_cases(json.dumps(data))


if __name__ == "__main__":
    unittest.main()
