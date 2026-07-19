---
name: wsq-assessment
description: Generate WSQ course assessments as professionally formatted Word documents (.docx) — a Written Assessment (WA/SAQ) that tests KNOWLEDGE plus ONE practical instrument that tests PRACTICAL ability: either a Case Study (CS) or a Practical Performance (PP), each as a question paper PLUS a model-answer / marking guide (4 DOCX). build_assessment.py is the single builder — set INSTRUMENT="CS" or "PP". ALWAYS FOLLOW THE ORIGINAL/REFERENCE ASSESSMENT: DO NOT CHANGE THE NUMBER OF QUESTIONS, same instrument type (never convert CS to PP or the reverse), same K/A criterion codes and mapping, same timings — only the content is rewritten from the course slides and labs. All questions are OPEN-ENDED (no multiple choice). Documents carry the WSQ house COVER PAGE (course title + logos + UEN) and no version-control record. Use when creating or revising assessments, written/practical/case-study questions, answer keys, or marking guides for a WSQ course.
---

> **Key principle:** The course material must be **100% aligned to the exam/skills domains** so that students who take the course can pass the exam.

# WSQ Assessment → DOCX (Written + Practical/Case-Study)

Generate two WSQ assessment instruments, each as a **question paper** and a matching **model-answer / marking guide** (four DOCX total). Pick the builder that matches the course's assessment design:

| Builder | Instruments | Best for |
|---------|-------------|----------|
| **`build_assessment.py`** (primary) | **WA (SAQ)** knowledge + **either PP (Practical Performance) or CS (Case Study)** — set by the `INSTRUMENT = "PP" \| "CS"` constant | Every course. Carries the **WSQ house cover page** (course title + Tertiary & course logos + UEN), identical to the Lesson Plan / Learner Guide — cover page only, no version-control record. PP = discrete activity tasks graded on what the learner built in class; CS = one coherent scenario worked through as tasks. |
| **`build_wsq_assessment.py`** (legacy) | **WA** + **CS** | Older WA + Case Study variant, kept for reference. Prefer `build_assessment.py` with `INSTRUMENT = "CS"` — it has the house cover page and the LMS link. |

## FOLLOW THE ORIGINAL (MANDATORY — read before writing anything)

If the course already has an assessment — a previous version, or a **reference paper** (look in `reference/`, `assessment/`, or whatever the trainer supplied) — **read it first and mirror it**. The new assessment is a revision of that paper, not a redesign:

1. **Same instrument type.** If the original is a **Case Study (CS)**, the new one is a Case Study. If it is a **Practical Performance (PP)**, it stays PP. **Never convert CS → PP or PP → CS.** Set `INSTRUMENT` in `build_assessment.py` to match, and keep the original's file naming (`Case Study (CS) - …` vs `PP Assessment - …`).
2. **Same question / task count.** Three SAQs and three tasks in the original means three and three in the new one. Do not add or drop items unless the user explicitly asks.
3. **Same criterion codes and the same mapping.** Keep the original's `K1…Km` / `A1…An` and the way they are distributed across the questions (e.g. Task 1 → A1, A2; Task 2 → A3, A4; Task 3 → A5).
4. **Same timings and instructions** (e.g. WA 60 minutes, CS 90 minutes) — take them from the original paper, not from habit.
5. **What you DO change:** the content — scenario, questions, and model answers — so they are drawn from *this* course's slides and labs. When the practical follows the labs, the tasks and their model answers are the lab procedure.
6. If you believe the original's structure is wrong, **say so and ask** — do not silently "improve" it.

