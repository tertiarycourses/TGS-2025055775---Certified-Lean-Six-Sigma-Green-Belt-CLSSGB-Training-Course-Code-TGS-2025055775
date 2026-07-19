#!/usr/bin/env python3
"""Generate labs/lab-NN-*.md + labs/README.md + labs/tools.md from the same
single source (course_data + data_domainN) that drives the PPT, LP and LG, so the
labs can never drift out of alignment with the rest of the courseware.
"""
import os
import re
import sys
import glob

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import course_data as C
from data_domain1 import DOMAIN1
from data_domain2 import DOMAIN2
from data_domain3 import DOMAIN3
from data_domain4 import DOMAIN4
from data_domain5 import DOMAIN5

ACT = sorted(DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5, key=lambda a: a["num"])
TOPICS = {t["num"]: t for t in C.TOPICS}


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
LABS = os.path.join(REPO, "labs")

TOOLS = {
    "5whys": ("5 Whys", "https://alfredang.github.io/5whys/"),
    "fishbone": ("Fishbone Diagram", "https://alfredang.github.io/fishbone/"),
    "pareto": ("Pareto Chart (collaborative)", "https://alfredang.github.io/paretochart/"),
    "novaspc": ("NovaSPC", "https://alfredang.github.io/novaspc/"),
}

# The running scenario is defined ONCE in data_domain1.py and imported here, so the
# labs, deck, LG and assessment can never drift onto different scenarios.
from data_domain1 import SCENARIO


def slug(title):
    t = title.replace("Elective — ", "")
    t = re.sub(r"[^a-zA-Z0-9 ]", "", t).lower()
    return "-".join(t.split())[:60]


def lab_md(a):
    kind = "Elective" if a.get("elective") else "Core"
    title = a["title"].replace("Elective — ", "")
    tp = TOPICS[a["topic"]]
    phase = tp["phase"]
    out = []
    out.append(f"# Lab {a['num']} — {title}")
    out.append("")
    out.append(f"**DMAIC phase:** {phase}  |  **Lab type:** {kind}  |  "
               f"**Course:** {C.TITLE} ({C.COURSE_CODE})")
    out.append("")
    if a.get("elective"):
        out.append("> **Elective lab.** Complete this lab if time allows during class, or afterwards as "
                   "additional practice. It extends the same Northwind Retail Distribution Centre scenario used by the "
                   "core labs.")
        out.append("")
    out.append("## Objective")
    out.append("")
    out.append(a["objective"])
    out.append("")
    out.append("## Scenario")
    out.append("")
    out.append(SCENARIO)
    out.append("")
    out.append("## What you will build")
    out.append("")
    out.append(a["build"])
    out.append("")
    out.append(f"**Tools and techniques:** {a['services']}")
    out.append("")
    # any tool URLs used by this lab
    used = []
    for _, cmd in a["steps"]:
        if cmd.startswith("http"):
            for key, (name, url) in TOOLS.items():
                if url == cmd and name not in [u[0] for u in used]:
                    used.append((name, url))
    if used:
        out.append("### Online tools used in this lab")
        out.append("")
        for name, url in used:
            out.append(f"- **{name}** — {url}")
        out.append("")
    out.append("## Steps")
    out.append("")
    for i, (instr, cmd) in enumerate(a["steps"], 1):
        out.append(f"### Step {i}")
        out.append("")
        out.append(instr)
        if cmd:
            out.append("")
            if cmd.startswith("http"):
                out.append(f"Open the tool: <{cmd}>")
            else:
                out.append("```")
                out.append(cmd)
                out.append("```")
        out.append("")
    out.append("## Check your work")
    out.append("")
    out.append(a["test"])
    out.append("")
    out.append("## Deliverable")
    out.append("")
    out.append(f"Save your output — it forms part of your Northwind improvement package and is your "
               f"revision material for the assessment.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE} · Version {C.VERSION} · "
               f"© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


def readme_md():
    out = []
    out.append(f"# Labs — {C.TITLE}")
    out.append("")
    out.append(f"**WSQ Course Code:** {C.COURSE_CODE}  |  **Version {C.VERSION} · {C.VERSION_DATE}**")
    out.append("")
    out.append("These labs follow the DMAIC roadmap end to end. Every lab builds on the same Northwind "
               "Retail Distribution Centre scenario, so your outputs accumulate into one complete "
               "improvement package.")
    out.append("")
    out.append("## Lab types")
    out.append("")
    out.append("- **Core** — completed by everyone; maps directly to the assessment.")
    out.append("- **Elective** — additional practice with further Lean Six Sigma tools; run when time "
               "allows or after the course.")
    out.append("")
    out.append("## Lab index")
    out.append("")
    out.append("| # | Lab | DMAIC phase | Type |")
    out.append("|---|-----|-------------|------|")
    files = {}
    for a in ACT:
        fn = f"lab-{a['num']:02d}-{slug(a['title'])}.md"
        files[a["num"]] = fn
        kind = "Elective" if a.get("elective") else "Core"
        title = a["title"].replace("Elective — ", "")
        out.append(f"| {a['num']} | [{title}]({fn}) | {TOPICS[a['topic']]['phase']} | {kind} |")
    out.append("")
    out.append("## The interactive toolkit")
    out.append("")
    out.append("See [tools.md](tools.md) for the browser-based problem-solving tools used in the labs.")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out), files


