# Contributing

This repository has one job: ship small, portable Agent Skills whose behavior is easy to inspect, test, and maintain.

## Repository model

- `skills/<name>/` is runtime. It is the source of truth for the installed skill and must remain portable.
- `development/<name>/` contains only tests, evals, fixtures, or maintenance tooling for that skill.
- `.claude-plugin/marketplace.json` is a distribution projection. Its skill versions must match the canonical versions in `SKILL.md`.
- `README.md` is the consumer entry point. Do not duplicate runtime behavior in separate documentation.

A development directory without a corresponding skill is dead material and should not remain here.

## Make changes at the smallest responsible layer

1. Inspect the current runtime and the evidence relevant to the problem.
2. Change the smallest rule, reference, script, test, or projection that can fix it.
3. Keep runtime guidance only when it materially changes behavior.
4. Use deterministic code only for machine-decidable properties.
5. Add an eval only for a distinct recurring failure mechanism.
6. Do not treat passing checks, polished output, or model agreement as proof of behavioral or creative quality.

Runtime must not depend on `development/` or repository-only structure.

When runtime semantics change, bump that skill's version intentionally. Repository-only cleanup, tests, evals, and documentation do not require a runtime version bump.

## Verify

Run the blocking repository validation:

```bash
python development/validate.py
```

For behavior changes, also run the smallest eval set capable of distinguishing the intended change. Compare baseline and candidate before claiming improvement when the claim is behavioral.

## Pull requests

A PR should make three things obvious:

- what concrete problem it fixes;
- why the chosen change is the smallest durable solution;
- what verification was actually run.

Keep generated release artifacts and temporary evaluation output out of source control.
