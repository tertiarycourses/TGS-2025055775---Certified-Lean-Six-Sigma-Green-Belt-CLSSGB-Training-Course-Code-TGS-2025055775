#!/usr/bin/env python3
"""Analyze teaching slides — Green Belt depth, DMAIC order."""
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


def analyze_phase(d):
    K = "ANALYZE"

    # ================= A. VARIATION AND STABILITY =================
    d.big_statement(
        "Analyze finds the proven root cause",
        "Measure told us the process runs at 8.5 percent late. Analyze answers the next "
        "question - WHY - and proves the answer with data, not opinion.",
        K, color=VIOLET)

    d.tile_grid("What the Analyze phase delivers", [
        ("A short list of validated causes", "Not 40 brainstormed guesses - the two or three the data actually supports"),
        ("A stratified problem", "Where the defects concentrate: which shift, which carrier, which product family"),
        ("Statistical evidence", "Hypothesis tests that separate a real signal from ordinary noise"),
        ("Quantified X to Y relationships", "Correlation and regression showing how much of Y each X explains"),
        ("A rejected-causes log", "Causes tested and cleared - so nobody re-litigates them in Improve"),
        ("A sponsor-ready story", "Statistics translated into money, risk and customer impact"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.flow_h("Steps of the Analyze phase", [
        "Chart the data over time and separate common from special cause variation",
        "Stratify and Pareto the defects to find where the problem concentrates",
        "Generate candidate causes with fishbone and 5 Whys",
        "Reduce the list by multi-voting, then test the survivors with hypothesis tests",
        "Quantify the surviving X to Y links with correlation and regression",
        "Confirm root causes at the tollgate and hand a proven list to Improve",
    ], kicker=K, color=VIOLET)

    d.compare_panels("Common cause vs special cause variation", [
        ("COMMON CAUSE", "Inherent, random, always present in the system", [
            "Built into the process design itself",
            "Many small sources acting together",
            "Predictable within a range - stable",
            "Fix requires a PROCESS CHANGE by management",
            "Northwind: normal 6 to 11 percent weekly late rate",
        ]),
        ("SPECIAL CAUSE", "Assignable to a specific identifiable event", [
            "Something changed - not part of the system",
            "One traceable source you can name",
            "Unpredictable - shows as a signal on the chart",
            "Fix is LOCAL: find it, remove it, prevent recurrence",
            "Northwind: 23 percent late the week the WMS server failed",
        ]),
    ], kicker=K, accent=TEAL)

    d.tile_grid("Why the distinction decides your whole strategy", [
        ("Wrong diagnosis, wrong owner", "Special cause is a local fix. Common cause needs management to change the system."),
        ("Blame follows the error", "Treating common cause as special makes you hunt for a guilty operator who does not exist."),
        ("Roughly 85 percent is systemic", "Most defects come from the process, not the person running it."),
        ("It sets the tool", "Special cause: investigate the event. Common cause: redesign with DMAIC."),
        ("Stability comes first", "You cannot judge capability or test causes on an unstable process."),
        ("It stops tampering", "Knowing the variation is common cause is what gives you licence to leave it alone."),
    ], kicker=K, cols=2, accent=TEAL)

    d.compare_panels("Tampering - what it looks like at Northwind", [
        ("THE TRIGGER", "A single ordinary point moves", [
            "Tuesday late rate rises from 8 to 11 percent",
            "Both values sit inside normal common cause range",
            "Nothing actually changed in the process",
            "But the number is visible on a daily report",
        ]),
        ("THE REACTION", "The supervisor adjusts", [
            "Two pickers moved from zone C to zone A",
            "Carrier cut-off pulled forward by 30 minutes",
            "The adjustment is made with good intentions",
            "No data supports the change - only the one point",
        ]),
        ("THE RESULT", "Variation roughly doubles", [
            "Zone C now short-staffed - it starts running late",
            "The next swing is bigger, prompting a bigger correction",
            "The process oscillates around the target",
            "Rule: never adjust a stable process on one data point",
        ]),
    ], kicker=K, accent=RED)

    p = _dg(d, "run-chart-base")
    if p:
        d.image_slide("Anatomy of a run chart", p, kicker=K,
                      caption="Time on the horizontal axis, the measure on the vertical axis, and a "
                              "MEDIAN centre line - not a mean, because the median resists outliers.",
                      accent=BLUE)

    d.tile_grid("How to build a run chart correctly", [
        ("Plot in TIME ORDER", "Sequence is the whole point - sorting the data destroys the information"),
        ("Use the MEDIAN centre line", "The median is not distorted by the extreme points you are hunting"),
        ("At least 15 to 20 points", "Fewer points cannot reliably show a trend, shift or oscillation"),
        ("Keep the interval constant", "Daily or weekly - do not mix, and do not skip periods"),
        ("Annotate known events", "Mark the server outage or the new carrier so signals can be explained"),
        ("Read patterns, not points", "One high point is noise. A PATTERN is a signal worth investigating."),
    ], kicker=K, cols=2, accent=BLUE)

    d.run_chart("Northwind order cycle time - 12 weeks (hours)",
                [("W1", 31.4), ("W2", 29.8), ("W3", 33.1), ("W4", 30.2), ("W5", 32.6),
                 ("W6", 28.9), ("W7", 34.0), ("W8", 31.1), ("W9", 29.5), ("W10", 33.4),
                 ("W11", 30.7), ("W12", 32.2)],
                kicker=K,
                note="Points scatter randomly either side of the median with no run, trend or "
                     "oscillation - this is a STABLE process showing only common cause variation.")

    d.run_chart("Northwind picking cycle time - a signal appears (hours)",
                [("W1", 30.6), ("W2", 31.2), ("W3", 30.1), ("W4", 31.8), ("W5", 30.4),
                 ("W6", 33.5), ("W7", 34.2), ("W8", 35.0), ("W9", 35.6), ("W10", 36.3),
                 ("W11", 37.1), ("W12", 37.9)],
                kicker=K,
                note="Six consecutive rising points from W6 - a TREND. Something changed at W6. "
                     "Go and find the event; do not average it away.")

    d.tile_grid("The six non-random run chart patterns", [
        ("TREND", "6 or more consecutive points all increasing, or all decreasing - drift or wear"),
        ("SHIFT", "8 or more consecutive points on ONE side of the median - the level has moved"),
        ("CLUSTER", "Points bunched together in one area - a batch, a shift or a single operator"),
        ("MIXTURE", "Points AVOID the median - usually two processes plotted as one"),
        ("OSCILLATION", "14 or more points alternating up and down - classic over-adjustment"),
        ("BIAS", "Too few or too many runs across the median versus what chance predicts"),
    ], kicker=K, cols=2, accent=AMBER)

    p = _dg(d, "run-chart-trend")
    if p:
        d.image_slide("Pattern 1 - TREND", p, kicker=K,
                      caption="Six or more consecutive points moving in the same direction. Tool wear, "
                              "gradual staffing loss or a slowly filling queue all read like this.",
                      accent=AMBER)

    p = _dg(d, "run-chart-shift")
    if p:
        d.image_slide("Pattern 2 - SHIFT", p, kicker=K,
                      caption="Eight or more consecutive points on one side of the median. The process "
                              "level has moved - a new method, new carrier or new system release.",
                      accent=AMBER)

    # ================= B. PARETO AND STRATIFICATION =================
    d.tile_grid("Using the Pareto principle properly", [
        ("Rank descending", "Categories on the horizontal axis, biggest first - always"),
        ("Add the cumulative line", "The 80 percent crossing point defines your project scope"),
        ("One category, one bar", "Categories must be mutually exclusive or the chart lies"),
        ("Beware the Other bar", "If Other is the tallest bar, your categories are wrong"),
        ("Pareto by COST too", "The most frequent defect is not always the most expensive one"),
        ("Re-Pareto after Improve", "The vital few change once you have fixed the first one"),
    ], kicker=K, cols=2, accent=AMBER)

    p = _dg(d, "pareto-chart")
    if p:
        d.image_slide("Reading a Pareto chart", p, kicker=K,
                      caption="Bars descend left to right; the red cumulative line climbs to 100 percent. "
                              "Where it crosses 80 percent, draw the line around your project.",
                      accent=AMBER)

    d.pareto_chart("Northwind late deliveries by cause - 357 late orders",
                   [("Picking delays", 142), ("Stock location errors", 89),
                    ("Carrier cut-off missed", 61), ("System downtime", 34),
                    ("Packing rework", 19), ("Other", 12)],
                   kicker=K,
                   note="Picking delays and stock location errors are 231 of 357 late orders - about "
                        "65 percent from just two causes. Add carrier cut-off and you pass 80 percent.")

    d.compare_panels("Stratifying the Northwind picking delays", [
        ("BY SHIFT", "Night shift is the concentration", [
            "Day shift: 38 of 142 picking delays",
            "Afternoon shift: 31 of 142",
            "Night shift: 73 of 142 - over half",
            "Night runs the same volume with 60 percent of the staff",
        ]),
        ("BY PRODUCT FAMILY", "Bulk beverages dominate", [
            "Bulk beverages: 61 of 142 delays",
            "Chilled goods: 44 of 142",
            "Ambient dry goods: 37 of 142",
            "Bulk beverages sit furthest from despatch",
        ]),
        ("BY CARRIER", "Essentially flat - not a driver", [
            "Carrier A: 49, Carrier B: 47, Carrier C: 46",
            "No meaningful concentration by carrier",
            "So carrier is NOT the picking-delay lever",
            "A flat stratification is a valid, useful answer",
        ]),
    ], kicker=K, accent=TEAL)

    d.tile_grid("Concentrated versus universal problems", [
        ("Concentrated is good news", "Night shift plus bulk beverages is a small, targeted, affordable fix"),
        ("Universal is a system issue", "Even spread across every stratum means the process design is the cause"),
        ("Plan strata BEFORE collecting", "You cannot stratify by a field you never recorded"),
        ("Common strata", "Shift, operator, machine, location, product, day of week, customer"),
        ("Flat is still an answer", "Ruling a factor OUT saves the team weeks of wasted effort"),
        ("Stratify then re-Pareto", "Every stratum deserves its own Pareto before you test causes"),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "boxplot")
    if p:
        d.image_slide("Boxplots - comparing groups visually", p, kicker=K,
                      caption="The box spans the interquartile range with the median inside it; the "
                              "whiskers reach the last non-outlier points and dots mark outliers.",
                      accent=BLUE)

    d.tile_grid("How to read a boxplot", [
        ("The median line", "The 50th percentile - half the data above, half below"),
        ("The box = IQR", "Q1 to Q3 - the middle 50 percent of the data sits inside the box"),
        ("The whiskers", "Reach to the furthest point within 1.5 x IQR of the box edge"),
        ("The outlier dots", "Points beyond the whiskers - investigate them, never delete them"),
        ("Box position = centring", "Boxes at different heights suggest the group means differ"),
        ("Box width = spread", "A wide box is an inconsistent group, even if the median looks fine"),
    ], kicker=K, cols=2, accent=BLUE)

    d.compare_panels("Boxplot of Northwind picking time by shift", [
        ("DAY SHIFT", "Median 26 min, IQR 22 to 31", [
            "Tight box - consistent performance",
            "Whiskers 17 to 38 minutes",
            "No outliers in 34 observations",
        ]),
        ("AFTERNOON SHIFT", "Median 28 min, IQR 24 to 34", [
            "Slightly higher and slightly wider",
            "Whiskers 19 to 44 minutes",
            "One outlier at 61 minutes",
        ]),
        ("NIGHT SHIFT", "Median 41 min, IQR 33 to 52", [
            "Clearly higher AND much wider box",
            "Whiskers 24 to 74 minutes",
            "Three outliers above 80 minutes",
        ]),
    ], kicker=K, accent=BLUE)

    # ================= C. ROOT CAUSE TOOLS =================
    d.tile_grid("Brainstorming ground rules", [
        ("NO criticism", "Not a word, not a face, not a sigh - judgement kills contribution instantly"),
        ("Quantity over quality", "Aim for volume first; the good ideas hide inside the long list"),
        ("Build on ideas", "Yes, and - hitch-hiking on someone else's idea is actively encouraged"),
        ("Wild ideas welcome", "It is far easier to tame a wild idea than to invigorate a dull one"),
        ("Everyone contributes", "Round-robin or silent written rounds stop one loud voice dominating"),
        ("Include the doers", "Pickers and drivers know causes no manager will ever think of"),
    ], kicker=K, cols=2, accent=VIOLET)

    p = _dg(d, "fishbone-skeleton")
    if p:
        d.image_slide("The fishbone / Ishikawa skeleton", p, kicker=K,
                      caption="The effect sits in the head of the fish; each bone is a cause category, "
                              "and each twig off a bone is a specific potential cause.",
                      accent=VIOLET)

    p = _dg(d, "fishbone-pizza")
    if p:
        d.image_slide("Worked fishbone example", p, kicker=K,
                      caption="A completed fishbone on a familiar everyday effect - note how each bone "
                              "is drilled two or three levels deep, not just labelled.",
                      accent=VIOLET)

    d.tile_grid("The 5M plus E categories", [
        ("MANPOWER", "People - skill, training, staffing level, fatigue, motivation, turnover"),
        ("METHOD", "The process - SOPs, sequence, batch rules, approvals, handoffs"),
        ("MACHINE", "Equipment - scanners, conveyors, the WMS, forklifts, printers"),
        ("MATERIAL", "Inputs - packaging, labels, stock condition, supplier quality"),
        ("MEASUREMENT", "The data - gages, definitions, reporting timing, system accuracy"),
        ("ENVIRONMENT", "Conditions - layout, temperature, lighting, congestion, season"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.fishbone("Northwind fishbone - orders shipped late", "Orders shipped late", [
        ("Manpower", ["Night shift under-staffed", "New pickers untrained", "High agency turnover"]),
        ("Method", ["No pick-path optimisation", "Batch release at 14:00 only", "Manual exception handling"]),
        ("Machine", ["RF scanners drop signal", "WMS slow at peak", "One conveyor line down"]),
        ("Material", ["Bulk beverages badly located", "Labels jam the printer", "Damaged outer cartons"]),
        ("Measurement", ["Late defined differently by team", "Timestamps captured at despatch only", "No per-zone data"]),
        ("Environment", ["Aisle congestion at peak", "Poor lighting in zone C", "Peak season volume surge"]),
    ], kicker=K)

    d.tile_grid("Running a fishbone session that works", [
        ("Write the effect precisely", "Orders shipped late beats poor performance - vague effects give vague bones"),
        ("Ask why on every twig", "One level of cause is a label. Three levels is an investigation."),
        ("Do it at the gemba", "Run it in the warehouse with the map and the data on the wall"),
        ("Circle the likely few", "Dot-vote to mark the causes worth testing with data"),
        ("Causes only, not solutions", "Someone will say we need a new WMS - park it, that is Improve"),
        ("It produces HYPOTHESES", "Nothing on the fishbone is a root cause until data confirms it"),
    ], kicker=K, cols=2, accent=VIOLET)

    p = _dg(d, "five-whys-example")
    if p:
        d.image_slide("5 Whys - worked example", p, kicker=K,
                      caption="Each answer becomes the next question. The chain stops at the level "
                              "where a countermeasure can actually be installed.",
                      accent=BLUE)

    d.ladder("5 Whys - Northwind late shipment", [
        ("PROBLEM", "Order 44821 shipped a day late"),
        ("WHY 1", "It missed the 16:00 carrier cut-off"),
        ("WHY 2", "Picking finished at 16:40, 40 minutes late"),
        ("WHY 3", "The picker walked the aisle three times for bulk beverages"),
        ("WHY 4", "Bulk beverage SKUs are stored across four non-adjacent zones"),
        ("ROOT", "Slotting rules use supplier code, not pick frequency - a SYSTEM cause"),
    ], kicker=K, accent=BLUE,
        note="The root cause is a slotting RULE, not a slow picker. That is fixable, ownable and "
             "will not recur once changed.")

    d.tile_grid("Rules that make 5 Whys reliable", [
        ("Stop at process or system", "If the answer is a person's name, you asked the wrong why"),
        ("Validate backwards", "Read the chain up using therefore - if it does not flow, a link is missing"),
        ("Five is a guide", "Sometimes three whys is enough; sometimes seven is needed"),
        ("Branch when needed", "One why can have two valid answers - follow both chains"),
        ("Each link needs evidence", "An unverified link makes every link below it worthless"),
        ("Beware the lazy root", "Human error and lack of training are almost never real root causes"),
    ], kicker=K, cols=2, accent=BLUE)

    d.tile_grid("Converging - multi-voting and NGT", [
        ("Why converge at all", "A fishbone yields 30 to 50 causes; you can only test a handful"),
        ("Each voter gets N/3 votes", "30 causes on the wall means 10 votes per participant"),
        ("Vote silently first", "Silent voting removes seniority pressure from the room"),
        ("Rank the top vote-getters", "Take the top five to eight forward for a second round"),
        ("Nominal group technique", "Structured rounds so quiet experts carry equal weight"),
        ("Votes select what to TEST", "The vote picks the test order - it never proves a cause"),
    ], kicker=K, cols=2, accent=TEAL)

    d.compare_panels("From suspected cause to proven root cause", [
        ("SUSPECTED", "It came out of the fishbone", [
            "Night shift picking is slower",
            "Based on team experience and observation",
            "Plausible - and completely untested",
            "Acting on it now is a gamble",
        ]),
        ("TESTED", "A hypothesis test is run", [
            "H0: night and day mean picking times are equal",
            "34 observations from each shift",
            "2-Sample T test, alpha = 0.05",
            "p = 0.003 - reject the null",
        ]),
        ("PROVEN", "Evidence plus process logic", [
            "Difference is statistically significant",
            "Slotting explains WHY it is slower",
            "Now it earns a place in the Improve plan",
            "And the rejected causes go into the log",
        ]),
    ], kicker=K, accent=RED)

    # ================= D. DESCRIPTIVE AND INFERENTIAL STATISTICS =================
    d.compare_panels("Descriptive vs inferential statistics", [
        ("DESCRIPTIVE", "Summarises the data you actually have", [
            "Mean, median, mode, range, standard deviation",
            "Histograms, boxplots, Pareto and run charts",
            "Makes NO claim beyond the data in hand",
            "Northwind: these 34 orders averaged 31.2 hours",
        ]),
        ("INFERENTIAL", "Generalises from the sample to the population", [
            "Hypothesis tests, confidence intervals, regression",
            "Carries a stated risk of being wrong - alpha",
            "Requires a properly random, representative sample",
            "Northwind: ALL orders average 31.2 hours, +/- 1.4",
        ]),
    ], kicker=K, accent=VIOLET)

    d.tile_grid("Population and sample - the vocabulary", [
        ("Population", "Every item of interest - all 4,200 Northwind orders in the month"),
        ("Sample", "The subset you actually measure - 34 randomly selected orders"),
        ("Parameter", "A number describing the POPULATION - mu for mean, sigma for standard deviation"),
        ("Statistic", "A number describing the SAMPLE - x-bar for mean, s for standard deviation"),
        ("Sampling distribution", "The distribution of the sample mean across many repeated samples"),
        ("Standard error", "The spread of that sampling distribution - s divided by the root of n"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.formula_card("Sampling - the two numbers that matter", [
        ("Standard error", "SE = s / sqrt(n)", "s = 6.2 hrs, n = 34: SE = 6.2 / 5.83 = 1.06 hours"),
        ("95% confidence interval", "x-bar +/- 1.96 x SE", "31.2 +/- 1.96 x 1.06 = 29.1 to 33.3 hours"),
        ("Effect of sample size", "n x 4 halves the SE", "n = 34 to n = 136 takes SE from 1.06 to 0.53"),
    ], kicker=K, accent=VIOLET,
        note="Precision improves with the SQUARE ROOT of n - four times the data buys only twice the precision.")

    # ================= E. HYPOTHESIS TESTING =================
    d.big_statement(
        "Hypothesis testing is THE Green Belt skill",
        "It is the mechanism that converts a difference you can see on a chart into a difference "
        "you can defend in a boardroom.",
        K, color=RED)

    d.compare_panels("H0 and Ha", [
        ("H0 - THE NULL", "Always an EQUALS statement", [
            "There is NO difference, NO effect, NO relationship",
            "Example: mu(night) = mu(day)",
            "Example: p(late) = 0.05 target",
            "It is the default we assume true until data says otherwise",
        ]),
        ("Ha - THE ALTERNATIVE", "Not equal, greater than, or less than", [
            "What you actually suspect is going on",
            "Two-tailed: mu(night) is NOT EQUAL to mu(day)",
            "One-tailed: mu(night) is GREATER THAN mu(day)",
            "Choose the tail BEFORE you look at the data",
        ]),
    ], kicker=K, accent=BLUE)

    d.content("Writing hypotheses correctly at Northwind", [
        "WRONG: H0 - the 34 night orders we sampled took the same time as the 34 day orders.",
        "RIGHT: H0 - the mean picking time of ALL night orders equals that of ALL day orders.",
        "The sample comparison needs no test - just subtract the two averages and you are done.",
        "The population claim is the one that carries risk, and therefore the one that needs a test.",
        "H0 always uses equals; the inequality (not equal, greater, less) always lives in Ha.",
        "State both hypotheses in writing BEFORE collecting or looking at the data.",
    ], kicker=K)

    d.flow_h("The hypothesis testing method", [
        "State H0 and Ha as claims about the population, before seeing the data",
        "Set the confidence level and alpha - typically 95 percent and 0.05",
        "Select the correct test from the data type and the question",
        "Collect the sample and run the test",
        "Compare the p-value against alpha and decide",
        "State the conclusion in business language for the sponsor",
    ], kicker=K, color=RED)

    d.formula_card("Confidence level and alpha", [
        ("95% confidence", "alpha = 0.05", "The standard for most business and service processes"),
        ("99% confidence", "alpha = 0.01", "Used where a false alarm is costly - safety, regulatory"),
        ("99.9% confidence", "alpha = 0.001", "Reserved for critical medical and life-safety decisions"),
    ], kicker=K, accent=BLUE,
        note="Alpha is the risk you accept of crying wolf - of declaring a difference that is not really there.")

    d.matrix2x2("Type I and Type II error",
                "The DECISION you make", "The TRUTH about H0",
                [("CORRECT decision",
                  "H0 is TRUE and you fail to reject it. No difference exists and you correctly report none."),
                 ("TYPE I ERROR - alpha",
                  "H0 is TRUE but you REJECT it. A false alarm. PRODUCER RISK, measured by alpha. You chase a cause that is not there."),
                 ("TYPE II ERROR - beta",
                  "H0 is FALSE but you ACCEPT it. A missed signal. CONSUMER RISK, measured by beta. A real cause goes undetected."),
                 ("CORRECT decision",
                  "H0 is FALSE and you reject it. A real difference exists and you detect it. Probability = POWER = 1 - beta.")],
                kicker=K, accent=AMBER)

    d.tile_grid("Type I, Type II and POWER at Northwind", [
        ("TYPE I - PRODUCER RISK", "Reject H0 when H0 is TRUE. Alpha = 0.05 is a 5 percent false alarm rate - you re-slot for no gain."),
        ("TYPE II - CONSUMER RISK", "Accept H0 when H0 is FALSE. Beta is typically 0.10 to 0.20 - night shift IS slower and you miss it."),
        ("POWER = 1 - beta", "Beta = 0.20 gives power = 0.80, the usual target. Power rises with sample size and effect size."),
        ("Set n to reach power", "Low power is why weak studies find nothing. Size the sample for power, never by habit."),
    ], kicker=K, cols=2, accent=AMBER)

    d.tile_grid("The four test selection questions", [
        ("1. What DATA TYPE is it?", "Continuous, or discrete / attribute - this splits the whole map first"),
        ("2. How many LEVELS of X?", "One group, two groups, or more than two groups being compared"),
        ("3. Is the data NORMAL?", "Normal points to the parametric tests; non-normal to the non-parametric"),
        ("4. What are you COMPARING?", "Means, medians, variances or proportions - each has its own test"),
    ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "hypothesis-test-selection")
    if p:
        d.image_slide("The hypothesis test selection map", p, kicker=K,
                      caption="Walk the map from the data type downwards. Every Green Belt should be "
                              "able to reach the right test in under thirty seconds.",
                      accent=TEAL)

    d.tile_grid("Test selection - the discrete and one-sample tests", [
        ("1-PROPORTION", "One factor, one level - comparing a RATE against a target. Late rate vs 5 percent."),
        ("2-PROPORTION", "Comparing PROPORTIONS between two samples. Carrier A late rate vs Carrier B."),
        ("1-SAMPLE T", "Comparing a sample MEAN to a TARGET. Mean cycle time vs the 24-hour promise."),
        ("CHI-SQUARE / 1-VARIANCE", "Comparing a VARIANCE to a target or to another sample's variance."),
    ], kicker=K, cols=2, accent=TEAL)

    d.tile_grid("Test selection - comparing groups", [
        ("PAIRED T", "SAME subjects measured BEFORE and AFTER a change. Same pickers, old vs new route."),
        ("2-SAMPLE T", "Comparing means from TWO DIFFERENT populations. Night pickers vs day pickers."),
        ("ANOVA", "Comparing means of MORE THAN TWO groups. Day vs afternoon vs night shift."),
        ("ONE-SAMPLE WILCOXON", "Comparing a MEDIAN to a target when the data is NOT normal."),
        ("MANN-WHITNEY", "Comparing MEDIANS between two groups when the data is NOT normal."),
        ("Choose before you collect", "The test dictates the sample structure - decide it in the data plan."),
    ], kicker=K, cols=2, accent=TEAL)

    d.big_statement(
        "The classic exam trap: paired or 2-sample?",
        "The SAME children before and after a vaccine is a PAIRED T. Vaccinated versus "
        "unvaccinated children is a 2-SAMPLE T. Same subjects means paired.",
        K, color=RED)

    d.compare_panels("Paired T vs 2-Sample T - tell them apart", [
        ("PAIRED T", "Same subjects, two measurements each", [
            "Same children before and after the vaccine",
            "Same pickers on the old route then the new route",
            "Data comes in natural PAIRS - it tests the differences",
            "More powerful, because it removes person-to-person variation",
        ]),
        ("2-SAMPLE T", "Two different, independent groups", [
            "Vaccinated children vs unvaccinated children",
            "Night shift pickers vs day shift pickers",
            "No pairing - the two samples need not even be equal in size",
            "Tests whether two population MEANS differ",
        ]),
    ], kicker=K, accent=RED)

    p = _dg(d, "p-value")
    if p:
        d.image_slide("The p-value", p, kicker=K,
                      caption="The p-value is compared against alpha - and against alpha only. It is "
                              "never compared against another p-value or against the confidence level.",
                      accent=VIOLET)

    d.compare_panels("The p-value decision rule", [
        ("p LESS THAN alpha", "The signal is real", [
            "REJECT the null hypothesis",
            "ACCEPT the alternative hypothesis",
            "With alpha = 0.05: p = 0.02 - REJECT",
            "Business reading: the difference is significant",
        ]),
        ("p MORE THAN alpha", "Not enough evidence", [
            "FAIL TO REJECT the null hypothesis",
            "You have NOT proved the null is true",
            "With alpha = 0.05: p = 0.13 - FAIL TO REJECT",
            "Business reading: no significant difference detected",
        ]),
    ], kicker=K, accent=VIOLET)

    d.formula_card("Worked example 1 - 1-Proportion test", [
        ("Setup", "n = 142, x = 38 failing", "Hypothesised proportion 0.20; alternative: GREATER THAN"),
        ("Result", "p = 0.031", "0.031 is LESS than alpha = 0.05 - so REJECT the null"),
        ("Conclusion", "Reject H0", "The failure rate IS significantly higher than 20 percent"),
    ], kicker=K, accent=TEAL,
        note="One factor, one level, a rate compared against a target - that is the 1-Proportion test.")

    d.formula_card("Worked example 2 - 2-Sample T test", [
        ("Setup", "Two teams, n = 34 each", "Comparing mean handling time between two independent teams"),
        ("Result", "p = 0.255", "0.255 is GREATER than alpha = 0.05 - so FAIL TO REJECT"),
        ("Conclusion", "Fail to reject H0", "13.76 vs 12.82 minutes: NOT significantly different"),
    ], kicker=K, accent=BLUE,
        note="The means differ by 0.94 minutes on the sample - but not by enough to claim the populations differ.")

    d.tile_grid("Failing to reject does NOT prove H0", [
        ("Check the power", "Under 80 percent power and the test was unlikely to find anything"),
        ("Check the sample size", "n = 10 will miss differences that n = 100 would find easily"),
        ("Look at the effect size", "A large practical gap with a large p means underpowered, not equal"),
        ("Check the measurement system", "Gage variation inflates the noise and buries the signal"),
        ("Report it honestly", "Say no significant difference detected, never no difference exists"),
        ("Consider re-testing", "Larger n, or a paired design, may reveal what the first test missed"),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("Translating statistics into sponsor language", [
        ("WHAT YOU RAN", "The statistical statement", [
            "2-Sample T, alpha = 0.05, n = 34 per shift",
            "Night mean 41.3 min vs day mean 26.4 min",
            "p = 0.003, well below alpha",
            "Reject H0 - the population means differ",
        ]),
        ("WHAT YOU SAY", "The business statement", [
            "Night shift takes about 15 minutes longer per order",
            "That gap drives roughly half of all late deliveries",
            "There is under a 1 percent chance this is a fluke",
            "Fixing night slotting is worth about S$180k a year",
        ]),
    ], kicker=K, accent=TEAL)

    # ================= F. CORRELATION AND REGRESSION =================
    d.tile_grid("Read the scatter plot before any number", [
        ("DIRECTION", "Positive rises left to right; negative falls. Establish the sign first."),
        ("SHAPE", "Straight or curved - a curve makes the linear R badly misleading"),
        ("STRENGTH", "A tight band means a strong relationship; a wide cloud means a weak one"),
        ("OUTLIERS", "A single far point can create or destroy an apparent correlation"),
        ("CLUSTERS", "Two separate clouds mean two processes - split and re-plot"),
        ("RANGE", "A relationship proven over 5 to 25 says nothing at all about 50"),
    ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "correlation-r-values")
    if p:
        d.image_slide("Correlation coefficient R", p, kicker=K,
                      caption="R runs from -1 (perfect negative) through 0 (no linear relationship) to "
                              "+1 (perfect positive). The sign is direction; the magnitude is strength.",
                      accent=BLUE)

    d.tile_grid("Interpreting R", [
        ("R = +1", "Perfect positive - every point sits exactly on an upward straight line"),
        ("R = -1", "Perfect negative - every point sits exactly on a downward straight line"),
        ("R = 0", "No LINEAR relationship - though a curved relationship may still exist"),
        ("THRESHOLD: 0.4", "Correlation is considered to occur at R of 0.4 or greater, or -0.4 or less"),
        ("Between -0.4 and 0.4", "Too weak to treat as a working relationship - do not build a fix on it"),
        ("Sign is not strength", "R = -0.85 is far stronger than R = +0.30, negative or not"),
    ], kicker=K, cols=2, accent=BLUE)

    d.formula_card("Coefficient of determination - worked example", [
        ("Correlation", "R = 0.860624", "A strong positive correlation, well above the 0.4 threshold"),
        ("R-squared", "r2 = R x R = 0.74", "0.860624 squared is approximately 0.74"),
        ("Interpretation", "74% explained", "About 74 percent of the variation in Y is related to X"),
        ("The remainder", "26% unexplained", "26 percent comes from other Xs or from measurement noise"),
    ], kicker=K, accent=VIOLET,
        note="A single X explaining 74 percent of Y is a strong lever - but 26 percent still lies elsewhere.")

    p = _dg(d, "regression-analysis")
    if p:
        d.image_slide("Linear regression - fitting the line", p, kicker=K,
                      caption="Regression fits the line that minimises the squared vertical distances "
                              "from the points, giving an equation you can predict with.",
                      accent=TEAL)

    d.formula_card("Regression - the fitted line and predictions", [
        ("The model", "y = mx + c", "m is the slope - the change in Y per one unit change in X"),
        ("Fitted line", "y = 3.3497x + 27.561", "Slope 3.3497, intercept 27.561, from the regression output"),
        ("Predict at x = 5", "y = 3.3497(5) + 27.561", "y = 16.7485 + 27.561 = 44.30"),
        ("Predict at x = 25", "y = 3.3497(25) + 27.561", "y = 83.7425 + 27.561 = 111.30"),
    ], kicker=K, accent=TEAL,
        note="Every extra unit of X adds 3.3497 to Y; at X = 0 the model predicts Y = 27.561.")

    d.tile_grid("Using regression in an improvement project", [
        ("Predict Y from X", "Set X and the equation gives the expected Y - a planning tool"),
        ("Solve in reverse", "Set the Y you need and solve for X to get the OPERATING WINDOW"),
        ("Northwind example", "Need cycle time under 24 hrs, so solve for the maximum pick-path length"),
        ("Never extrapolate", "Fitted over x = 5 to 25? Then x = 60 is a guess, not a prediction"),
        ("Check the residuals", "Residuals must scatter randomly - a pattern means the model is wrong"),
        ("Confirm with a pilot", "The equation sets the target; the pilot proves it in the real process"),
    ], kicker=K, cols=2, accent=TEAL)

    d.compare_panels("Does your data qualify for regression?", [
        ("QUALIFIES", "Both variables quantitative", [
            "Pick-path metres vs picking minutes",
            "Order line count vs cycle time hours",
            "Staff on shift vs orders despatched",
            "Both X and Y are continuous or ratio data",
        ]),
        ("DOES NOT QUALIFY", "One variable is a category", [
            "Carrier name vs late orders - carrier is a label",
            "Product family vs defects - family is a label",
            "Shift name vs picking time - shift is a label",
            "Use Pareto, or a 2-Sample T / ANOVA instead",
        ]),
    ], kicker=K, accent=AMBER)

    d.big_statement(
        "Correlation does not prove causation",
        "But it does not negate it either. Correlation STARTS a causal argument - confirm "
        "it with process knowledge, a designed experiment, or a pilot.",
        K, color=RED)

    d.tile_grid("Confirming that a correlation is causal", [
        ("Process knowledge", "Can an engineer explain the physical mechanism from X to Y?"),
        ("Temporal order", "X must change BEFORE Y changes - effects never precede their causes"),
        ("Look for a lurking X", "Ice cream and drownings both track summer - the season is the cause"),
        ("Designed experiment", "Deliberately set X at levels and observe Y - the strongest evidence"),
        ("Run a pilot", "Change X in one zone, hold the others - the Green Belt's practical DOE"),
        ("Dose-response", "More X producing proportionately more Y strengthens the causal case"),
    ], kicker=K, cols=2, accent=RED)

    d.content("Northwind - the Analyze phase conclusion", [
        "Stratification: 73 of 142 picking delays sit on night shift, concentrated in bulk beverages.",
        "5 Whys: bulk beverage SKUs are slotted by supplier code rather than by pick frequency.",
        "2-Sample T: night 41.3 min vs day 26.4 min, p = 0.003 - a real and significant difference.",
        "Regression: pick-path length explains about 74 percent of the variation in picking time.",
        "Carrier was tested and CLEARED - a flat stratification, so it is logged as a rejected cause.",
        "Proven root cause: the slotting rule. That is what Improve will change and Control will hold.",
    ], kicker=K)

    d.tile_grid("Common Analyze phase mistakes", [
        ("Skipping straight to solutions", "The team names a fix in week one and spends Analyze justifying it"),
        ("Testing without stratifying", "Pooled data hides the very concentration you are looking for"),
        ("Wrong test chosen", "2-Sample T on paired data - a correct calculation of the wrong thing"),
        ("Treating p as proof of size", "A tiny p on a trivial difference is significant but worthless"),
        ("Correlation read as cause", "The most expensive single error in the whole Analyze phase"),
        ("Stopping 5 Whys at a person", "Human error is a symptom - keep drilling to the system"),
    ], kicker=K, cols=2, accent=RED)

    d.checkpoint("Analyze phase - checkpoint", [
        "Distinguish common cause from special cause, and give the correct response to each.",
        "State the numeric rule for a TREND and for a SHIFT on a run chart.",
        "Same children before and after a vaccine - which test, and why not the other one?",
        "Alpha is 0.05 and p = 0.13. What is your decision, and what have you NOT proved?",
        "Define Type I and Type II error, name each risk, and state what power equals.",
        "R = 0.860624. What is r-squared, and what exactly does that number mean?",
    ], K)
