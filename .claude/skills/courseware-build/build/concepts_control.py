#!/usr/bin/env python3
"""Control teaching slides — Green Belt depth, DMAIC order."""
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


def control_phase(d):
    K = "CONTROL"

    # ================= A. CONTROL FOUNDATIONS =================
    d.tile_grid("What the Control phase delivers", [
        ("A live control plan", "Every CTQ metric with its owner, sample plan, limits and reaction plan"),
        ("Control charts in use", "The process monitored on the floor, not in a monthly report"),
        ("Updated SOPs and training", "The new way of working written down and taught to every shift"),
        ("Verified capability", "Re-measured Cp and Cpk proving the gain is real and statistically significant"),
        ("Finance-validated benefit", "Savings signed off so the business recognises the money"),
        ("Formal handover and closure", "Process owner accepts, lessons captured, replication identified"),
    ], kicker=K, cols=2, accent=RED)

    p = _dg(d, "control-steps")
    if p:
        d.image_slide("Steps of the Control phase", p, kicker=K,
                      caption="Control moves from monitoring the improved process, to documenting it, "
                              "to handing it over with a named owner.",
                      accent=RED)

    d.compare_panels("Why gains evaporate - and the antidote", [
        ("The drift", "What happens with no Control phase", [
            "Nobody owns the metric after the team disbands",
            "Nobody knows what to do when it goes out of limits",
            "The SOP still describes the old process",
            "New starters are trained by the person next to them",
            "Six months later the baseline is back",
        ]),
        ("The antidote", "What Control installs", [
            "One named owner per CTQ metric",
            "A written reaction plan triggered by the chart",
            "SOPs rewritten and version controlled",
            "Training plan plus a scheduled audit",
            "A daily huddle at a visible board",
        ]),
    ], kicker=K, accent=RED)

    # ================= B. PROCESS CAPABILITY =================
    d.compare_panels("Process CONTROL vs process CAPABILITY", [
        ("In control", "Stable - the voice of the process", [
            "Variation is predictable over time",
            "Only common cause variation is present",
            "No signals on the control chart",
            "Says nothing about the customer spec",
            "You can forecast it - you may still fail it",
        ]),
        ("Capable", "Stable AND on target for the customer", [
            "Low variation AND centred on the requirement",
            "Output fits comfortably inside the spec limits",
            "Measured by Cp and Cpk",
            "Requires control first - it is a precondition",
            "This is what the customer actually feels",
        ]),
    ], kicker=K, accent=VIOLET)

    p = _dg(d, "accuracy-precision")
    if p:
        d.image_slide("Accuracy vs precision - the target analogy", p, kicker=K,
                      caption="Think of shots at a target: where the group sits is accuracy, "
                              "how tight the group is is precision.",
                      accent=BLUE)

    p = _dg(d, "normal-distribution")
    if p:
        d.image_slide("Capability is the curve inside the spec limits", p, kicker=K,
                      caption="Capability asks a simple question: how much of this distribution "
                              "falls between LSL and USL?",
                      accent=VIOLET)

    p = _dg(d, "cp-formula")
    if p:
        d.image_slide("The Cp formula", p, kicker=K,
                      caption="Cp = (USL - LSL) / 6s - specification width divided by process spread.",
                      accent=VIOLET)

    d.formula_card("Cp - specification width over process spread", [
        ("Cp", "Cp = (USL - LSL) / 6s", "Specification width divided by process spread"),
        ("Northwind", "Cp = 48 / (6 x 6)", "USL = 48 hrs, LSL = 0 hrs, s = 6 hrs -> Cp = 48 / 36 = 1.33"),
        ("Reading it", "Cp >= 1  ->  potentially capable", "Below 1 the spread alone guarantees defects"),
    ], kicker=K, accent=VIOLET,
        note="Cp >= 1 means POTENTIALLY capable - the spread would fit, IF the process were centred.")

    p = _dg(d, "cpk-formula")
    if p:
        d.image_slide("The Cpk formula", p, kicker=K,
                      caption="Cpk uses the distance from the mean to the NEAREST spec limit - "
                              "so it exposes an off-centre process that Cp would pass.",
                      accent=TEAL)

    d.compare_panels("Diagnosing with Cp and Cpk together", [
        ("Cp good, Cpk good", "Narrow and centred", [
            "Spread fits the spec and sits on target",
            "The process is genuinely capable",
            "Action: hold the gain with SPC",
        ]),
        ("Cp good, Cpk poor", "Narrow but off-centre", [
            "The spread is fine - the process is OFF-CENTRE",
            "Do NOT launch a variation reduction project",
            "Action: shift the mean back onto target",
        ]),
        ("Cp poor", "Too much spread", [
            "The spread alone will not fit inside the spec",
            "Centring cannot rescue it",
            "Action: reduce variation before centring",
        ]),
    ], kicker=K, accent=TEAL)

    d.big_statement(
        "Cpk of 1.33 is the usual minimum",
        "Cpk 1.33 is about a 4 sigma process and the usual minimum for customer "
        "satisfaction. Many organisations target 2.0, with 1.5 acceptable.",
        K, color=AMBER)

    p = _dg(d, "capability-ratios")
    if p:
        d.image_slide("Capability ratio thresholds", p, kicker=K,
                      caption="Read the ratio against the threshold your customer or industry demands - "
                              "automotive and medical typically demand more.",
                      accent=AMBER)

    p = _dg(d, "capability-sigma-map")
    if p:
        d.image_slide("Mapping capability ratios to sigma level", p, kicker=K,
                      caption="Capability ratio and sigma level are two views of the same thing: "
                              "how many standard deviations fit between the mean and the spec.",
                      accent=AMBER)

    d.ladder("Capability thresholds a Green Belt should know", [
        ("Cpk < 1.0", "Process spread exceeds the spec - defects are guaranteed"),
        ("Cpk = 1.0", "Spec limits sit exactly at 3 sigma - marginal, no safety margin"),
        ("Cpk = 1.33", "About 4 sigma - the usual minimum for customer satisfaction"),
        ("Cpk = 1.50", "Minimum acceptable in many organisations - a real safety margin"),
        ("Cpk = 2.00", "Six sigma performance - the common corporate target"),
    ], kicker=K, accent=AMBER,
        note="Northwind's Cp of 1.33 is only POTENTIAL capability - check Cpk before claiming success.")

    d.big_statement(
        "Never plot spec limits on a control chart",
        "Control limits come from the PROCESS - the voice of the process. Spec limits come "
        "from the CUSTOMER. Mixing them makes both meaningless.",
        K, color=RED)

    d.compare_panels("Control limits vs specification limits", [
        ("Control limits", "The voice of the PROCESS", [
            "Calculated from the process data itself",
            "Sit at +/- 3 standard deviations from the centre line",
            "Tell you whether the process is stable",
            "Move when the process genuinely changes",
            "Belong on the control chart",
        ]),
        ("Specification limits", "The voice of the CUSTOMER", [
            "Set by the customer, contract or regulation",
            "Have nothing to do with process variation",
            "Tell you whether output is acceptable",
            "Change only when the requirement changes",
            "Belong on a capability histogram, NEVER on the chart",
        ]),
    ], kicker=K, accent=RED)

    d.tile_grid("Why mixing them is dangerous", [
        ("You stop reacting to signals", "If spec limits are wider, real out-of-control points sit inside them and get ignored"),
        ("You over-react to noise", "If spec limits are tighter, you chase common cause variation and make things worse"),
        ("You cannot judge stability", "Stability is a property of the process only - the customer's opinion is irrelevant to it"),
        ("You cannot judge capability", "Capability compares the process spread to the spec - two separate charts, two questions"),
    ], kicker=K, cols=2, accent=RED)

    # ================= C. STATISTICAL PROCESS CONTROL =================
    p = _dg(d, "control-charts-intro")
    if p:
        d.image_slide("What a control chart is", p, kicker=K,
                      caption="A control chart is a run chart with statistically calculated limits, "
                              "so a signal can be distinguished from noise.",
                      accent=BLUE)

    p = _dg(d, "spc-chart-in-control")
    if p:
        d.image_slide("Anatomy of a control chart in control", p, kicker=K,
                      caption="Centre line at the process average, UCL and LCL at +/- 3 standard "
                              "deviations, with the space between divided into zones.",
                      accent=BLUE)

    d.tile_grid("The parts of a control chart", [
        ("Centre line (CL)", "The process average - the level the process is currently running at"),
        ("UCL and LCL", "Upper and lower control limits at +/- 3 standard deviations from the centre line"),
        ("Zone C", "Within 1 sigma of the centre line - where most points should fall"),
        ("Zone B", "Between 1 and 2 sigma from the centre line - either side"),
        ("Zone A", "Between 2 and 3 sigma from the centre line - the outer band before the limits"),
        ("The time axis", "Points plotted in the order produced - sequence is the whole point"),
    ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "control-chart-selection")
    if p:
        d.image_slide("The control chart selection decision tree", p, kicker=K,
                      caption="Start with the data type, then the subgroup size or what you are counting.",
                      accent=TEAL)

    d.flow_h("How to select a control chart", [
        "Is the data CONTINUOUS (measured) or DISCRETE (counted)?",
        "If continuous: can it be sensibly subgrouped, and what is the subgroup size?",
        "If discrete: are you counting DEFECTIVE UNITS or DEFECTS?",
        "For discrete: is the sample size CONSTANT or does it VARY?",
        "Select the chart, then calculate limits from at least 20-25 subgroups",
    ], kicker=K, color=TEAL)

    d.tile_grid("CONTINUOUS (variable) data - three charts", [
        ("I-MR chart", "Individuals and Moving Range - use when the data cannot be sensibly subgrouped"),
        ("Xbar-R chart", "Subgroups with size UNDER 8 - plots the subgroup mean and the subgroup range"),
        ("Xbar-S chart", "Subgroups with size 8 OR MORE - plots the subgroup mean and standard deviation"),
        ("Why the split at 8", "With larger subgroups the standard deviation estimates spread better than the range"),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("DISCRETE data - what are you counting?", [
        ("Defective UNITS, size VARIES", "p-chart - the proportion of units that are defective in each sample"),
        ("Defective UNITS, size CONSTANT", "np-chart - the raw number of defective units per constant-size sample"),
        ("Counts of DEFECTS, size VARIES", "u-chart - defects per unit, where sample size changes between samples"),
        ("Counts of DEFECTS, size CONSTANT", "c-chart - the raw count of defects per constant-size sample"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.compare_panels("Defective units vs defects - what decides the chart", [
        ("Defective UNITS", "Pass or fail per unit", [
            "One unit is either defective or it is not",
            "Northwind: an order is late or on time",
            "Sample size varies  ->  p-chart",
            "Sample size constant  ->  np-chart",
        ]),
        ("Counts of DEFECTS", "A unit can carry several", [
            "One unit can have many defects at once",
            "Northwind: errors found on one shipment",
            "Sample size varies  ->  u-chart",
            "Sample size constant  ->  c-chart",
        ]),
    ], kicker=K, accent=VIOLET)

    p = _dg(d, "xbar-r-chart")
    if p:
        d.image_slide("Xbar-R chart - continuous data in small subgroups", p, kicker=K,
                      caption="Two charts read together: the Xbar chart tracks the subgroup average, "
                              "the R chart tracks the within-subgroup spread.",
                      accent=TEAL)

    p = _dg(d, "p-chart")
    if p:
        d.image_slide("p-chart - proportion defective, varying sample size", p, kicker=K,
                      caption="Northwind's natural chart for late orders: the proportion late each day, "
                              "with limits that widen when the daily volume is low.",
                      accent=VIOLET)

    p = _dg(d, "u-chart")
    if p:
        d.image_slide("u-chart - defects per unit with varying sample size", p, kicker=K,
                      caption="Use when one unit can carry several defects - for example picking errors "
                              "per shipment across days of differing volume.",
                      accent=VIOLET)

    p = _dg(d, "control-limits-calc")
    if p:
        d.image_slide("Calculating the control limits", p, kicker=K,
                      caption="Centre line = the process average. UCL and LCL sit 3 standard deviations "
                              "either side of it.",
                      accent=BLUE)

    d.formula_card("Control limits at +/- 3 standard deviations", [
        ("Centre line", "CL = process average", "The mean of all the plotted subgroup values"),
        ("Upper limit", "UCL = CL + 3 x sigma", "Three standard deviations above the centre line"),
        ("Lower limit", "LCL = CL - 3 x sigma", "Three standard deviations below the centre line"),
    ], kicker=K, accent=BLUE,
        note="Use at least 20-25 subgroups so the limits are stable, and recalculate only when the process genuinely changes.")

    d.big_statement(
        "Eight rules turn a chart into a signal",
        "A point outside the limits is only rule 1. Seven more patterns show the process "
        "changed even when every point sits inside the limits.",
        K, color=RED)

    p = _dg(d, "spc-out-of-control")
    if p:
        d.image_slide("The out-of-control patterns", p, kicker=K,
                      caption="Each pattern has a statistical meaning - learn to read the shape, "
                              "not just the last point.",
                      accent=RED)

    d.tile_grid("The eight out-of-control rules (1 to 4)", [
        ("Rule 1 - one point beyond a limit", "A single point outside UCL or LCL. Act immediately - the chance of this at random is about 3 in 1,000."),
        ("Rule 2 - nine points one side", "Nine points in a row on one side of the centre line - the process level has shifted."),
        ("Rule 3 - six points trending", "Six points in a row steadily increasing or decreasing - a trend, such as tool wear or fatigue."),
        ("Rule 4 - fourteen alternating", "Fourteen points alternating up and down - often over-correction, or variation between machines or shifts."),
    ], kicker=K, cols=1, accent=RED)

    d.tile_grid("The eight out-of-control rules (5 to 8)", [
        ("Rule 5 - two of three in zone A", "Two out of three points in a row in zone A or beyond - a special cause creating sudden high variation."),
        ("Rule 6 - four of five in zone B", "Four out of five points in a row in zone B or beyond - a shift or a major causation problem."),
        ("Rule 7 - fifteen in zone C", "Fifteen points in a row within zone C - limits may be stale; recalculate if variation genuinely improved."),
        ("Rule 8 - eight with none in zone C", "Eight points in a row either side, NONE in zone C - you may be measuring two processes as one."),
    ], kicker=K, cols=1, accent=RED)

    d.flow_h("Responding to an out-of-control signal", [
        "Confirm the signal is real - check the measurement and the data entry first",
        "Contain: protect the customer from any product or service already affected",
        "Investigate the assignable cause at the gemba, while the trail is fresh",
        "Remove the cause and record it on the chart annotation and the reaction log",
        "Recalculate limits only if the process itself permanently changed",
    ], kicker=K, color=AMBER)

    d.compare_panels("Common vs special cause - two responses", [
        ("Common cause", "The process behaving normally", [
            "Random variation inherent in the design",
            "Every point inside the limits, no pattern",
            "Wrong response: adjust after each point",
            "Right response: change the process design",
            "Requires management action, not operator action",
        ]),
        ("Special cause", "Something new has entered", [
            "A signal under one of the eight rules",
            "Assignable to a specific event or condition",
            "Wrong response: ignore it as noise",
            "Right response: investigate and remove it",
            "Usually actionable locally, at the process",
        ]),
    ], kicker=K, accent=AMBER)

    # ================= D. SUSTAINING THE GAIN =================
    p = _dg(d, "control-plan-format")
    if p:
        d.image_slide("The control plan format", p, kicker=K,
                      caption="Every row is one CTQ metric, carried across to a named owner "
                              "and a written reaction plan.",
                      accent=TEAL)

    d.tile_grid("The eight columns of a control plan", [
        ("Process step", "Which step in the improved process this control sits on"),
        ("CTQ metric", "The critical-to-quality characteristic being monitored"),
        ("Specification", "The customer requirement or target the metric must meet"),
        ("Measurement method", "How the value is obtained, with the operational definition"),
        ("Sample size", "How many units or transactions are measured each time"),
        ("Frequency", "How often the measurement is taken - hourly, per shift, daily"),
        ("OWNER", "The named role accountable - never a department, always a person"),
        ("REACTION PLAN", "The specific action taken when the metric breaches its limit"),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("Northwind control plan - the four tracked metrics", [
        ("Order processing time", "Time from order received to release for picking - measured per order, sampled daily"),
        ("Number of late orders", "Orders delivered after the promised date - p-chart on the daily proportion late"),
        ("Picking time", "Time to pick a complete order in the warehouse - sampled per shift by zone"),
        ("Shipping errors", "Wrong item, wrong quantity or wrong address - counted per shipment, u-chart"),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("Standard Operating Procedures that people actually use", [
        ("Purpose", "Why this procedure exists and which CTQ it protects"),
        ("Scope", "Which process, which shifts, which sites it applies to"),
        ("Step-by-step instructions", "The new standard way of working, in the order it is done"),
        ("Quality checks", "What to verify at each step and what good looks like"),
        ("Escalation", "Who to call, when, and what to do while waiting"),
        ("Short and visual", "One page with photos beats ten pages of prose - nobody reads the ten"),
    ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels("Huddles and Gemba - two habits that hold the gain", [
        ("The team huddle", "Short daily stand-up at the board", [
            "Ten to fifteen minutes, standing, same time daily",
            "Read yesterday's chart, name anything red",
            "Assign one owner and one action per issue",
            "Surfaces problems while they are still small",
        ]),
        ("Go to Gemba", "Leadership goes to where the work happens", [
            "See the actual process, not the report about it",
            "Ask questions, do not issue instructions",
            "Verify the SOP matches what is really done",
            "Signals that the metric matters to management",
        ]),
    ], kicker=K, accent=AMBER)

    d.tile_grid("Training and the audit schedule", [
        ("Who needs training", "Every shift and every relief worker - not just the day team who piloted it"),
        ("What they are trained on", "The new SOP, the chart, the reaction plan and their role in it"),
        ("Competency check", "Observed once at the process, not a signature on an attendance sheet"),
        ("Audit frequency", "Weekly for the first month, then monthly once the control is stable"),
        ("What the audit checks", "Is the chart current, are limits respected, was the reaction plan followed"),
        ("Who audits", "A named role outside the immediate team, reporting to the process owner"),
    ], kicker=K, cols=2, accent=BLUE)

    d.flow_h("Verifying the gain", [
        "Re-measure using the SAME operational definitions as the baseline",
        "Recompute Cp and Cpk on the improved process data",
        "Run a hypothesis test comparing before and after",
        "Confirm the difference is statistically significant, not random",
        "Only then declare the improvement and update the control limits",
    ], kicker=K, color=VIOLET)

    d.tile_grid("Verification and benefit validation", [
        ("Same definitions", "Change the operational definition and you are comparing two different things"),
        ("Same measurement system", "The MSA from Measure must still hold, or the comparison is meaningless"),
        ("Enough data", "A handful of good days is not evidence - collect a defensible sample"),
        ("Hypothesis test", "Proves the shift is bigger than the noise the process produces anyway"),
        ("Finance sign-off", "A benefit Finance has not signed off will not be recognised by the business"),
        ("Hard vs soft benefit", "Separate cash savings from capacity released - Finance treats them differently"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.tile_grid("Presenting results to stakeholders", [
        ("Title as a question", "Did late deliveries actually fall? beats Control chart of late orders"),
        ("One graphic per slide", "One clear chart that answers the question - not three competing ones"),
        ("Conclusion in plain words", "State what it means for the business, not what the statistic is called"),
        ("Label every axis", "The graphic must survive being forwarded on without you in the room"),
        ("Leadership audience", "They want the benefit and the evidence it is under control"),
        ("Process team audience", "They want the workflow detail and what changes at their step"),
    ], kicker=K, cols=2, accent=BLUE)

    d.flow_h("Handover and project closure", [
        "Formal handover: the process owner accepts the control plan and signs for it",
        "30/60/90-day reviews scheduled with the owner and the sponsor",
        "Lessons learned captured while the team still remembers them",
        "Replication opportunities identified in other sites, lines or product groups",
        "Formal closure: benefits validated, project closed, team recognised",
    ], kicker=K, color=TEAL)

    d.tile_grid("The Control tollgate checklist", [
        ("Improvement verified", "Re-measured capability plus a hypothesis test proving significance"),
        ("Control plan complete", "Every CTQ metric has limits, frequency, a named owner and a reaction plan"),
        ("Charts live on the floor", "Correct chart type selected, limits calculated, being updated daily"),
        ("SOPs and training done", "Documents updated, every shift trained, competency observed"),
        ("Benefits validated", "Finance has signed off the hard and soft benefits"),
        ("Handover accepted", "Process owner has accepted, reviews scheduled, project formally closed"),
    ], kicker=K, cols=2, accent=RED)

    d.checkpoint("Checkpoint - Control", [
        "A process is in control but producing defects. Is it capable? What does that tell you?",
        "Cp is 1.5 but Cpk is 0.8. What is wrong with the process, and what is the fix?",
        "Why must specification limits never be plotted on a control chart?",
        "Northwind counts late orders daily with varying volume - which control chart, and why?",
        "Which out-of-control rule fires on nine points in a row on one side of the centre line?",
        "Name the two control plan columns without which the plan will not sustain the gain.",
    ], K)
