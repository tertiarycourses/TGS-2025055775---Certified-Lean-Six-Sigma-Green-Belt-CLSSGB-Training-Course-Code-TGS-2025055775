"""
Domain 5 — The CONTROL phase and project closure.

Labs 23-25. The Yellow Belt writes a simple control plan; the Green Belt builds
STATISTICAL process control — selects the correct control chart for the data type,
calculates the limits, applies the out-of-control rules, and proves the improvement
held with a re-measured capability index.

Lab 24 (control plan) maps directly to PP Assessment Task 3 (A4, A5).
"""

DOMAIN5 = [
    dict(
        num=23, topic=5,
        title="Statistical Process Control — Chart Selection and Control Limits",
        objective="Select, build and interpret the correct control chart for the process (A4, A5).",
        desc="A control chart is how a process tells you it has drifted before it produces a "
             "defect. Choosing the WRONG chart for the data type invalidates every signal it "
             "gives, so selection comes first — then the limits, then the rules for reading it.",
        build="A correctly selected control chart with calculated limits and the eight rules applied.",
        services="SPC, control chart selection tree, Xbar-R, Xbar-S, I-MR, p, np, c, u charts, control limits, zones",
        steps=[
            ("Establish the difference between control limits and specification limits: control limits come from the process itself (the voice of the process), specification limits come from the customer (the voice of the customer). Never plot spec limits on a control chart.", ""),
            ("Walk the control chart selection tree. First question: is your data continuous (variable) or discrete (attribute)?", ""),
            ("For CONTINUOUS data, ask whether it can be sensibly subgrouped. If not, use an Individuals and Moving Range (I-MR) chart.", ""),
            ("For continuous data in subgroups, use Xbar-R when the subgroup size is under 8, and Xbar-S when the subgroup size is 8 or more.", ""),
            ("For DISCRETE data, ask whether you are counting DEFECTIVE UNITS or DEFECTS. This distinction decides the next branch.", ""),
            ("For defective units (pass/fail): use a p-chart when the sample size varies, and an np-chart when the sample size is constant.", ""),
            ("For counts of defects: use a u-chart when the sample size varies, and a c-chart when the sample size is constant.", ""),
            ("Select the correct chart for your Northwind data and write down the justification against the tree.", ""),
            ("Build the chart: plot the points in time order, calculate and draw the centre line, then the upper and lower control limits at +/- 3 standard deviations.", ""),
            ("Divide the chart into zones: zone C within 1 sigma of the centre line, zone B between 1 and 2 sigma, zone A between 2 and 3 sigma.", ""),
            ("Apply out-of-control rule 1: any single point beyond the UCL or LCL. Investigate immediately — the probability of this happening by chance is roughly 3 in 1,000.", ""),
            ("Apply rule 2: nine consecutive points on the same side of the centre line, indicating the process level has shifted.", ""),
            ("Apply rule 3: six consecutive points steadily increasing or decreasing, indicating a trend.", ""),
            ("Apply rule 4: fourteen consecutive points alternating up and down, often caused by over-adjustment.", ""),
            ("Apply rules 5 and 6: two of three consecutive points in zone A, or four of five in zone B or beyond, indicating a sudden shift.", ""),
            ("Apply rules 7 and 8: fifteen consecutive points inside zone C (limits may need recalculating), or eight consecutive points with none in zone C (you may be charting two different processes).", ""),
            ("Record every signal your chart shows and the assignable cause you found for each.", ""),
        ],
        test="You can justify your chart choice against the selection tree, your limits are calculated at +/- 3 sigma, and you have applied all eight out-of-control rules.",
    ),
    dict(
        num=24, topic=5,
        title="Control Plan, SOP, Visual Management and Response Plan",
        objective="Build the control plan that sustains the improvement (A4, A5).",
        desc="This lab maps directly to Task 3 of the Practical Performance assessment. The control "
             "plan is the document that keeps the gain after the project team disbands. Without a "
             "named owner and a defined reaction plan, processes drift back to their old "
             "performance within months.",
        build="A complete control plan, an SOP for the improved method and a visual management board design.",
        services="Control plan, control limits, monitoring frequency, reaction plan, SOP, visual management, team huddles, gemba",
        steps=[
            ("Build the control plan table with one row per control point and these columns: process step, CTQ metric, specification, measurement method, sample size, frequency, owner and reaction plan.", ""),
            ("Select the key process metrics to track. For Northwind: order processing time, number of late orders, picking time and shipping errors.", ""),
            ("Define the data collection method for each metric: who collects it, how often, and where it is recorded.", ""),
            ("Set the control limits — the acceptable performance thresholds that trigger a response.", ""),
            ("Write the corrective action for each metric: exactly what happens when performance breaches the control limit, and who decides.", ""),
            ("Assign roles and responsibilities: name the individual accountable for each control point, not a department.", ""),
            ("Write the SOP for the improved method: purpose, scope, step-by-step instructions, quality checks and escalation path.", ""),
            ("Make the SOP visual and short. A one-page illustrated work instruction at the point of use beats a twenty-page document nobody opens.", ""),
            ("Design the visual management board: which metrics are displayed, updated how often, by whom, and visible to whom.", ""),
            ("Set up the daily team huddle: a short stand-up at the board reviewing yesterday's performance and today's risks.", ""),
            ("Plan the gemba walk cadence — leadership going to where the work happens to see the process, not the report.", ""),
            ("Build the training plan so every person performing the process is trained on the new standard, with a record of who was trained and when.", ""),
            ("Add an audit schedule to verify the control plan is actually being followed — controls that are not audited quietly stop happening.", ""),
        ],
        test="Every control point has a named owner, a monitoring frequency and a specific reaction plan stating what to do when the metric breaches its limit.",
    ),
    dict(
        num=25, topic=5,
        title="Verify the Gain, A3 Storyboard, Handover and Project Closure",
        objective="Prove the improvement is real and hand the process over (A5, K1).",
        desc="Close the project properly: re-measure capability, prove statistically that the "
             "improvement is real rather than random, quantify the financial benefit with Finance, "
             "tell the story on a single A3 page, and formally transfer ownership to the process "
             "owner.",
        build="A before/after capability comparison, a validated benefit, an A3 storyboard and a signed handover.",
        services="Re-measured Cp/Cpk, hypothesis test of improvement, benefit validation, A3 report, handover, lessons learned",
        steps=[
            ("Collect post-improvement data using exactly the same operational definitions and sampling method as your baseline — otherwise the comparison is meaningless.", ""),
            ("Recalculate the process metrics: yield, RTY, DPMO and sigma level, using the same DUDO definitions from Lab 12.", ""),
            ("Recalculate Cp and Cpk and compare against the baseline values from Lab 13.", ""),
            ("Run a hypothesis test comparing before and after performance — state H0 as 'no difference' and prove the improvement is statistically significant, not random variation.", ""),
            ("Report the p-value and confirm you can reject H0 at your chosen alpha. An improvement you cannot prove statistically is not yet an improvement.", ""),
            ("Quantify the financial benefit and have Finance validate it — a benefit the finance team has not signed off will not be recognised by the business.", ""),
            ("Build the A3 storyboard on one page: background, current state, goal, root cause analysis, countermeasures, results, and follow-up actions.", ""),
            ("Include the before and after charts on the A3 — the visual comparison communicates faster than any table of numbers.", ""),
            ("Present the results tailored to the audience: leadership wants the benefit and how it is controlled; the process team wants the workflow detail.", ""),
            ("Follow the presentation rules: ask a question as the slide title, show one clear graphic that answers it, and state the conclusion in plain business language.", ""),
            ("Hand over formally: walk the process owner through the control plan, the SOP, the charts and the reaction plan, then obtain their signature.", ""),
            ("Agree the post-project review date — typically 30, 60 and 90 days — to confirm the gain has held.", ""),
            ("Capture lessons learned: what worked, what did not, and what you would do differently on the next project.", ""),
            ("Identify replication opportunities: where else in the business does this same problem exist, and could this solution be copied across?", ""),
            ("Close the project formally with the sponsor and release the team.", ""),
        ],
        test="Your after-capability beats the baseline, the improvement is proven with a hypothesis test and a stated p-value, and the process owner has signed the handover.",
    ),
]
