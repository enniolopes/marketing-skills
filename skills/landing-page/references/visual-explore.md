# Visual exploration — externalize the creative hypothesis before code hardens it

Load this reference for HIGH-END/FRONTIER CREATE, major visual REFINE, or any case where visual direction materially determines the result and is still open.

The purpose is not to generate more images. It is to make important creative decisions observable before substantial implementation narrows the search space.

## Core principle

When visual quality materially determines the outcome, externalize the highest-risk creative hypothesis in the medium capable of judging it **before expensive commitment**.

For visually ambitious work, FLUX is a preferred thinking surface when available and appropriate. Browser prototypes, Figma/design canvas, SVG/CSS, typography studies, real UI, photography, diagrams, or other media may be better for some questions.

Quality-first means spending more time or generation quality when that can materially improve the chosen direction or prevent later rework. It does not mean generating without a decision purpose.

## Keep three knowledge layers separate

REAL REFERENCES
→ external repertoire and evidence

SYNTHETIC EXPLORATIONS
→ new combinations, mutations, provocations

DESIGN PROTOTYPES
→ hypotheses for this actual page

Synthetic moodboards do not replace real repertoire. Avoid the closed loop:

model prior → generated moodboard → model studies its own prior → generated design

Prefer:

product truth + real visual culture + non-adjacent references
→ agent synthesis
→ synthetic exploration
→ artifact comparison

FLUX is a creative synthesizer, not the source of repertoire.

## Reference grounding

Use discovery.md's three pools before or alongside synthetic exploration:

- **Pool A — category/adjacent:** grammar, saturation, proof norms, anti-references.
- **Pool B — peer-class craft:** composition, typography, imagery integration, motion, responsive transformation.
- **Pool C — non-adjacent culture/material:** editorial, architecture, cinema, photography, fashion, industrial design, cartography, science, materials, print, historical/domain objects.

For each reference, know what property is transferable and what must not be copied.

## Exploration levels

### 1. Visual-world studies

Explore the product's material/cultural world before defaulting to "landing page" imagery.

Possible material:
- tools, instruments, interfaces, diagrams;
- physical environments and manufacturing/process cues;
- editorial forms and notation;
- photography, light, crop, surface, texture;
- typography character and density;
- data/technical visualization;
- packaging, signage, objects, archives;
- product/domain language and symbols.

Output: a specific visual world with causal dependence on the subject.

Do not require these studies when supplied brand/product materials already establish the world strongly.

### 2. Direction frames

Externalize materially different governing ideas as first-viewport or representative compositions.

A useful default for open HIGH-END CREATE is three direction frames, but three is not a quota. Two genuinely different hypotheses can be enough; five near-identical restylings are not divergence.

Direction difference should primarily change one or more of:
- governing idea;
- composition logic;
- information-to-image relationship;
- spatial hierarchy;
- dominant medium;
- narrative device;
- signature mechanism.

Changing palette, radius, font family, or hero image while preserving the same idea is variation, not divergence.

Compare the artifacts before reading the rationale.

### 3. Critical-section studies

Use these when the selected direction is strong but a material region remains unresolved: hero, proof, product explanation, key transition, conversion block, interaction, or imagery relationship.

Good premise + weak realization → REFINE.

Weak/unproven premise → VARY or RE-DIVERGE.

Do not polish a weak local premise merely because implementation already exists.

### 4. Whole-page composition studies

Use when macro rhythm, density, signature placement, visual accumulation, or section-to-section massing remains materially uncertain.

For FRONTIER work this evidence is expected. For HIGH-END work use it when the page is substantial enough that first-viewport studies cannot reveal the main compositional risk.

A generated full-page comp is a **compositional hypothesis**, never an implementation specification. Its detailed text, UI, spacing, and controls may be fictional.

## Mutation semantics

**DIVERGENCE**

Change the governing idea or visual/compositional logic.

**VARIATION**

Change expression while preserving the governing idea.

**REFINEMENT**

Repair a diagnosed weakness in a selected expression.

Do not call same-direction generator variations "new concepts."

## Art-direction packet

Before an important generation, define only what governs the result:

