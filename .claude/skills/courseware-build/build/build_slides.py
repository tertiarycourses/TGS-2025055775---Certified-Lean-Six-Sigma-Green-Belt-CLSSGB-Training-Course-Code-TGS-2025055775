#!/usr/bin/env python3
"""Build the CLSSGB slide deck — all-white Tertiary house style, DMAIC order.

Structure:
  Cover -> Admin (TRAQOM, trainers x2, ground rules, LMS, lesson plan x4 days,
  TSC, outcomes, course outline, briefing, assessment, assessment flow, practice exam)
  -> Foundations -> D -> M -> A -> I -> C  (each phase: concept slides then its labs)
  -> Wrap-up -> Assessment -> Assessment Flow -> Digital Attendance -> TRAQOM -> Thank You

Content comes entirely from course_data.py + data_domainN.py + concepts.py so the
PPT, LP, LG and labs stay 100% aligned.
"""
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5
from components import (Deck, BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT,
                        WHITE, LINE, DMAIC_COLORS)
import concepts

ACTIVITIES = DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5


def _find_repo(start):
    env = os.environ.get("COURSE_REPO")
    if env and os.path.isdir(env):
        return env
    d = start
    for _ in range(8):
        d = os.path.dirname(d)
        if os.path.isdir(os.path.join(d, "courseware")) and os.path.isdir(os.path.join(d, "labs")):
            return d
    return os.path.dirname(os.path.dirname(HERE))


REPO = _find_repo(HERE)
ASSETS = os.path.join(REPO, "courseware", "assets")


def asset(name):
    p = os.path.join(ASSETS, name)
    return p if os.path.exists(p) else None


d = Deck(C, repo_assets=ASSETS)

# ============================================================ COVER
d.cover(logo=asset("tertiary-logo.png"))

# ============================================================ ADMIN
d.section("COURSE ADMINISTRATION", "Welcome & Housekeeping", "")

