# Creative Control — preserve intent without freezing the solution

Read this at DIRECT for CREATE/major REFINE, and again only when materially new evidence or a possible pivot appears.

The purpose is not to make design procedural. It is to keep the page-level purpose governing local decisions while leaving the solution free to change.

## Core rule

Preserve the problem more strongly than the current solution.

Preserve creative intent more strongly than its current expression.

Treat a chosen direction as a **working hypothesis**, not a contract.

Keep this control model internal. Do not narrate its taxonomy to the user or turn it into visible page structure unless that genuinely helps the work.

## Compact working state

For long, high-ambition, multi-context, or handoff-prone work, externalize only the state most likely to drift. Keep it ephemeral unless the project explicitly needs a durable artifact.

~~~yaml
landing_page_state:
  mode: CREATE # CREATE | REFINE | REPAIR
  quality_bar: high_end # standard | high_end | frontier
  goal:
  truth:
    known: []
    blocking_unknowns: []
  intent:
    page_job:
    proposition:
    primary_action:
  active_invariants: []
  direction:
    governing_idea:
    signature:
    falsifier:
  visual_search:
    status: open # not_needed | open | shortlisted | committed
    unresolved_question:
    selected_artifact:
  largest_material_risk:
  largest_creative_upside:
  next_valid_evidence:
  done_when: []
~~~

This is a memory aid, not a form and not a chain-of-thought transcript. Populate only what materially prevents drift. A short REPAIR often needs none of it.

Do not commit this state into the customer's production repository by default.

## Unequal inertia

Think in five layers:

1. **TRUTH** — product/business facts, available proof, authoritative constraints, hard technical constraints.
2. **INTENT** — page job, audience/arrival context, offer, proposition, primary action, proof/friction model.
3. **DIRECTION** — governing creative idea, emotional target, signature, content/interaction thesis, restraint.
4. **EXPRESSION** — narrative/composition, hierarchy, visual grammar, imagery treatment, motion, responsive form.
5. **EXECUTION** — code, exact styling, assets, crops, timings, breakpoints, performance and micro-craft.

They should not move at the same rate.

- TRUTH changes only with better evidence, authority or a real constraint.
- INTENT changes when the page is solving the wrong decision or a stronger truthful framing is established.
- DIRECTION needs enough stability to create coherence, but may be abandoned when it produces the wrong meaning or a materially stronger idea emerges.
- EXPRESSION should change freely when a better realization of the same idea appears.
- EXECUTION is cheap to revise.

Explorations are outside this chain: they are disposable and may be strange, incomplete or rejected without consequence.

## Preserve material intent across layers

After SYNTHESIZE, keep only the few truth/intent properties whose loss would make downstream work materially wrong or weaker. Treat them as active invariants until better evidence, authority or a deliberate intent change invalidates them.

An active invariant states **what must survive**, not how to implement it. `A resolved product/configuration must remain attached to the conversion path` is an invariant; `use a sticky CTA` is a solution. When the page has a primary visitor task or transition that downstream design could degrade, preserve **task integrity** as an active invariant: from arrival through the intended transition, the path remains discoverable, understandable, and efficient for the page job. A working CTA is not sufficient if navigation, motion, scroll choreography, responsive adaptation, context loss, or another expressive choice adds avoidable effort. Additional effort is justified only when it materially serves the page job.

Do not create a fixed schema or ledger; usually one to three invariants are enough, and none are needed when the page intent already carries everything material without risk of drift.

At the few transitions where loss is plausible — committing a direction, judging a representative artifact, and final refinement — ask:

- what did this layer receive that it is not allowed to lose?
- does the proposed transformation preserve or strengthen it?
- what observable result would falsify that preservation?

If an invariant is wrong, revise it at TRUTH/INTENT with valid evidence or authority. Otherwise fix the downstream layer rather than silently weakening the requirement.

## Direction without a schema

Before substantial implementation, be able to state compactly:

- the governing idea;
- the signature or dominant expression;
- what the direction should make clearer, more credible, more appropriate or more memorable;
- what observable failure would make the idea wrong.

Do not require a fixed form or persisted object. Do not freeze colors, fonts, layouts, libraries or effects unless they are intrinsically part of the idea.

A useful direction generates decisions. A weak direction merely describes styling.

