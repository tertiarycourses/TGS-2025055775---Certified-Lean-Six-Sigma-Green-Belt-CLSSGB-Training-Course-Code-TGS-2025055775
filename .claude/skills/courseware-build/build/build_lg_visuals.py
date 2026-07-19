#!/usr/bin/env python3
"""Generate one Learner-Guide visual per lab, into courseware/assets/lg-visuals/.

Each visual is DERIVED FROM THE LAB DATA (data_domainN.py) — the lab number,
title, DMAIC phase, the deliverable and the step list — so a visual can never
describe a lab that no longer exists or has been renumbered. Re-run this whenever
the labs change; build_learner_guide.py embeds whatever it finds here.

Output per lab N:  lab-NN-visual.png   a "what you will build" card showing the
                                       phase, deliverable, tools and the steps.
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

ACT = sorted(DOMAIN1 + DOMAIN2 + DOMAIN3 + DOMAIN4 + DOMAIN5, key=lambda a: a["num"])
TOPICS = {t["num"]: t for t in C.TOPICS}

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch, Rectangle

BLUE = "#1F6FEB"; TEAL = "#10B981"; VIOLET = "#8B5CF6"
AMBER = "#F59E0B"; RED = "#EF4444"
INK = "#111827"; GREY = "#555B66"; LIGHT = "#F3F5F8"; LINE = "#D8DEE9"

PHASE_COLOR = {
    "FOUNDATIONS": BLUE, "DEFINE": BLUE, "MEASURE": TEAL,
    "ANALYZE": VIOLET, "IMPROVE": AMBER, "CONTROL": RED,
}


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
OUT = os.path.join(REPO, "courseware", "assets", "lg-visuals")
os.makedirs(OUT, exist_ok=True)


def wrap(text, width):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if len(t) <= width:
            cur = t
        else:
            lines.append(cur); cur = w
    if cur:
        lines.append(cur)
    return lines


def card(ax, x, y, w, h, fill=LIGHT, edge=None, lw=1.0):
    ax.add_patch(FancyBboxPatch((x, y), w, h,
                                boxstyle="round,pad=0.0,rounding_size=0.06",
                                linewidth=lw, edgecolor=edge or LINE,
                                facecolor=fill, mutation_aspect=0.55))


def build(a):
    phase = TOPICS[a["topic"]]["phase"]
    col = PHASE_COLOR.get(phase, BLUE)
    steps = a["steps"]

    fig = plt.figure(figsize=(11.0, 5.6), dpi=170)
    ax = fig.add_axes([0, 0, 1, 1]); ax.axis("off")
    ax.set_xlim(0, 11); ax.set_ylim(0, 5.6)
    ax.add_patch(Rectangle((0, 0), 11, 5.6, facecolor="white", edgecolor="none"))

    # accent bar + kicker + title
    ax.add_patch(Rectangle((0.42, 4.72), 0.075, 0.62, facecolor=col, edgecolor="none"))
    ax.text(0.63, 5.22, f"LAB {a['num']}  ·  {phase}", color=col,
            fontsize=10.5, fontweight="bold", va="center")
    tl = wrap(a["title"].replace("Elective — ", ""), 56)[:2]
    ax.text(0.63, 4.86 if len(tl) == 1 else 4.94, tl[0], color=INK,
            fontsize=17, fontweight="bold", va="center")
    if len(tl) > 1:
        ax.text(0.63, 4.60, tl[1], color=INK, fontsize=17, fontweight="bold", va="center")
    ax.plot([0.42, 10.58], [4.40, 4.40], color=LINE, lw=1.2)

    # ---- left: what you will build + tools
    card(ax, 0.42, 2.42, 4.55, 1.80, fill=LIGHT, edge=LINE)
    ax.add_patch(Rectangle((0.42, 2.42), 0.06, 1.80, facecolor=col, edgecolor="none"))
    ax.text(0.68, 4.02, "YOU WILL BUILD", color=col, fontsize=9, fontweight="bold", va="center")
    for i, ln in enumerate(wrap(a["build"], 44)[:4]):
        ax.text(0.68, 3.74 - i * 0.30, ln, color=INK, fontsize=10.5, va="center")

    card(ax, 0.42, 0.52, 4.55, 1.72, fill="white", edge=LINE)
    ax.text(0.68, 2.02, "TOOLS & TECHNIQUES", color=GREY, fontsize=9, fontweight="bold", va="center")
    for i, ln in enumerate(wrap(a["services"], 46)[:4]):
        ax.text(0.68, 1.72 - i * 0.30, ln, color=GREY, fontsize=10, va="center")

    # ---- right: the step ladder
    card(ax, 5.22, 0.52, 5.36, 3.70, fill="white", edge=LINE)
    ax.text(5.46, 4.02, f"STEPS  ({len(steps)})", color=col, fontsize=9,
            fontweight="bold", va="center")
    show = steps[:7]
    top = 3.66
    gap = 0.40
    for i, (instr, _cmd) in enumerate(show):
        y = top - i * gap
        ax.add_patch(plt.Circle((5.62, y), 0.115, color=col, zorder=3))
        ax.text(5.62, y, str(i + 1), color="white", fontsize=7.6, fontweight="bold",
                ha="center", va="center", zorder=4)
        txt = wrap(instr, 60)[0]
        if len(instr) > len(txt):
            txt = txt.rstrip(" ,.;") + "…"
        ax.text(5.86, y, txt, color=INK, fontsize=9.2, va="center")
    if len(steps) > len(show):
        ax.text(5.86, top - len(show) * gap, f"+ {len(steps) - len(show)} more steps — see the guide",
                color=GREY, fontsize=9, style="italic", va="center")

    ax.text(0.42, 0.22, f"{C.TITLE}  ·  {C.COURSE_CODE}  ·  Version {C.VERSION}",
            color=GREY, fontsize=7.6, va="center")

    fn = os.path.join(OUT, f"lab-{a['num']:02d}-visual.png")
    fig.savefig(fn, facecolor="white")
    plt.close(fig)
    return fn


if __name__ == "__main__":
    made = [build(a) for a in ACT]
    print(f"Saved {len(made)} lab visuals to {OUT}")
