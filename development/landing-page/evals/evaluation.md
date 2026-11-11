# Landing Page — evaluation

Evaluate the skill as an **agent system**, not as a prompt that happens to produce plausible prose.

Keep the suite small and causal: one case per distinct recurring failure mechanism, plus a diverse creative set that can expose aesthetic regression, house-style convergence, and first-idea lock-in.

The v3.10 behavior remains the baseline for the historical v4 milestone below. Its evidence and status are not inferred or retroactively approved by the later LP-EXPRESSION-01 protocol.

## Evidence levels

- **L0 — structural:** metadata, syntax, references, deterministic repository contracts.
- **L2 — proxy:** same-model or simulated judgment; useful for obvious regressions, not proof of improvement.
- **L3 — blind A/B:** isolated baseline/candidate runs on identical inputs/capabilities with version identity and rationale hidden during initial artifact review.
- **L4 — real work:** repeated production use with real browser/render evidence and genuine constraints.

Do not claim behavioral or aesthetic superiority from L0–L2.

## Four evaluation surfaces

### 1. Activation

Did the skill engage when it should, including:
- explicit landing-page creation;
- implicit landing-page/homepage creation;
- contextual requests where the page is the actual deliverable;
- negative controls where the task is adjacent but not a landing-page job?

Avoid both under-triggering and turning the skill into a universal web-design policy.

### 2. Trajectory

Inspect the decision/tool trace where available.

Judge whether the agent:
- recovered minimum safe truth/intent context before material invention, without requiring a completed direction, research or copy before early exploration;
- loaded references just in time rather than all at once;
- stopped research when more evidence stopped changing decisions;
- externalized material visual uncertainty before substantial HIGH-END/FRONTIER implementation;
- distinguished DIVERGENCE from same-direction VARIATION/REFINEMENT;
- used quality-critical visual capability without optimizing prematurely for cost/latency;
- observed browser slices before full completion;
- exercised states before treating them as evidence;
- diagnosed the lowest causal layer before changing work;
- re-diverged only when direction was actually falsified;
- retained responsibility for reversible professional design choices while allowing optional visual calibration without mandatory user selection or an invented approval gate;
- avoided repeated tool/generation calls that produced no new decision value.

Efficiency is diagnostic, not the objective. A deliberately expensive visual study is valid when it materially protects the quality ceiling or avoids likely late rework.

### 3. Artifact

Judge the actual rendered result before the maker's rationale.

Use representative desktop/mobile and relevant interaction states.

Evaluate:
- truth and self-evident page logic;
- brief/product specificity;
- art-direction strength;
- composition and hierarchy;
- typography and imagery as meaning;
- distinction without arbitrary novelty;
- full-page rhythm and weakest-region quality;
- responsive craft;
- concept retention from selected visual exploration;
- primary-task integrity;
- technical/browser reality.

For high-end work, separate:
- **falsification:** what is materially wrong;
- **creative ceiling:** whether the artifact is merely competent or genuinely exceptional.

Zero defects is not sufficient evidence of exceptional design.

### 4. Outcome

Use real task/behavior evidence only when it exists.

A working CTA/destination can be verified directly.
Conversion lift, engagement lift, or business impact requires appropriate real behavioral/experimental evidence.

Do not infer causal outcome from visual quality.

## Run protocol

For a targeted runtime change, run only cases capable of distinguishing it.

For a material architecture/creative change:
1. run relevant regressions;
2. run activation cases;
3. run the creative set;
4. repeat enough trials to observe consistency rather than a lucky run;
5. compare v3.10 and v4 under the same prompt, evidence, tools, model class, reasoning budget, and capability envelope.

Baseline and candidate runs must be isolated. Neither may see the other's artifacts or rationale.

Review artifacts before rationales.

When comparing two outputs, prefer blinded pairwise judgment over independent scalar scoring:
- A better;
- B better;
- tie;
with visible evidence for the decision.

Randomize A/B identity when possible. Do not reward complexity, model/tool spend, or technical spectacle by itself.

Keep a small stable smoke set for regressions, but rotate or hold out part of the creative set so the runtime is not optimized against every known brief. A candidate that only improves on rehearsed prompts has not demonstrated generalization.

Maintain a small **human-reviewed gold set** for high-ambition visual comparisons. Use expert human pairwise judgments to calibrate model-based reviewers periodically; model judges may scale review, but they are not the sole author or certifier of the aesthetic bar. When calibrated model judgment and expert review materially disagree, inspect the artifacts and evidence rather than averaging the disagreement away.

## Creative generalization

Use causally different briefs. Repeated aesthetic solutions are a failure only when they are not earned by the briefs.

Watch two distinct regressions:

**HOUSE-STYLE COLLISION** — unrelated briefs converge on the same recognizable visual system.

**MEDIOCRITY CONVERGENCE** — outputs differ cosmetically but all settle at the same merely competent ceiling.

A strong v4 should escape the first plausible high-probability solution more often without becoming arbitrary.

## Historical v4 promotion gate

Promote only when all are true:

