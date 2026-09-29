# Verification and Refinement

Load this during material CREATE or major REFINE once there is an inspectable browser/render state, and keep it active through completion when those tools are available. Use the relevant subset for REPAIR.

The core rule is:

**Code is implementation evidence. Pixels and interaction are experience evidence.**

For award-caliber, animation-heavy, WebGL/3D/canvas, or technically ambitious work, also load `technical-excellence.md`; passing generic build/visual QA is not sufficient for creative-development excellence.

A build can pass while the page is visually poor. A screenshot can look excellent while interaction is broken. Verify both.

## Verification rule

For each applicable quality claim, use:

`quality claim → relevant state → plausible falsifier → cheapest valid oracle/evidence → finding severity`

Evidence only answers a claim for the state it actually observed. Before judging or capturing a region/state, exercise what makes it real and allow relevant lazy, async, loading, animation or interaction-driven behavior to settle. A screenshot of an unloaded lazy region, a closed menu, or an unexercised sticky/interactive state is not evidence for that state.

For visual claims, choose the smallest useful observation as `state × viewport × scope` — for example, `settled × mobile × first viewport`. Screenshots are strong evidence for appearance, comparison and composition, not for interaction behavior; exercise motion, sticky states, menus and task flows in the browser, then capture the relevant state when a still image helps judgment.

Examples:

| Claim | Falsifier | Valid evidence |
|---|---|---|
| page renders | load/runtime failure | browser load / server response |
| primary CTA works | click does not produce intended result | actual interaction + resulting navigation/state |
| primary task preserves intent | path becomes materially harder to discover, understand or complete because of downstream design | exercised end-to-end task path in the real browser |
| mobile composition works | hierarchy/crop/action fails at mobile | rendered mobile viewport inspection |
| build is valid | repository check fails | declared build/typecheck/lint command actually run |
| visual direction is coherent | rendered relationships contradict the grammar | perceptual review of full page/screenshots |
| accessibility property passes | the relevant criterion fails | actual accessibility tooling/manual evidence appropriate to the claim |
| performance is good | measured behavior misses the claimed standard | measured evidence, not code inspection |

Never claim evidence that was not collected. If no valid oracle is available, report the gap rather than upgrading judgment into proof.

## Deterministic QA

Prefer tools for falsifiable properties.

Run repository-declared checks when available and relevant:

- build;
- typecheck;
- lint;
- tests;
- framework-specific validation.

In the browser inspect for:

- console errors;
- failed network assets relevant to the page;
- broken internal/external destinations on primary actions;
- accidental horizontal scroll;
- clipped or overlapping content;
- missing fonts/images;
- broken sticky/fixed elements;
- invalid interactive states;
- focus visibility and basic keyboard flow;
- obvious accessibility violations through available tooling.

Do not invent ad-hoc destructive commands. Respect repository conventions.

## Viewport QA

At minimum for material pages, inspect a representative desktop viewport and a representative mobile viewport. Add tablet/intermediate widths when layout transitions are complex or when defects appear between the extremes.

Do not test mobile only by narrowing until the page technically fits. Look for intended recomposition:

- hierarchy preserved;
- copy measures and line breaks remain controlled;
- imagery crop still communicates;
- tap targets remain usable;
- navigation remains clear;
- no meaningful interaction relies only on hover;
- dense desktop compositions simplify or resequence appropriately.

## Primary-task integrity

When the page has a primary visitor task or conversion transition, exercise that path end to end in every relevant representative state instead of validating only the CTA or isolated controls. Judge the task-integrity invariant from `control.md`: the visitor should be able to discover what to do, understand the consequence, and complete the intended transition without avoidable effort introduced by direction, navigation, motion, scroll choreography, responsive adaptation, or context loss.

Do not optimize for the shortest conceivable path when the page job genuinely requires explanation, proof, configuration, or deliberate pacing. The failure is **unearned friction**: effort added by the expression that does not materially serve the visitor decision or page job. If the task is prevented or effectively unusable, classify it as `BLOCKER`; if it still works but a downstream creative/interaction choice materially burdens it, classify it as `MATERIAL`.

## Perceptual QA

Review the rendered page as a hostile design critic rather than its author. The checks below are different ways to find material failure, not separate definitions of quality.

### First viewport

Ask:

- What receives attention first?
- Can I identify the product/page job quickly?
- Is the primary action evident?
- Does this feel specific to the product?
- Is there one dominant visual idea?
- Is any element competing with the thesis?

### Full page

Scroll at normal reading speed. Ask:

- Does the page accumulate meaning or restart every section?
- Does visual intensity vary intentionally?
- Are sections mechanically repetitive?
- Is there a weak middle after a strong hero?
- Does imagery remain meaningful?
- Does the CTA architecture stay coherent?
- Does the footer feel like part of the same system?

