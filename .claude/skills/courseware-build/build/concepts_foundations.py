#!/usr/bin/env python3
"""Foundations teaching slides — Green Belt depth, DMAIC order."""
import os
from pptx.util import Inches, Pt
from components import (BLUE, TEAL, AMBER, RED, VIOLET, INK, GREY, LIGHT, WHITE,
                        LINE, DMAIC_COLORS)

HERE = os.path.dirname(os.path.abspath(__file__))


def _dg(d, name):
    """Resolve a diagram imported from the original trainer deck."""
    import glob
    for p in glob.glob(os.path.join(d.REPO_ASSETS, "diagrams", name + ".*")):
        return p
    return None


def foundations(d):
    d.section("FOUNDATIONS", "Six Sigma Foundations & The Green Belt Role", "00",
              "Quality - Lean - Six Sigma - Y = f(X) - Belt roles - COPQ - Project selection - DMAIC")

    # ---------------- 1. What is quality ----------------
    d.compare_panels(
        "Three Common Answers - Only One Survives",
        [("Defect-free", "The zero-defect answer",
          ["Sounds strong, but defect-free of WHAT?",
           "A part with no scratches can still be late",
           "Says nothing about what the buyer valued",
           "Verdict: incomplete"]),
         ("Meets specification", "The engineering answer",
          ["Better - it is measurable and auditable",
           "But WHO wrote the spec, and from what?",
           "A wrong spec, met perfectly, is still failure",
           "Verdict: necessary, not sufficient"]),
         ("Meets customer expectations", "The Six Sigma answer",
          ["The customer defines what good looks like",
           "The spec is then derived from that voice",
           "Covers delivery, service and cost, not just parts",
           "Verdict: this is the one we use"])],
        kicker="DEFINING QUALITY", accent=BLUE)

    d.tile_grid(
        "Quality in a Nutshell - Four Obligations",
        [("Understand requirements", "Capture what the customer actually needs - Voice of the Customer, not assumption."),
         ("Design to satisfy them", "Translate needs into specific, measurable CTQ requirements the process can be built around."),
         ("Deliver consistently", "Consistency is the hard part - variation, not the average, is what customers feel."),
         ("Improve continuously", "Requirements move. A process that stands still is quietly getting worse.")],
        kicker="THE WORKING DEFINITION", cols=2, accent=BLUE)

    d.big_statement(
        "Northwind Retail Distribution Centre",
        "Our running case for four days: order fulfilment, 12,400 orders a month, promised in 48 hours. "
        "Today 18 per cent arrive late and customers are leaving. Every tool gets applied here.",
        "THE RUNNING SCENARIO", color=TEAL)

    # ---------------- 2. What is Lean ----------------
    d.flow_h(
        "The Five Lean Principles",
        ["Specify VALUE from the customer's point of view - only they can define it",
         "Map the VALUE STREAM - every step, value-add and non-value-add alike",
         "Create FLOW - remove the queues, batches and stoppages between steps",
         "Establish PULL - produce only what the next step actually calls for",
         "Pursue PERFECTION - repeat the cycle; the target keeps moving"],
        kicker="LEAN THINKING - WOMACK & JONES", color=TEAL)

    d.tile_grid(
        "Lean at Northwind - What It Would See",
        [("Waiting", "Picked orders sit 4.2 hours on the staging floor waiting for the carrier sweep."),
         ("Motion", "Fast-moving SKUs stored at the far aisle - pickers walk 11 km per shift."),
         ("Over-processing", "Every order double-checked, including the 92 per cent that were never in doubt."),
         ("Inventory", "Three weeks of packaging stock tying up cash and floor space.")],
        kicker="MUDA - THE ENEMY", cols=2, accent=TEAL)

    # ---------------- 3. What is Six Sigma ----------------
    d.compare_panels(
        "Why Variation - Not the Average - Is the Enemy",
        [("The average lies", "Both DCs average 46 hours",
          ["Northwind: 46 hours average delivery",
           "Southport: 46 hours average delivery",
           "Identical on the monthly report",
           "Completely different customer experience"]),
         ("Northwind", "Average 46 h, spread 28 to 71 h",
          ["18 per cent of orders breach the 48 h promise",
           "Customers cannot plan around it",
           "Expediting cost SGD 340k a year",
           "High variation - low capability"]),
         ("Southport", "Average 46 h, spread 43 to 49 h",
          ["Under 1 per cent breach the promise",
           "Customers trust the date given",
           "Almost no expediting",
           "Low variation - high capability"])],
        kicker="THE CENTRAL INSIGHT", accent=VIOLET)

    # ---------------- 4. Lean Six Sigma ----------------
    d.vs_diagram(
        "Lean + Six Sigma = Lean Six Sigma",
        ("Lean", ["Speed, flow and lead time",
                  "Removes waste and non-value-add steps",
                  "Fast, visual, shop-floor tools",
                  "Weak on statistical proof"]),
        ("Six Sigma", ["Accuracy, capability and variation",
                       "Removes defects and inconsistency",
                       "Rigorous data and statistics",
                       "Can be slow on obvious waste"]),
        ("LEAN SIX SIGMA",
         "Do the right things fast AND right - waste removal with statistical proof, run through DMAIC"),
        kicker="FOUNDATIONS 4 - THE COMBINATION")

    d.tile_grid(
        "When Each Half Does the Heavy Lifting",
        [("Long lead time, few defects", "Lean leads - map the value stream, cut queues and batch sizes."),
         ("Short lead time, many defects", "Six Sigma leads - find the Xs driving variation and control them."),
         ("Both problems at once", "Lean first to expose the real process, then Six Sigma on what remains."),
         ("Neither is clear yet", "Measure first. Never choose the toolkit before you have baseline data.")],
        kicker="CHOOSING YOUR EMPHASIS", cols=2, accent=BLUE)

    # ---------------- 5. History ----------------
    d.timeline(
        "How We Got Here - A Short History",
        [("1920s", "Shewhart at Bell Labs invents the control chart and common vs special cause"),
         ("1950s", "Toyota Production System - Ohno and Shingo build flow, pull and waste removal"),
         ("1986", "Motorola coins Six Sigma - Bill Smith links variation to field failure"),
         ("1995", "GE under Jack Welch scales it enterprise-wide and reports billions in benefit"),
         ("2000s", "Lean and Six Sigma merge into the combined Lean Six Sigma body of knowledge")],
        kicker="FOUNDATIONS 5 - HISTORY", accent=AMBER)

    # ---------------- 6. Y = f(X) ----------------
    d.big_statement(
        "Y = f(X)",
        "The output Y is a function of the process inputs X. You cannot manage Y directly - "
        "you can only find, verify and control the vital few Xs that drive it.",
        "FOUNDATIONS 6 - THE CENTRAL MODEL", color=RED)

    p = _dg(d, "y-fx-model")
    if p:
        d.image_slide("The Y = f(X) Model", p, kicker="THE CENTRAL MODEL",
                      caption="Y is the dependent output the customer feels; the Xs are the independent inputs you control.",
                      accent=RED)

    d.two_col(
        "Y and X at Northwind",
        [("Y = order delivered within 48 hours", 0),
         ("Dependent - it is an OUTCOME", 1),
         ("Measured after the fact", 1),
         ("Cannot be changed by instruction", 1),
         ("Shouting at the Y does nothing", 1),
         ("This is what the customer feels", 1)],
        [("Candidate Xs driving that Y", 0),
         ("Pick path length and pick errors", 1),
         ("Carrier sweep schedule and cut-off time", 1),
         ("Order-entry accuracy at the front end", 1),
         ("Stock accuracy in the pick face", 1),
         ("Shift staffing versus order arrival profile", 1)],
        kicker="APPLYING Y = f(X)", lhead="THE Y - OUTPUT", rhead="THE Xs - INPUTS",
        lcolor=RED, rcolor=BLUE)

    d.tile_grid(
        "Three Kinds of X - Know Which You Have",
        [("Controllable X", "You can set it and hold it - cut-off time, slot layout, batch size. This is where solutions live."),
         ("Noise X", "Real but not economically controllable - weather, traffic, customer order mix. Design robustness against it."),
         ("Critical X", "A controllable X that is statistically proven to move Y. The vital few you will control in phase C.")],
        kicker="CLASSIFYING INPUTS", cols=1, accent=RED)

    # ---------------- 7. Classical vs Six Sigma quality ----------------
    p = _dg(d, "classical-vs-six-sigma")
    if p:
        d.image_slide("Classical Quality vs Six Sigma Quality", p, kicker="TWO PHILOSOPHIES",
                      caption="Left - inspect and sort after the fact. Right - understand and control the Xs before the defect exists.",
                      accent=AMBER)

    d.compare_panels(
        "Classical vs Six Sigma - Side by Side",
        [("Classical Quality", "Detection and containment",
          ["Inspect the output, sort good from bad",
           "Goal is conformance to specification",
           "Defect cost is treated as unavoidable",
           "Quality owned by the QA department",
           "Reacts to the symptom"]),
         ("Six Sigma Quality", "Prevention and variation reduction",
          ["Study the process, control the Xs",
           "Goal is reduced variation around target",
           "Defect cost is treated as recoverable waste",
           "Quality owned by the process owner",
           "Removes the root cause"])],
        kicker="PHILOSOPHY SHIFT", accent=AMBER)

    p = _dg(d, "focus-of-six-sigma")
    if p:
        d.image_slide("The Focus of Six Sigma", p, kicker="WHAT WE ACTUALLY WORK ON",
                      caption="Move the mean onto target AND shrink the spread - both are required for capability.",
                      accent=VIOLET)

    # ---------------- 8. Sigma level and DPMO ----------------
    d.ladder(
        "Sigma Level to DPMO - The Verified Table",
        [("1 sigma", "690,000 DPMO\n69% defective\nnot a business"),
         ("2 sigma", "308,000 DPMO\n30.8% defective\nchronic firefighting"),
         ("3 sigma", "66,800 DPMO\n6.7% defective\ntypical company today"),
         ("4 sigma", "6,210 DPMO\n0.62% defective\ngood performer"),
         ("5 sigma", "233 DPMO\n0.023% defective\nindustry leader"),
         ("6 sigma", "3.4 DPMO\nworld class\nthe goal")],
        kicker="THE CONVERSION TABLE", accent=VIOLET,
        note="Most organisations run between 3 and 4 sigma. Each step up is roughly a ten-fold cut in defects.")

    d.tile_grid(
        "Why 3.4 and Not 2 Per Billion - The 1.5 Sigma Shift",
        [("The short-term picture", "A perfectly centred process with six sigma between mean and spec gives about 2 defects per BILLION."),
         ("Processes drift", "Over weeks and months the mean wanders - tool wear, staff changes, supplier lots, seasonality."),
         ("Motorola's allowance", "Empirically that long-term drift is about 1.5 sigma, so the effective margin is 4.5 sigma."),
         ("The result", "4.5 sigma in the tail gives 3.4 DPMO. That is why six sigma means 3.4, not 0.002.")],
        kicker="THE LONG-TERM SHIFT", cols=2, accent=VIOLET)

    p = _dg(d, "sigma-shift")
    if p:
        d.image_slide("The 1.5 Sigma Long-Term Shift", p, kicker="SHORT TERM VS LONG TERM",
                      caption="Short-term capability is measured over a snapshot; long-term performance absorbs the drift.",
                      accent=VIOLET)

    p = _dg(d, "six-sigma-std-dev")
    if p:
        d.image_slide("Six Standard Deviations Between Mean and Spec", p, kicker="WHAT 'SIX SIGMA' LITERALLY MEANS",
                      caption="The name is geometric - six standard deviations must fit between the process mean and the nearest limit.",
                      accent=VIOLET)

    p = _dg(d, "six-sigma-capability")
    if p:
        d.image_slide("Process Capability at Different Sigma Levels", p, kicker="CAPABILITY COMPARED",
                      caption="Same spec limits, different spreads - capability is the ratio of customer tolerance to process voice.",
                      accent=VIOLET)

    # ---------------- 9. COPQ ----------------
    p = _dg(d, "copq-iceberg")
    if p:
        d.image_slide("The COPQ Iceberg", p, kicker="VISIBLE VS HIDDEN COST",
                      caption="What accounting reports is the tip. The submerged costs are larger and rarely on anyone's ledger.",
                      accent=RED)

    d.compare_panels(
        "Above the Waterline and Below It",
        [("Visible COPQ", "Measured, budgeted, argued over",
          ["Scrap and written-off stock",
           "Rework and re-picking",
           "Warranty and credit notes",
           "Returns processing and freight",
           "Inspection and sorting labour"]),
         ("Hidden COPQ", "Real money, no cost code",
          ["Lost customers and lost future orders",
           "Expediting and premium freight",
           "Overtime to recover the schedule",
           "Excess inventory held as a safety net",
           "Damaged reputation and lost bids"])],
        kicker="THE TWO HALVES", accent=RED)

    d.tile_grid(
        "COPQ at Northwind - Building the Business Case",
        [("Expedited freight", "SGD 340,000 a year in premium carrier charges to rescue late orders."),
         ("Service credits", "SGD 185,000 in contractual late-delivery credits issued to key accounts."),
         ("Recovery overtime", "SGD 96,000 in weekend shifts run purely to clear the late backlog."),
         ("Churned accounts", "Two accounts lost last year - SGD 1.2m of annual revenue, entirely hidden.")],
        kicker="MAKING IT CONCRETE", cols=2, accent=RED)

    # ---------------- 10. Belt roles ----------------
    d.ladder(
        "The Six Sigma Belt Pathway",
        [("White Belt", "Awareness only\nunderstands the vocabulary\nsupports as a team member"),
         ("Yellow Belt", "Team member\ncollects data, maps process\ndoes not lead projects"),
         ("GREEN BELT", "Leads scoped projects\npart-time, own function\nowns the analysis"),
         ("Black Belt", "Full-time practitioner\ncross-functional projects\ncoaches Green Belts"),
         ("Master Black Belt", "Deployment leader\ntrains and certifies belts\nowns the programme")],
        kicker="THE PATHWAY", accent=TEAL,
        note="Alongside the belts sit the Champion and Sponsor - executives who select projects, fund them and remove barriers.")

    d.two_col(
        "Green Belt vs Yellow Belt - Be Precise",
        [("A Yellow Belt", 0),
         ("Contributes to someone else's project", 1),
         ("Collects data as instructed", 1),
         ("Helps build the process map", 1),
         ("Uses basic tools - checksheet, Pareto", 1),
         ("Does not own the charter or the analysis", 1),
         ("Does not face the tollgate panel", 1)],
        [("A GREEN BELT", 0),
         ("LEADS a scoped DMAIC project end to end", 1),
         ("Owns the charter, scope and problem statement", 1),
         ("OWNS the statistical analysis - MSA, capability, hypothesis tests", 1),
         ("RUNS the tollgate reviews with the Champion", 1),
         ("Selects and defends the vital few Xs", 1),
         ("Hands over a control plan to the process owner", 1)],
        kicker="THE THREE THINGS THAT DIFFER", lhead="YELLOW BELT", rhead="GREEN BELT",
        lcolor=AMBER, rcolor=TEAL)

    p = _dg(d, "belt-roles")
    if p:
        d.image_slide("Six Sigma Roles and Responsibilities", p, kicker="WHO DOES WHAT",
                      caption="Champion selects and funds; Black Belt coaches; Green Belt delivers; process owner sustains.",
                      accent=TEAL)

    d.tile_grid(
        "The Non-Belt Roles You Must Work With",
        [("Champion", "Senior leader who selects the project, approves the charter and clears organisational barriers."),
         ("Sponsor", "Owns the business area and the benefit. Signs off the financial validation with Finance."),
         ("Process Owner", "Runs the process day to day and inherits your control plan. Must be on the team from day one."),
         ("Finance Representative", "Independently validates claimed savings. Without their sign-off the benefit is an opinion.")],
        kicker="THE SUPPORTING CAST", cols=2, accent=BLUE)

    # ---------------- 11. Project selection ----------------
    d.tile_grid(
        "Traits of a Good Green Belt Project",
        [("Clear, measurable Y", "The output can be counted or timed today - no new measurement system required first."),
         ("Cause is genuinely unknown", "If everyone already knows the fix, do not run DMAIC. Just do it."),
         ("Scoped to weeks, not years", "One process, one site, one product family. 3 to 6 months of part-time effort."),
         ("Real, quantified pain", "A COPQ or customer number attached. If you cannot size it, you cannot defend it."),
         ("Data is available", "Historical data exists or can be collected inside the project timeline."),
         ("Willing process owner", "Someone will inherit the controls. No owner means no sustained gain.")],
        kicker="SELECTION CRITERIA", cols=2, accent=AMBER)

    d.matrix2x2(
        "Prioritising Candidates - Impact vs Effort",
        "EFFORT / DIFFICULTY  (low on the left, high on the right)",
        "IMPACT",
        [("Quick wins - DO NOW", "High impact, low effort. Take these immediately, often without a full DMAIC. Build credibility early."),
         ("Major projects - PLAN", "High impact, high effort. The proper home of a Green Belt DMAIC project. Charter it properly."),
         ("Fill-ins - MAYBE LATER", "Low impact, low effort. Fine as team practice, but do not build a programme on them."),
         ("Thankless tasks - AVOID", "Low impact, high effort. Politely decline. This is where Green Belt projects go to die.")],
        kicker="THE PRIORITISATION MATRIX", accent=AMBER)

    p = _dg(d, "cause-solution-matrix")
    if p:
        d.image_slide("The Cause and Solution Matrix", p, kicker="CHOOSING THE RIGHT METHOD",
                      caption="Ask two questions first - do we know the cause, and do we know the solution?",
                      accent=BLUE)

    # ---------------- 12. Baseline, entitlement, benchmark ----------------
    d.tile_grid(
        "The Three Reference Points",
        [("Baseline", "What the process delivers TODAY, measured over a representative period. Northwind: 82 per cent on time."),
         ("Entitlement", "The best the CURRENT process has ever sustained, with no new investment. Northwind: 91 per cent in March."),
         ("Benchmark", "The best anyone achieves - internal sister site or external competitor. Southport DC: 98 per cent.")],
        kicker="DEFINITIONS", cols=1, accent=TEAL)

    d.content(
        "Using Them to Set the Goal",
        ["Baseline tells you where you start - it must come from data, never from memory or opinion.",
         "Entitlement proves the target is achievable, because the process has already hit it at least once.",
         "The gap from baseline to entitlement is normally pure variation - exactly what DMAIC removes.",
         "Beyond entitlement usually needs capital or redesign, which is a different project and a different budget.",
         "A Green Belt goal that lands between baseline and entitlement is credible; beyond benchmark is fantasy."],
        kicker="TARGET SETTING", size=18)

    # ---------------- 13. DMAIC roadmap ----------------
    d.dmaic_wheel(
        "The DMAIC Roadmap and Its Deliverables",
        [("D", "Define", ["Project charter", "SIPOC map", "Voice of Customer", "CTQ tree", "Scoped problem statement"]),
         ("M", "Measure", ["Detailed process map", "Data collection plan", "MSA / Gage R&R", "Baseline capability", "Baseline sigma level"]),
         ("A", "Analyse", ["Value stream analysis", "Fishbone and 5 Whys", "Pareto of causes", "Hypothesis tests", "Verified vital few Xs"]),
         ("I", "Improve", ["Solution generation", "Prioritised solutions", "Pilot and FMEA", "Piloted results", "Implementation plan"]),
         ("C", "Control", ["Control plan", "Control charts", "SOPs and training", "Handover to owner", "Financial validation"])],
        kicker="THE FIVE PHASES")

    d.flow_h(
        "The Five Tollgate Reviews",
        ["DEFINE gate - is the problem real, scoped and worth solving?",
         "MEASURE gate - is the data trustworthy and the baseline agreed?",
         "ANALYSE gate - are the vital few Xs proven, not just suspected?",
         "IMPROVE gate - has the solution been piloted and the risk assessed?",
         "CONTROL gate - is the gain held, and has Finance validated it?"],
        kicker="GOVERNANCE", color=BLUE, colors=DMAIC_COLORS)

    p = _dg(d, "dmaic-cycle")
    if p:
        d.image_slide("The DMAIC Cycle", p, kicker="THE IMPROVEMENT ENGINE",
                      caption="DMAIC is a closed loop - Control feeds the next Define, which is how continuous improvement is sustained.",
                      accent=BLUE)

    # ---------------- 14. DMAIC vs PDCA vs DFSS ----------------
    d.compare_panels(
        "DMAIC vs PDCA vs DFSS - When to Use Which",
        [("PDCA", "Plan - Do - Check - Act",
          ["For small, fast, local improvements",
           "Cause is largely understood already",
           "Days to weeks, minimal data",
           "No formal tollgates or charter",
           "The engine of daily kaizen"]),
         ("DMAIC", "Define - Measure - Analyse - Improve - Control",
          ["For an EXISTING process that underperforms",
           "Cause is unknown and must be proven",
           "3 to 6 months, data and statistics",
           "Formal charter and five tollgates",
           "The Green Belt default"]),
         ("DFSS / DMADV", "Define - Measure - Analyse - Design - Verify",
          ["For a NEW process, product or service",
           "Or when DMAIC hits entitlement and stops",
           "Longest and most expensive route",
           "Requires design and capital authority",
           "Usually Black Belt or above"])],
        kicker="FOUNDATIONS 14 - CHOOSING THE METHOD", accent=VIOLET)

    # ---------------- checkpoint ----------------
    d.checkpoint(
        "Checkpoint - Foundations",
        ["Who ultimately defines quality, and why do the other two answers fail?",
         "State Y = f(X) in your own words. Why can a manager not manage Y directly?",
         "What is the DPMO at 3 sigma and at 6 sigma, and why is six sigma 3.4 rather than 0.002?",
         "Name three things a Green Belt does that a Yellow Belt does not.",
         "Cause unknown, solution unknown - which method, and why not Just Do It?",
         "Define baseline, entitlement and benchmark using the Northwind numbers."],
        kicker="RECAP - FOUNDATIONS")