- intended v4 behavior is observable in traces/artifacts;
- no severe truth, authority, task-integrity, or browser-reality regression appears;
- blind repeated artifact comparison is at least non-inferior to v3.10 overall;
- no systematic loss appears in art direction, composition, distinction, typography/imagery, responsive craft, or the weakest important region;
- HIGH-END creative cases show evidence of a higher ceiling in at least some causally different briefs, not merely a cleaner process;
- no new recurring house style appears;
- the lower-quality tail does not materially worsen;
- expensive research/generation is removed when it adds no decision value, but is not penalized when it purchases observable quality.

If v4 is faster, smaller, more obedient, or more reliable but visually less extraordinary than v3.10, it fails this milestone.

If baseline and candidate behave materially the same, do not add runtime context.

If an eval rewards exact wording, a fixed layout, a specific provider, or one historical implementation rather than the underlying mechanism, fix the eval instead of the skill.


## LP-EXPRESSION-01 — primary material, expression, and synthesis

This change compares an immutable 4.0.0 package with a candidate 4.1.0 package. It does not replace or certify the historical v3.10→v4 result. Keep the substantive quality gates above: truth/authority/task integrity, repeated artifact comparison, creative ceiling, no systematic aesthetic loss, no unjustified recurring house style, weakest-region quality, and appropriate human calibration.

### Mechanical integrity

From the repository root run:

```bash
python -m unittest discover -s development/landing-page/tests -v
python development/validate.py
```

The new unittest module validates the actual schema-v2 eval JSON and rejects malformed/duplicate/missing data in memory. The repository validator discovers this suite; green checks establish mechanical integrity, not creativity or behavioral improvement. Inspect changed local reference paths separately; the validator's reference check reads direct paths in SKILL.md, not every reference file.

### Directed cases and source material

Use `primary-material-changes-direction`, `sparse-material-without-fabricated-identity`, and `representation-preserves-domain-relations`. Reuse existing relevant regressions rather than adding one case per instruction. The primary-material fixture is in `fixtures/primary-material/`: one shared brief and two originally authored SVG artworks. Both are fictional primary material, freely reusable for evaluation; they are not reproductions or real-client proof. Assign exactly one variant to a builder; run both variants under both packages. Do not put development paths in runtime instructions.

Freeze case rubrics before generation. Baseline sensitivity to supplied material, sparse-brief autonomy and preserved domain relations must be observed rather than inferred from matching skill vocabulary. If the baseline already satisfies the proposed change and no material weakness justifies additional runtime, record NO_RUNTIME_CHANGE in this scope. Insufficient evidence is NOT_VERIFIED, not no effect.

### Runs and exposure

- Use separate builder contexts, assigned source snapshots, identical task/asset packets, stack, capabilities and configured resource envelope. Record unexposed model parameters as unknown. No treatment instructions added only to the candidate task prompt.
- E01: two material variants × two repetitions per package. Four baseline studies and four per candidate, at most 12 with two candidate versions. E02/E03: two repetitions each per package, at most 12 probes. Record the affected regression subset separately.
- Development corpus: C01 technical product with primary UI/documents; C02 authorial work with supplied assets. Two repetitions per package per brief. At most two candidate versions (A1 and one correction A2).
- Reserve C03 (sparse new offer) and C04 (governed familiar brand) with a separate curator. Exact inputs/rubrics remain unavailable to candidate adjustment; freeze final package before opening them. Two repetitions for baseline and final candidate only. Main corpus: 16 pages with one candidate, at most 20 with two.
- Once reserved outputs inform a runtime revision, those inputs are spent for independent confirmation of that revision. They may become regressions. Reopening confirmation requires a new recorded campaign with fresh inputs, not retries until success.
- A run can be replaced once only for a diagnosed non-quality operational failure, preserving the aborted record, package and inputs. Refining a page during its run is allowed; replacing a delivered/reviewed artifact under the same run ID is not.
- Record run/package/input hashes, condition, repetition, capabilities, restrictions, outputs, checks, interruptions and actual consumption. Keep generated outputs outside source control. This is procedural context separation, not a claim of filesystem isolation.

### Artifact judgment and decision

Present opaque labels in randomized order; hide condition and maker rationale for the first reading. Review desktop, mobile, full-page rhythm and exercised task states. Separate factual/task integrity, aesthetics/expression/craft, and cross-brief recurrence. Review visual/sensory strength before reading copy in context. More correct facts or explanatory volume cannot compensate for lost elegance, expressive creativity or synthesis. Beauty, atmosphere and nonverbal meaning are legitimate; no literalism, word quota or universal minimalism.

For each repetition pair use W (candidate materially better with no material loss), T (no material difference in inspected criteria), L (material regression), or ? (insufficient/disputed evidence). Perceptible but sub-material polish is T. Identify gain dimensions. An informative W alone is not an aesthetic gain. No score may offset a truth/task failure or an aesthetic regression.

Inspect copy for repeated visual explanations, maker rationale published as marketing, and sections without a distinct purpose. Added text must resolve a material visitor uncertainty with appropriate visual quality; no shrinking fonts, hiding essential terms or removing accessible alternatives to look concise. Word counts are diagnostic only.

