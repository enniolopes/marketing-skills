#!/usr/bin/env python3
"""Minimal validation for the standalone Agent Skills in this repository.

Run locally and in CI with:

    python development/validate.py

This checks mechanical contracts only: runtime shape, metadata, references,
marketplace projections, Python syntax, and unit tests. It does not prove
behavioral or creative quality.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
LICENSE = "CC-BY-NC-4.0"
SEMVER = re.compile(r"^\d+\.\d+\.\d+$")
SKILL_NAME = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
TEXT_SUFFIXES = {".md", ".json", ".py", ".txt", ".yaml", ".yml"}
RUNTIME_FORBIDDEN_NAMES = {"README.md", "tests", "evals", "docs", "dist"}
RUNTIME_FORBIDDEN_REFS = ("development/", "systems/")
RUNTIME_PATH = re.compile(r"\b(?:references?|templates?|scripts)/[A-Za-z0-9_.\-/]+")


def rel(path: Path) -> str:
    return path.relative_to(REPO_ROOT).as_posix()


def load_json(path: Path, errors: list[str]) -> dict | None:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        errors.append(f"{rel(path)}: invalid JSON ({exc})")
        return None
    if not isinstance(data, dict):
        errors.append(f"{rel(path)}: JSON root must be an object")
        return None
    return data


def frontmatter(path: Path) -> dict[str, str]:
    """Read the repository's intentionally small one-line YAML metadata subset."""
    lines = path.read_text(encoding="utf-8").splitlines()
    if not lines or lines[0].strip() != "---":
        return {}
    out: dict[str, str] = {}
    parent: str | None = None
    for line in lines[1:]:
        if line.strip() == "---":
            return out
        key, sep, value = line.partition(":")
        if not sep or not key.strip():
            continue
        if line.startswith((" ", "\t")) and parent:
            out[f"{parent}.{key.strip()}"] = value.strip().strip("'\"")
        else:
            parent = key.strip()
            out[parent] = value.strip().strip("'\"")
    return {}


def check_runtime_tree(root: Path, errors: list[str]) -> None:
    for path in root.rglob("*"):
        if path.name in RUNTIME_FORBIDDEN_NAMES:
            errors.append(f"{rel(path)}: development material inside runtime")
        if not (path.is_file() and path.suffix in TEXT_SUFFIXES):
            continue
        text = path.read_text(encoding="utf-8", errors="replace")
        for ref in RUNTIME_FORBIDDEN_REFS:
            if ref in text:
                errors.append(f"{rel(path)}: runtime depends on repository path {ref!r}")


def check_skill(path: Path, names: set[str], errors: list[str]) -> str:
    skill = path / "SKILL.md"
    if not skill.is_file():
        errors.append(f"{rel(path)}: missing SKILL.md")
        return ""

    fm = frontmatter(skill)
    name = fm.get("name", "")
    description = fm.get("description", "")
    compatibility = fm.get("compatibility")
    version = fm.get("metadata.version", "")

    if name != path.name:
        errors.append(f"{rel(skill)}: name must match directory")
    if not (1 <= len(name) <= 64) or not SKILL_NAME.fullmatch(name):
        errors.append(f"{rel(skill)}: name violates Agent Skills naming constraints")
    if not (1 <= len(description) <= 1024):
        errors.append(f"{rel(skill)}: description must be 1..1024 characters")
    if compatibility is not None and not (1 <= len(compatibility) <= 500):
        errors.append(f"{rel(skill)}: compatibility must be 1..500 characters")
    if fm.get("license") != LICENSE:
        errors.append(f"{rel(skill)}: license must be {LICENSE}")
    if not SEMVER.match(version):
        errors.append(f"{rel(skill)}: metadata.version must be semver")
    if name in names:
        errors.append(f"{rel(path)}: duplicate runtime name {name!r}")

    for match in RUNTIME_PATH.findall(skill.read_text(encoding="utf-8")):
        if not (path / match.rstrip(".,;:)")).exists():
            errors.append(f"{rel(skill)}: missing direct runtime reference {match!r}")

    names.add(name)
    check_runtime_tree(path, errors)
    return version


def discover_skills(errors: list[str]) -> dict[str, tuple[str, str]]:
    root = REPO_ROOT / "skills"
    if not root.is_dir():
        errors.append("skills/: missing")
        return {}

    names: set[str] = set()
    expected: dict[str, tuple[str, str]] = {}
    for path in sorted(p for p in root.iterdir() if p.is_dir()):
        version = check_skill(path, names, errors)
        expected[path.name] = (f"./skills/{path.name}", version)
    return expected


def check_development_ownership(skills: set[str], errors: list[str]) -> None:
    root = REPO_ROOT / "development"
    if not root.is_dir():
        errors.append("development/: missing")
        return
    for path in sorted(p for p in root.iterdir() if p.is_dir() and p.name != "__pycache__"):
        if path.name not in skills:
            errors.append(f"{rel(path)}: no corresponding skill; remove or move this development material")


def check_marketplace(expected: dict[str, tuple[str, str]], errors: list[str]) -> None:
    path = REPO_ROOT / ".claude-plugin" / "marketplace.json"
    data = load_json(path, errors) if path.is_file() else None
    if data is None:
        if not path.is_file():
            errors.append(".claude-plugin/marketplace.json: missing")
        return

    plugins = {
        item.get("name"): item
        for item in data.get("plugins", [])
        if isinstance(item, dict) and item.get("name")
    }
    if len(plugins) != len(data.get("plugins", [])):
        errors.append(f"{rel(path)}: every plugin needs a unique name")
        return
    if set(plugins) != set(expected):
        errors.append(f"{rel(path)}: entries must match skills/")
        return

    for name, (source, version) in expected.items():
        item = plugins[name]
        if item.get("source") != source or not item.get("description"):
            errors.append(f"marketplace {name!r}: wrong source or missing description")
        if item.get("version") != version:
            errors.append(f"marketplace {name!r}: version must match canonical runtime")
        if item.get("strict") is not False:
            errors.append(f"marketplace {name!r}: standalone skill needs strict=false")


def compile_python(errors: list[str]) -> None:
    result = subprocess.run(
        [sys.executable, "-m", "compileall", "-q", "skills", "development"],
        cwd=REPO_ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode:
        errors.append("python compile failed: " + (result.stderr or result.stdout).strip())


def run_tests(skills: set[str], errors: list[str]) -> int:
    suites = 0
    for name in sorted(skills):
        path = REPO_ROOT / "development" / name / "tests"
        if not path.is_dir():
            continue
        suites += 1
        result = subprocess.run(
            [sys.executable, "-m", "unittest", "discover", "-s", str(path)],
            cwd=REPO_ROOT,
            capture_output=True,
            text=True,
        )
        if result.returncode:
            errors.append(f"{rel(path)}: tests failed\n{result.stderr.strip()}")
    return suites


def main() -> int:
    errors: list[str] = []
    expected = discover_skills(errors)
    skills = set(expected)
    check_development_ownership(skills, errors)
    check_marketplace(expected, errors)
    compile_python(errors)
    suites = run_tests(skills, errors)

    if errors:
        print(f"invalid ({len(errors)}):")
        for error in errors:
            print(f"- {error}")
        return 1

    print(f"valid: {len(skills)} skill(s); {suites} test suite(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
