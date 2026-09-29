# Landing Page — evaluation

`cases.json` is intentionally small: one case per distinct failure mechanism plus four briefs for creative generalization. Judge behavior and rendered work, not runtime vocabulary.

## Evidence

- **L0 — structural:** CI, syntax and deterministic contracts.
- **L2 — proxy:** same-model or simulated comparison; useful for obvious regressions, not proof of improvement.
- **L3 — blind A/B:** independent baseline/candidate runs on identical inputs with version identity hidden from reviewers.
- **L4 — real work:** repeated production use with browser/render evidence and genuine constraints.

Do not claim behavioral superiority from L0–L2.

## Run

For a targeted change, run only regression cases that can distinguish it. For a material creative or composition change, also run the four creative briefs. Keep baseline and candidate isolated and give both the same prompt, evidence, tools and capability envelope. Review desktop/mobile artifacts before rationales, and only treat a visual artifact as evidence for states that were actually loaded, exercised and allowed to settle.

## Judge

Use five dimensions:

1. **Truth and intent** — factual claims, page job and conversion logic stay grounded, material truth/intent properties survive downstream hierarchy, interaction and implementation unless deliberately revised with valid evidence or authority, and the page's job, argument progression and intended action remain recoverable from the artifact before rationale is considered.
2. **Causal scope** — local defects stay local; upstream failures reopen only what they invalidate.
3. **Specificity and expression** — the governing idea and composition depend on this product/domain rather than a recurring house style or reflexive anti-default posture.
4. **Craft and reality** — hierarchy, typography, imagery, motion, responsive behavior and implementation survive rendered inspection where relevant; evidence must observe the state it claims to judge; for generated imagery, judge art direction, product-specific relevance, asset craft, integration, responsive crop, loading behavior and browser composition rather than generator success in isolation.
5. **Context efficiency** — extra research, process or rules must materially improve a decision; polish, novelty and completeness are not quality proxies.

Across creative briefs, flag repeated solutions only when they lack brief-specific causality. Familiar mechanisms are valid when earned.

## Decision rule

Promote a candidate only when its intended behavior difference is observable, no severe truth/intent regression appears, and creative quality is non-inferior overall. If baseline and candidate behave materially the same, do not add context. If an eval rewards exact wording, a fixed layout or one historical implementation rather than the underlying decision, fix the eval instead of the runtime.