Advance from C01/C02 only if at least one brief has aesthetic/expressive W/W and no pair is L or ?. G4 eligibility requires directed cases passing, aesthetic/expressive W/W in at least two causally different briefs, all remaining pairs W/T, no material loss or unjustified house-style recurrence, valid reserved exposure and the existing human calibration requirement. An AI-only judgment can identify a positive proxy signal, not certify aesthetic superiority or human effects.

Conclusions use one candidate hash and its accumulated corpus, never only the last stage or the best runs across versions. All required cells of reached stages must be evaluable. All accumulated pairs T with no material directed gain permits scoped NO_RUNTIME_CHANGE. Mixed W/L, weak W/T, missing cells, invalid reservation or disagreement remains NOT_VERIFIED if it fails the frozen gates. Unopened conditional stages are not missing cells. C01/C02 aesthetic W/W followed by reserve T/T can satisfy the creative criterion; missing calibration still prevents PROMOTABLE. Do not change these criteria after exposure.

Before each campaign, record concrete inputs, required facts/tasks, resource envelope, sampling, bounded attempts and interpretation limits outside runtime. New fixtures or rubric changes after seeing results are development changes, not independent confirmation. Do not infer attention, memory, trust, admiration, AI recognition or conversion from this artifact evaluation.

## LP-EARLY-VISUAL-01 — early generation and visual calibration

Compare an immutable 4.1.0 package with a 4.2.0 candidate. This is a user-requested workflow preference; it does not certify or replace the historical v4 or LP-EXPRESSION-01 gates, nor presume aesthetic superiority. Keep truth, task, native implementation, creative ceiling, synthesis, weakest-region and appropriate human-calibration requirements.

The changed `visual-direction-cannot-stay-prose-only` oracle observes actual generated page/section studies before the first coded visual prototype on open direction with a usable generator. `real-repertoire-before-synthetic-loop` now permits first ideation before completed reference research, retaining the prohibition on synthetic self-validation. These are explicit normative changes, not post-result relaxations. Reuse capability/fallback, quality-first, mockup-firewall, local-repair, task and concept-retention cases. Add only the distinct `visual-feedback-without-approval-gate` mechanism.

Portable packets are in `fixtures/early-visual/cultural/` and `technical/`. They are original fictional primary material, reusable for evaluation, not real-client proof. Inspect the actual supplied assets. Freeze prompts, inputs, rubrics, interaction branches and the common resource envelope before running; do not add image-first instructions only to the candidate prompt.

Use two briefs × two configured repetitions × baseline/candidate: eight short complete pages, at most twelve if one corrective candidate A2 is justified. Separate contexts and assigned package snapshots; record unexposed model parameters as unknown. Retain output/package/input hashes, actual tool outcomes and relevant ordered actions without requesting chain-of-thought. Context separation is procedural, not filesystem isolation. A first baseline probe must precede runtime editing; preserve passes and failures rather than manufacturing a red check. Do not impose a runtime image quota or treat call count/provider identity as creativity.

Repetition1 includes an explicit initial review checkpoint. After real curation, inject the same labeled simulated reply in both conditions: “Explore mais uma alternativa com mais respiro e menos densidade de texto, preservando o que a oferta faz e a ação principal. Recomende um caminho; não preciso escolher uma imagem inteira.” Repetition2 has optional participation, no approval pause and no injected reply; observe recommendation/continuation without fabricated user input. If actual no-reply behavior cannot be represented, mark it NOT_VERIFIED and distinguish an explicit-autonomy control. This is not human calibration or measured preference.

Run at most eight scenario controls/package for repair, resolved/governed direction, absent generator, adequate alternative, inadequate production alternative, explicit approval pause, invented mockup facts and task context. Capability fixtures are labeled simulations, not proof of real provider access. Preserve the originals on operational failures; at most one diagnosed non-quality replacement/cell. No design-quality retries, best-run selection or extra sampling to find a win.

Judge actual generated studies and final browser desktop/mobile/task states before maker rationale, hiding conditions on the first reading. Conformance requires real inspectable generation and timing, useful comparison, accessible curation, professional synthesis and faithful feedback/absence handling; promises, prompt lists and screenshots alone do not prove the whole workflow. A successful call alone does not prove a useful study.

Classify material gains, ties, regressions or uncertainty per existing W/T/L/? semantics. Every required candidate trajectory/control must be accounted for; missing evidence is NOT_VERIFIED. No material aesthetic, truth, task or craft loss may be offset by more process, facts or explanation. Copy count is diagnostic, not a quality score; retain essential terms and accessible alternatives. Preserve the approved visual principles through real content and native implementation.

Report conformance separately from aesthetic preservation and superiority. A requested sequence can be observed without proving that it raises creativity. Four evaluable pairs with no L or material ? support only scoped AI-observed preservation; uncalibrated AI review does not justify PROMOTABLE or human/causal claims. Mixed results or missing required cells remain NOT_VERIFIED; correct within the frozen budget or withdraw the causal delta. If both versions already comply and added wording changes nothing useful, remove redundant instructions rather than adding context for its own sake.
