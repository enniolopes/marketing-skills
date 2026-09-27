#!/usr/bin/env python3
"""Run condition-hidden control/treatment behavioral evals for the research plugin.

Dry by default. Pass --execute to invoke Claude Code and incur model usage.
Executed runs use Claude Code bare mode so host plugins, skills, hooks, memory and CLAUDE.md
cannot contaminate the control. Bare mode requires provider credentials (for the Anthropic
API, ANTHROPIC_API_KEY). Treatment loads only the local research and explorer plugins.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fixtures

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]
SCENARIOS = HERE / "scenarios.json"
JUDGE_PROMPT = HERE / "judge" / "research-eval-judge.md"
PLUGIN = REPO / "systems" / "research"
EXPLORER = REPO / "skills" / "explorer"
VALIDATOR = PLUGIN / "skills" / "research-map" / "scripts" / "validate_all.py"
EXPECTED_TREATMENT_PLUGINS = {"research", "explorer"}


def command(*args: str, cwd: Path | None = None, timeout: int | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(list(args), cwd=cwd, capture_output=True, text=True, timeout=timeout)


def repo_sha() -> str:
    result = command("git", "rev-parse", "HEAD", cwd=REPO)
    return result.stdout.strip() if result.returncode == 0 else "unknown"


def load_scenarios() -> dict[str, dict]:
    data = json.loads(SCENARIOS.read_text(encoding="utf-8"))
    return {item["id"]: item for item in data["scenarios"]}


def safe_snapshot(root: Path, initial: str) -> str:
    committed = command("git", "diff", f"{initial}..HEAD", "--", ".", cwd=root).stdout
    working = command("git", "diff", "--", ".", cwd=root).stdout
    status = command("git", "status", "--short", cwd=root).stdout
    return "# committed diff\n" + committed + "\n# working diff\n" + working + "\n# status\n" + status


def preserve_artifacts(root: Path, destination: Path) -> dict[str, Any]:
    """Preserve tracked and nonignored new files before the temp repo disappears.

    Do not follow symlinks out of the fixture. Record omissions explicitly so
    absent bytes cannot be mistaken for reviewed evidence.
    """
    listing = command("git", "ls-files", "-z", "--cached", "--others", "--exclude-standard", cwd=root)
    if listing.returncode:
        raise RuntimeError("cannot enumerate eval artifacts")
    records = []
    for name in sorted(set(listing.stdout.split("\0")) - {""}):
        path = root / name
        record: dict[str, Any] = {"path": name}
        if path.is_symlink() or any(p.is_symlink() for p in path.parents if p != root and root in p.parents):
            record["status"] = "omitted-symlink"
        elif not path.is_file():
            record["status"] = "missing"
        else:
            data = path.read_bytes()
            target = destination / "artifacts" / name
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(data)
            record.update(status="saved", size=len(data), sha256=hashlib.sha256(data).hexdigest())
        records.append(record)
    manifest = {"scope": "tracked and nonignored untracked files; symlinks not followed", "files": records}
    (destination / "artifacts.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    return manifest


def artifact_excerpt(destination: Path, manifest: dict, paths: list[str], budget: int = 120000) -> str:
    """Expose changed file content to the judge, marking binary/size omissions."""
    selected = set(paths)
    chunks = []
    for record in manifest["files"]:
        if record["path"] not in selected:
            continue
        header = f"\nFILE {record['path']} ({record['status']})\n"
        if record["status"] != "saved":
            chunks.append(header)
            continue
        try:
            content = (destination / "artifacts" / record["path"]).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            chunks.append(header + "[binary; bytes retained, semantic inspection NOT_VERIFIED]\n")
            continue
        available = max(0, budget)
        excerpt = content[:available]
        budget -= len(excerpt)
        chunks.append(header + excerpt)
        if len(excerpt) < len(content):
            chunks.append("\n[omitted from judge context; full bytes retained; affected judgment NOT_VERIFIED]\n")
    return "\n".join(chunks)


def runner_cmd(prompt: str, condition: str, model: str, max_turns: int) -> list[str]:
    cmd = [
        "claude",
        "--bare",
        "-p",
        prompt,
        "--model",
        model,
        "--output-format",
        "stream-json",
        "--verbose",
        "--max-turns",
        str(max_turns),
        "--permission-mode",
        "auto",
        "--no-session-persistence",
    ]
    if condition == "treatment":
        cmd.extend(["--plugin-dir", str(PLUGIN), "--plugin-dir", str(EXPLORER)])
    return cmd


def json_events(transcript: str) -> list[dict[str, Any]]:
    events: list[dict[str, Any]] = []
    for raw in transcript.splitlines():
        try:
            event = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if isinstance(event, dict):
            events.append(event)
    return events


def system_init(transcript: str) -> dict | None:
    for event in json_events(transcript):
        if event.get("type") == "system" and event.get("subtype") == "init":
            return event
    return None


def startup_check(transcript: str, condition: str) -> tuple[bool, str]:
    init = system_init(transcript)
    if init is None:
        return False, "FAIL: no system/init event; condition isolation cannot be verified\n"
    plugins = {
        str(item.get("name", ""))
        for item in init.get("plugins", [])
        if isinstance(item, dict) and item.get("name")
    }
    errors = init.get("plugin_errors", []) or []
    lines = [f"plugins={sorted(plugins)}", f"plugin_errors={errors}"]
    if errors:
        return False, "FAIL: plugin load errors\n" + "\n".join(lines) + "\n"
    if condition == "control":
        contaminated = plugins & EXPECTED_TREATMENT_PLUGINS
        if contaminated:
            return False, "FAIL: control contaminated by treatment plugin(s): " + ", ".join(sorted(contaminated)) + "\n" + "\n".join(lines) + "\n"
    else:
        missing = EXPECTED_TREATMENT_PLUGINS - plugins
        if missing:
            return False, "FAIL: treatment missing plugin(s): " + ", ".join(sorted(missing)) + "\n" + "\n".join(lines) + "\n"
    return True, "PASS: condition startup verified\n" + "\n".join(lines) + "\n"


def _walk_tool_uses(value: Any, uses: list[dict[str, Any]]) -> None:
    if isinstance(value, dict):
        if value.get("type") == "tool_use" and value.get("name"):
            uses.append({"name": str(value["name"]), "input": value.get("input", {})})
        for child in value.values():
            _walk_tool_uses(child, uses)
    elif isinstance(value, list):
        for child in value:
            _walk_tool_uses(child, uses)


def tool_uses(transcript: str) -> list[dict[str, Any]]:
    """Extract actual structured tool-use blocks; prose mentions do not count."""
    uses: list[dict[str, Any]] = []
    for event in json_events(transcript):
        _walk_tool_uses(event, uses)
    return uses


def changed_paths(root: Path, initial: str) -> list[str]:
    paths: set[str] = set()
    for args in (
        ("git", "diff", "--name-only", f"{initial}..HEAD", "--", "."),
        ("git", "diff", "--name-only", "--", "."),
        ("git", "ls-files", "--others", "--exclude-standard"),
    ):
        result = command(*args, cwd=root)
        if result.returncode == 0:
            paths.update(line.strip() for line in result.stdout.splitlines() if line.strip())
    return sorted(paths)


def deterministic_observations(root: Path, initial: str, transcript: str) -> dict[str, Any]:
    """Record machine-observable facts before asking an LLM to judge semantics.

    This layer deliberately does not decide scenario PASS/FAIL. It captures generic facts
    that should outrank a later semantic guess: actual tool calls, available tools when the
    host reports them, changed paths, and durable review records.
    """
    init = system_init(transcript) or {}
    available_tools = init.get("tools", []) or []
    if not isinstance(available_tools, list):
        available_tools = []
    uses = tool_uses(transcript)

    def input_text(use: dict[str, Any]) -> str:
        try:
            return json.dumps(use.get("input", {}), ensure_ascii=False, sort_keys=True)
        except TypeError:
            return str(use.get("input", {}))

    reviewer2_calls = [
        index
        for index, use in enumerate(uses)
        if use.get("name") in {"Task", "Agent"} and "reviewer-2" in input_text(use).lower()
    ]
    separate_agent_calls = [
        index for index, use in enumerate(uses) if use.get("name") in {"Task", "Agent"}
    ]
    review_records = sorted(
        path.relative_to(root).as_posix()
        for path in (root / ".research" / "reviews").glob("REVIEW-*.md")
    ) if (root / ".research" / "reviews").is_dir() else []

    return {
        "available_tools": [str(item) for item in available_tools],
        "tool_uses": [
            {"index": index, "name": use.get("name"), "input": use.get("input", {})}
            for index, use in enumerate(uses)
        ],
        "changed_paths": changed_paths(root, initial),
        "separate_agent_invoked": bool(separate_agent_calls),
        "separate_agent_call_indices": separate_agent_calls,
        "reviewer2_invoked": bool(reviewer2_calls),
        "reviewer2_call_indices": reviewer2_calls,
        "review_records": review_records,
    }


def validate_fixture(root: Path) -> str:
    result = command(
        sys.executable,
        str(VALIDATOR),
        str(root / "RESEARCH.map"),
        "--root",
        str(root),
        "--offline",
        cwd=root,
    )
    return result.stdout + ("\nSTDERR\n" + result.stderr if result.stderr else "")


def judge_run(
    scenario: dict,
    transcript: str,
    diff: str,
    validator: str,
    observations: dict[str, Any],
    model: str,
    timeout: int,
) -> str:
    prompt = f"""Judge this completed research eval run. The experimental condition is hidden from you.