### Semantic reverse-read

Before consulting the intended rationale, infer from the rendered artifact itself:

- what job the page appears to perform;
- how the major regions seem to build the argument and what conclusion they lead toward;
- which action appears primary and what visitor context it preserves or discards;
- what seems to make the offer specific or credible.

Compare that reconstruction with the page intent and any active invariants from `control.md`. A material mismatch is semantic drift even when each local design decision looks competent. If the maker's rationale is required to explain a material relationship that the page itself does not communicate, treat that as an unresolved Meaning defect rather than a documentation gap.

### Craft sweep

Inspect high-risk details such as headline line breaks, paragraph measures, image crops, icon consistency, optical alignment, control typography/states, section transitions, sticky content, forms/error states, and mobile spacing/wrapping. These examples are not exhaustive.

### Anti-generic / counterfeit-quality test

Ask:

- Could most of this design survive an unrelated product/logo swap?
- Which important decision is merely **signaling** premium, creativity, sophistication or technical authority instead of producing the underlying quality?
- Did surface polish make an unresolved proposition, hierarchy, composition or interaction look finished?
- Which visual decision has weak causal dependence on this brief and is present mainly because it is a familiar category or trend default?
- Did component convenience replace composition, or did repeated geometry replace coherent variation?
- Is novelty or technical complexity adding cognitive/runtime cost without adding meaning, identity, proof or a useful experience job?
- Is imagery doing narrative/evidentiary work rather than acting as decoration?
- Are structural devices encoding information rather than simulating sophistication?
- Did reference research broaden the solution or make it imitate the category?
- Is there one memorable idea or many weak attempts at interest?

When a false proxy appears, repair the **underlying quality** rather than banning the surface form or adding another decorative layer. Keep any form that the brief genuinely earns. If genericity is conceptual, revise the governing decision rather than ornamenting it.

## Concept fidelity

When a visual concept/reference was accepted before implementation:

1. capture the concept/reference and current implementation in the same QA pass;
2. compare composition, typography, scale, crop, palette, spacing, imagery, containers, and motion intent;
3. identify the largest material mismatches;
4. fix them in descending perceptual impact;
5. re-render after each meaningful correction set.

Do not silently reinterpret the accepted design into a generic component system. A reference is not permission to ship screenshot-as-UI; keep real UI, text, controls, and interactions code-native where appropriate.

## Build in visual slices

For material CREATE and major REFINE work, when browser/render tools exist, do not accumulate substantial visual implementation without observing it. Render when a composition, interaction, responsive decision, asset integration, or active invariant becomes materially judgeable; do not wait for an arbitrary section count or the completed page.

1. implement the smallest representative slice that tests the highest material uncertainty or active invariant; this is often the first viewport, but not necessarily;
2. exercise the real state, render it, and capture a screenshot when a still image will improve comparison or inspection;
3. correct the largest semantic, compositional or craft drift while the decision is still cheap to change;
4. implement the next materially judgeable slice and inspect continuity with what already exists;
5. continue until complete;
6. run full-page rhythm and responsive passes.

The default loop is `MAKE → RENDER → OBSERVE → CORRECT → CONTINUE`. Captures are working evidence, not process ceremony; generate the states and views that can change a decision rather than building a screenshot archive for its own sake.

This preserves a coherent direction while reducing late-stage visual debt and exposes semantic drift while the solution is still cheap to change.

## Render loop

The first successful render begins QA. When browser/render tools exist:

1. run the app using repository-declared commands;
2. exercise the relevant page states and let lazy/async/interaction-driven content settle;
3. inspect the first viewport and complete narrative;
4. exercise the primary task end to end, including the intended destination/state and any decision-relevant context that should survive;
5. inspect representative desktop/mobile and any additional warranted viewports;
6. capture screenshots when useful;
7. run deterministic checks available in the environment;
8. use perceptual/multi-lens review to find the largest remaining falsifier;
9. identify the lowest causal layer that explains it;
10. make a targeted correction and render again;
11. repeat until no material falsifier remains or a concrete blocker prevents improvement.

## Refinement strategy

Converge rather than churn.

After each render:

1. identify the single largest remaining defect or mismatch;
2. diagnose its root layer: semantics, hierarchy, composition, system, asset, implementation, responsive behavior, or micro-craft;
3. make the smallest change that addresses the root cause;
4. render again;
5. keep improvements that survive comparison.

Do not regenerate a solved page because of a local defect.

## Accessibility floor

Follow WCAG 2.2 AA where applicable and reasonably testable. In particular, protect:

