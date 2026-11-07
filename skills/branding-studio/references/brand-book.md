# Brand book — a working document for the people who execute

Use when guidelines, a brand book or an equivalent handoff is a deliverable. Build it after the identity has survived the declared touchpoints.

The brand book is a working document, written by the organization for the people who execute, that compiles the brand system as built and tested, so that a person who did not take part in the project makes correct work without asking anyone. It is worth exactly what its worst element is worth.

It is not a sales piece, not a presentation and not a landing page; it is still an application of the brand, seen by whoever executes and by whoever decides. The brand appears in it through the system applied to the document and through the pieces shown, never through the prose.

## 1. Before the book starts

Do not start the book until all of these exist:

1. the system has survived the declared touchpoints and the admitted renders are listed in the operator report;
2. the direction criteria, as sharpened in COMMIT DIRECTION;
3. `book.readers` in the contract (`spec-schema.md`): two to five readers, each with a role, a language and two to six tasks written as verb + object + situation ("send the logo to the printer", "write the late-invoice notice"). The owner is always a reader. When no tasks exist, propose the default readers below to the owner through `client-loop.md` and have them confirm;
4. the masters, the tokens, the font files and, when verbal identity is in scope, real copy.

Default readers for a small business: the owner; whoever makes pieces (a designer, a freelancer or a tool); whoever produces them (a printer, a developer); whoever writes messages.

## 2. Fixed structure

The order is fixed. A section exists only when a reader task needs it; no section exists to complete the list.

| # | Section | Content | Mode |
|---|---|---|---|
| 0 | Cover | Brand name, "Brand manual", version, date, whom to ask. Nothing else. | — |
| 1 | Contents | Anchors. Titles are written as tasks ("Use the logo", "Choose the colors"). | lookup |
| 2 | Start here | The first piece in ten minutes: the most frequent reader task, in steps, with its files and the finished example. No explanation. | do |
| 3 | The brand on one page | At most 150 words: what the company does, for whom, what the brand must make people perceive (the direction criteria in plain words), the trait that makes it recognizable. | explain |
| 4 | Elements | One section per element the tasks need, in this order: the name and how to write it; the logo; colors; typography; images and illustration; composition; motion. Each in the unit of §3. | do, lookup |
| 5 | Voice and messages | Only when verbal identity is in scope: principles written as writing decisions, tone by moment, examples per verbal touchpoint, right and wrong with real copy. | do, lookup |
| 6 | Applications | One page per declared touchpoint: the admitted render, dimensions, files, production notes, and the mark "Rule" or "Room". | do, lookup |
| 7 | Files | A table: file, what it is for, format, where it goes. Every file downloadable from the folder. | lookup |
| 8 | When the rule does not cover it | Whom to ask, how to propose a change, what never to do without asking. | do |
| 9 | Version | Version, date, what changed in this version in at most five lines. | lookup |

Forbidden anywhere in the book: a marketing hero (a claim, slogan or campaign image), a manifesto, an opening slogan, a list of personality adjectives, an archetype, "our values" without a decision attached, a section without a task, an invented reader, a render below the floor, and process vocabulary (contract, schema, thesis, signature, maturity, route, evidence, open questions, prompts).

## 3. The section unit

Every section in Elements, Voice and Applications has the same parts, in this order:

1. **Title as a task.**
2. **Mark:** "Rule" (fixed; changes only with a new version) or "Room" (varies within what the section says).
3. **Why:** one sentence. The only explanation allowed in the section.
4. **Rules:** one per sentence, imperative, condition before action; "must" for the non-negotiable, "may" for the permitted. Never "avoid", "try to", "ideally", "whenever possible".
5. **Values:** a table with the numbers reproduction depends on (hex, CMYK, minimum sizes, margins, weights, file names). Where reproduction does not depend on a number, there is no number.
6. **Right and wrong:** at least one pair. Visual pairs in `figure` with the caption "Right:" or "Wrong:" and the reason in one sentence; verbal pairs in `blockquote` with the same captions.
7. **Files:** the ones the task uses, linked to the folder.
8. **When it does not cover:** one sentence, whom to ask.

A section without a right-and-wrong pair is not ready.

## 4. Writing rules

