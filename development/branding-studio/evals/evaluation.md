# Branding Studio — evaluation

Evaluate behavior and artifacts, not whether the model repeats runtime terminology. `cases.json` is intentionally small: each case represents a different failure mechanism, not a rule in the skill.

## Evidence levels

- **L0 — structural:** CI, packaging, syntax and deterministic-tool contracts.
- **L2 — proxy:** same-model or simulated comparison; useful for falsifying obvious regressions, not proving superiority.
- **L3 — blind A/B:** independent baseline/candidate runs on identical inputs, with runtime identity hidden from reviewers. Minimum useful level for a claim of better branding behavior.
- **L4 — real work:** genuine constraints, operators and external outcomes. Market/perception claims require their own evidence.

## Run

For a targeted change, run only the regression cases that can distinguish it. For a material creative-system change, also run the four creative briefs. Use the transfer test when guidelines or system handoff are affected.

Keep baseline and candidate isolated. Give them the same prompt, evidence and tools. Review artifacts before rationales whenever an artifact exists.

## Judge

Use seven dimensions:

1. **Truth and evidence fit** — no invented reality; each claim uses evidence capable of settling it.
2. **Decision quality** — autonomy is appropriate; exploration, commitment and correction happen at the right level.
3. **Specificity** — consequential choices depend on this brand rather than category autocomplete or arbitrary novelty.
4. **Generativity** — the system can make materially different new work without copying one layout, phrase or device.
5. **Craft, ambition and reality** — representative artifacts survive perceptual, functional and production constraints relevant to the brief, and the strongest one holds beside the adjacent-category bar named at direction; force is judged through its mechanisms (one dominant decision, one decisive jump, type as image, color by proportion, restraint), not as a taste verdict; when generated imagery is material, judge art direction, relevance, asset craft, coherence across the image family, persistence/integration and contextual performance rather than generator success.
   A numeric score, average or ranking-as-measurement for creative quality anywhere in the output is a failure of this dimension, whatever the artifact looks like; a comparison is judged by whether its criteria preceded the candidates and whether the floor and an in-market bar were in the set.
6. **Reader fit** — every reader-facing deliverable is in the audience's language and register, has been rendered and looked at on the reader's surfaces, and carries nothing from the process; its level is the level of its weakest visible element, so one weak image in a strong book scores as a weak book.
7. **Context efficiency** — extra process, rules or state must earn their cost; completeness and polish are not quality proxies.

Across creative briefs, flag repeated aesthetic or verbal solutions only when recurrence lacks brief-specific causality. Recurrence itself is not a failure.

## Decision rule

Promote a candidate only when the intended behavior difference is observable, no severe truth/authority/production regression appears, and creative quality is non-inferior overall. If baseline and candidate behave materially the same, do not add context. If a case rewards wording, a fixed template or one historical implementation rather than the underlying decision, fix the eval instead of the runtime.
