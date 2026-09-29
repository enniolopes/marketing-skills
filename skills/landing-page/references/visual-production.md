# Visual production — make the page imagery exceptional and real

Load this reference when a CREATE or material REFINE depends on generated or edited raster imagery: hero/key art, bespoke photography, illustration, complex compositing, image-led storytelling, background scenes, or another central visual asset.

The objective is not to fill image slots. It is to produce **relevant, product-specific, high-craft imagery that materially improves the page's communication and visual distinction in the real browser**.

This reference owns **production assets that will appear in the delivered page**. Disposable moodboards, direction frames, provocations, and pre-code composition studies belong to `visual-explore.md`. A study becomes production only when the chosen direction requires that image itself as a real asset.

## Invariants

1. **Relevance before spectacle.** A stunning image that could serve an unrelated product fails.
2. **Art direction before generation.** The page's intent and governing direction determine the image; generator aesthetics do not determine the page.
3. **Quality contract before provider.** Prefer the strongest appropriate official FLUX path described by `environment.md`, but provider identity never substitutes for artifact quality.
4. **Quality is invariant.** Missing capability never justifies a generic placeholder, weaker concept, or inferior medium merely to finish.
5. **Generated is not finished.** A material image is complete only after production, inspection, refinement, persistence, integration, browser rendering and contextual QA.

## 1. Decide whether generated imagery is actually the right medium

Choose imagery only when it has a communication job. A central image should materially do one or more of these:
- demonstrate or clarify the product/domain;
- establish the material/emotional world;
- embody a brief-specific metaphor or transformation;
- create the page's dominant signature;
- communicate subject matter faster or more powerfully than prose;
- support a narrative transition that other media cannot perform as well.

Prefer real product UI, supplied assets, diagrams, code-native graphics, SVG, CSS, canvas/WebGL or typography when those are truer and stronger.

Do not generate fake product screenshots, customer evidence, partner logos, awards, certifications, integrations, metrics or other proof as if they were real. Generated imagery may be expressive or conceptual; it may not fabricate product truth.

Visible page copy stays code-native unless text intrinsically belongs inside the artwork.

## 2. Preflight the production path before committing an image-dependent direction

When a committed direction materially depends on generated imagery, identify the required capability before treating the direction as production-ready.

Use `environment.md` for the current provider/host profile. The durable rule is:

1. define what the asset requires — generation/editing, reference control, typography/detail precision, resolution, compositing, or other constraints;
2. prefer the strongest appropriate official FLUX capability available;
3. if FLUX requires a legitimate user connection/configuration action, request that action without asking for secrets in chat;
4. use another backend only when FLUX cannot be used in the current environment and the alternative can independently meet the same art-direction and craft bar;
5. if no available path can preserve the selected direction, keep the direction and report visual production as blocked rather than redesigning downward for convenience.

Do not create repository-wide provider wrappers or credential files merely to reach an image service.

## 3. Direct the image from the page job

Before material generation, establish the smallest art-direction packet that can govern the image. Depending on the asset, include:
- visitor communication job;
- connection to the page's governing idea/signature;
- subject and truthful product/domain cues;
- composition, dominant mass and focal hierarchy;
- intended empty/quiet regions for adjacent typography or UI;
- framing, crop, perspective or camera behavior;
- lighting, atmosphere and material/texture behavior;
- realism/stylization level;
- palette relationship to the page/brand;
- emotional register;
- intended viewport/aspect ratio and likely responsive crops;
- useful references and the role each reference should influence;
- negative constraints that prevent genericity, false product implication or visual drift.

Translate those decisions into the production request required by the available FLUX surface. Prompt syntax is implementation detail; the communication and art direction are the durable decisions.

## 4. Produce and vary within the committed direction

If the governing visual idea is still uncertain, return to `visual-explore.md` and re-diverge there. Production should not disguise conceptual uncertainty as same-direction image variations.

For a hero, key visual, or new imagery grammar inside a committed direction, do not accept the first plausible generation merely because it is polished. Produce enough candidates/variations to judge the asset and repair material defects. Judge the actual artifacts against:
- truth and communication job;
- product/brand specificity;
- compositional strength and hierarchy;
- emotional fit;
- distinction without arbitrary novelty;
- craft/detail integrity;
- relationship to nearby typography, UI and motion;
- crop potential across required viewports;
- whether the image strengthens the page's signature instead of competing with it.

Select the strongest candidate yourself. Spectacle without causal relevance is a failure.

## 5. Refine through generation and editing

Use generation, editing, variation, compositing and reference-driven continuation as iterative production operations.

Repair the largest defect rather than restarting indiscriminately. Typical defects include:
- focal point conflicts with headline/CTA;
- generic stock-like subject treatment;
- incorrect product/domain cues;
- anatomy/object/detail failures;
- accidental text or logos;
- weak negative space;
- color or light that fights the page system;
- crop failure at target aspect ratios;
- excess texture/noise behind important content;
- image style drifting from adjacent sections or brand assets.

A successful API/MCP response proves only that an image was generated. It does not prove the image belongs on the page.

## 6. Persist before integration

Once an image is accepted for continued use, make it a real project/workspace asset when the environment permits. Do not depend on temporary generation URLs.

Preserve only provenance that future work materially needs: approved reference assets, art direction, and model/capability choice when continuation or reproducibility depends on them. Do not build a permanent prompt archive by default.

After art approval, prepare web delivery deliberately: appropriate dimensions, format, compression and responsive variants where useful. Do not optimize so early that compression hides unresolved visual defects.

## 7. Integrate into the actual page

Place the real asset in the implementation before judging completion. Evaluate it with the surrounding composition, not on a generator canvas.

Check:
- hierarchy with headline, proof and CTA;
- intended negative space and text contrast;
- crop/focal behavior at desktop, tablet and mobile sizes that matter;
- responsive art direction rather than blind center-cropping;
- whether important subject matter remains legible;
- image sharpness and loading behavior;
- layout stability and performance impact;
- interaction/motion relationship when relevant;
- whether the image makes the page more specific or merely more decorated.

If the image works in isolation but weakens the browser composition, edit/regenerate/recompose and render again.

## 8. Keep image systems coherent

When several generated images appear on the same page, keep family resemblance without forcing identical framing.

Use approved references and art-direction rules to stabilize relevant properties such as:
- light/materiality;
- realism/stylization;
- palette interaction;
- camera/framing logic;
- texture/detail density;
- recurring product/domain cues.

A page containing several individually impressive but stylistically unrelated images is a collage, not a resolved system.

## 9. Completion gate

Do not declare a premium CREATE/REFINE complete when imagery material to the committed direction is only described, prompted, placeholder-quality, unpersisted, not integrated, or not inspected in the browser.

A missing image-generation capability is a real blocker when no equal-or-stronger producible alternative exists. Report that blocker precisely. A production brief can be handed off, but it is not the missing final asset.