def tools_md():
    out = []
    out.append("# Lean Six Sigma Toolkit")
    out.append("")
    out.append(f"*{C.TITLE} · {C.COURSE_CODE}*")
    out.append("")
    out.append("## Interactive online tools")
    out.append("")
    out.append("These browser-based tools are used during the labs. No installation or licence needed.")
    out.append("")
    out.append("| Tool | What it does | Used in |")
    out.append("|------|--------------|---------|")
    # Which labs use which tool is DERIVED from the lab content, so these
    # references can never drift out of step with the lab numbering.
    def _labs_using(*keywords):
        hits = []
        for a in ACT:
            blob = " ".join([a["title"], a["desc"], a["services"],
                             " ".join(s[0] for s in a["steps"])]).lower()
            if any(k in blob for k in keywords):
                hits.append(a["num"])
        if not hits:
            return "-"
        return ("Lab " if len(hits) == 1 else "Labs ") + ", ".join(str(n) for n in hits)

    five = _labs_using("5 whys", "five whys")
    fish = _labs_using("fishbone", "ishikawa")
    pare = _labs_using("pareto")
    spc = _labs_using("run chart", "control chart", "spc", "process capability")
    out.append(f"| [5 Whys](https://alfredang.github.io/5whys/) | Build and share a 5 Whys root-cause chain | {five} |")
    out.append(f"| [Fishbone Diagram](https://alfredang.github.io/fishbone/) | Build an Ishikawa cause-and-effect diagram | {fish} |")
    out.append(f"| [Pareto Chart](https://alfredang.github.io/paretochart/) | Collaborative session: the team brainstorms and votes, and the Pareto chart builds itself live | {pare} |")
    out.append(f"| [NovaSPC](https://alfredang.github.io/novaspc/) | Run charts, SPC charts (c, u, np, p, X-mR, X̄-R, X̄-s) and process capability from your own CSV | {spc} |")
    out.append("")
    out.append("### Using the collaborative Pareto tool")
    out.append("")
    out.append("1. One team member creates a session and shares the access code.")
    out.append("2. Everyone else joins the session using that code.")
    out.append("3. The team brainstorms candidate causes into the session.")
    out.append("4. Each member votes on the causes that matter most.")
    out.append("5. The live Pareto chart reveals the vital few to act on.")
    out.append("")
    out.append("## Templates you will produce")
    out.append("")
    for a in ACT:
        title = a["title"].replace("Elective — ", "")
        out.append(f"- **Lab {a['num']} — {title}:** {a['build']}")
    out.append("")
    out.append("## Formula quick reference")
    out.append("")
    out.append("| Metric | Formula |")
    out.append("|--------|---------|")
    out.append("| Yield | (Good units / Total units) × 100 |")
    out.append("| DPU | Defects / Units |")
    out.append("| DPO | Defects / (Units × Opportunities per unit) |")
    out.append("| DPMO | DPO × 1,000,000 |")
    out.append("| First Pass Yield (FPY) | Units passing with no rework / Units started |")
    out.append("| Rolled Throughput Yield (RTY) | FPY₁ × FPY₂ × … × FPYₙ |")
    out.append("| Process Cycle Efficiency | Value-added time / Total lead time |")
    out.append("| Takt time | Available working time / Customer demand |")
    out.append("")
    out.append("### Sigma level reference")
    out.append("")
    out.append("| Sigma | DPMO | Yield |")
    out.append("|-------|------|-------|")
    for s, d, y in [("1σ", "690,000", "31%"), ("2σ", "308,000", "69%"), ("3σ", "66,800", "93.3%"),
                    ("4σ", "6,210", "99.38%"), ("5σ", "233", "99.977%"), ("6σ", "3.4", "99.99966%")]:
        out.append(f"| {s} | {d} | {y} |")
    out.append("")
    out.append("## The eight wastes — DOWNTIME")
    out.append("")
    for letter, name, ex in [
        ("D", "Defects", "Wrong ticket category; work that must be redone"),
        ("O", "Overproduction", "Reports nobody reads"),
        ("W", "Waiting", "Tickets sitting in the triage queue"),
        ("N", "Non-utilised talent", "Skilled agents doing routine data entry"),
        ("T", "Transport", "Tickets bouncing between teams"),
        ("I", "Inventory", "A growing backlog of unassigned tickets"),
        ("M", "Motion", "Switching between four systems for one ticket"),
        ("E", "Extra-processing", "Approvals that add no customer value"),
    ]:
        out.append(f"- **{letter} — {name}:** {ex}")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*© 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