Instructions:
- Write in the readers' language (`book.readers.language`), in the organization's first person plural ("our logo", "our colors").
- Use the imperative. One rule per sentence. At most twenty words per sentence.
- Give values and file names instead of qualifiers: "leave a 24 px margin", not "leave generous breathing room".
- Define a technical term the first time or replace it with the common word.
- Titles predict content. No title is a question.

Forbidden in instructions:
- adjectives of quality or emotion: unique, innovative, elegant, sophisticated, powerful, human, authentic, modern, premium, inspiring, and their equivalents;
- metaphor ("the brand breathes"), personification, rhetorical questions, exclamation marks, slogans, "we believe", "our essence", "journey", "DNA";
- vague permission: "you can", "feel free";
- explanation outside "Why" and section 3;
- any sentence that describes the brand instead of saying what to do.

Examples of brand copy:
- in the audience's language (`strategy.audience.language`), in the brand's voice, always inside `figure`, `blockquote`, `code`, `pre` or `samp`. This is how a reader and `scripts/book_checks.py` tell an instruction from an example.

## 5. Form and expression

- One HTML file at the root of the served folder; assets, fonts and downloadable files in the folder; CSS in the file; no scripts; no external requests; `<html lang>` set to the readers' language.
- A document page: one reading column for instructions, with plates free to span the page; contents fixed at the side on wide screens and at the top on narrow ones; disclosure with `details`/`summary`; an anchor on every section; a print stylesheet that starts each section on a new page and shows every value without truncation.
- The brand enters through the system applied to the page, the pieces shown at useful size, and the precision of the document. Forbidden is function, not form: no slogan, no manifesto, no scroll effect, no image or block that neither shows an element of the system nor serves a task. Each Elements section opens with a **plate**: the element itself at full force (the symbol at scale, colour in its proportions, type as image), full width when the element needs it. The cover is an application of the brand carrying the cover content of §2.

A familiar documentation pattern is accepted when a reader task needs its function; its form comes from the system. Do not ban navigation because generic navigation looks generic.

## 6. Production

1. **Sources.** Compile from the built truth: masters, tokens, admitted renders, real copy. The contract checks the book; it does not generate it.
2. **Prototype.** "Start here", one Elements section, one Applications page and the Files table, with real content. Render on a phone, on a desktop and in print. Judge the prototype for force beside the bar before transfer (`identity-craft.md` §2); a prototype that transfers but does not hold beside the bar is not scaled. When the document's expression is open, explore it in the generator's exploration regime first. Give an isolated context only the prototype and have it execute two reader tasks. Repair structure, register and navigation. Only then scale.
3. **Scale.** The remaining sections in the same unit.
4. **Judge** (§7). 5. **Deliver** (§8).

## 7. Judging, in this order

1. `scripts/book_checks.py <folder>` passes or carries a justified exception. It decides package shape only: no scripts or external requests, self-containment, resolvable relative references, alt text, orphan files, print stylesheet, contract and report kept out of the folder; it warns on a missing `lang` and on flag words or exclamation marks outside example elements. It says nothing about transfer or expression.
2. **Integrity.** Every value appears once and equals its source; every render is the admitted one; every file in the table exists and opens.
3. **Transfer.** An isolated context receives only the book and each reader's tasks and executes them; each task comes back as done or blocked, with the sentence or the absence that blocked it. Without an isolated context, the maker executes them in a cold pass and the report says so.
4. **Worst element**, searched in this order of severity: a rule that leads a reader to do wrong work; a value, a file or a section a task needs and that is missing; a render below the bar; a sentence that breaks §4. Raise it to the floor or remove it; repeat until none remains. A removal becomes a named gap in the report. The floor has two sides: nothing below it is shown, and nothing a task needs is missing.
5. **Expression.** The craft of the document, judged by `judging.md` against the bar, as a document, not as a campaign, by the strongest available judge (`judging.md` §4).
6. **Owner.** At delivery the owner executes one reader task using only the book (`client-loop.md`).

The book's maturity is the lowest of the six. `final` requires all six.

## 8. Delivery

Deliver the book and the folder. Deliver the contract separately as an operating file. In the operator report: the readers and their tasks; the result of each task in the transfer test; the worst element found in each round and what was done; the sections left out and why; who judged; the maturity. None of this inside the book.
