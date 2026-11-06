# Canonical brand state

Use `brand-spec.json` as the sparse private operating contract for future brand work. It records what is in force, not how it got there. Persist only information whose absence would materially increase future drift.

Canonical template: `templates/brand-spec.template.json`.

## Version fields

Keep schema compatibility separate from brand evolution:
- `meta.schema_version` — structural schema version. Current canonical schema is `5`.
- `meta.version` — this brand contract's semantic version, starting independently from the schema (for example `1.0.0`).

Increment `meta.version` when durable brand meaning/rules change. Do not change `meta.schema_version` for ordinary brand evolution.

Legacy specs (schema 4, v3 or earlier) remain operable and are interpreted using their historical shape until a meaningful migration occurs.

## Core contract

A schema-5 contract keeps only the always-useful decision core:
- `meta` — schema version, brand-contract version, brand identity, `tier` (the contract's maturity: `provisional` or `full`) and declared touchpoints;
- `strategy` — brand job, audience (with the language the brand speaks to it), offer truth, alternatives, position, right to win and desired meaning;
- `creative_direction` — thesis, principles, signature and criteria;
- `book` — the readers the brand book is written for, when a book is in scope.

Add expression/domain blocks only when they are materially active: `verbal`, `visual`, `naming`, `architecture`, or other medium-specific rules future operators genuinely need.

Absence means "not material to this contract," not "forgot to complete the template."

## Instrument, not ledger

The contract has no lifecycle fields. No item carries a `status`, a date of change, a superseded predecessor or a record of a rejected alternative. Version control owns history; the delivery report owns pending matters. Top-level blocks such as `evidence`, `history`, `changelog`, `decisions`, `open_questions` or `unresolved` do not belong in the file.

Do not persist:
- rejected or superseded creative routes;
- prompts or internal reasoning transcripts;
- research notes or the list of sources consulted;
- routine trial applications after they have done their job;
- framework outputs that do not govern future work;
- empty placeholder sections;
- a field merely because another brand might need it.

## Provenance as `basis`

When a clause depends on a fact that a future operator might otherwise overturn for the wrong reason, attach `basis`: one sentence stating the fact, with its source only when the source is inspectable. A basis records something you inspected or the owner supplied, never a plausible-sounding figure; if it is a hypothesis, the sentence says so. Attach it to the clause, not to a separate table; no IDs, no references.

```json
"right_to_win": {
  "statement": "The only network that already operates in 27 states.",
  "basis": "Kitchen registry, 2025 census: 1,340 active units."
}
```

Prefer concise causal language over a rationale on every object. Most clauses need no `basis`.

## Criteria, not techniques

For anything the brand produces repeatedly (a contextual render, a lockup export, a piece of copy), the contract persists the acceptance criterion, never the production technique: what must hold in the result and how a future operator verifies it. A criterion survives a change of tool; a technique becomes false the day the capability changes, and a contract that records one forces a rewrite or, worse, a compliant regression. When a criterion cannot be automated, the clause may say why in one sentence, so that nobody replaces it with a check that measures the wrong thing.

## Strategy and direction fields

- `brand_job` — the business/organizational transition the brand must help produce; not a mission statement.
- `audience.primary` — who the system primarily needs to serve; `audience.language` — the language the brand speaks to them (BCP 47 tag such as `pt-BR`), which every reader-facing deliverable is written in; `audience.not_for` only when it materially improves future judgment.
- `offer_truth` — what expression must not contradict.
- `alternatives` — only the decision-changing alternatives against which the brand must be understood.
- `position` — the intended meaning relative to those alternatives; a slogan only when the slogan itself is the durable decision.
- `right_to_win` — the credible basis that makes the position defensible.
- `desired_meaning` — what the system intends to make associable; achieved perception remains an external claim.
- `creative_direction.thesis`, `principles` (only rules that materially change choices), `signature` (the characteristic cue that makes the system cohere), `criteria` (the direction criteria in force: the perceptions the work must produce and avoid, confirmable from an artifact alone, which future work is judged against) and `excludes` only when likely false routes need preventing.

- `book.readers` — two to five readers of the brand book, each with `role`, `language` (BCP 47 tag) and `tasks`, two to six strings written as verb + object + situation. The owner is always one. Present only when a book is in scope; it is durable because who executes the brand changes less than the brand does. Nothing else about the book is persisted: its structure and rules live in `brand-book.md`, its pending matters in the report.

In a `provisional` contract, `position`, `right_to_win` and `desired_meaning` may be absent or carry a `basis` that says they are hypotheses; a `full` contract requires them. The validator warns in the first case and fails in the second: a required field invites an invented one, and an invented strategy is worse than a missing one.

## Verbal and visual blocks

Use open objects rather than forcing every brand into the same inventory.

Examples of legitimate keys when needed:
- `verbal.principles`, `verbal.tone_by_moment`, `verbal.message_behavior`, `verbal.excludes`;
- `visual.identity_grammar`, `visual.typography`, `visual.palette`, `visual.logo`, `visual.imagery`, `visual.iconography`, `visual.composition`, `visual.motion`, `visual.tokens`, `visual.contrast_pairs`.

A token or palette entry carries its role (`identity-craft.md`, naming of elements) as its key and the reader-facing name, in the book readers' language (the audience's language when `book.readers` is absent), in `name`; renaming is then one edit.

```json
"green": { "$type": "color", "$value": "#1F6E43", "name": "Verde Rede" }
```

When a visual decision governs future work, persist the durable behavior or relationship another operator needs, not merely the asset or value. Keep examples, channel recipes and one-off application choices out of canonical state.

## Naming

Add `naming` only when naming is part of the brand contract. Preserve the selected name, its strategic job when needed, material exclusions and dated clearance/linguistic triage. Triage does not become definitive legal clearance merely because it is persisted.

## Architecture

Add `architecture` only for brands that participate in a multi-brand relationship (`house-of-brands`, `endorsed`, `branded-house`, `hybrid`). Architecture policy can intentionally require shared cues; similarity is not universally a defect.

## Production state

For production assets such as a logo, use explicit status when needed:
- `final` — reproducible master exists and applicable production checks can be run;
- `concept` — direction exists but production remains unresolved;
- `external_craft_required` — specialist execution is needed and acceptance criteria/brief should be supplied.

This is the current state of an asset, not a history; what earns `final` is owned by `visual-artifact-production.md`.

## Machine-checkable structures

When declared, tokens use a consistent shape with resolvable aliases, contrast pairs reference the actual colors of a real text/background relationship, and modular typography carries enough numbers for its math to be checked. Validation establishes only those structural properties.

## Publication

The contract is an operating file for the people and agents who run the brand. Keep it outside any directory the host serves publicly; the public package is the brand book and its assets. Publish the contract alongside them only when the owner decides the strategy it contains is public.

## Migration

On the next meaningful CREATE/EVOLVE operation, migrate by **compressing** valid state into schema 5:
- set `meta.schema_version` to `5`;
- add `strategy.audience.language`;
- fold each `evidence` record that a clause still depends on into that clause's `basis`; discard the rest, including `status`, `evidence_refs` and any other lifecycle field;
- give tokens a reader-facing `name` where the book will display them;
- preserve valid strategy, equity and production rules;
- remove exploration history and ceremonial fields;
- do not redesign merely to migrate schema.

APPLY/AUDIT may operate a legacy spec without forcing migration when the existing state is sufficient for the requested artifact.
