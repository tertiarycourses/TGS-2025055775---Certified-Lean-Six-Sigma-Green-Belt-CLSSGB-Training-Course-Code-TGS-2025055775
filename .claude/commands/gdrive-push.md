---
description: Push this course's courseware (PPT + PDF, Learner Guide, Lesson Plan, assessments) to the user-provided Google Drive courseware folder — archiving superseded versions into archive/ first, never deleting, and emitting anyone-with-link viewer links.
argument-hint: <google-drive-courseware-folder-link>
---

# /gdrive-push — push the courseware to Google Drive

Push this course repo's current courseware to the user's Google Drive courseware folder. Superseded Drive copies are **moved to `archive/`** (only when the file actually changed); unchanged files are skipped; **nothing on Drive is ever deleted**.

**Folder link (required, user-supplied):** `$ARGUMENTS`

## HARD RULES

1. **Never push without the user's folder link.** If `$ARGUMENTS` is empty or is not a Drive folder link/ID, **ask (AskUserQuestion) and stop** until it is given. Never fall back to a default or remembered folder. The link is `https://drive.google.com/drive/folders/<FOLDER_ID>` — any `/u/N/` only selects a browser profile and is **not** part of the ID.
2. **QA must pass first.** Run **`/courseware-qa`**. **Do not push on a failing audit** — stop, report the failures, fix them, re-audit.
3. **Push the current build.** The LMS only stores *links*, so whatever lands on Drive is what learners get. Generate the PPT/LG/LP **PDFs** before pushing (`/courseware-gen`).
4. **Dry-run first, always.** Show the plan, then push for real.
5. **Never delete on Drive.** Superseded files are *moved* to each folder's lowercase `archive/` subfolder.

## Transport — rclone, not the MCP connector

The Google Drive **MCP connector cannot move or delete files**, so it cannot archive-and-replace — it would only pile up duplicates. Use **rclone**, which supports server-side move, MD5 change-detection (`--checksum`) and folder scoping (`--drive-root-folder-id`). The MCP connector may still be used read-only to verify.

One-time setup if missing: `brew install rclone`, then `rclone config create gdrive drive scope=drive` and complete the Google sign-in **as the account that owns (or has Editor on) the destination folder**.

## The archive convention

The archive subfolder is **`archive/`**. Some older course folders use **`old versions/`** — when you meet one, **merge it into `archive/`** (server-side move, never delete) and remove the empty folder, so every course has one archive convention:

```bash
rclone move "gdrive:<Folder>/old versions" "gdrive:<Folder>/archive" --drive-root-folder-id <ID>
rclone rmdir "gdrive:<Folder>/old versions" --drive-root-folder-id <ID>
```

**rclone will not archive into a subfolder of the destination** — `--backup-dir` inside the destination fails with *"destination and parameter to --backup-dir mustn't overlap"*. So when the archive lives **inside** the target folder (as `archive/` does), do it in two steps: **first `rclone moveto` each superseded file into `<Folder>/archive/<YYYY-MM-DD>/`, then `rclone copy` the new files in.** Do not reach for `--backup-dir`.

Watch for folder names with a **trailing space** (e.g. `"Assessment "`) — quote every remote path.

## Assessment sharing

The **question papers** (WA, PP, Case Study) must be **anyone-with-link (viewer)** so learners can open them from the LMS. Emit and check their links:

```bash
rclone link "gdrive:Assessment /<WA or PP/CS question paper>.docx" --drive-root-folder-id <ID>
```

The **answer keys** (`Answer to …` / `Answers to …`) stay in the Drive folder for the trainer — they are **not** linked out, **not** attached to the LMS, and **never** pushed to GitHub.

## Steps

1. **Sweep local junk** so it can't be pushed:
   ```bash
   find . -name ".DS_Store" -type f -delete
   find . -name '~$*'       -type f -delete   # Word/Excel lock files
   ```
2. **Run the pusher** from the course repo root — the script lives in `.claude/scripts/` (project) or `~/.claude/scripts/`:
   ```bash
   python3 <scripts-dir>/gdrive_push.py "<folder-link>" --dry-run   # preview — always
   python3 <scripts-dir>/gdrive_push.py "<folder-link>"             # real push
   ```
3. **Show the dry-run plan** per Drive folder — Master Trainer Slides / Learner Guide / Lesson Plan / Assessment / Activities — naming what is archived, what is uploaded, and what is skipped as unchanged. Then do the real push.
4. **Report** per folder: files archived → `archive/`, files uploaded, and each file's **anyone-with-link viewer link**.

## What goes where

| Drive folder | Contents |
|---|---|
| Master Trainer Slides | the **PPT** + its PDF |
| Learner Guide | the **learner slides PDF** and the **LG PDF** |
| Lesson Plan | the **LP PDF** |
| Assessment | **all four** assessment DOCX — both question papers **and** both answer keys |

Drive is the **trainer's store** and the only place the answer keys live. That is exactly why they must travel no further: `/tms-push` attaches **only the two question papers** to the LMS, and `assessment/` is never pushed to GitHub.

## Then

Run **`/tms-push`** to write these Drive links into the course record on lms-tms.tertiaryinfotech.com.
