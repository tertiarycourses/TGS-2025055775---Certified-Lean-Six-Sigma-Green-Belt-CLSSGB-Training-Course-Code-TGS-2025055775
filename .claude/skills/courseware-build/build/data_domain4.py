"""
Domain 4 — The IMPROVE phase.

Labs 19-22. The Yellow Belt suggests improvements; the Green Belt SELECTS them
against weighted criteria, RISK-ASSESSES them with FMEA before they go live, and
PILOTS them against the measured baseline before committing.

Lab 21 (solution selection matrix) maps directly to PP Assessment Task 2 (A3).
"""

DOMAIN4 = [
    dict(
        num=19, topic=4,
        title="Solution Generation, Benchmarking and Brainwriting",
        objective="Generate a wide solution set against the proven root causes (A5).",
        desc="Only now — with root causes proven by data — is it legitimate to talk about "
             "solutions. Diverge deliberately before converging: structured techniques produce "
             "far better solution sets than an open discussion dominated by the loudest voice.",
        build="A solution log of at least fifteen candidate solutions mapped to proven root causes.",
        services="Brainstorming, brainwriting, six thinking hats, anti-brainstorming, benchmarking, SCAMPER",
        steps=[
            ("List your validated root causes from Lab 17 and 18 — every solution must trace to one of them. Solutions without a cause are pet projects.", ""),
            ("Run a structured brainstorm with the ground rules displayed: no criticism during generation, quantity over quality, build on others' ideas, wild ideas welcome.", ""),
            ("Run brainwriting for the quieter participants: each person writes three ideas silently, then passes the sheet on for others to build upon.", ""),
            ("Apply anti-brainstorming: ask how you could make the problem WORSE, then invert each answer into an improvement.", ""),
            ("Use six thinking hats to examine the leading ideas from different perspectives — facts, feelings, risks, benefits, creativity and process.", ""),
            ("Benchmark: identify who performs this process best, internally or in another industry, and record what they do differently.", ""),
            ("Follow the four benchmarking steps — plan what to benchmark, collect the comparison data, analyse the gap, and adapt rather than copy.", ""),
            ("Map every generated solution against the root cause it addresses in a two-column table, and discard any that address no proven cause.", ""),
            ("Group similar solutions and remove exact duplicates, keeping at least fifteen distinct candidates.", ""),
        ],
        test="You have at least fifteen distinct solutions, every one traces to a root cause proven with data, and at least three came from benchmarking.",
    ),
    dict(
        num=20, topic=4,
        title="Lean Countermeasures — 5S, Poka-Yoke, Pull, JIT and Standard Work",
        objective="Apply proven Lean countermeasures to the identified wastes (A5).",
        desc="Lean supplies a catalogue of countermeasures with a strong track record. Rather than "
             "inventing a fix from scratch, match the waste type you found in Lab 8 to the "
             "countermeasure that reliably addresses it — and prefer poka-yoke, which prevents "
             "the error, over inspection, which merely detects it.",
        build="A countermeasure plan applying 5S, poka-yoke, pull and standard work to your process.",
        services="5S, poka-yoke levels, pull system, kanban, JIT, heijunka, jidoka, standard work",
        steps=[
            ("Apply 5S to the physical or digital workspace: Sort (remove what is not needed), Set in order (a place for everything), Shine (clean and inspect), Standardise (make it visual), Sustain (audit it).", ""),
            ("Design a poka-yoke for your highest-severity defect. Work through the three levels: prevent the error occurring, detect it as it occurs, or detect it before it passes downstream.", ""),
            ("Prefer prevention over detection — a connector that only fits one way beats a checklist asking the operator to check the orientation.", ""),
            ("Evaluate whether a pull system would help: does work get pushed into the process faster than it can be consumed, creating queues?", ""),
            ("Design a kanban signal that lets a downstream step pull work only when it has capacity.", ""),
            ("Consider heijunka (load levelling) if demand arrives in peaks — levelling the load reduces both overtime and idle time.", ""),
            ("Apply jidoka: build in the ability to stop the process automatically when a defect is detected, rather than continuing to produce defects.", ""),
            ("Write standard work for the improved method: the sequence, the takt time, the standard WIP and the quality checks.", ""),
            ("Make the standard work visual — a photo or one-page diagram at the workstation beats a document in a shared drive.", ""),
            ("Map each countermeasure back to the specific waste from your DOWNTIME analysis in Lab 8.", ""),
        ],
        test="Every countermeasure traces to a specific waste, and your poka-yoke prevents or detects the error rather than relying on someone remembering to check.",
    ),
    dict(
        num=21, topic=4,
        title="Solution Selection Matrix and Cost-Benefit Analysis",
        objective="Select the most feasible and impactful solutions using weighted criteria (A3, A5).",
        desc="This lab maps directly to Task 2 of the Practical Performance assessment. Score every "
             "candidate solution against weighted criteria so the decision is transparent and "
             "defensible — feasibility, cost, impact and time to implement — then confirm the "
             "selection with a cost-benefit analysis.",
        build="A weighted solution selection matrix with ranked results and a cost-benefit analysis.",
        services="Solution selection matrix, weighted criteria, feasibility, cost, impact, effort-impact grid, cost-benefit analysis",
        steps=[
            ("List your candidate solutions from Labs 19 and 20 down the rows of the matrix.", ""),
            ("Define the selection criteria across the columns: Feasibility (is it practical to implement?), Cost (is it cost-effective?), Impact (does it significantly reduce the defect?), and Time to implement (how quickly?).", ""),
            ("Assign a weight to each criterion reflecting what matters to the sponsor — impact and cost usually carry the highest weights.", ""),
            ("Agree the scoring scale before scoring anything, and write down what a 1 and a 5 mean for each criterion so scores are comparable.", ""),
            ("Score every solution against every criterion with the team, not alone — divergent scores usually reveal a hidden assumption worth discussing.", ""),
            ("Calculate the weighted score for each solution: multiply each score by its criterion weight and sum across the row.", ""),
            ("Rank the solutions by total weighted score and identify the top three.", ""),
            ("Cross-check the ranking on an effort-impact grid — look for the high-impact, low-effort quick wins in the top-left quadrant.", ""),
            ("Run a cost-benefit analysis on the top solution: implementation cost, ongoing cost, expected annual benefit and payback period.", ""),
            ("Sanity-check the selected solution against the root cause it addresses and confirm it does not simply move the problem downstream.", ""),
            ("Document the rationale for the selection — a sponsor will ask why the obvious expensive option was not chosen.", ""),
        ],
        test="Your matrix has weighted criteria with a defined scoring scale, every solution is scored, and your top-ranked solution has a payback period calculated.",
    ),
    dict(
        num=22, topic=4,
        title="FMEA, Risk Priority Numbers, DOE and Piloting",
        objective="Risk-assess and pilot the selected solution before full rollout (A5).",
        desc="A solution that fails in production costs more than the problem it fixed. FMEA "
             "systematically asks how the change could fail, how bad that would be and how likely "
             "it is to be caught. Then pilot at small scale and measure against the baseline before "
             "committing.",
        build="A completed FMEA with RPN scores, a DOE plan and a pilot plan with success criteria.",
        services="FMEA, severity, occurrence, detection, RPN, DOE factors and levels, pilot design, rollback plan",
        steps=[
            ("List every process step of the NEW improved process in the FMEA worksheet.", ""),
            ("For each step, identify the potential failure modes — the ways this step could go wrong.", ""),
            ("For each failure mode, record the potential effect on the customer and the potential cause.", ""),
            ("Score Severity 1-10: how serious is the effect on the customer if this failure occurs?", ""),
            ("Score Occurrence 1-10: how likely is this cause to happen?", ""),
            ("Score Detection 1-10, remembering the scale is inverted — 1 means it is almost certainly caught, 10 means it escapes undetected.", ""),
            ("Calculate the Risk Priority Number: RPN = Severity x Occurrence x Detection.", ""),
            ("Sort by RPN descending and address the highest scores first. Treat any Severity of 9 or 10 as requiring action regardless of its RPN.", ""),
            ("Write the recommended action for each high-RPN row, assign an owner and a date, then recalculate the projected RPN after the action.", ""),
            ("Plan a designed experiment for the settings you must optimise: list the factors, choose two levels (high and low) for each, and note that a 2^k design tests all combinations.", ""),
            ("Record why DOE beats one-factor-at-a-time testing: OFAT cannot reveal the INTERACTION between two factors, only their individual effects.", ""),
            ("Design the pilot: define the scope (one shift, one product family), the duration, the success criteria and the measurement method.", ""),
            ("Set the pilot success criteria against your measured baseline from Lab 12 and 13 — the pilot must beat the baseline by a stated margin.", ""),
            ("Write the rollback plan: what triggers stopping the pilot and how the process reverts safely.", ""),
            ("Run the pilot, collect data using the same operational definitions as your baseline, and compare like with like.", ""),
            ("Decide: scale up, adjust and re-pilot, or stop. Record the decision and the evidence behind it.", ""),
        ],
        test="Every FMEA row has an RPN, the highest RPNs have owned actions with dates, and your pilot has quantified success criteria measured against the Lab 13 baseline.",
    ),
]