- page job and visitor context;
- governing hypothesis;
- truthful product/domain cues;
- dominant composition and focal hierarchy;
- intended quiet space for copy/UI;
- framing/crop/camera;
- lighting/materiality/realism;
- palette relationship;
- emotional register;
- viewport/aspect/crop needs;
- reference role for each input;
- signature;
- mutation axis;
- negative constraints preventing genericity, false proof, accidental logos/text, or category autocomplete.

Prompt syntax is provider detail. The art direction is the durable decision.

## Multi-reference discipline

Give each reference a role.

Typical roles:
- TRUTH ANCHOR — actual product/object/interface characteristics;
- COMPOSITION — mass, scale, negative space, tension;
- MATERIAL/LIGHT — surface, photographic behavior;
- TYPOGRAPHIC CHARACTER — density, scale relation, editorial rhythm;
- NON-ADJACENT CULTURE — one transferable principle.

Extract principles. Do not ask the generator to copy identity or exact layout.

When a reference could imply real product UI, proof, metrics, certifications, customers, or logos, explicitly forbid invention.

## Provocations

A provocation deliberately pushes a dimension far enough to reveal possibilities. It need not be directly implementable.

Examples of mutation prompts:
- make the concept radically quiet;
- remove category-web language and represent the product's operational logic;
- treat the subject like a scientific publication;
- treat the product like a precision physical object;
- push editorial scale relationships to an extreme;
- translate the product into a cinematic sequence;
- translate the domain into an industrial instrument or archival system.

Extract the useful property from a successful provocation. Do not implement the picture literally.

Provocations may relax feasibility. They may not relax truth.

## Selection rule

Do not choose the most spectacular image. Choose the direction that creates the strongest combined result across:

brief fit × product specificity × communication power × visual idea × hierarchy × asset truth × distinction × implementation potential

Ask:
- what is the governing idea visible in the artifact?
- what would remain memorable after closing it?
- which major decision could be transplanted to an unrelated brand?
- does the image/type/space relationship carry meaning?
- does the direction create useful tension, silence, rhythm, scale, density, or materiality?
- what observable result would falsify it?

If none of the explored directions is strong enough, re-diverge. Do not select a weak winner merely because a batch was generated.

## Stopping rule

Continue visual exploration while a material creative uncertainty remains and another artifact has a plausible chance to change the commitment.

Stop when:
- the governing idea is specific and defensible;
- the strongest alternative has been meaningfully tested;
- the defining visual relationship is observable, not merely described;
- remaining uncertainty is better resolved in the real browser;
- additional generations are only producing same-direction style noise.

Quality-first is not quantity-first.

## Mockup → implementation firewall

Never pixel-copy a generated study.

GENERATED ARTIFACT
→ EXTRACT TRANSFERABLE PRINCIPLES
→ RECONSTRUCT NATIVELY FOR WEB
→ RENDER IN REAL BROWSER
→ CHECK CONCEPT RETENTION

Extract only:
- governing idea;
- dominant hierarchy;
- composition principle;
- scale relationships;
- typographic relationships;
- image/crop behavior;
- color/material logic;
- rhythm/density;
- signature;
- motion implication.

Do not transfer:
- generated testimonials, metrics, logos, awards, integrations;
- fake product screenshots or labels;
- invented interface states;
- generated factual copy;
- impossible spatial relationships that fail responsive semantics.

Reconstruct with real HTML/CSS/JS, real copy, real product assets, and responsive behavior.

## Concept-retention check

After browser reconstruction, compare the implementation to the selected exploration for **principle fidelity**, not pixel fidelity.

Ask:
- which property made the visual study exceptional?
- did componentization normalize its scale, tension, crop, silence, asymmetry, density, depth, or image/type relationship?
- did responsive adaptation preserve the thesis or merely shrink it?
- did real content expose a flaw in the concept?

If a defining property was lost, fix expression/execution. If the concept fails under real content/browser constraints, re-diverge.

The browser remains sovereign.

## Anti-ritual

Do not:
- generate moodboards because HIGH-END is selected when supplied evidence already resolves the visual world;
- create full-page comps for a tiny page whose real-browser prototype is the better oracle;
- count color/font variants as conceptual divergence;
- keep generating after the decision has stopped changing;
- favor a weaker direction because it is easier for the current generator;
- treat provider identity as quality proof;
- turn the exploration archive into permanent repository clutter by default.

The output of this reference is a stronger creative commitment, not a pile of images.
