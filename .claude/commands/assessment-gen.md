---
description: Generate the WSQ assessment set for this course — the Written Assessment (WA/SAQ) and the PP or Case Study, each as a question paper and an answer key — mirroring the original paper, then audit with /courseware-qa.
---

# /assessment-gen — generate the assessment set (WA + PP/CS)

Generate this course's assessment: the **Written Assessment (WA / SAQ)** that tests **knowledge**, and **one** practical instrument that tests **ability** — a **Practical Performance (PP)** *or* a **Case Study (CS)** — each as a **question paper** and a matching **answer key** (four DOCX). Standards: <https://tertiarycourses.github.io/wsqcourseware/>.

Use the **`wsq-assessment` skill** and its `build_assessment.py`. Run the builder in place; it writes into `assessment/`.

## Step 1 — read the ORIGINAL first (never skip)

Look in `reference/`, `assessment/` (a previous version), or whatever the trainer supplied. **The new assessment is a revision of that paper, not a redesign.** Mirror it:

- **Same instrument type.** A **Case Study stays a Case Study**; a PP stays a PP. **Never convert one to the other.** Set `INSTRUMENT = "CS"` or `"PP"` to match.
- **Same number of questions.** 3 SAQs and 3 tasks in the original means **3 and 3** in the new one. **Do not add, drop, split or merge an item** — the only exception is an explicit instruction from the user.
- **Same K/A codes and the same mapping** (e.g. Task 1 → A1, A2; Task 2 → A3, A4; Task 3 → A5).
- **Same timings** (e.g. WA 60 minutes, CS 90 minutes) — from the paper, not from habit.

**What you DO change:** the content — scenario, questions and model answers — rewritten from *this* course's slides and labs.

If there is no original, derive the counts and codes from the TSC / competency unit and say so.

## Step 2 — write the content

- **WA = knowledge.** Every question answerable from the **slides**; tag each with its `K` codes and cite the slide in the key.
- **PP/CS = ability.** One coherent scenario. **Every task aligns to an actual lab** and cites it; the **model answer is the lab procedure** applied to the scenario.
- **ALL questions OPEN-ENDED.** Zero multiple choice.
- **Everything is covered in class** — nothing assessed that the slides and labs do not teach.

## Step 3 — full K & A coverage (the build enforces this)

- The **WA covers every K** (`K1 … Km`); the **PP/CS covers every A** (`A1 … An`).
- Every question/task **prints its own codes** on the paper (e.g. `(K1, K2)`, `(A3, A4)`); the answer key repeats the **identical** codes.
- `check_coverage()` prints the coverage map and **fails the build** on an orphan. **A missing K or A is an issue to flag to the user — never ship it.**

## Step 4 — format

- **Cover page on every one of the four documents**, naming the **correct instrument**: "Written Assessment (SAQ)", "Practical Performance (PP)" or "Case Study (CS)", with the keys marked as the Answer Key. **Cover page only — no version-control record.**
- **Page layout is fixed:** page 1 the cover; **page 2 = Trainee Information + Instructions to Candidate (with the clickable LMS link https://lms-tms.tertiaryinfotech.com/) + the Grading / For Official Use Only block, and nothing else**; the **scenario and questions start on page 3**. Answer keys are trainer copies: cover, then model answers.
- Boxed answer space under every question and task; model-answer tables as **real Word tables**.
- **DOCX only** — no PDFs for the assessment set.

## Step 5 — after generating

1. Run **`/courseware-qa assessment`**. Fix every failure, regenerate, re-run until it passes.
2. Report the **K/A coverage table** (code → question(s) → lab/slide).
3. **Distribution:** the assessment is **confidential** — it is **never pushed to GitHub** (keep `assessment/` git-ignored) and goes to **Google Drive only**. On the LMS, attach **only the two question papers** (the WA paper and the PP/CS paper); the **answer keys are trainer-only and never go to the LMS**.
