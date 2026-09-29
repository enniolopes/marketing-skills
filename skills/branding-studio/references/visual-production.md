# Visual production — make the brand imagery real

Load this reference when generated or edited raster imagery is material to exploration or to the deliverable: photography, illustration, key art, compositing, campaign imagery, image-led mockups, or a branded image system.

Generated imagery has two roles. **Exploration**: boards that make lineages comparable, contextual scenes onto which vector work is composited so a declared touchpoint (packaging, apron, storefront, signage) can be seen where it lives, and reference boards that show an imagery behavior (light, distance, framing, subject) before it is written down as an instruction. **Production**: the brand's own image assets. Use the exploration role whenever a capable backend exists, whether or not final assets will be generated.

## Invariants

1. **Relevance before spectacle.** A technically impressive image that could belong to an unrelated brand fails.
2. **Art direction before generation.** Generation executes a visual thesis; it does not substitute for one. A prompt is implementation detail; the art direction is the durable decision.
3. **FLUX first.** Prefer the official Black Forest Labs FLUX capability when the imagery matters to the quality of the result.
4. **Quality is invariant.** Missing capability never authorizes an inferior medium, a placeholder or a weakened direction merely to finish.
5. **Generated is not finished.** An asset is complete only after inspection, refinement, persistence as a real file, integration into the actual application and re-inspection there.

## 1. Choose the medium by the artifact

Controlled vector or code-native production for final logo masters, precise icons and symbols, deterministic patterns, UI, diagrams, editable text, layout and book composition. Generative raster when it materially improves the direction: exploration boards and contextual scenes, bespoke photography or photographic worlds, illustration systems, key visuals, materials and textures, editing and reference-driven variation. Do not generate an asset merely because a generator is available.

The photographic register is the highest-risk class a reader will see: it is read first, it is judged by an eye that is expert without training, and it is the register the agent controls least. Choose it for a delivered image only where it can be brought to the floor on that surface; otherwise choose a register the agent controls (vector, code-native, an illustration system of the brand's own) or one excellent scene in place of several average ones. Decide this in BUILD SYSTEM, before any render exists, not after a weak render is already in hand.

## 2. Preflight the production path

Once a direction materially depends on generated imagery, verify a production path before treating it as production-ready, in this order:

1. an official FLUX capability already usable through the host;
2. the official remote FLUX MCP (`https://mcp.bfl.ai`) when the host supports remote MCP, then already-configured official BFL API/tooling when the environment can execute it safely. `BFL_API_KEY` is a secret: never print it, persist it in runtime files or ask the user to paste it into chat;
3. if FLUX is supported but needs a user connection/configuration action, ask for that action before changing backend;
4. treat FLUX as unavailable only when no supported path exists, setup cannot be completed in the session, or a reasonable attempt fails;
5. only then another available generator, and only if it independently meets the same quality bar;
6. if no path preserves the direction at the required quality, keep the direction and mark the deliverable **blocked**.

Respect an explicit user requirement for another backend with the same gates. Do not create repo-global clients, adapters or credentials merely to reach FLUX.

## 3. From art direction to request

Before generation, establish only the constraints that govern the image: brand job and intended meaning, subject and exclusions, composition and focal hierarchy, framing and camera behavior, light and atmosphere, material behavior, realism versus abstraction, palette relationship to the identity, brand-specific cues, relationship to typography and devices, intended application and crop, and the role of each reference.

Compile that packet for the actual operation, not for a generic prompt: generation from text needs subject, context, composition, appearance and application constraints; an edit needs what changes, what stays invariant and how the change integrates; reference-driven generation needs each reference mapped to the property it contributes; video needs the event, the material motion and continuity. Use current provider-native guidance for syntax and controls; do not freeze remembered model dialect into brand logic. Do not use quality incantations (`premium`, `cinematic`, `award-winning`) as substitutes for unresolved direction, and do not invent negative prompts, camera parameters or control structures the active mode does not support. If writing the request requires a new creative decision, resolve it in the direction or system, not in the prompt.

## 4. Diverge, select, repair

For a central image or a new image grammar, do not accept the first plausible generation. Produce a small set of materially different candidates, varying the visual solution rather than seed-level cosmetics, and select the strongest yourself against the quality target and the named bar. A beautiful but generic image loses to a specific, causally earned one.

When a candidate is close, repair the smallest causal input (one reference, one control, one instruction) while preserving what succeeded, instead of rewriting the whole request. Look for the generator's typical defects before judging the idea: wrong crop or focal hierarchy, generic subject treatment, inconsistent light or material, anatomy and detail failures, accidental text or pseudo-marks, palette drift. If repeated local repairs reveal that the art direction is under-resolved, return the issue upstream. A technically successful request is not a quality pass.

## 5. Build an imagery system, not a gallery

When the brand needs multiple images, stabilize family resemblance deliberately through approved key assets and references: subject treatment, framing, light and materiality, palette interaction, stylization level, recurring cues. Generate enough range to test whether the grammar survives different subjects and touchpoints. Individually strong images that read as unrelated campaigns are an unresolved system; identical compositions are not coherence.

## 6. Contextual scenes

A contextual scene exists to expose scale, material, distance and light, not to hide weak decisions or to prove the identity by polish. Three rules govern it:

1. **The scene is this brand's world.** Place, objects, people, hour and light come from the brand's reality and its imagery behavior, never from the category's stock scene. A scene that would serve a competitor equally well has failed before the mark enters it.
2. **The mark enters by faithful reproduction or by recomposition of the master, and every render is checked against the master at magnification.** A generator given the mark reproduces it faithfully on a simple surface and silently redraws it on a hard one (curved, textured, oblique, small), and color alone does not separate the two cases; so the check is per render, on the drawn form, never a batch pass. When the drawn form deviates, keep the scene and recompose the master over it; do not discard a strong scene for a weaker composite and do not accept the redrawn mark.
3. **A recomposed element belongs to the scene.** It takes the scene's perspective, its light where the surface is uniform, and the material's response (ink on paper, print on fabric, enamel on metal); an element that sits on top of the photograph instead of inside it is a defect of craft, not of compliance.
4. **Deterministic content keeps authority.** Generative editing may improve the surrounding scene, material transition, edge behavior, grain, light or shadow, but it does not silently gain authority to redraw exact brand geometry, readable copy, UI, pages or dense documents. Keep the exact master/application as the source for that content and inspect the assembled result after any generative refinement. If refinement corrupts deterministic content, restore/recompose it or keep the controlled composite rather than accepting a more photoreal but false render.

Generated raster may inform logo exploration; what a final master requires is owned by `visual-artifact-production.md`.

## 7. Persist, integrate, look again

An accepted asset becomes a real file in the project; a temporary service URL is not a deliverable. Preserve only the provenance future production needs (approved source and reference assets, the art direction, the model choice when continuation depends on it), never a prompt archive.

Judge the image again inside the actual application: hierarchy with type and identity elements, crop at real sizes, palette and material relationships, whether it carries the meaning without narration, whether the application stays specific when the logo is secondary, and whether the set preserves family resemblance with range. An excellent isolated image in a weak application is not finished for that use.

## Completion

The completion gate is owned by `visual-artifact-production.md`; an image counts toward it only once persisted, integrated and re-inspected in the application. When capability is unavailable, report the precise blocker, preserve the strongest direction, and label any production brief as a brief, not as the missing asset.