## Hard rules (do not break)
- **DO NOT CHANGE THE NUMBER OF QUESTIONS.** The count of WA questions and of practical tasks in the original / reference / previous assessment is fixed — 3 SAQs and 3 tasks stay 3 and 3. Never add, drop, split or merge an item to make the content fit; rewrite the wording and the model answers inside the existing count. The **only** exception is an explicit instruction from the user to change the count.
- **DO NOT CHANGE THE INSTRUMENT TYPE.** A Case Study course stays a Case Study; a PP course stays PP.
- **PAGE LAYOUT IS FIXED: cover → page 2 → page 3.** On every question paper: **page 1 is the WSQ cover page**; **page 2 carries the Trainee Information, the Instructions to Candidate AND the Grading / For Official Use Only block — nothing else**; the **scenario and the questions/tasks start on page 3**, after a page break. Never let a question, a task or the scenario begin on page 2, and never push the instructions or the grading block onto page 3. (Answer keys are trainer copies: cover, then the model answers — no trainee information, instructions or grading.) `build_assessment.py` enforces this with `candidate_block()` + `instructions()` + `grading()` followed by `page_break()`.
- **NO multiple choice. Every question is OPEN-ENDED.** Short-answer with a ruled/boxed answer space; never emit a)/b)/c)/d) options.
- **The Written Assessment (WA) tests KNOWLEDGE.** Every question must be answerable from the course **slides / modules**. Tag each with a knowledge code (K1, K2, …) and cite the source in the answer key.
- **The practical instrument tests PRACTICAL ability.** For **PP**, each task maps to an **Ability** (A1, A2, …) and to an **activity the learner did in class**; the model answer **is the lab build steps** (name the exact triggers/actions and cite the activity). For **CS**, use **one coherent scenario** built from the in-class activities.
- **EVERY K AND EVERY A MUST BE COVERED — no exceptions.** The **WA covers the Knowledge items (K1 … Km)** and the **practical instrument (PP *or* CS) covers the Abilities (A1 … An)**. Every question/task must print the codes it covers, and the union across the paper must be the complete set. **If any K or A is missing, FLAG IT AS AN ISSUE and tell the user — do not ship the assessment.** `build_assessment.py` enforces this: `check_coverage()` prints the coverage map and **fails the build** on an orphaned K or A. See *Ability coverage* below.
- **The Case Study follows the labs too.** A CS is one coherent scenario, but its tasks and model answers are still drawn from the **in-class labs** — each task cites the lab(s) it comes from, and the model answer is the lab procedure applied to the scenario. Same rule as PP: nothing is assessed that was not done in class.
- **Everything is "covered in class."** Do not test content that is not in the slides or labs.
- **Keep the question/task count stable** when revising an existing assessment — see the DO NOT CHANGE THE NUMBER OF QUESTIONS rule above.

## Ability coverage (MANDATORY)

The TSC gives the course a fixed set of Abilities (`A1 … An`) and Knowledge items (`K1 … Km`). The assessment is only valid if **every one of them is actually assessed somewhere**. An orphaned ability — one that appears in the competency unit but that no question tests — is the single most common reason an assessment is rejected.

1. **Full coverage.** Across the practical questions (**PP or CS** — whichever the course uses), the union of the declared abilities must equal `{A1 … An}` — no ability left untested. Likewise the WA questions must jointly cover `{K1 … Km}`. **A missing K or A is an ISSUE to be flagged to the user, not a caveat to be shipped.** Before you write a single question, list the abilities and knowledge items and treat it as a checklist you must exhaust.
2. **Declare the codes in the question itself.** Every PP/CS task ends with its ability codes in parentheses — e.g. `(A2, A3)`. Every WA question ends with its knowledge codes — e.g. `(K1, K3)`. The candidate and the assessor must both be able to see, on the question paper, what is being assessed.
3. **Mirror the codes in the answer key.** Each model answer opens with the same codes (`Suggested Answer: A2, A3 — …`) and the heading above it repeats them (`Question 2 (A2, A3)`). Question paper and answer key must never disagree.
4. **One question may carry several abilities**, and one ability may appear in more than one question. What is forbidden is an ability appearing in **none**. With four PP questions and five abilities, a valid split is e.g. Q1→A1, Q2→A2+A3, Q3→A5, Q4→A4.
5. **Map each ability to the activity that genuinely demonstrates it.** Do not assign an ability to a question whose lab does not exercise it — e.g. do not tag a chatbot lab with the RAG ability (`Apply context augmentation using RAG…`) when that lab has no vector database in it. If the requested mapping and the labs disagree, say so and propose the mapping the evidence supports.
6. **State the coverage explicitly when you report back**, as a small table: ability → question(s) → activity. If any ability is uncovered, that is a failure, not a caveat.

## How to use `build_assessment.py` (WA + PP/CS)
The script lives **in this skill** and runs **in place** — do NOT copy it into the course repo. It auto-detects the course repo root by walking up from its own location to the nearest dir containing a `.git` folder (or both `courseware/` and `assessment/`), and writes the four DOCX into `<repo>/assessment/`. Override with `REPO=/path/to/course` if needed.

1. Ensure the sibling **tertiary-lesson-plan** skill is installed — the script reuses its **`prodoc.py`** for the cover page + version control + page numbers (the import auto-falls-back from the project `.claude/skills/` to `~/.claude/skills/`).
2. Edit the **CONFIG** block: `TITLE`, `COURSE_CODE`, **`INSTRUMENT`** (`"CS"` or `"PP"` — must match the original assessment), `WA_MINUTES` / `PRACTICAL_MINUTES`, `Q_VER`/`A_VER` (single standardised version string, e.g. `"v5"`), `ORG_LOGO`, `COURSE_LOGO`.
3. Fill the two content lists **from the course materials**:
   - `WRITTEN` — `(criterion, context, question, [model-answer points])`. Read the concept slides and turn each key concept into one open-ended knowledge question. Keep it to the concepts actually taught.
   - `SCENARIO` + `PRACTICAL` — one continuous scenario, then `(label, criterion, task_prompt, box_caption, [model build-step points])` per task. Each task maps to one LO and to a class activity; the model points **are** the lab procedure (cite the activity numbers).