- keyboard access and visible focus;
- semantic headings/landmarks/controls;
- accessible names for interactive controls;
- text alternatives for informative imagery that preserve the information relevant to its communication or decision role; decorative imagery should not create redundant noise;
- text contrast (generally at least 4.5:1 for normal text and 3:1 for large text, subject to WCAG exceptions);
- reflow/resizing;
- non-color-only communication;
- reduced-motion preferences;
- target size/spacing (WCAG 2.2 AA specifies at least 24×24 CSS px or qualifying spacing/equivalent exceptions).

Do not claim full WCAG conformance from a cursory automated audit.

## Performance integrity

Performance affects perceived design quality.

Avoid obvious sources of preventable degradation:

- enormous unoptimized hero media;
- unnecessary client-side JavaScript;
- layout-shifting media without dimensions;
- gratuitous animation work on the main thread;
- excessive web-font payloads;
- dependencies added for trivial effects.

When actual performance measurement is in scope and tools permit, use current Core Web Vitals as reference targets: LCP ≤ 2.5s, INP ≤ 200ms, CLS ≤ 0.1 at the 75th percentile. Local synthetic measurement is not equivalent to field percentiles; describe evidence accurately.

## Hard-stop defects

Do not sign off while any applicable defect remains:

- runtime/build failure;
- blank/partially broken render;
- primary action broken;
- primary task technically works but downstream design or interaction materially obscures or burdens it without serving the page job;
- missing central image/font;
- clipped primary content;
- accidental wrapping that damages hierarchy;
- unreadable text;
- horizontal mobile overflow;
- unusable mobile navigation or CTA;
- obvious contrast/focus defect;
- placeholder boxes or rough temporary assets in a premium result;
- large concept-to-browser mismatch;
- central section that looks prototype-grade;
- unsupported marketing proof represented as real;
- known materially weaker viewport or page region.

If the environment prevents verification, state exactly what remains unverified.

## Multi-lens review for premium work

Use separate lenses because they expose different classes of failure.

### Lens 1 — first-time visitor

Temporarily ignore implementation intent and inspect only what a new visitor can perceive:

- What is this?
- Who is it for?
- What is the primary promise?
- What makes it credible?
- What action is expected?
- What context is missing because the builder already knows the product?

### Lens 2 — creative director

Inspect concept strength:

- Is the governing idea defensible and brief-specific?
- What makes the page memorable after the browser is closed?
- Which section feels derivative of current web trends or category autocomplete?
- Does the signature express the product or merely demonstrate technique?
- Is any familiar premium/creative signal standing in for a weaker underlying idea?
- Is there enough contrast between quiet/supporting regions and the dominant moment?

### Lens 3 — craft reviewer

Inspect the weakest 10%, not the strongest 10%:

- where does quality drop?
- which line break/crop/alignment/spacing relation feels approximate?
- which state or section edge would receive a design-review comment?
- which mobile decision looks like a fallback rather than a composition?

### Lens 4 — creative developer / technical jury

For ambitious work inspect loading/perceived performance, responsive/device behavior, document structure/semantics, motion/frame behavior, accessibility and graceful degradation.

A technically impressive page that fails one of these materially is not award-caliber.

## Finding severity

Classify findings internally:

- `BLOCKER` — breaks truth, primary function, accessibility/safety, core rendering, or makes the experience materially unusable/misleading;
- `MATERIAL` — clearly prevents premium/agency-signoff quality, including generic composition, counterfeit quality masking an unresolved decision, weak section, broken responsive hierarchy, significant fidelity drift, or visible jank;
- `POLISH` — real improvement whose absence does not undermine the page's concept or professional integrity.

Do not hand off with known BLOCKER or MATERIAL findings that are fixable in the current environment.

## Final pass and stop rule

After the last material change and before handoff, perform a fresh holistic visual inspection of the complete settled artifact in representative desktop and mobile states. Do not rely on screenshots from an earlier revision or inspect only the region that changed. Re-run the relevant perceptual and multi-lens review against the final page, including full-page rhythm and the weakest 10%; if that pass triggers another material correction, inspect the resulting final state again.

Then walk every **applicable** quality dimension from `SKILL.md`. For each, ask what remaining observation could still falsify the claim that it is resolved and whether the valid oracle has been applied to the relevant exercised state. Re-run the semantic reverse-read when active invariants were material to the work. Do not create a second checklist of quality definitions here.

Stop refinement when:

1. all applicable hard gates pass;
2. no BLOCKER/MATERIAL falsifier remains;
3. the weakest important region is still professional and coherent with the whole;
4. another change would be preference-level, conflict with a constraint, or risk destabilizing a stronger solved decision.

This is stronger than “looks good” and more practical than pretending perfection is measurable.