# ---------------------------------------------------------------- write
os.makedirs(LABS, exist_ok=True)
for old in glob.glob(os.path.join(LABS, "lab-*.md")):
    os.remove(old)

readme, files = readme_md()
written = 0
for a in ACT:
    path = os.path.join(LABS, files[a["num"]])
    with open(path, "w") as f:
        f.write(lab_md(a))
    written += 1

with open(os.path.join(LABS, "README.md"), "w") as f:
    f.write(readme)
with open(os.path.join(LABS, "tools.md"), "w") as f:
    f.write(tools_md())

core = sum(1 for a in ACT if not a.get("elective"))


# ---------------------------------------------------------------- repo README
def repo_readme(files):
    n = len(ACT)
    out = []
    out.append(f"# {C.COURSE_CODE} - {C.TITLE}")
    out.append("")
    out.append(f"> **Course:** WSQ - {C.TITLE}  ")
    out.append(f"> **Course Code:** {C.COURSE_CODE}  ")
    out.append("> **Register here:** https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html")
    out.append("")
    out.append(f"These are the hands-on lab exercises for the WSQ {C.TITLE} course delivered by "
               "[Tertiary Infotech Academy Pte Ltd](https://www.tertiarycourses.com.sg/).")
    out.append("")
    out.append(f"This repository contains **{n} guided Lean Six Sigma Yellow Belt labs** "
               f"({core} core and {n-core} elective), structured around the **DMAIC roadmap** and grounded in the "
               "Council for Six Sigma Certification (CSSC) Yellow Belt body of knowledge.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Courseware")
    out.append("")
    out.append("| Artifact | File |")
    out.append("|----------|------|")
    # URL-encode spaces/parens so the Markdown links work on GitHub
    def enc(p):
        return p.replace(" ", "%20").replace("(", "%28").replace(")", "%29")
    lg_md = f"LG-{C.SHORT_TITLE}.md"
    out.append(f"| **Slide deck** | `courseware/{C.SHORT_TITLE}-{C.VERSION}.pptx` (and `.pdf`) |")
    out.append(f"| **Learner Guide (Markdown)** | [{lg_md}]({enc(lg_md)}) |")
    out.append(f"| **Learner Guide (DOCX/PDF)** | `courseware/LG-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append(f"| **Lesson Plan (DOCX/PDF)** | `courseware/LP-{C.SHORT_TITLE}.docx` (and `.pdf`) |")
    out.append("| **Lab Index** | [labs/README.md](labs/README.md) |")
    out.append("| **Tools and Templates** | [labs/tools.md](labs/tools.md) |")
    out.append("")
    out.append("> **Note:** assessment papers, answer keys and trainer-only materials are intentionally "
               "not published in this repository.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## How to use")
    out.append("")
    out.append("1. Read the Learner Guide first — it follows the same DMAIC order as the course.")
    out.append("2. Complete the core labs in order using the Northwind Retail Distribution Centre scenario.")
    out.append("3. Complete the elective labs if time allows, or as post-course practice.")
    out.append("4. Keep every worksheet — the final lab combines them into one improvement package.")
    out.append("5. Review the 'Check your work' step at the end of each lab before moving on.")
    out.append("")
    out.append("---")
    out.append("")
    out.append("## Lab catalogue")
    out.append("")
    for t in C.TOPICS:
        acts = [a for a in ACT if a["topic"] == t["num"]]
        if not acts:
            continue
        # t['title'] already leads with the phase name for the DMAIC topics, so
        # don't print it twice ("Define — Define — Scope the Problem").
        heading = t["title"] if t["title"].lower().startswith(t["phase"].lower()) \
            else f"{t['phase'].title()} — {t['title']}"
        out.append(f"### {heading}")
        out.append("")
        for a in acts:
            title = a["title"].replace("Elective — ", "")
            tag = " *(elective)*" if a.get("elective") else ""
            out.append(f"- [Lab {a['num']} - {title}](labs/{files[a['num']]}){tag}")
        out.append("")
    out.append("---")
    out.append("")
    out.append("## Repository structure")
    out.append("")
    out.append("```")
    out.append("courseware/          slide deck (PPTX + PDF), Learner Guide, Lesson Plan")
    out.append("  archive/           superseded deck versions")
    out.append("  assets/            diagrams and images used by the deck")
    out.append("labs/                the 14 lab worksheets + index + toolkit")
    out.append(f"LG-{C.SHORT_TITLE}.md")
    out.append("                     Learner Guide (Markdown mirror of the DOCX)")
    out.append(".claude/skills/courseware-build/build/")
    out.append("                     single-source generators: one content module")
    out.append("                     drives the deck, LP, LG and labs")
    out.append("```")
    out.append("")
    out.append("All artifacts are generated from `course_data.py` + `data_domainN.py`, so the deck, "
               "Lesson Plan, Learner Guide and labs stay 100% aligned.")
    out.append("")
    out.append("## Interactive tools")
    out.append("")
    out.append("- [5 Whys](https://alfredang.github.io/5whys/) — root-cause chain builder")
    out.append("- [Fishbone Diagram](https://alfredang.github.io/fishbone/) — Ishikawa cause-and-effect builder")
    out.append("- [Pareto Chart](https://alfredang.github.io/paretochart/) — collaborative team brainstorm, vote and live chart")
    out.append("- [NovaSPC](https://alfredang.github.io/novaspc/) — run charts, SPC charts and process capability")
    out.append("")
    out.append("## Reference")
    out.append("")
    out.append("- [Council for Six Sigma Certification - Lean Six Sigma Yellow Belt Certification](https://www.sixsigmacouncil.org/lean-six-sigma-yellow-belt-certification/)")
    out.append("- [Course registration page](https://www.tertiarycourses.com.sg/wsq-certified-lean-six-sigma-yellow-belt-clssyb-training.html)")
    out.append("- [labs/tools.md](labs/tools.md) - templates, formulas and free tools used in the labs")
    out.append("")
    out.append("## Free tools used")
    out.append("")
    out.append("- Microsoft Excel, LibreOffice Calc, or Google Sheets")
    out.append("- Draw.io / diagrams.net for SIPOC, process maps and fishbone diagrams")
    out.append("- The interactive tools listed above")
    out.append("- Whiteboard or sticky notes for facilitation activities")
    out.append("")
    out.append("---")
    out.append("")
    out.append(f"*Version {C.VERSION} · {C.VERSION_DATE} · © 2026 {C.ORG}*")
    out.append("")
    return "\n".join(out)


with open(os.path.join(REPO, "README.md"), "w") as f:
    f.write(repo_readme(files))

print(f"Saved {written} lab files to {LABS}  ({core} core, {written-core} elective)")
print("Saved labs/README.md, labs/tools.md and README.md")