SCENARIO STATE
{scenario['state']}

EXPECTED BEHAVIOR
{scenario['expect']}

DETERMINISTIC OBSERVATIONS
{json.dumps(observations, indent=2, ensure_ascii=False)}

RUNNER TRANSCRIPT
{transcript}

REPOSITORY DIFF/STATUS
{diff}

VALIDATOR OUTPUT
{validator}
"""
    with tempfile.TemporaryDirectory(prefix="research-judge-") as tmp:
        result = command(
            "claude",
            "--bare",
            "-p",
            prompt,
            "--model",
            model,
            "--output-format",
            "text",
            "--append-system-prompt-file",
            str(JUDGE_PROMPT),
            "--max-turns",
            "4",
            "--permission-mode",
            "dontAsk",
            "--no-session-persistence",
            cwd=Path(tmp),
            timeout=timeout,
        )
    return result.stdout + ("\nSTDERR\n" + result.stderr if result.stderr else "")


def one_run(
    scenario: dict,
    condition: str,
    repetition: int,
    model: str,
    judge_model: str,
    max_turns: int,
    timeout: int,
    out_root: Path,
    execute: bool,
    judge: bool,
) -> Path:
    with tempfile.TemporaryDirectory(prefix=f"research-eval-{scenario['id']}-") as tmp:
        root = Path(tmp)
        user_prompt = fixtures.build(scenario["id"], root)
        initial = command("git", "rev-parse", "HEAD", cwd=root).stdout.strip()
        full_prompt = (
            "Work directly in the current research repository and complete the user's request. "
            "Inspect files and execute available checks/code when needed; do not merely describe what you could do.\n\n"
            + user_prompt
        )
        cmd = runner_cmd(full_prompt, condition, model, max_turns)
        stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
        run_id = f"{stamp}-r{repetition}"
        destination = out_root / scenario["id"] / condition / run_id
        destination.mkdir(parents=True, exist_ok=True)
        metadata = {
            "scenario": scenario["id"],
            "class": scenario.get("class"),
            "condition": condition,
            "repetition": repetition,
            "model": model,
            "repo_sha": repo_sha(),
            "initial_fixture_commit": initial,
            "command": cmd,
            "prompt": full_prompt,
            "isolation": "claude --bare; treatment loads only local research + explorer via --plugin-dir",
        }
        (destination / "metadata.json").write_text(json.dumps(metadata, indent=2) + "\n", encoding="utf-8")

        if not execute:
            (destination / "DRY_RUN.txt").write_text("Command not executed. Pass --execute.\n", encoding="utf-8")
            return destination

        env = os.environ.copy()
        env["CLAUDE_CODE_SKIP_PROMPT_HISTORY"] = "1"
        try:
            proc = subprocess.run(cmd, cwd=root, capture_output=True, text=True, timeout=timeout, env=env)
            transcript = proc.stdout
            stderr = proc.stderr
            exit_code = proc.returncode
        except subprocess.TimeoutExpired as exc:
            transcript = exc.stdout.decode(errors="replace") if isinstance(exc.stdout, bytes) else (exc.stdout or "")
            partial_error = exc.stderr.decode(errors="replace") if isinstance(exc.stderr, bytes) else (exc.stderr or "")
            stderr = partial_error + f"\nTIMEOUT after {timeout}s\n"
            exit_code = 124
        (destination / "transcript.jsonl").write_text(transcript, encoding="utf-8")
        (destination / "stderr.txt").write_text(stderr, encoding="utf-8")
        (destination / "exit_code.txt").write_text(str(exit_code) + "\n", encoding="utf-8")

        startup_ok, startup = startup_check(transcript, condition)
        (destination / "startup_check.txt").write_text(startup, encoding="utf-8")
        diff = safe_snapshot(root, initial)
        validator = validate_fixture(root)
        observations = deterministic_observations(root, initial, transcript)
        artifacts = preserve_artifacts(root, destination)
        diff += "\n# Changed artifact contents\n" + artifact_excerpt(destination, artifacts, observations["changed_paths"])
        (destination / "diff.patch").write_text(diff, encoding="utf-8")
        (destination / "validator.txt").write_text(validator, encoding="utf-8")
        (destination / "observations.json").write_text(
            json.dumps(observations, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
        )

        if judge:
            if startup_ok and exit_code == 0:
                judgment = judge_run(
                    scenario,
                    transcript,
                    diff,
                    validator,
                    observations,
                    judge_model,
                    timeout,
                )
            else:
                judgment = "VERDICT: NOT_VERIFIED\n\nOBSERVED\nRun invalid before adjudication.\n\nCRITERION\nCondition isolation and successful runner startup are prerequisites.\n\nEVIDENCE\n" + startup + f"runner exit code={exit_code}\n\nFAILURE_MECHANISM\neval-infrastructure\n\nMECHANIZABLE\nyes — startup is mechanically observable\n\nMECHANIZATION\nsystem/init plugin gate\n"
            (destination / "judgment.txt").write_text(judgment, encoding="utf-8")
        return destination


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run isolated research behavioral evals (dry by default).")
    parser.add_argument("--scenario", action="append", help="scenario id; repeatable; default all")
    parser.add_argument("--condition", choices=["control", "treatment", "both"], default="both")
    parser.add_argument("--repetitions", type=int, default=3)
    parser.add_argument("--model", default="opus")
    parser.add_argument("--judge-model", default="opus")
    parser.add_argument("--max-turns", type=int, default=20)
    parser.add_argument("--timeout", type=int, default=900)
    parser.add_argument("--out", type=Path, default=HERE / "runs" / repo_sha())
    parser.add_argument("--execute", action="store_true", help="invoke Claude Code in bare mode; requires provider credentials")
    parser.add_argument("--judge", action="store_true", help="invoke a condition-hidden judge after each valid executed run")
    args = parser.parse_args(argv)

    scenarios = load_scenarios()
    selected = args.scenario or list(scenarios)
    unknown = [item for item in selected if item not in scenarios]
    if unknown:
        parser.error("unknown scenario(s): " + ", ".join(unknown))
    if args.repetitions < 1:
        parser.error("--repetitions must be >= 1")
    if args.execute and not os.environ.get("ANTHROPIC_API_KEY"):
        print("warning: --bare does not use Claude subscription OAuth; set ANTHROPIC_API_KEY (or configured provider credentials)", file=sys.stderr)
    conditions = ["control", "treatment"] if args.condition == "both" else [args.condition]

    outputs: list[Path] = []
    for scenario_id in selected:
        for condition in conditions:
            for repetition in range(1, args.repetitions + 1):
                path = one_run(
                    scenarios[scenario_id],
                    condition,
                    repetition,
                    args.model,
                    args.judge_model,
                    args.max_turns,
                    args.timeout,
                    args.out,
                    args.execute,
                    args.judge,
                )
                outputs.append(path)
                print(path)
    print(f"{len(outputs)} run directory/directories created" + (" and executed" if args.execute else " (dry run)"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
