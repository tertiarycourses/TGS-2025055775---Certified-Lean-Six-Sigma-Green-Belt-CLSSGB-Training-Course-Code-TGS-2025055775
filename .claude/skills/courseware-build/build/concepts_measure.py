#!/usr/bin/env python3
"""Measure teaching slides — Green Belt depth, DMAIC order."""
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


def measure_phase(d):
    K = "MEASURE"

    # ================= A. PROCESS MAPPING =================
    d.big_statement(
        "Measure replaces opinion with data",
        "Define told us what hurts. Measure tells us how much, how often and where - "
        "in numbers a finance director would sign off on.",
        K, color=TEAL)

    d.tile_grid("What the Measure phase delivers", [
        ("A validated process map", "How the work actually flows today, including every handoff and rework loop"),
        ("A data collection plan", "What is measured, by whom, how often, with what operational definition"),
        ("A trustworthy measurement system", "MSA proves the gage is not the source of the variation"),
        ("A quantified baseline", "DPMO, yield, sigma level and process capability before any change"),
        ("Refined problem statement", "The Define scope narrowed to where the data says the pain sits"),
        ("Evidence for the tollgate", "Numbers the sponsor can act on, not anecdotes"),
    ], kicker=K, cols=2, accent=TEAL)

    d.flow_h("Steps of the Measure phase", [
        "Map the current process as it really runs, not as the SOP claims",
        "Identify the output Y and the candidate input Xs to measure",
        "Write operational definitions and build the data collection plan",
        "Validate the measurement system with MSA before trusting any number",
        "Collect the baseline data using a defensible sampling method",
        "Compute baseline yield, DPMO, sigma level and capability",
    ], kicker=K, color=TEAL)

    p = _dg(d, "process-symbols")
    if p:
        d.image_slide("Standard process mapping symbols", p, kicker=K,
                      caption="Oval = start/stop. Rectangle = activity. Diamond = decision. "
                              "D-shape = delay. Document shape = paperwork produced.",
                      accent=BLUE)

    d.flow_h("Steps to create a process map", [
        "Agree the start and stop boundary with the process owner",
        "Walk the process physically - go and see, do not map from a desk",
        "Capture each step on a sticky note with the people who do the work",
        "Sequence the notes, add decisions, delays and every rework loop",
        "Validate the map with a second shift or second team",
        "Add data: time per step, queue time, defect rate, headcount",
    ], kicker=K, color=BLUE)

    d.content("Key questions to evaluate a process map", [
        "Is any step done twice, or done differently by different people on different shifts?",
        "Where does work stop and wait, and how long does it sit there on average?",
        "Which steps exist only to check, inspect or correct someone else's earlier work?",
        "Where does the work change hands, and what is lost or delayed at each handoff?",
        "Which steps would the customer actually be willing to pay for?",
        "Which decisions are made without a written rule, so each person decides differently?",
    ], kicker=K)

    p = _dg(d, "process-flowchart")
    if p:
        d.image_slide("A worked process flowchart", p, kicker=K,
                      caption="Notice the rework loop: every backward arrow is a hidden factory "
                              "consuming capacity nobody has budgeted for.",
                      accent=BLUE)

    p = _dg(d, "swimlane-map")
    if p:
        d.image_slide("Swimlane (deployment) process map", p, kicker=K,
                      caption="Each horizontal lane is one role or department. Count the crossings - "
                              "that count predicts your defect rate better than any survey.",
                      accent=VIOLET)

    d.tile_grid("How to read a swimlane map", [
        ("One lane per actor", "Role, team or system - never a person's name. Lanes survive staff turnover."),
        ("Count the crossings", "Every lane crossing is a handoff: a queue, a re-entry, a chance to lose context."),
        ("Look for ping-pong", "Work bouncing between two lanes signals unclear ownership or missing authority."),
        ("Find the orphan steps", "Steps nobody claims are where things silently stall over a weekend."),
        ("Mark the decision lanes", "Approvals concentrated in one lane create a bottleneck by design."),
        ("Time each crossing", "Handoff wait time is usually larger than all touch time combined."),
    ], kicker=K, cols=2, accent=VIOLET)

    d.two_col("Northwind: swimlanes in order fulfilment",
              [("Customer Service takes the order and validates credit", 0),
               ("Handoff 1 to Warehouse Planning for wave allocation", 1),
               ("Warehouse Planning releases the pick wave twice daily", 0),
               ("Handoff 2 to Pickers on the floor", 1),
               ("Pickers pick, Packers pack and label", 0),
               ("Handoff 3 to Dispatch for carrier manifest", 1)],
              [("Six lane crossings per order", 0),
               ("Average queue at each crossing: 40 to 220 minutes", 1),
               ("Touch time across all steps: about 34 minutes", 0),
               ("Everything else is waiting", 1),
               ("357 of 4,200 orders late each month - 8.5 percent", 0),
               ("Most late orders cross a crossing on a Friday", 1)],
              kicker=K, lhead="THE FLOW", rhead="WHAT THE MAP REVEALED",
              lcolor=BLUE, rcolor=RED)

    d.waste_wheel("The 8 wastes of Lean - DOWNTIME", [
        ("D", "Defects"), ("O", "Overproduction"), ("W", "Waiting"),
        ("N", "Non-utilised talent"), ("T", "Transport"), ("I", "Inventory"),
        ("M", "Motion"), ("E", "Extra-processing"),
    ], kicker=K,
        note="Waste consumes capacity, cash and lead time while adding nothing the customer values.")

    p = _dg(d, "eight-wastes")
    if p:
        d.image_slide("The eight wastes in detail", p, kicker=K,
                      caption="Learn DOWNTIME as a walking checklist - one pass of the floor should "
                              "produce at least one example of each.",
                      accent=RED)

    d.tile_grid("DOWNTIME at Northwind", [
        ("D - Defects", "Mis-picks returned by the customer; wrong labels forcing a full re-pack."),
        ("O - Overproduction", "Printing pick lists for the whole day at 06:00 when only half can be picked by noon."),
        ("W - Waiting", "Packed cartons sitting on the dispatch dock waiting for the 16:00 carrier collection."),
        ("N - Non-utilised talent", "Experienced pickers who know the slotting problem are never asked about it."),
        ("T - Transport", "Fast-moving SKUs slotted at the far aisle, so every wave walks the full length."),
        ("I - Inventory", "Six weeks of slow-moving stock blocking the prime pick face near dispatch."),
        ("M - Motion", "Packers reaching across the bench for tape and labels 300 times a shift."),
        ("E - Extra-processing", "Three separate manual checks of the same pick before it reaches dispatch."),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("Value-added analysis - the three categories", [
        ("Value-Added", "Customer would pay for it - VA", [
            "Physically transforms the product or service",
            "Done right the first time",
            "The customer explicitly wants it",
            "Northwind: picking, packing, loading",
            "Typically 5 to 20 percent of steps"]),
        ("Business-Value-Added", "Required, but not customer value - BVA", [
            "Needed for legal, tax or regulatory reasons",
            "Required to keep the business running",
            "Customer would not pay extra for it",
            "Northwind: customs paperwork, credit check",
            "Minimise it - you cannot delete it"]),
        ("Non-Value-Added", "Pure waste - NVA, delete it", [
            "Inspection, rework, transport, waiting",
            "Adds cost and lead time, adds no value",
            "Northwind: triple checks, dock queue",
            "Typically 60 to 90 percent of lead time",
            "This is your improvement opportunity"]),
    ], kicker=K, accent=AMBER)

    # ================= B. VALUE STREAM MAPPING =================
    d.tile_grid("The three layers of a VSM", [
        ("Material flow", "Bottom half, left to right: how the physical work or the order moves through the process."),
        ("Information flow", "Top half, right to left: forecasts, schedules and signals that trigger the work."),
        ("The timeline ladder", "Underneath: process time on the lower step, waiting time on the upper step."),
        ("Data boxes", "Under each process: cycle time, changeover, uptime, headcount, batch size."),
        ("Inventory triangles", "Between processes: how much work sits in queue and for how long."),
        ("The summary line", "Total lead time versus total value-added time - the efficiency headline."),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "vsm-full")
    if p:
        d.image_slide("A complete value stream map", p, kicker=K,
                      caption="Read the information flow right to left across the top, the material "
                              "flow left to right along the bottom, and the ladder for the timeline.",
                      accent=TEAL)

    p = _dg(d, "vsm-icons")
    if p:
        d.image_slide("Standard VSM icons", p, kicker=K,
                      caption="Use the standard icon set so any Lean practitioner anywhere can read "
                              "your map without a legend.",
                      accent=TEAL)

    d.flow_h("Steps to create a value stream map", [
        "Pick one product family or one order type - never map everything at once",
        "Walk the stream backwards from the customer to the supplier",
        "Draw the material flow with a data box under every process step",
        "Add the information flow: what triggers each step and from where",
        "Draw the timeline ladder and record process time and wait time",
        "Compute lead time, value-added time and process cycle efficiency",
    ], kicker=K, color=TEAL)

    d.formula_card("Process cycle efficiency", [
        ("Process Cycle Efficiency", "PCE = VA time / Lead time",
         "Northwind: 34 min VA against 4 days (5,760 min) lead time."),
        ("Northwind PCE", "34 / 5760 = 0.0059",
         "0.59 percent - well under the 10 percent typical of service processes."),
        ("Improvement target", "Halve lead time, PCE doubles",
         "Attack the queues, not the touch time - the queues own the lead time."),
    ], kicker=K, accent=TEAL,
        note="Most service and transactional processes run under 10 percent PCE. World class is above 25 percent.")

    d.tile_grid("The core Lean metrics", [
        ("Work in Process (WIP)", "How many units are inside the process right now, including everything queuing."),
        ("Lead time", "Elapsed time from customer request to customer receipt, waiting included."),
        ("Cycle time", "Time to complete one unit at a step, or the interval between completed units."),
        ("Throughput", "Units completed per unit of time - the actual output rate of the process."),
        ("Takt time", "The customer demand rhythm the process must match to avoid backlog or idle time."),
        ("Little's Law", "Lead time = WIP / Throughput. Cut WIP and lead time falls with no extra staff."),
    ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "takt-time")
    if p:
        d.image_slide("Takt time explained", p, kicker=K,
                      caption="Takt = available working time divided by customer demand for that same period.",
                      accent=VIOLET)

    d.formula_card("Takt time - worked example", [
        ("Available time", "58 x 7.5 x 3600 sec",
         "58 staff productive for 7.5 hours per day = 1,566,000 seconds available."),
        ("Takt time", "Takt = Avail time / Demand",
         "1,566,000 / 4,500 transactions = 348 seconds per transaction."),
        ("Interpretation", "One unit every 348 sec",
         "Any step whose cycle time exceeds 348 sec is a bottleneck and must be rebalanced."),
    ], kicker=K, accent=VIOLET,
        note="Use only productive time - exclude breaks, briefings and planned downtime from the available time.")

    d.compare_panels("Takt vs cycle time vs lead time", [
        ("Takt time", "Set by the customer, not by you", [
            "Available time divided by demand",
            "Changes only when demand changes",
            "The target rhythm for every step",
            "Northwind: 348 seconds per transaction"]),
        ("Cycle time", "Set by the process design", [
            "Time for one step to finish one unit",
            "Compare each step against takt",
            "Steps above takt are bottlenecks",
            "Balance the line towards takt"]),
        ("Lead time", "What the customer experiences", [
            "Request to receipt, waiting included",
            "Dominated by queues, not touch time",
            "Little's Law: WIP / throughput",
            "Northwind: about 4 days"]),
    ], kicker=K, accent=BLUE)

    # ================= C. DATA AND SAMPLING =================
    d.compare_panels("Types of data", [
        ("Qualitative", "Attribute / categorical data", [
            "Describes a category or an attribute",
            "Counted, not measured",
            "Pass/fail, late/on-time, defect type",
            "Needs large samples for precision",
            "Northwind: order late yes or no"]),
        ("Quantitative", "Variable / measurement data", [
            "A number on a real measurement scale",
            "Measured on a continuum",
            "Cycle time, weight, distance, cost",
            "Far more information per data point",
            "Northwind: hours from order to despatch"]),
    ], kicker=K, accent=AMBER)

    d.tile_grid("Discrete, continuous, nominal, ordinal", [
        ("Discrete data", "Counts of whole things - 3 defects, 17 late orders. No meaningful value between 3 and 4."),
        ("Continuous data", "Any value on a scale - 4.37 hours, 12.6 kg. Infinitely divisible, richest information."),
        ("Nominal data", "Named categories with no order - carrier A, B, C; defect type; region."),
        ("Ordinal data", "Ordered categories with unequal gaps - satisfaction 1 to 5, priority high/medium/low."),
        ("Why it matters", "t-tests and capability need continuous data. Proportions and chi-square need attribute."),
        ("Green Belt rule", "Prefer continuous wherever you can get it - you need far fewer samples for the same power."),
    ], kicker=K, cols=2, accent=AMBER)

    d.tile_grid("The data collection plan - six columns", [
        ("What", "The exact measure: 'hours from order cut-off to carrier scan', not 'delivery performance'."),
        ("Who", "The named person or system responsible for capturing each observation."),
        ("When", "Frequency and timing - every order, hourly sample, one shift in three."),
        ("How", "The instrument, the system report, the check sheet, the exact recording method."),
        ("Sample size", "Calculated, not guessed - see the sample size formula in the next section."),
        ("Stratification", "The factors recorded alongside each point: shift, carrier, SKU class, day of week."),
    ], kicker=K, cols=2, accent=BLUE)

    d.tile_grid("Operational definitions - two people, one number", [
        ("The test", "Two trained people measure the same thing independently and get the same number."),
        ("Define the measure", "'Late' means the carrier scan timestamp is after 18:00 on the promised date."),
        ("Define the method", "Which system field, which report, which rounding rule, which time zone."),
        ("Define the boundary", "What counts and what is excluded - cancellations, samples, internal transfers."),
        ("Define the decision", "The exact criterion that separates conforming from non-conforming."),
        ("Test it before use", "Run a pilot with two people. If they disagree, the definition is not yet done."),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "sampling-techniques")
    if p:
        d.image_slide("Sampling techniques", p, kicker=K,
                      caption="Only random-based methods support statistical inference. "
                              "Convenience and judgment sampling do not.",
                      accent=RED)

    d.tile_grid("The four random sampling techniques", [
        ("Simple random", "Every unit has an equal chance of selection. Use a random number generator, not intuition."),
        ("Stratified random", "Split the population into homogeneous strata, then sample randomly within each stratum."),
        ("Systematic", "Take every Nth unit after a random start. Beware hidden cycles matching your interval."),
        ("Cluster", "Randomly select whole groups (a depot, a shift) and measure everything within them."),
    ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels("Random vs non-random sampling", [
        ("Random methods", "Valid for statistical analysis", [
            "Simple random, stratified, systematic, cluster",
            "Selection probability is known",
            "Sampling error can be quantified",
            "Confidence intervals are meaningful",
            "Conclusions generalise to the population"]),
        ("Non-random methods", "NOT valid for statistical analysis", [
            "Convenience sampling - whatever is nearby",
            "Judgment sampling - what looks typical",
            "Selection probability is unknown",
            "Bias cannot be measured or corrected",
            "Use only for scoping, never for inference"]),
    ], kicker=K, accent=RED)

    p = _dg(d, "sample-size-continuous")
    if p:
        d.image_slide("Sample size for continuous data", p, kicker=K,
                      caption="n = (1.96 s / d) squared, where s is the standard deviation and "
                              "d is the acceptable margin of error.",
                      accent=VIOLET)

    d.formula_card("Sample size - continuous data", [
        ("Formula", "n = (1.96 s / d)^2",
         "n = sample size, s = standard deviation, d = margin of error, 1.96 = 95 percent confidence."),
        ("Worked example", "n = (1.96 x 10 / 5)^2",
         "Estimate mean cycle time within 5 days, preliminary s = 10 days."),
        ("Result", "3.92^2 = 15.4 -> n = 16",
         "Sixteen observations. Always round the calculated sample size UP."),
    ], kicker=K, accent=VIOLET,
        note="Halving the margin of error d quadruples the required sample size - precision is expensive.")

    p = _dg(d, "sample-size-discrete")
    if p:
        d.image_slide("Sample size for discrete data", p, kicker=K,
                      caption="Attribute data needs far larger samples than continuous data for the "
                              "same confidence - another reason to prefer continuous measures.",
                      accent=VIOLET)

    d.tile_grid("Sample size in practice", [
        ("Where does s come from", "A pilot sample of 20 to 30 points, or historical data from the same process."),
        ("Choosing d", "Set by the decision, not by convenience: how wrong can you afford the estimate to be."),
        ("Why 1.96", "The z value for 95 percent confidence - the Six Sigma community default."),
        ("Always round up", "15.4 becomes 16. Rounding down silently degrades your confidence level."),
        ("More is not always better", "Beyond the calculated n you spend money to shrink an already adequate interval."),
        ("Attribute data costs more", "Estimating a proportion precisely may need hundreds of units, not sixteen."),
    ], kicker=K, cols=2, accent=VIOLET)

    # ================= D. MEASUREMENT SYSTEM ANALYSIS =================
    d.big_statement(
        "If the gage varies, you chase phantoms",
        "Total observed variation = actual process variation + measurement system variation. "
        "MSA proves how much of what you see is real before you spend a cent fixing it.",
        K, color=RED)

    p = _dg(d, "msa-variation-tree")
    if p:
        d.image_slide("Sources of variation - the MSA tree", p, kicker=K,
                      caption="Observed variation splits into true process variation and measurement "
                              "system variation, which splits again into repeatability and reproducibility.",
                      accent=RED)

    d.formula_card("The variation equation", [
        ("Total observed", "Var(total) = Var(proc) + Var(MS)",
         "Variances add, standard deviations do not. Always work in variance terms."),
        ("Measurement system", "Var(MS) = Var(rep) + Var(repro)",
         "Repeatability is the equipment; reproducibility is the appraiser."),
        ("The goal", "Var(MS) small vs Var(total)",
         "Aim for the measurement system to consume under 10 percent of total variation."),
    ], kicker=K, accent=RED)

    d.tile_grid("Resolution - the ten-bucket rule", [
        ("The rule", "The device increment must be about one tenth of the tolerance or the variation of interest."),
        ("Bad example", "Scale reads to 1 kg but the spec band is 2 kg - you have only 2 buckets, not 10."),
        ("Good example", "Timestamp to the second when detecting improvements measured in minutes."),
        ("Symptom of failure", "Data clumps onto only two or three distinct values across the whole sample."),
        ("Northwind case", "Despatch recorded to the nearest day cannot detect a 4-hour improvement."),
        ("The fix", "Change the recording increment before doing anything else - it is often free."),
    ], kicker=K, cols=2, accent=AMBER)

    p = _dg(d, "msa-accuracy")
    if p:
        d.image_slide("Accuracy, linearity and stability", p, kicker=K,
                      caption="Accuracy is the offset from truth. Linearity is whether that offset "
                              "changes across the range. Stability is whether it drifts over time.",
                      accent=BLUE)

    d.compare_panels("Accuracy, linearity, stability", [
        ("Accuracy (Bias)", "Offset from the true value", [
            "Difference between the average reading and truth",
            "Requires a known reference standard",
            "Constant bias is correctable by calibration",
            "Example: scale reads 0.4 kg high every time"]),
        ("Linearity", "Does the bias change across the range", [
            "Bias measured at low, mid and high values",
            "Accurate at 10 kg but 3 percent high at 100 kg",
            "Detected by measuring several known standards",
            "A linearity failure cannot be fixed by one offset"]),
        ("Stability", "Does the bias drift over time", [
            "Same standard measured repeatedly over weeks",
            "Plotted on a control chart to detect drift",
            "Drives the calibration interval",
            "Example: gage drifts after 200 uses"]),
    ], kicker=K, accent=BLUE)

    p = _dg(d, "msa-repeatability")
    if p:
        d.image_slide("Repeatability and reproducibility", p, kicker=K,
                      caption="Gage R&R quantifies both components so you know whether to fix the "
                              "equipment or retrain and re-standardise the people.",
                      accent=VIOLET)

    d.compare_panels("Repeatability vs Reproducibility", [
        ("Repeatability", "Equipment variation - EV", [
            "SAME appraiser, SAME item, repeated measures",
            "Variation inherent in the device or method",
            "Poor result means the instrument is the problem",
            "Fix: better gage, better fixture, finer resolution",
            "Northwind: same clerk, same order, two readings"]),
        ("Reproducibility", "Appraiser variation - AV", [
            "DIFFERENT appraisers, SAME item, same conditions",
            "Variation caused by who is doing the measuring",
            "Poor result means the definition or training failed",
            "Fix: operational definitions, training, standard work",
            "Northwind: three clerks grading the same 'late' order"]),
    ], kicker=K, accent=VIOLET)

    d.flow_h("Attribute Gage R&R - the procedure", [
        "Select at least 20 samples spanning good, bad and borderline cases",
        "Label the samples opaquely so no appraiser can infer the answer",
        "Record the known correct attribute for each sample from an expert or master",
        "Have 2 to 3 appraisers assess every sample independently",
        "Repeat the assessment in a RANDOMISED order so trial 1 cannot be recalled",
        "Score agreement: within appraiser, between appraisers, and against the standard",
    ], kicker=K, color=VIOLET)

    d.tile_grid("Attribute Gage R&R - rules that make it valid", [
        ("At least 20 samples", "Fewer than 20 and a single disagreement swings the percentage wildly."),
        ("Include the borderline", "Easy pass and easy fail items flatter the system. Edge cases are the real test."),
        ("Opaque labelling", "Random codes, no sequence, no visible grouping by known condition."),
        ("Known standard required", "Without an expert-agreed truth you can measure agreement but not correctness."),
        ("Randomise every trial", "Otherwise appraisers repeat their memory of trial 1 instead of re-assessing."),
        ("Blind the appraisers", "Never let them see each other's calls or their own previous scores."),
    ], kicker=K, cols=2, accent=VIOLET)

    d.tile_grid("Variable Gage R&R - acceptance criteria", [
        ("% Study Variation", "0 to 10 pass  |  10 to 30 caution  |  30 and above fail"),
        ("% Tolerance", "0 to 10 pass  |  10 to 30 caution  |  30 and above fail"),
        ("% Contribution", "0 to 1 pass  |  1 to 9 caution  |  10 and above fail"),
        ("Distinct Categories", "10 or more pass  |  6 to 10 caution  |  1 to 5 fail"),
    ], kicker=K, cols=1, size=16, accent=RED)

    d.content("Reading the Gage R&R acceptance table", [
        "Percent Study Variation compares measurement error against the total observed variation.",
        "Percent Tolerance compares measurement error against the customer specification width.",
        "Percent Contribution is variance-based, so its thresholds are the squares of the others.",
        "Number of Distinct Categories is how many separate levels the system can actually tell apart.",
        "DECISION RULE: one caution with all other metrics passing is acceptable for use.",
        "Anything landing in the fail zone means repair or replace the measurement system first.",
    ], kicker=K)

    d.compare_panels("What to do with a failing Gage R&R", [
        ("Repeatability fails", "The equipment is the problem", [
            "Improve gage resolution or condition",
            "Add a fixture to standardise positioning",
            "Service, calibrate or replace the device",
            "Automate the reading where possible"]),
        ("Reproducibility fails", "The people or the method are the problem", [
            "Rewrite the operational definition",
            "Retrain all appraisers to one standard",
            "Add reference samples and visual aids",
            "Create standard work for the measurement"]),
        ("Both fail", "Stop the project data collection", [
            "Do not collect a baseline with this system",
            "Fix the measurement system as a mini-project",
            "Re-run the Gage R&R to confirm the fix",
            "Only then proceed to baseline collection"]),
    ], kicker=K, accent=RED)

    # ================= E. PROCESS PERFORMANCE METRICS =================
    p = _dg(d, "dudo-analysis")
    if p:
        d.image_slide("DUDO analysis", p, kicker=K,
                      caption="Defect, Unit, Defect Opportunity, Observed defects - agree all four "
                              "before you compute a single metric.",
                      accent=BLUE)

    d.tile_grid("DUDO - the four definitions", [
        ("D - Defect", "Any failure to meet a customer requirement - one CTQ not satisfied on one unit."),
        ("U - Unit", "The thing being produced or delivered that the customer receives. One order at Northwind."),
        ("D - Defect Opportunity", "Every distinct way a single unit could fail. A form with 10 fields has 10."),
        ("O - Observed defects", "The actual count of defects found in the sample you inspected."),
        ("Why opportunities matter", "DPMO normalises complexity so a 10-field form compares fairly with a 60-field one."),
        ("Be conservative", "Inflating the opportunity count artificially flatters your sigma level. Auditors check this."),
    ], kicker=K, cols=2, accent=BLUE)

    d.two_col("DUDO applied to Northwind",
              [("Unit: one customer order", 0),
               ("Defect: order not despatched by the promised cut-off", 0),
               ("Opportunities: 1 per order (on-time or not)", 0),
               ("Observed: 357 late in the month", 0)],
              [("Baseline volume: 4,200 orders per month", 0),
               ("Defect rate: 357 / 4,200 = 8.5 percent", 0),
               ("First pass yield: 91.5 percent", 0),
               ("This is the number the whole project moves", 0)],
              kicker=K, lhead="DEFINITIONS", rhead="THE BASELINE",
              lcolor=BLUE, rcolor=RED)

    d.compare_panels("Three ways to measure yield", [
        ("Classic Yield", "Units out / units in", [
            "Counts anything that eventually shipped",
            "Rework and retest are invisible",
            "Always the most flattering number",
            "Hides all the cost of poor quality"]),
        ("First Pass Yield", "Right first time at ONE step", [
            "Units through with no rework or repair",
            "Computed step by step",
            "Exposes rework at each individual step",
            "The honest per-step measure"]),
        ("Rolled Throughput Yield", "Right first time ACROSS all steps", [
            "RTY = FPY1 x FPY2 x ... x FPYn",
            "Probability a unit passes every step cleanly",
            "Falls fast as step count rises",
            "The true customer experience"]),
    ], kicker=K, accent=RED)

    p = _dg(d, "rolled-throughput-yield")
    if p:
        d.image_slide("Rolled throughput yield", p, kicker=K,
                      caption="Multiply the first pass yields of every step. Long processes with "
                              "good-looking steps still deliver poor overall yield.",
                      accent=RED)

    d.formula_card("Rolled throughput yield - worked example", [
        ("RTY formula", "RTY = FPY1 x FPY2 x ... x FPYn",
         "Multiply the first pass yield of every step in the process chain."),
        ("Five steps at 95%", "RTY = 0.95^5",
         "0.95 x 0.95 x 0.95 x 0.95 x 0.95 = 0.7738."),
        ("The hidden factory", "77.4% vs 95% headline",
         "Each step looks excellent, yet 22.6 percent of units are reworked somewhere."),
    ], kicker=K, accent=RED,
        note="The hidden factory is the capacity, cost and lead time consumed by rework that no budget line shows.")

    d.formula_card("DPU, DPO and DPMO", [
        ("DPU", "DPU = Defects / Units",
         "Average defects carried by each unit produced."),
        ("DPO", "DPO = Defects / (U x O)",
         "Defects per single opportunity, normalised for unit complexity."),
        ("DPMO", "DPMO = DPO x 1,000,000",
         "Scaled to a million opportunities so any two processes can be compared."),
    ], kicker=K, accent=VIOLET)

    d.formula_card("DPMO - worked example (forms)", [
        ("Opportunities", "10 fields x 90 forms = 900",
         "Each form has 10 fields, so each form carries 10 defect opportunities."),
        ("Observed defects", "2 errors found",
         "Two incorrectly completed fields across the entire 90-form sample."),
        ("DPMO", "(2 / 900) x 1,000,000",
         "= 2,222 DPMO. Note this is far better than 2 defects in 90 forms sounds."),
    ], kicker=K, accent=VIOLET,
        note="The opportunity count changes the answer dramatically - define it once, document it, never change it mid-project.")

    d.formula_card("DPMO - Northwind baseline", [
        ("Units and defects", "4,200 orders, 357 late",
         "One opportunity per order: the order is either on time or it is not."),
        ("DPMO", "(357 / 4200) x 1,000,000",
         "= 85,000 DPMO. This is the number the project must move."),
        ("Sigma level", "85,000 DPMO -> ~2.9 sigma",
         "Between 3 sigma (66,800) and 2 sigma (308,000) - closer to 3."),
    ], kicker=K, accent=RED,
        note="Northwind operates at roughly 2.9 sigma - typical for an unimproved transactional process.")

    d.ladder("The sigma scale - DPMO at each level", [
        ("1 sigma", "690,000 DPMO"),
        ("2 sigma", "308,000 DPMO"),
        ("3 sigma", "66,800 DPMO"),
        ("4 sigma", "6,210 DPMO"),
        ("5 sigma", "233 DPMO"),
        ("6 sigma", "3.4 DPMO"),
    ], kicker=K, accent=TEAL,
        note="Each sigma level is roughly a ten-fold reduction in defects - the gains get harder as you climb.")

    # ================= F. BASELINE CAPABILITY =================
    d.compare_panels("Descriptive statistics - centre and spread", [
        ("Measures of centre", "Where the data sits", [
            "Mean: the arithmetic average, uses every value",
            "Median: the middle value when sorted",
            "Mode: the most frequently occurring value",
            "Median resists outliers; the mean does not",
            "Report both when the data is skewed"]),
        ("Measures of spread", "How much the data varies", [
            "Range: maximum minus minimum, uses 2 points",
            "Standard deviation: average distance from the mean",
            "Variance: standard deviation squared - variances add",
            "Spread is the enemy - Six Sigma attacks variation",
            "Northwind despatch: mean 6.4 h, s 3.1 h"]),
    ], kicker=K, accent=BLUE)

    d.tile_grid("Reading histogram shape", [
        ("Bell shaped", "Symmetric, single peak. Common cause variation only. Normal tools apply."),
        ("Right skewed", "Long tail towards high values. Typical of times, delays and costs."),
        ("Left skewed", "Long tail towards low values. Often a ceiling or a cap in the process."),
        ("Bi-modal - two peaks", "TWO PROCESSES measured as one. Stratify by shift, carrier, line, then re-plot."),
        ("Truncated / cut off", "A cliff edge usually means data is being filtered, rounded or censored."),
        ("Isolated island", "A small separate cluster - a distinct special cause worth investigating alone."),
    ], kicker=K, cols=2, accent=AMBER)

    d.normal_curve("The normal distribution and the empirical rule", kicker=K,
                   note="68.26 percent within +/-1 sigma, 95.46 percent within +/-2 sigma, "
                        "99.73 percent within +/-3 sigma.")

    p = _dg(d, "normal-distribution")
    if p:
        d.image_slide("The normal distribution", p, kicker=K,
                      caption="Symmetric about the mean, fully described by two parameters: "
                              "the mean (location) and the standard deviation (spread).",
                      accent=VIOLET)

    d.tile_grid("The empirical rule in practice", [
        ("+/- 1 sigma", "68.26 percent of all observations fall inside one standard deviation of the mean."),
        ("+/- 2 sigma", "95.46 percent of all observations fall inside two standard deviations."),
        ("+/- 3 sigma", "99.73 percent - which is why 3 sigma control limits flag only rare events."),
        ("Beyond 3 sigma", "About 0.27 percent, or 2,700 per million - too many for a Six Sigma process."),
        ("Northwind applied", "Mean 6.4 h, s 3.1 h means about 95 percent despatch between 0.2 and 12.6 hours."),
        ("Check normality first", "Use a histogram and a normal probability plot before applying these percentages."),
    ], kicker=K, cols=2, accent=VIOLET)

    d.compare_panels("Voice of the customer vs voice of the process", [
        ("Voice of the Customer", "Specification limits - USL and LSL", [
            "Set by the customer, contract or regulation",
            "USL: upper specification limit",
            "LSL: lower specification limit",
            "Never calculated from your own process data",
            "Northwind: despatch within 8 hours of cut-off"]),
        ("Voice of the Process", "Control limits and the distribution", [
            "Calculated from what the process actually does",
            "Mean and standard deviation of real output",
            "Control limits are +/-3 sigma of the process",
            "Tells you what the process CAN deliver today",
            "Northwind: mean 6.4 h, s 3.1 h"]),
    ], kicker=K, accent=TEAL)

    p = _dg(d, "cp-formula")
    if p:
        d.image_slide("The Cp formula", p, kicker=K,
                      caption="Cp = (USL - LSL) / 6s - the ratio of the allowed spread to the "
                              "actual process spread. Cp ignores centring.",
                      accent=TEAL)

    d.formula_card("Baseline capability - Cp", [
        ("Cp", "Cp = (USL - LSL) / 6s",
         "Specification width divided by the natural process width of six standard deviations."),
        ("Interpretation", "Cp = 1.0 means just fits",
         "Cp below 1 cannot meet spec even when perfectly centred. Cp of 1.33 is a common minimum."),
        ("The limitation", "Cp ignores the mean",
         "A perfectly narrow process sitting off-centre still produces defects. Cpk fixes this - taught in Control."),
    ], kicker=K, accent=TEAL,
        note="Cp is potential capability. Cpk is actual capability and is covered fully in the Control phase.")

    d.tile_grid("Interpreting the baseline capability number", [
        ("Cp below 1.00", "The process spread is wider than the specification. Defects are guaranteed."),
        ("Cp 1.00 to 1.33", "Marginal. Any small drift in the mean immediately produces defects."),
        ("Cp 1.33 or above", "The commonly accepted minimum for a controlled process."),
        ("Cp 2.00", "The Six Sigma standard - spec width is twice the natural process width."),
        ("Northwind baseline", "Wide spread against an 8-hour promise gives a Cp well below 1."),
        ("What Cp does not tell you", "Nothing about centring. Always pair Cp with Cpk before concluding."),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "run-chart-base")
    if p:
        d.image_slide("Baseline run chart", p, kicker=K,
                      caption="Plot the baseline over time before summarising it - a stable process "
                              "and a drifting one can share the same mean and standard deviation.",
                      accent=BLUE)

    d.run_chart("Northwind baseline - late orders per week",
                [("W1", 78), ("W2", 92), ("W3", 71), ("W4", 116), ("W5", 84),
                 ("W6", 97), ("W7", 69), ("W8", 121), ("W9", 88), ("W10", 103),
                 ("W11", 74), ("W12", 109)],
                kicker=K,
                note="Common cause variation around a stable median - the process is consistently bad, "
                     "not occasionally bad. That means a system fix, not a people fix.")

    d.tile_grid("Common Measure phase mistakes", [
        ("Skipping MSA", "The single most common Green Belt failure - the whole baseline becomes unusable."),
        ("Mapping from a desk", "The SOP map is fiction. Walk the process or you will map the wrong thing."),
        ("Guessing the sample size", "Undersized samples give confident conclusions that do not replicate."),
        ("Ignoring bi-modality", "Summarising two processes as one produces a mean that describes neither."),
        ("Inflating opportunities", "Gaming the opportunity count to flatter DPMO destroys project credibility."),
        ("No stratification data", "Forgetting to record shift and carrier means re-collecting everything later."),
    ], kicker=K, cols=2, accent=RED)

    d.checkpoint("Measure phase - checkpoint", [
        "Which is the bigger lever at Northwind: touch time or queue time, and how do you know?",
        "State the sample size formula for continuous data and explain each of its terms.",
        "Explain the difference between repeatability and reproducibility, with a fix for each.",
        "Five steps each at 95 percent first pass yield - what is the RTY, and what does the gap mean?",
        "Compute Northwind's DPMO from 4,200 orders and 357 late, and give the sigma level.",
        "Your histogram is bi-modal. What has almost certainly happened, and what do you do next?",
    ], K)