4. Run it in place — from the project copy of the skill:
   `python3 .claude/skills/wsq-assessment/build_assessment.py`
   (or `REPO=/path/to/course python3 ~/.claude/skills/wsq-assessment/build_assessment.py`). It writes into `<repo>/assessment/`:
   `WA (SAQ) - <Title> - <VER>.docx`, `Answer to WA (SAQ) - <Title> - <VER>.docx`, and — depending on `INSTRUMENT` —
   `Case Study (CS) - <Title> - <VER>.docx` + `Answer to Case Study (CS) - <Title> - <VER>.docx`, or
   `PP Assessment - <Title> - <VER>.docx` + `Answer to PP Assessment - <Title> - <VER>.docx`.
5. Assessments are delivered as **DOCX only** — do not generate PDFs for the assessment set.
6. Keep the question paper and its answer key on the **same version string** (e.g. both `v5`) to avoid confusion.

## Document format (WSQ house style)
- **Cover page** — same as the Lesson Plan / Learner Guide (Tertiary Infotech Academy logo, UEN, instrument name, "For", course logo, course title, TGS ref, "Conducted by", version). Cover page only — assessments do **not** include a Document Version Control Record.
- **Question paper** — **page 1: the WSQ cover page. Page 2: Trainee Information + Instructions to Candidate + Grading / For Official Use Only (Grade C / NYC, assessor name/NRIC/date/signature) — and nothing else. Page 3 onwards: the scenario and the questions/tasks**, each with a **boxed answer space**. A page break separates page 2 from page 3.
- **Submission instruction** — the Instructions to Candidate must tell the candidate to complete the answers on the document provided and **upload the completed answers to the LMS at https://lms-tms.tertiaryinfotech.com/** (rendered as a real clickable Word hyperlink). This replaces the old "email / upload to Google Drive" note. `build_assessment.py` already does this via its `LMS_URL` constant + `add_hyperlink()` helper — keep the link in sync there if the portal URL ever changes.
- **Answer document** — the model answers / marking guide: each question/task with "Suggestive answers (not exhaustive):" bullet points (WA cites the slide/module; PP lists the lab build steps and cites the activities).
- Body is **Arial 11**; every page has the copyright + page-number footer.

## Criterion tagging
- Written knowledge items → `K1, K2, …`.
- Practical/case-study tasks → `A1, A2, …` (the TSC Abilities; `LO1, LO2, …` only where the course states outcomes rather than abilities). Keep the same numbering across the question paper and its answer key.
- The codes are **printed on the question**, not just held in the answer key — see *Ability coverage*.

## Quality checklist before saving
- [ ] **The number of questions/tasks is IDENTICAL to the original/reference assessment (unless the user asked to change it).**
- [ ] **The instrument type matches the original (CS stays CS, PP stays PP), as do the K/A codes, their mapping and the timings.**
- [ ] Zero multiple-choice questions anywhere.
- [ ] **Every ability `A1 … An` is assessed by at least one PP question, and every knowledge item `K1 … Km` by at least one WA question — no orphans.**
- [ ] **Every question prints its own codes** (`(A2, A3)` / `(K1, K3)`), and the answer key repeats the identical codes.
- [ ] Each ability is tagged to a question whose lab actually demonstrates it.
- [ ] Every WA question traces to a slide/module; every PP/CS answer traces to a class activity/lab.
- [ ] One coherent PP/CS scenario (not disconnected mini-cases), and every PP/CS task cites the lab it comes from.
- [ ] Cover page present (no version-control record), and it **names the correct instrument** (Written Assessment (SAQ) / Practical Performance (PP) / Case Study (CS)).
- [ ] **Page 2 of every question paper carries the Trainee Information, the Instructions AND the Grading block — and the scenario/questions start on page 3.**
- [ ] Instructions to Candidate carry the clickable LMS submission link (https://lms-tms.tertiaryinfotech.com/), not a Google Drive / email note.
- [ ] Answer-key wording is guidance ("award the mark where the candidate covers…"), not a rigid script.
- [ ] Old/mismatched assessment files (previous versions, other courses) removed from the output folder.

## Versioning rule (MANDATORY — every update)

Every content update to a courseware artifact MUST, in the same change:

1. **Bump the version number** (and the version date) in the generator/template — e.g. `VERSION="vNN"` for slide decks (the version is also part of the output filename), `VERSION = "N.N"` plus a new `VERSIONS` entry for DOCX documents.
2. **Document the change in the Document Version Control Record** — add a row (Version Number | Effective Date of Release | Summary of Included Changes | Author) wherever the document carries one (Learner Guide / Lesson Plan). For slide decks the bumped version must appear on the cover page and in the filename.
3. **Regenerate the outputs**, remove (`git rm`) the superseded versioned files, and update any references to the versioned filename (README, slides that cite the document, etc.).

Never regenerate an artifact with content changes while keeping the old version number.
