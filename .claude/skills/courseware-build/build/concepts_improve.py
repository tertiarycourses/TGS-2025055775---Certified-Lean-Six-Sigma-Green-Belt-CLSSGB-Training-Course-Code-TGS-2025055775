#!/usr/bin/env python3
"""Improve teaching slides — Green Belt depth, DMAIC order."""
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


def improve_phase(d):
    K = "IMPROVE"

    # ================= A. WHAT IMPROVE DELIVERS =================
    d.tile_grid("What the Improve phase delivers", [
        ("A generated solution set", "Many candidate solutions, each traced to a statistically proven root cause"),
        ("A selected solution", "Chosen by the team with a weighted selection matrix, not by the loudest voice"),
        ("A risk assessment", "FMEA on the new process, with actions taken on the highest RPNs"),
        ("Piloted evidence", "The solution tested at small scale against the baseline before full rollout"),
        ("An implementation plan", "Who does what, by when, with the change management wrapped around it"),
        ("A demonstrated improvement", "Northwind late deliveries moving from 8.5% toward the 3.0% target"),
    ], kicker=K, cols=2, accent=AMBER)

    d.flow_h("Steps of the Improve phase", [
        "Generate many candidate solutions against each proven root cause",
        "Map every solution back to a cause - discard the orphans",
        "Select using weighted criteria agreed by the team",
        "Assess risk with FMEA and mistake-proof the new design",
        "Pilot at small scale against the baseline, then decide",
        "Plan the rollout and manage the change with the people",
    ], kicker=K, color=AMBER)

    d.compare_panels("Legitimate solution vs pet project", [
        ("Legitimate", "Traceable to proven data", [
            "Cause proved by a hypothesis test at p < 0.05",
            "Solution attacks that specific cause",
            "Expected effect on Y can be estimated",
            "Measurable against the 8.5% baseline",
        ]),
        ("Pet project", "Traceable to somebody's opinion", [
            "Cause never tested, only asserted",
            "Solution was chosen before the analysis",
            "Effect on Y cannot be described",
            "Usually expensive and usually IT",
        ]),
    ], kicker=K, accent=RED)

    # ================= B. SOLUTION GENERATION =================
    d.tile_grid("Solution generation techniques", [
        ("Classic brainstorming", "Group generates aloud; quantity first, no criticism, build on others' ideas"),
        ("Brainwriting", "Each person writes 3 ideas silently, then passes the sheet on to be built upon"),
        ("Six Thinking Hats", "Deliberately switch modes so every angle gets equal airtime"),
        ("Anti-brainstorming", "Ask how to make the problem WORSE, then invert every answer"),
        ("SCAMPER", "Substitute, Combine, Adapt, Modify, Put to other use, Eliminate, Reverse"),
        ("Benchmarking", "Borrow proven ideas from inside, from rivals and from other industries"),
    ], kicker=K, cols=2, accent=BLUE)

    d.two_col("Anti-brainstorming at Northwind",
        [("How could we make late deliveries MUCH worse?", 0),
         ("Give pickers no route sequence at all", 1),
         ("Release all orders to the floor at 4pm", 1),
         ("Let anyone override the dispatch priority", 1),
         ("Never tell drivers about traffic or road closures", 1),
         ("Train new pickers by watching a colleague once", 1)],
        [("Now invert each answer into a solution", 0),
         ("Print an optimised pick route on every pick list", 1),
         ("Level order release across the whole shift", 1),
         ("Lock dispatch priority to a documented rule", 1),
         ("Push live traffic alerts to the driver app", 1),
         ("Certify pickers against standard work before solo picking", 1)],
        kicker=K, lhead="Make it worse", rhead="Invert it", lcolor=RED, rcolor=TEAL)

    # ================= C. BENCHMARKING =================
    d.compare_panels("Three types of benchmarking", [
        ("Internal", "Another site or shift in your own firm", [
            "Cheapest and fastest to arrange",
            "Data is comparable and accessible",
            "Northwind: the Tuas DC runs 3.1% late",
            "Risk: you only copy your own habits",
        ]),
        ("Competitive", "A direct competitor in your market", [
            "Most relevant performance comparison",
            "Hardest to get real data from",
            "Use public reports and industry surveys",
            "Risk: legal and confidentiality limits",
        ]),
        ("Functional", "Best-in-class in ANY industry", [
            "Compare the FUNCTION, not the product",
            "Fulfilment: study a pizza chain or courier",
            "Usually the source of breakthroughs",
            "Risk: needs the most adaptation work",
        ]),
    ], kicker=K, accent=TEAL)

    p = _dg(d, "benchmarking-steps")
    if p:
        d.image_slide("The four benchmarking steps", p, kicker=K,
                      caption="Plan what to benchmark, collect the comparison data, analyse the gap, "
                              "then ADAPT - never simply copy.", accent=TEAL)

    # ================= D. MAPPING SOLUTIONS TO CAUSES =================
    d.two_col("Northwind: solutions mapped to proven causes",
        [("Proven root cause (from Analyse)", 0),
         ("Late order release after the 4pm cut-off", 1),
         ("Pick errors on the top 12 fast-moving SKUs", 1),
         ("No documented dispatch priority rule", 1),
         ("New pickers untrained on the scanner", 1),
         ("Unmapped: 'the WMS is old'", 1)],
        [("Candidate solution", 0),
         ("Level order release across the shift (heijunka)", 1),
         ("Poka-yoke: scan-verify SKU before the tote closes", 1),
         ("Standard work: one documented dispatch rule", 1),
         ("Certification against standard work before solo picking", 1),
         ("DISCARD - no proven cause, this is a pet project", 1)],
        kicker=K, lhead="Cause", rhead="Solution", lcolor=RED, rcolor=TEAL)

    # ================= E. SOLUTION SELECTION MATRIX =================
    p = _dg(d, "solution-selection-matrix")
    if p:
        d.image_slide("The solution selection matrix", p, kicker=K,
                      caption="Score each solution against weighted criteria, then total. "
                              "This is the tool your Practical Performance Task 2 requires.", accent=BLUE)

    d.tile_grid("The four standard selection criteria", [
        ("Feasibility", "Is it practical? Can we do it with the people, skills and systems we have?"),
        ("Cost", "Is it cost-effective? Capital plus running cost against the benefit"),
        ("Impact", "Does it significantly reduce the defect? How much of the 8.5% does it remove?"),
        ("Time to implement", "How quickly can it be in place and producing the effect?"),
    ], kicker=K, cols=2, accent=BLUE)

    d.flow_h("How to run the selection matrix", [
        "Agree the criteria and the WEIGHT of each with the team",
        "Agree the scoring scale BEFORE scoring - e.g. 1 = poor, 5 = excellent",
        "Score every solution against every criterion, as a team, not alone",
        "Multiply each score by its weight and total the row",
        "Rank descending, then sanity-check the top ranked against the cause map",
    ], kicker=K, color=BLUE)

    d.formula_card("Calculating the weighted score", [
        ("Weighted score", "Sum of (score x weight)",
         "Scan-verify: (5x3)+(4x2)+(5x4)+(4x1) = 47"),
        ("Criterion weight", "Importance rating 1 - 5",
         "Impact weighted 4; time to implement weighted 1"),
        ("Score scale", "1 = poor  ...  5 = excellent",
         "Agreed and written down BEFORE any solution is scored"),
    ], kicker=K, accent=BLUE,
        note="Same scale, same weights, every solution - otherwise the ranking is meaningless.")

    d.two_col("Northwind worked example - weights and scores",
        [("Weights agreed by the team", 0),
         ("Impact on late % - weight 4", 1),
         ("Feasibility - weight 3", 1),
         ("Cost effectiveness - weight 2", 1),
         ("Time to implement - weight 1", 1),
         ("Scale agreed: 1 = poor, 5 = excellent", 1)],
        [("Weighted totals", 0),
         ("Scan-verify poka-yoke = 47  (rank 1)", 1),
         ("Level the order release = 42  (rank 2)", 1),
         ("Documented dispatch rule = 39  (rank 3)", 1),
         ("Picker certification = 35  (rank 4)", 1),
         ("Replace the WMS = 22  (rank 5, and no proven cause)", 1)],
        kicker=K, lhead="Setup", rhead="Result", lcolor=AMBER, rcolor=TEAL)

    # ================= F. EFFORT-IMPACT, CBA, PUGH =================
    d.formula_card("Cost-benefit analysis and payback", [
        ("Net benefit", "Annual benefit - annual cost",
         "$180,000 saved - $30,000 running = $150,000 per year"),
        ("Benefit-cost ratio", "Benefit / Cost",
         "180,000 / 30,000 = 6.0 - every $1 spent returns $6"),
        ("Payback period", "Investment / Annual net benefit",
         "$75,000 / $150,000 = 0.5 years, i.e. about 6 months"),
    ], kicker=K, accent=VIOLET,
        note="Have Finance validate the benefit figure - a saving they will not sign off is not a saving.")

    # ================= G. 5S =================
    p = _dg(d, "5s-wheel")
    if p:
        d.image_slide("The 5S cycle", p, kicker=K,
                      caption="Sort, Set in order, Shine, Standardise, Sustain - the fifth S is the "
                              "one that fails, because it needs audits and leadership.", accent=TEAL)

    d.flow_h("The five S", [
        "SORT: remove everything not needed for today's work",
        "SET IN ORDER: a place for everything, positioned by frequency of use",
        "SHINE: clean and inspect - cleaning IS inspection",
        "STANDARDISE: make the first three S the documented normal",
        "SUSTAIN: audit, coach and lead until it survives without you",
    ], kicker=K, color=TEAL)

    d.tile_grid("5S - physical and digital examples", [
        ("Sort - physical", "Clear the obsolete totes and dead stock out of the pick aisle"),
        ("Sort - digital", "Archive the 40 dead report files nobody has opened in a year"),
        ("Set in order - physical", "Fast-moving SKUs at waist height, slow movers high or low"),
        ("Set in order - digital", "One agreed folder tree; the live dispatch file pinned, not searched"),
        ("Shine - physical", "Daily scanner and label-printer clean-and-check by the shift team"),
        ("Shine - digital", "Weekly data hygiene: purge duplicate customer address records"),
        ("Standardise - both", "Shadow boards and aisle labels; a file naming convention that is enforced"),
        ("Sustain - both", "A short weekly 5S audit with a score, reviewed by the shift leader"),
    ], kicker=K, cols=2, accent=TEAL)

    # ================= H. POKA-YOKE =================
    d.big_statement(
        "Poka-yoke: design the error out",
        "Mistake proofing assumes people will err, because they will. Change the process "
        "so the error is impossible, or is caught the instant it happens.",
        K, color=RED)

    p = _dg(d, "poka-yoke-examples")
    if p:
        d.image_slide("Poka-yoke examples", p, kicker=K,
                      caption="Everyday mistake proofing: the design makes the wrong action "
                              "physically impossible rather than merely discouraged.", accent=RED)

    d.ladder("Levels of mistake proofing - climb toward prevention", [
        ("4. Inspect after the fact", "Found by audit or by the customer - not mistake proofing at all"),
        ("3. Detect downstream", "Caught before it reaches the customer - internal damage done"),
        ("2. Detect at source", "Caught the instant it occurs, at the workstation, by the operator"),
        ("1. Prevent", "The error cannot physically occur at all - the strongest control"),
    ], kicker=K, accent=RED,
        note="Always climb toward prevention: a connector that only fits one way beats a checklist.")

    d.compare_panels("Prevention beats detection", [
        ("Prevent", "The error is impossible", [
            "USB-C plug fits either way round",
            "Car will not start unless it is in park",
            "System blocks dispatch without a scan",
            "Strongest, and usually cheapest to run",
        ]),
        ("Detect at source", "Caught as it happens", [
            "Scanner beeps on the wrong SKU at the tote",
            "Tote weight check fails at the pack bench",
            "Form rejects an invalid postcode on entry",
            "Good - but the error still occurred",
        ]),
        ("Detect downstream", "Caught before it escapes", [
            "Final audit at the loading bay",
            "100% inspection before the van leaves",
            "Weakest and the most expensive to sustain",
            "A checklist lives here, not at level 1",
        ]),
    ], kicker=K, accent=RED)

    # ================= I. PULL, JIT, HEIJUNKA, JIDOKA =================
    p = _dg(d, "push-vs-pull")
    if p:
        d.image_slide("Push versus pull", p, kicker=K,
                      caption="Push is driven by a schedule upstream; pull is triggered by real "
                              "consumption downstream.", accent=BLUE)

    d.compare_panels("Push vs pull, and the kanban signal", [
        ("Push", "Work released by a schedule", [
            "Built to a forecast, which is always wrong",
            "Queues and WIP build between steps",
            "Defects hide inside the queue for days",
            "Bottleneck is drowned, upstream is idle",
        ]),
        ("Pull", "Work released by a signal", [
            "Downstream consumption triggers upstream",
            "WIP is capped by the number of signals",
            "Problems surface fast - the queue is short",
            "Lead time becomes predictable",
        ]),
        ("Kanban", "The signal itself", [
            "A card, a bin, a slot or a screen tile",
            "No card means no production - WIP is capped",
            "Removing a card deliberately shrinks WIP",
            "Northwind: capped pick waves per hour",
        ]),
    ], kicker=K, accent=BLUE)

    d.two_col("Northwind: order release before and after levelling",
        [("Before - peaked release", 0),
         ("09:00-15:00: pickers idle, 40% utilisation", 1),
         ("16:00-18:00: 65% of the day's orders released", 1),
         ("Overtime paid almost every evening", 1),
         ("Error rate rises sharply under the rush", 1),
         ("Late deliveries cluster on the evening wave", 1)],
        [("After - levelled release", 0),
         ("Orders released in even waves across the shift", 1),
         ("Peak headcount requirement drops", 1),
         ("Overtime cost falls, idle time falls too", 1),
         ("Error rate stabilises - no end-of-day rush", 1),
         ("Late % falls without adding any headcount", 1)],
        kicker=K, lhead="Peaks", rhead="Levelled", lcolor=RED, rcolor=TEAL)

    # ================= J. STANDARD WORK =================
    d.tile_grid("The elements of standard work", [
        ("The work sequence", "The exact order of steps, the same way every time, by every operator"),
        ("Takt time", "The customer demand rate the sequence must keep pace with"),
        ("Standard WIP", "The minimum in-process stock needed to run the sequence without stalling"),
        ("Quality checks", "Where the check happens, what is checked and what to do on a fail"),
    ], kicker=K, cols=2, accent=AMBER)

    # ================= K. FMEA =================
    p = _dg(d, "fmea-example")
    if p:
        d.image_slide("FMEA worksheet example", p, kicker=K,
                      caption="One row per failure mode: effect, cause, current controls, then "
                              "S, O and D rated 1-10 to give the RPN.", accent=RED)

    d.tile_grid("What each FMEA row captures", [
        ("Process step", "The specific step being assessed - work down the new process map"),
        ("Potential failure mode", "What could go wrong at this step - wrong SKU picked into the tote"),
        ("Potential effect", "What the CUSTOMER experiences - wrong item delivered, order returned"),
        ("Potential cause", "Why the failure mode occurs - two similar SKUs in adjacent bins"),
        ("Current controls", "What exists today to prevent or detect it - a visual check only"),
        ("S, O, D and RPN", "The three ratings and their product, used to rank the risk"),
    ], kicker=K, cols=2, accent=RED)

    d.compare_panels("The three FMEA ratings, each 1 to 10", [
        ("Severity (S)", "How serious for the customer", [
            "1 = customer would not even notice",
            "10 = safety, legal or total loss of the order",
            "Rate the EFFECT, not the failure mode",
            "Severity is rarely reduced without redesign",
        ]),
        ("Occurrence (O)", "How likely is the cause", [
            "1 = extremely unlikely, once in years",
            "10 = happens almost every shift",
            "Use real data where you have it",
            "Poka-yoke is how you drive O down",
        ]),
        ("Detection (D)", "SCALE IS INVERTED", [
            "1 = almost certainly caught before escape",
            "10 = escapes to the customer undetected",
            "A HIGH D is BAD - this trips everybody up",
            "Better controls lower D, they do not raise it",
        ]),
    ], kicker=K, accent=RED)

    d.formula_card("Risk Priority Number", [
        ("RPN", "RPN = S x O x D",
         "Wrong SKU picked: S=7, O=6, D=5 gives RPN = 210"),
        ("Ranking", "Sort RPN descending",
         "Address the highest RPN rows first, then work down the list"),
        ("Projected RPN", "Recalculate S x O x D after action",
         "Scan-verify drops D from 5 to 2: 7 x 6 x 2 = 84"),
    ], kicker=K, accent=RED,
        note="RPN ranges from 1 to 1000. It is a ranking device, not an absolute measure of risk.")

    d.big_statement(
        "Severity 9 or 10 always requires action",
        "Act on any Severity of 9 or 10 REGARDLESS of its RPN. A rare, well-detected "
        "catastrophe still scores a low RPN - and still ends careers.",
        K, color=RED)

    d.flow_h("Running an FMEA", [
        "List every step of the NEW process and its failure modes",
        "For each mode record the effect, the cause and the current controls",
        "Rate S, O and D from 1 to 10 with the team using agreed scales",
        "Calculate RPN, sort descending, flag all S = 9 or 10 rows",
        "Assign an action, an owner and a date to the top rows",
        "Recalculate the projected RPN and verify it after implementation",
    ], kicker=K, color=RED)

    d.two_col("Northwind FMEA - top rows and actions",
        [("Failure mode and initial rating", 0),
         ("Wrong SKU picked: S=7 O=6 D=5, RPN 210", 1),
         ("Order missed the 4pm cut-off: S=6 O=7 D=4, RPN 168", 1),
         ("Van dispatched with wrong priority: S=6 O=5 D=5, RPN 150", 1),
         ("Chilled item left out of chiller: S=9 O=2 D=3, RPN 54", 1),
         ("Address record stale: S=5 O=4 D=6, RPN 120", 1)],
        [("Action and projected RPN", 0),
         ("Scan-verify at tote close - D 5 to 2, RPN 84", 1),
         ("Level the release across the shift - O 7 to 3, RPN 72", 1),
         ("Lock the documented dispatch rule - O 5 to 2, RPN 60", 1),
         ("ACTED ON DESPITE RPN 54 - Severity is 9", 1),
         ("Address validation at order entry - D 6 to 2, RPN 40", 1)],
        kicker=K, lhead="Before", rhead="After", lcolor=RED, rcolor=TEAL)

    # ================= L. DESIGN OF EXPERIMENTS =================
    d.big_statement(
        "DOE: change several factors on purpose",
        "DOE varies factors together so you learn their individual effects AND how they "
        "interact - in far fewer runs than trial and error.",
        K, color=VIOLET)

    d.compare_panels("Why one-factor-at-a-time is inadequate", [
        ("OFAT", "Change one thing, hold the rest", [
            "Feels rigorous and is easy to explain",
            "Needs many runs for very little information",
            "CANNOT reveal INTERACTIONS between factors",
            "Only ever finds each factor's individual effect",
        ]),
        ("Designed experiment", "Vary factors together, by design", [
            "Estimates main effects AND interactions",
            "More information from fewer total runs",
            "Effects are estimated with known precision",
            "Result generalises across the factor space",
        ]),
    ], kicker=K, accent=VIOLET)

    d.tile_grid("DOE vocabulary", [
        ("Response (Y)", "The output you are trying to improve - delivery time in hours"),
        ("Factor (X)", "An input you deliberately set - driver experience, GPS, dispatcher policy"),
        ("Level", "The setting a factor is run at - GPS: no or yes; experience: 0 or 1 year"),
        ("Run", "One combination of all factor levels, with the response measured"),
        ("Main effect", "The average change in Y when one factor moves from low to high"),
        ("Interaction", "When one factor's effect on Y DEPENDS on the level of another factor"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.formula_card("Full factorial run count", [
        ("2^k design", "Runs = 2 raised to power k",
         "k = 4 factors at 2 levels each gives 2^4 = 16 runs"),
        ("With replication", "Runs = 2^k x replicates",
         "16 runs replicated twice = 32 deliveries measured"),
        ("Goal for this study", "Baseline - target reduction",
         "72 hour baseline, goal to reduce by 24 hours"),
    ], kicker=K, accent=VIOLET,
        note="A full factorial tests every combination, so every main effect and interaction is estimable.")

    d.tile_grid("Worked DOE - furniture delivery process", [
        ("The response", "Delivery time in hours - baseline 72 hours, goal to reduce by 24 hours"),
        ("Factor 1: driver experience", "Two levels: 0 years of experience versus 1 year"),
        ("Factor 2: GPS", "Two levels: no GPS fitted versus GPS fitted"),
        ("Factor 3: dispatcher policy", "Two levels: no policy versus dispatcher follows the policy"),
        ("Factor 4: pieces of furniture", "Two levels: 1 piece versus 5 pieces on the delivery"),
        ("The design", "Four factors at two levels = a 16-run full factorial grid"),
    ], kicker=K, cols=2, accent=VIOLET)

    d.compare_panels("Existing data vs a designed experiment", [
        ("Existing (historical) data", "Already sitting in the system", [
            "Faster and much cheaper to obtain",
            "No disruption to live operations",
            "You did NOT control the other variables",
            "Factors are often confounded - causality is weak",
        ]),
        ("Designed experiment", "Run deliberately, to a plan", [
            "You set the levels and randomise the runs",
            "Other variables are held or balanced out",
            "Supports a genuine causal conclusion",
            "Costs money, time and operational disruption",
        ]),
    ], kicker=K, accent=AMBER)

    # ================= M. PILOTING =================
    d.tile_grid("Designing the pilot", [
        ("Scope", "One shift, one product family, one bay - small enough to control and reverse"),
        ("Duration", "Long enough to cover normal variation, including a peak day and a quiet day"),
        ("Success criteria", "Numeric, agreed up front, measured AGAINST THE BASELINE of 8.5%"),
        ("Measurement method", "The same operational definition and gage used in Measure - no new metric"),
        ("Rollback plan", "Exactly how to revert, who decides, and how fast - agreed before you start"),
        ("Who is involved", "The operators who do the work, briefed and trained before day one"),
    ], kicker=K, cols=2, accent=TEAL)

    d.flow_h("The three pilot outcomes", [
        "SCALE UP: criteria met, no new risks - plan the full rollout",
        "ADJUST AND RE-PILOT: partial effect - fix the weakness and run it again",
        "STOP: no effect or new risks appear - revert and return to the cause analysis",
    ], kicker=K, color=TEAL)

    d.run_chart("Northwind pilot: weekly late % on the pilot shift",
        [("W1", 8.6), ("W2", 8.4), ("W3", 8.7), ("W4", 6.2), ("W5", 4.9),
         ("W6", 4.1), ("W7", 3.4), ("W8", 3.2)],
        kicker=K,
        note="Scan-verify and levelled release went live at W4. A sustained shift, not a single good week.",
        median_label="Median")

    # ================= N. IMPLEMENTATION AND CHANGE =================
    # ================= O. TOLLGATE =================
    d.tile_grid("The Improve tollgate checklist", [
        ("Solutions map to proven causes", "Every selected solution names the cause and the evidence for it"),
        ("Selection was documented", "Weighted matrix with agreed criteria, weights and scale, scored as a team"),
        ("Risk assessed", "FMEA complete; top RPNs actioned and all S = 9 or 10 rows addressed"),
        ("Piloted against the baseline", "Results measured with the Measure-phase definitions, versus 8.5%"),
        ("Benefit validated", "Finance has agreed the cost-benefit and the payback period"),
        ("Ready for Control", "Implementation plan, standard work and owners in place for full rollout"),
    ], kicker=K, cols=2, accent=AMBER)

    d.checkpoint("Checkpoint - Improve", [
        "Why must a solution be traceable to a PROVEN root cause before it is considered?",
        "In a solution selection matrix, what must be agreed BEFORE any scoring begins?",
        "Name the three levels of poka-yoke - and say which is strongest, and why.",
        "In FMEA, why is a Detection score of 10 bad news rather than good news?",
        "Which FMEA rows must be actioned regardless of their RPN?",
        "What can a designed experiment reveal that one-factor-at-a-time cannot?",
    ], K)
