# Brand book — an information product and a branded touchpoint

Use when guidelines, a brand book or an equivalent handoff is a deliverable. Build it after the identity has survived the declared touchpoints. It is for people who did not participate in the project, so they can understand the brand, find what they need, make correct new work and recognize drift.

The brand book is both **interactive documentation** and **an expression of the brand**. It must teach and retrieve well while carrying the same level of craft as the identity it describes. A beautiful book that is hard to use fails; a usable generic manual that suppresses the brand also fails.

## 1. Readers and jobs decide the experience

Name the actual readers from the owner's operation, not from a template, and the jobs that bring each reader to the book. Typical jobs are to understand the brand, apply a rule, verify a decision, retrieve a value or download an asset.

Design for two modes:
- **reading** — a newcomer can acquire the governing logic without consuming every production detail;
- **lookup** — an experienced operator can reach a known rule, value or asset without rereading the narrative.

Language is the audience's language (`strategy.audience.language`). Repository or host conventions govern code and commits, never a touchpoint.

The default medium is one self-contained HTML document unless the owner requires another medium that can render the system. Screen and print are different layouts of the same information product, not unrelated artifacts; each preserves the reader's job and hierarchy in its medium.

## 2. Plan the experience before scaling it

Before laying out the full book, resolve only the decisions that would become expensive after repetition:
- **information architecture** — how the knowledge is partitioned and ordered around reader jobs;
- **reading hierarchy** — what must be understood first and what can remain in deeper detail;
- **wayfinding** — how a reader knows where they are and reaches another relevant region;
- **retrieval** — how rules, exact values and downloadable assets are found;
- **responsive roles** — how small screen, large screen and print preserve the same informational priorities without becoming one compressed layout;
- **brand embodiment** — how grid, typography, color, image, motion if relevant and interaction behavior come from the brand grammar rather than generic documentation UI;
- **visual material** — which images and applications are strong enough to teach the system at meaningful size.

Do not prescribe a chapter count, component library, grid, breakpoint, target size, reading-level count or page rhythm universally. Those are consequences of the brand, content and reader jobs.

Wayfinding is a required function when the document's complexity needs it; its form still belongs to the brand. Do not ban navigation because generic navigation is off-brand. Build the necessary function from the system's own grammar.

This plan is working material, not canonical brand state.

## 3. Keep three content layers distinct

**Reference** — exact values, inventories, lockup variants, minimum sizes, contrast pairs, downloads. These agree with the contract and assets, but need not be generated from them. Source-of-truth coherence is verified at acceptance; it is not a required production method. A number appears only where reproduction depends on it.

**How-to** — imperative rules that let an operator do the job. Titles predict content; terms are defined at first use or replaced by plain ones. Element names are the ones fixed by the brand system.

**Explanation** — the compact causal chain behind the brand: brand job, position, thesis, principles and behavior. It helps a reader generalize without turning every rule into rationale.

Cover only dimensions the system actually has. Process vocabulary never reaches the published artifact: no schema, route names, evidence ledger, open questions, prompts or internal maturity discussion. Pending matters go to the operator report.

## 4. Prove a representative prototype before fanout

Do not begin by reproducing the full table of contents. First make the smallest real slice capable of exposing the document's hard tensions.

The prototype should contain enough real content to test, where relevant:
- orientation and navigation;
- a dense reference/rule region;
- an expressive brand moment;
- retrieval of an asset or exact value;
- small-screen and large-screen behavior;
- print composition.

A full chapter is often a useful slice, but it is not a universal requirement. The slice is valid only if it can falsify the intended architecture, hierarchy, density, retrieval and media behavior.

Render it, use it as the named readers, repair the structure, then scale the proven grammar. Do not spend craft effort across a full book whose information architecture or layout logic has not survived this prototype.

## 5. The document itself must carry the brand

The book's interface grammar is an application of the brand grammar, not of the browser's defaults. Grid, type scale, margins, color fields, imagery and interaction behavior derive from the system where those dimensions exist.

A familiar web pattern is not forbidden merely because it is familiar; it fails when its form arrives from medium autocomplete instead of a reader need and the brand's governing logic.

Use visual material selectively. A render from TEST IN USE enters the book only when it is strong enough to function as evidence that the system produces good work. Layout follows admitted material; there is no slot per touchpoint waiting to be filled. Fewer strong examples beat complete weak coverage.

Do not sacrifice clarity to expression. Do not sacrifice expression to generic documentation convenience.

## 6. Judge an absolute floor before the weakest element

A uniformly mediocre book may have no conspicuously weak component. Judge the whole product against four orthogonal properties before ranking local elements:

- **Transfer** — a reader who did not participate can orient, find, understand and apply what their job requires. Evidence: perform the relevant reader tasks without the maker explaining the interface.
- **Expression** — the document has the force, rhythm and craft expected from the creative direction and holds beside the named bar. Evidence: judge rendered views without the author's rationale.
- **Integrity** — the book faithfully represents the current system, masters, assets and exact rules. Evidence: inspect against the sources and use deterministic checks only for properties code can actually decide.
- **Delivery** — the artifact works in the media it claims to serve: representative screen extremes, print, keyboard/accessibility behavior when applicable, relative asset paths and offline/self-contained packaging. Evidence: execute and render those media.

Start review at the largest scale: **whole experience → reader task/flow → weak region → component → detail**. Do not polish local components while the architecture itself fails.

Only after the absolute floor holds, apply the package's weakest-element rule and raise or remove the weakest admitted visible element.

## 7. Package and readiness

Use one folder the host already serves statically when possible:
- book at the folder root;
- fonts and assets needed by the book inside the folder, with downloads where the reader job requires them;
- relative references so the package survives offline use and a host change;
- print styles implementing a deliberately composed print layout;
- contract outside the served folder unless the owner explicitly chooses to publish it.

Prefer no client-side script when the experience can be delivered with semantic HTML and CSS; add runtime behavior only when a real reader job earns it. No external request may be required for the book to remain usable offline.

`scripts/book_checks.py <folder>` decides only the existing mechanical package properties: self-containment, resolvable relative references, alt text, orphan files, print stylesheet and contract separation. It establishes nothing about transfer, expression or overall UX.

Before calling the book **ready**, **final** or **publishable**:
1. relevant deterministic checks pass or carry an explicit justified exception;
2. the book has been rendered and inspected in each claimed medium;
3. representative reading and lookup tasks clear Transfer;
4. rendered views clear Expression against the named bar;
5. Integrity has been checked against the actual sources;
6. no known visible element remains below the floor.

"Later" is not a state. A real external blocker names exactly what unavailable reality or capability prevents completion. Owner acceptance can reduce scope or accept a lower maturity, but it cannot convert missing evidence into a final artifact.

## Delivery

Deliver the book and the assets its readers need. Deliver the contract separately as an operating file. Report unresolved truth, authority, capability and lower-maturity gaps to the operator, never inside the book.