For HIGH-END/FRONTIER CREATE or materially open visual REFINE, a direction that exists only as prose is not yet sufficiently tested for commitment. Use `visual-explore.md` to externalize the highest-risk visual hypothesis before substantial visual implementation. The artifact is evidence about the hypothesis, not a contract to copy.

## Exploration can be intuitive

A new idea does not need a complete rationale before it may be explored. Use intuition, non-adjacent references and wildcard routes when they may open useful territory.

For a serious route, know only enough to test it:

- governing idea;
- connection it might have to the page intent;
- expressive territory it unlocks;
- likely failure;
- smallest prototype/render that would teach something.

Prefer making the uncertain thing visible over writing more rationale about it.

Exploration may be intuitive. Commitment must become defensible.

Do not keep every explored route in working memory once it stops adding decision value.

## Learning runs both directions

Decisions usually flow from TRUTH toward EXECUTION, but learning can travel upward.

A render, composition experiment or real asset may reveal that the current direction is wrong. More importantly, creative work may reveal a **better proposition or page framing** that was not obvious during synthesis.

When downstream work suggests an upstream improvement:

1. treat it as a hypothesis, not as permission to rewrite facts;
2. test it against real product evidence, audience context and business authority;
3. if it is better and truthful, deliberately update INTENT and revalidate downstream work;
4. if it is only visually attractive, keep the existing intent.

Creativity may discover strategy. It may not invent truth.

## Observe before patching

When a material problem appears, ask for the lowest level that fully explains it.

- **TRUTH** — an assumed capability, claim, proof source or constraint is wrong.
- **INTENT** — the proposition, action, proof model or visitor decision is wrong.
- **DIRECTION** — the governing idea produces the wrong meaning, emotion, specificity or category signal.
- **EXPRESSION** — the idea remains sound, but narrative, hierarchy, rhythm, visual grammar or responsive composition is weak.
- **EXECUTION** — the design decision is sound; implementation/craft is failing.

Fix the lowest level that explains the evidence. A downstream defect does not justify reopening everything above it. An upstream change requires downstream revalidation, not automatic destruction of solved work.

Repeated downstream exceptions are themselves evidence. If many local fixes are required to keep a direction working, question whether the next upstream layer is actually the problem instead of accumulating patches.

## REFINE or RE-DIVERGE

**REFINE** when the current governing idea still serves the truthful intent and the defect belongs to expression or execution.

**RE-DIVERGE** when the governing idea itself is materially falsified, has become generic after rendering, cannot be supported by real evidence, or a demonstrably stronger idea appears.

Do not protect a direction because implementation has already begun. Do not reopen a strong direction merely because novelty is possible.

For a late better idea, compare it against truth and intent rather than sunk cost. Preserve solved work that remains compatible.

## Unresolved creative questions

Some decisions are best postponed until the relevant artifact exists. Keep a material uncertainty mentally explicit and resolve it at the earliest useful render/prototype rather than asking the user to choose a reversible design preference.

Do not turn these uncertainties into a formal register unless the task is long enough that forgetting them is a demonstrated risk.

## Anti-rigidity

The control model is failing if it causes any of these:

- the first plausible direction becomes sacred;
- every experiment needs justification before exploration;
- internal control vocabulary leaks into the visible design;
- unrelated briefs converge on one house aesthetic;
- qualitative judgment is replaced by fake numerical precision;
- a stronger late idea is rejected because work has already begun;
- local craft defects trigger full redesigns;
- process/schema completion receives more attention than the rendered page.

The goal is continuity of purpose, not continuity of form.

## Adaptive operating loop

For material work:

`OBSERVE → MODEL → CHOOSE → MAKE → OBSERVE → DIAGNOSE → UPDATE`

The loop serves the artifact; it is not a phase checklist.

Choose the next action by expected improvement to the final result. Resolve the largest material risk or highest-value creative uncertainty with evidence of sufficient fidelity before the current commitment makes it expensive to reverse. When two actions have comparable value, prefer the simpler/cheaper one. Do not choose a cheaper action that materially lowers the creative ceiling or increases likely rework.

Ground truth and intent. Explore widely enough to find a point of view. Commit only long enough to build coherent evidence. Let real output teach what prose could not. Then improve the current idea, reopen the lowest causal layer that explains the failure, or deliberately replace the direction.