d.flow_h("Digital Attendance (Mandatory)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Repeat for AM, PM and the assessment",
    "Keep 75% attendance to stay eligible for funding",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

# --- two trainer profile cards (house hard rule) ---
d.trainer_slide("YOUR TRAINER · GENERAL", "Your Trainer",
                "General Trainer template —\nto be completed by the trainer",
                [("Name", ""), ("Title / Designation", ""), ("Qualifications", ""),
                 ("Areas of expertise", ""), ("Training & industry experience", ""), ("Contact", "")],
                initials="?", accent=GREY)
d.trainer_slide("YOUR TRAINER", C.TRAINER,
                "Principal Trainer\nTertiary Infotech Academy Pte. Ltd.",
                [("Role", "Principal Trainer, Tertiary Infotech Academy Pte. Ltd."),
                 ("Qualifications", "PhD; Certified Lean Six Sigma Black Belt practitioner and trainer."),
                 ("Delivers", "WSQ courses on Lean Six Sigma, quality management and data analytics."),
                 ("Experience", "Process improvement across manufacturing, service and technology sectors."),
                 ("Founder", "Founder and lead instructor at Tertiary Infotech / Tertiary Courses.")],
                initials="AA", accent=BLUE)

d.content("Let's Know Each Other", [
    "Your name, organisation and role.",
    "Your experience with process improvement, quality or data analysis.",
    "Have you completed a Yellow Belt or run an improvement project before?",
    "One process at work that frustrates you — we may use it as your course scenario.",
], kicker="ICE-BREAKER")

# NOTE: assets/trainer-*.jpeg and assets/ground-rules.jpeg were screenshots of
# slides from a DIFFERENT course (CompTIA CySA+, TGS-2024049211) and carried that
# course's name and code in their footers. They have been deleted; these slides are
# rendered natively from this course's own components instead.
d.tile_grid("Ground Rules", [
    "Set your mobile phone to silent mode.",
    "Participate actively — no question is too small.",
    "Mutual respect: agree to disagree.",
    "One conversation at a time.",
    "Be punctual; return from breaks on time.",
    "75% attendance is required for certification.",
], kicker="HOUSEKEEPING", cols=2, size=15)

# --- Download course material ---
lms = asset("lms_download.png") or asset("lms-download.png")
if lms:
    d.image_slide("Download Your Course Material", lms,
                  kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com",
                  caption="Log in to lms-tms.tertiaryinfotech.com to download the slides, Learner Guide and lab files.")
else:
    d.flow_h("Download Your Course Material", [
        "Go to lms-tms.tertiaryinfotech.com",
        "Sign in with the account details given in class",
        "Open this course from your dashboard",
        "Download the slides, Learner Guide and lab files",
        "Keep them open — the assessment is open book",
    ], kicker="COURSE PORTAL · lms-tms.tertiaryinfotech.com", color=TEAL)

# --- Lesson plan: 4 days ---
d.two_col("Lesson Plan — Days 1 & 2",
          [("Day 1 — " + C.DAY_THEMES[1], 0),
           ("Digital attendance (AM) · Introductions", 1),
           ("Foundations: quality, Lean, Six Sigma, Y = f(X)", 1),
           ("Sigma level, DPMO, COPQ, belt roles, DMAIC", 1),
           ("Labs 1-2 — project selection, Y = f(X), baseline sigma", 1),
           ("DEFINE: VOC, affinity, Kano, CTQ trees", 1),
           ("Charter, problem statement, SIPOC, stakeholders", 1),
           ("Labs 3-6 — VOC/Kano, CTQ tree, charter, SIPOC", 1)],
          [("Day 2 — " + C.DAY_THEMES[2], 0),
           ("Digital attendance (AM)", 1),
           ("MEASURE: process mapping, swimlanes, 8 wastes", 1),
           ("VSM, takt time, lean metrics", 1),
           ("Data types, sampling, sample size calculation", 1),
           ("MSA / Gage R&R — accuracy, repeatability, reproducibility", 1),
           ("Yield, DPU, DPO, DPMO, RTY, baseline capability", 1),
           ("Labs 7-13 — mapping, VSM, sampling, MSA, metrics", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 1", rhead="Day 2")

d.two_col("Lesson Plan — Days 3 & 4",
          [("Day 3 — " + C.DAY_THEMES[3], 0),
           ("Digital attendance (AM)", 1),
           ("ANALYZE: common vs special cause, run charts", 1),
           ("Pareto, stratification, boxplots", 1),
           ("Fishbone, 5 Whys, multi-voting", 1),
           ("Hypothesis testing: H0/Ha, alpha, p-values, test selection", 1),
           ("Type I & II errors, correlation, regression", 1),
           ("Labs 14-18 — run charts, Pareto, root cause, hypothesis tests", 1)],
          [("Day 4 — " + C.DAY_THEMES[4], 0),
           ("Digital attendance (AM)", 1),
           ("IMPROVE: solution generation, benchmarking", 1),
           ("Solution selection matrix, 5S, poka-yoke, FMEA, DOE", 1),
           ("CONTROL: SPC, control chart selection, Cp/Cpk", 1),
           ("Out-of-control rules, control plan, SOP, handover", 1),
           ("Labs 19-25 — selection matrix, FMEA, SPC, control plan", 1),
           ("Revision · Briefing · Final Assessment (WA + PP)", 1)],
          kicker="SCHEDULE · 9:30am-6:30pm with a 1-hour lunch",
          lhead="Day 3", rhead="Day 4")

# --- WSQ TSC alignment ---
d.content(f"Skills Framework — TSC: {C.TSC_TITLE}", [
    f"TSC Code: {C.TSC_CODE}",
] + C.TSC_ABILITIES + C.TSC_KNOWLEDGE, kicker="WSQ SKILLS FRAMEWORK", size=15)

d.tile_grid("Learning Outcomes", [
    ("LO1 — Lead & scope", "Define the problem, scope the work and charter the project."),
    ("LO2 — Map & baseline", "SIPOC, detailed process maps and value stream maps."),
    ("LO3 — Valid measurement", "Sampling, sample size, MSA/Gage R&R and capability."),
    ("LO4 — Analyse statistically", "Pareto, run charts, hypothesis testing, regression."),
    ("LO5 — Prove root cause", "Fishbone, 5 Whys and statistical evidence."),
    ("LO6 — Select & de-risk", "Selection matrices, FMEA and DOE before piloting."),
    ("LO7 — Sustain the gain", "SPC control charts, Cp/Cpk and the control plan."),
], kicker="WHAT YOU'LL ACHIEVE", cols=2, size=14)

d.dmaic_wheel("Course Outline — We Follow DMAIC End to End", [
    ("D", "Define", ["VOC, Kano, CTQ trees", "Charter & problem statement", "SIPOC, stakeholders", "Labs 3-6"]),
    ("M", "Measure", ["Mapping, VSM, takt", "Sampling & sample size", "MSA, DPMO, capability", "Labs 7-13"]),
    ("A", "Analyze", ["Run charts, Pareto", "Fishbone, 5 Whys", "Hypothesis tests, regression", "Labs 14-18"]),
    ("I", "Improve", ["Solution selection", "5S, poka-yoke, FMEA", "DOE and piloting", "Labs 19-22"]),
    ("C", "Control", ["SPC & control charts", "Cp/Cpk capability", "Control plan, handover", "Labs 23-25"]),
], kicker="COURSE ROADMAP · 4 DAYS · 25 HANDS-ON LABS")

roadmap = asset("clssgb-dmaic-roadmap.png")
if roadmap:
    d.image_slide("The DMAIC Roadmap", roadmap, kicker="COURSE ROADMAP",
                  caption="Every topic, lab and assessment task in this course sits inside one of these five phases.")

# --- Briefing BEFORE assessment (house hard rule) ---
d.tile_grid("Briefing for Assessment", [
    ("Clear your desk", "Phones and other materials go under the table or on the floor."),
    ("No photos or recording", "Assessment scripts must not be photographed or recorded."),
    ("No discussion", "The assessment is individual work — no talking once it starts."),
    ("Black or blue pen", "Use a black or blue pen for hard-copy assessments."),
    ("No correction fluid", "No liquid paper or correction tape — strike through instead."),
    ("Scripts collected on time", "All scripts are collected when time is up."),
], kicker="BEFORE YOU SIT THE ASSESSMENT", cols=2, size=15, accent=VIOLET)

d.tile_grid("Assessment", [
    ("Written Assessment (WA)", "Short-Answer Questions (SAQ) — 2 questions (K1, K2), 60 minutes."),
    ("Practical Performance (PP)", "3 applied DMAIC tasks (A1-A5), 90 minutes."),
    ("Open book", "Slides, Learner Guide and approved materials only."),
    ("Attendance", C.ASSESSMENT["note"]),
    ("Appeals", "An appeal process is available if required."),
], kicker="FINAL ASSESSMENT", cols=1, size=14, accent=VIOLET)

# NOTE: courseware/assets/assessment-flow.jpeg is NOT used — it is a screenshot
# from a DIFFERENT course (CompTIA CySA+, TGS-2024049211) and names the wrong
# instrument ("Case Study"). This course is assessed by WA + PP, so the flow is
# always rendered natively from this course's own data.
ASSESSMENT_FLOW = [
    "TRAQOM survey — scan the QR code on the LMS",
    "Assessment digital attendance — scan the SSG QR",
    "Sit the WA (SAQ), then the PP — open book",
    "Submit your answers on the LMS",
    "Sign the Assessment Summary Record",
]
d.flow_h("Assessment Flow", ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY", color=VIOLET)

# NOTE: no Practice Exam slide — there is no Six Sigma practice exam on
# exams.tertiaryinfotech.com. The bundled clssgb-practice-exam.png has been
# deleted; do not reintroduce this slide for this course.

# ============================================================ FOUNDATIONS
concepts.foundations(d)

# ============================================================ DMAIC PHASES + LABS
PHASE_FN = {
    1: concepts.define_phase,
    2: concepts.measure_phase,
    3: concepts.analyze_phase,
    4: concepts.improve_phase,
    5: concepts.control_phase,
}
TOPIC_ACTS = {t["num"]: [a for a in ACTIVITIES if a["topic"] == t["num"]] for t in C.TOPICS}


def render_labs(acts, phase_label):
    for a in acts:
        opt = a.get("elective", False)
        tag = f"LAB {a['num']}"
        d.activity_overview(tag, a["title"], a["desc"], a["build"], a["services"],
                            kicker=f"{phase_label} · HANDS-ON", elective=opt)
        steps = a["steps"]
        total = len(steps)
        # Truncate the eyebrow on a WORD boundary — a hard character cut breaks
        # mid-word ("...Affinity Diagra") on long lab titles.
        _t = a["title"]
        if len(_t) > 38:
            _t = _t[:38].rsplit(" ", 1)[0].rstrip(" ,.;:-") + "…"
        short = _t
        # Group the steps 4 to a slide: every step keeps its full wording, but the
        # deck stays near the 4-day target instead of one slide per step.
        PER = 4
        for i in range(0, total, PER):
            d.steps_group(f"LAB {a['num']} · {short}", a["title"],
                          steps[i:i + PER], i + 1, total)
        d.test_slide(a["title"], a["test"], kicker=f"LAB {a['num']} · VERIFY")


# Foundations labs (topic 0) come right after the foundations concepts
render_labs(TOPIC_ACTS.get(0, []), "FOUNDATIONS")

for t in C.TOPICS:
    if t["num"] == 0:
        continue
    idx = t["num"] - 1
    col = DMAIC_COLORS[idx % len(DMAIC_COLORS)]
    d.section(f"DMAIC · {t['phase']}", t["title"], t["code"], t["subtitle"])
    # concept tiles: chunk at 8 so the grid never overflows
    cons = t["concepts"]
    for i in range(0, len(cons), 8):
        chunk = cons[i:i + 8]
        suffix = "" if len(cons) <= 8 else f" ({i // 8 + 1})"
        d.tile_grid(f"Key Concepts — {t['phase'].title()}{suffix}", chunk,
                    kicker=f"{t['phase']} · {t['weighting']} OF THE COURSE",
                    cols=2, size=14, accent=col)
    # teaching content for this phase
    PHASE_FN[t["num"]](d)
    # labs that belong to this phase
    acts = TOPIC_ACTS.get(t["num"], [])
    if acts:
        core = [a for a in acts if not a.get("elective")]
        opts = [a for a in acts if a.get("elective")]
        rows = []
        for a in core:
            rows.append((f"Lab {a['num']} — {a['title'][:46]}", a["build"][:70]))
        for a in opts:
            rows.append((f"Lab {a['num']} (elective) — {a['title'].replace('Elective — ', '')[:40]}",
                         a["build"][:70]))
        # tile_grid caps out around 6 rows at cols=1; chunk so nothing overflows
        for i in range(0, len(rows), 6):
            chunk = rows[i:i + 6]
            suffix = "" if len(rows) <= 6 else f" ({i // 6 + 1})"
            d.tile_grid(f"Hands-On Labs — {t['phase'].title()}{suffix}", chunk,
                        kicker="WHAT YOU'LL DO", cols=1, size=14, accent=col)
        render_labs(acts, f"DMAIC · {t['phase']}")
    # phase recap
    d.content(f"Recap — {t['phase'].title()}",
              [c[0] + " — " + c[1] for c in t["concepts"]][:6],
              kicker="PHASE RECAP", size=14)

# ============================================================ WRAP-UP
d.section("WRAP-UP", "Course Summary & Next Steps", "")
d.dmaic_wheel("What You Achieved — The Full DMAIC Journey", [
    ("D", "Define", ["Captured VOC and CTQs", "Wrote the charter", "Built the SIPOC", "Mapped stakeholders"]),
    ("M", "Measure", ["Mapped the value stream", "Sized the sample", "Proved the gage", "Baselined capability"]),
    ("A", "Analyze", ["Read the run chart", "Built the Pareto", "Tested the hypothesis", "Fitted the regression"]),
    ("I", "Improve", ["Scored the solutions", "Ran the FMEA", "Designed the experiment", "Piloted the change"]),
    ("C", "Control", ["Selected the chart", "Recalculated Cp/Cpk", "Built the control plan", "Handed over"]),
], kicker="YOUR IMPROVEMENT PACKAGE")

d.tile_grid("Your Integrated Improvement Package", [
    ("Project selection & charter", "Business case, problem statement, goal, scope and RACI."),
    ("Customer requirements", "VOC log, affinity diagram, Kano classification and CTQ tree."),
    ("Process baseline", "SIPOC, swimlane map, VSM, takt time and waste walk."),
    ("Valid measurement", "Sampling plan, calculated sample size and Gage R&R verdict."),
    ("Performance baseline", "Yield, RTY, DPMO, sigma level and baseline Cp/Cpk."),
    ("Proven root causes", "Pareto, Fishbone, 5 Whys, hypothesis tests and regression."),
    ("Selected improvements", "Weighted selection matrix, FMEA with RPNs and a pilot plan."),
    ("Sustained control", "Control chart, control plan, SOP, A3 and signed handover."),
], kicker="WHAT YOU BUILT", cols=2, size=13)

d.tile_grid("Final Readiness Checklist", [
    "Can you explain each DMAIC phase and the deliverable that closes it?",
    "Can you write a problem statement with no cause and no solution in it?",
    "Can you calculate DPMO and convert it to a sigma level?",
    "Can you decide whether a measurement system can be trusted?",
    "Can you choose the right hypothesis test for a question and data type?",
    "Can you apply the p-value rule and state the business conclusion?",
], kicker="BEFORE THE ASSESSMENT", cols=1, size=14, accent=TEAL)

d.tile_grid("Final Readiness Checklist (2)", [
    "Can you select the correct control chart for your data?",
    "Can you calculate Cp and Cpk and say whether the issue is spread or centring?",
    "Can you apply the eight out-of-control rules to a control chart?",
    "Can you build a control plan with named owners and reaction plans?",
    "Can you prove your improvement held using a hypothesis test?",
], kicker="BEFORE THE ASSESSMENT", cols=1, size=14, accent=TEAL)

d.tile_grid("Continuing Your Lean Six Sigma Journey", [
    ("Run a real project", "Apply DMAIC to one scoped process in your own area."),
    ("Black Belt", "The next step — leads complex projects and mentors Green Belts."),
    ("Keep the templates", "Your lab outputs are reusable templates for real projects."),
    ("Coach others", "Teaching a Yellow Belt is the fastest way to deepen your practice."),
], kicker="NEXT STEPS", cols=2, size=15, accent=AMBER)

# ============================================================ CLOSE (house order)
# Assessment -> Assessment Flow -> Digital Attendance -> TRAQOM -> Thank You
d.big_statement("Final Assessment",
                "Written Assessment (SAQ, 2 questions, 60 minutes) then the Practical "
                "Performance (3 tasks, 90 minutes). Both are open book.",
                "ASSESSMENT", color=VIOLET)

d.flow_h("Assessment Flow", ASSESSMENT_FLOW, kicker="ON ASSESSMENT DAY", color=VIOLET)

d.flow_h("Digital Attendance (Assessment)", [
    "Trainer displays the SSG digital attendance QR code",
    "Scan the QR code with your phone camera",
    "Key in your NRIC/FIN and submit",
    "Attendance must be recorded before you begin the papers",
], kicker="TRAQOM · SSG DIGITAL ATTENDANCE", color=BLUE)

d.flow_h("TRAQOM Survey", [
    "Open the TRAQOM survey link on the LMS",
    "Key in the last four characters of your NRIC/FIN",
    "Key in the six-digit course run ID",
    "Complete and submit — your feedback shapes this course",
], kicker="YOUR FEEDBACK", color=TEAL)

d.content("Certificate & Support", [
    "Two e-certificates are awarded on demonstrating competency and achieving at least 75% attendance.",
    "A SkillsFuture Statement of Attainment (SOA) is issued for the WSQ assessment.",
    "Email: enquiry@tertiaryinfotech.com",
    "Tel / WhatsApp: +65 6100 0613",
], kicker="AFTER THE COURSE")

d.big_statement("Thank You!",
                "Now go and lead one DMAIC project end to end — that is what a Green Belt is for.",
                "END OF COURSE", color=BLUE)

# ============================================================ TRANSITIONS + SAVE
d.apply_transitions(kind="fade", dur_ms=700)

out = os.path.join(REPO, "courseware", f"{C.SHORT_TITLE}-{C.VERSION}.pptx")
d.prs.save(out)
print(f"✅ {out}")
print(f"   {len(d.prs.slides._sldIdLst)} slides")
