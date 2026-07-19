"""
Domain 1 — Foundations and the DEFINE phase.

Labs 1-6. Every lab uses the SAME running scenario as the PP assessment — the
Northwind Retail Distribution Centre order-fulfilment process — so the courseware
and the assessment are one continuous story. A Green Belt LEADS these activities;
the Yellow Belt only contributed to them.

Grounded in the CSSC "Six Sigma: A Complete Step-by-Step Guide" (Ch 1-11 for the
foundations, Ch 12+ for Green Belt depth) and the original v21 trainer deck.
"""

# ---------------------------------------------------------------- shared scenario
SCENARIO = (
    "Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm "
    "warehouse. Customers are complaining about late deliveries and the company is "
    "receiving negative feedback on social media. The Distribution Manager has asked "
    "you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — "
    "from order release to carrier handover."
)

DOMAIN1 = [
    dict(
        num=1, topic=0,
        title="The Green Belt Role, Project Selection and Business Case",
        objective="Select a viable DMAIC project and justify it with a business case (A1).",
        desc="Establish what a Green Belt is accountable for versus a Yellow or Black Belt, "
             "then screen candidate projects against objective selection criteria and build "
             "the business case that wins sponsorship. A Green Belt leads the project and "
             "owns the analysis — this lab sets that expectation.",
        build="A belt responsibility matrix, a scored project selection screen and a costed business case.",
        services="Belt role matrix, project selection criteria, COPQ estimate, business case",
        steps=[
            ("Compare the White, Yellow, Green, Black and Master Black Belt roles in a table — for each, record who leads, who analyses and who sponsors.", ""),
            ("Write down the three things a Green Belt does that a Yellow Belt does not: leads a scoped project, runs the statistical analysis, and owns the tollgate reviews.", ""),
            ("Read the Northwind scenario. List four candidate improvement projects that could be run in this distribution centre.", ""),
            ("Score each candidate 1-5 against: measurable gap, data availability, manageable scope, sponsor support, and customer impact.", ""),
            ("Reject any candidate that is a known solution in disguise ('install a new WMS') — a DMAIC project must start from a problem, not an answer.", ""),
            ("Estimate the Cost of Poor Quality for your chosen project: rework hours, expedited freight, credits issued and lost repeat custom.", ""),
            ("Write a four-line business case: the gap, the annualised COPQ, the improvement target and the resource ask.", ""),
        ],
        test="Your selected project scores highest on the criteria table, contains no pre-selected solution, and your business case states an annualised dollar figure.",
    ),
    dict(
        num=2, topic=0,
        title="Y = f(X), Sigma Level, DPMO and the DMAIC Roadmap",
        objective="Express the problem as Y = f(X) and calculate the baseline sigma level (K1, A4).",
        desc="Every Six Sigma project rests on one model: the output Y is a function of the "
             "process inputs Xs. Translate the Northwind problem into that model, then convert "
             "the baseline defect data into DPMO and a sigma level so improvement can be proven "
             "numerically later.",
        build="A Y = f(X) statement, a DPMO calculation and a baseline sigma level.",
        services="Y = f(X) model, DPU, DPO, DPMO, sigma level, DMAIC tollgates",
        steps=[
            ("Write the project Y — the single output metric the customer feels. For Northwind: order fulfilment lead time, or percentage of orders shipped on time.", ""),
            ("Brainstorm at least eight candidate Xs — the process inputs that could drive that Y (picking method, staffing, slotting, system downtime, order profile, shift, carrier cut-off).", ""),
            ("Write the relationship formally as Y = f(X1, X2, ... Xn) and state which Xs you can control and which you cannot.", ""),
            ("Take the baseline data: 4,200 orders shipped last month, 357 of them late. Calculate the defect rate as a proportion.", ""),
            ("Calculate DPMO using DPMO = (defects / (units x opportunities per unit)) x 1,000,000. Treat each order as one opportunity for a late-delivery defect.", ""),
            ("Look up the resulting DPMO on the sigma conversion table to read off the baseline sigma level.", ""),
            ("Map the five DMAIC phases against your project and name the tollgate deliverable that ends each phase.", ""),
        ],
        test="Your Y is a measurable customer-facing output, you have at least eight Xs, and your DPMO and sigma level are calculated from the 357/4,200 baseline.",
    ),
    dict(
        num=3, topic=1,
        title="Voice of the Customer, Affinity Diagram and Kano Analysis",
        objective="Capture VOC and classify requirements using affinity and Kano analysis (A1, K2).",
        desc="Green Belts do not guess what the customer wants — they collect it, cluster it and "
             "classify it. Gather raw VOC, group it into themes with an affinity diagram, then use "
             "Kano analysis to separate the requirements that merely prevent dissatisfaction from "
             "the ones that actually delight.",
        build="A VOC log, an affinity diagram of themes and a Kano classification table.",
        services="VOC sources, affinity diagram, Kano model, Must-Be / One-Dimensional / Delighter",
        steps=[
            ("List your VOC sources and split them into reactive (complaints, returns, social media) and proactive (surveys, interviews, gemba walks).", ""),
            ("Record at least twelve verbatim customer statements for the Northwind order-fulfilment process — use the customer's own words, not your summary.", ""),
            ("Write each verbatim on a separate sticky note or row so it can be moved independently.", ""),
            ("Build the affinity diagram: cluster the verbatims into natural themes in silence first, then name each cluster.", ""),
            ("Classify each theme against the Kano model — Must-Be (expected, causes dissatisfaction if absent), One-Dimensional (more is better), or Delighter (unexpected).", ""),
            ("Mark which Kano category each theme belongs to and note that Must-Be requirements never generate satisfaction, only its absence.", ""),
            ("Identify the one theme that, if fixed, would most reduce complaints — this becomes your project focus.", ""),
        ],
        test="You have at least twelve verbatims, every verbatim sits in a named affinity cluster, and every cluster carries a Kano classification.",
    ),
    dict(
        num=4, topic=1,
        title="CTQ Tree — Translating Customer Needs into Measurable Requirements",
        objective="Translate VOC into measurable CTQ requirements with targets and limits (A1, A4).",
        desc="A customer need is not measurable; a CTQ is. Drive each VOC theme down through "
             "need to driver to a Critical-to-Quality requirement that carries a metric, a target "
             "and specification limits — because the Measure phase can only baseline what has "
             "been defined numerically.",
        build="A three-level CTQ tree with metric, target, USL and LSL for each requirement.",
        services="CTQ tree, operational definitions, specification limits, performance metrics",
        steps=[
            ("Take your top VOC theme (for example 'my order arrives late') and write it at the root of the tree.", ""),
            ("Level 2 — break the need into drivers: what specifically must be true for that need to be met (picked on time, packed correctly, handed to carrier before cut-off).", ""),
            ("Level 3 — convert each driver into a CTQ with a unit of measure (order-to-ship hours, picking accuracy percentage, carrier cut-off compliance rate).", ""),
            ("For each CTQ write an operational definition: exactly how it is measured, by whom, from which system field, and when the clock starts and stops.", ""),
            ("Set the target and the specification limits (USL/LSL) for each CTQ from the customer promise, not from current performance.", ""),
            ("Check each CTQ against the test: could two different people measure this and get the same number? If not, tighten the operational definition.", ""),
            ("Select the one CTQ that becomes your project Y and confirm it matches the Y you wrote in Lab 2.", ""),
        ],
        test="Every CTQ has a unit of measure, a target, specification limits and an operational definition unambiguous enough for two people to apply identically.",
    ),
    dict(
        num=5, topic=1,
        title="Project Charter, Problem Statement, Goal Statement and Scope",
        objective="Charter the project with a problem statement, goal, scope and business case (A1, A2).",
        desc="The charter is the project's contract with its sponsor. Write a problem statement "
             "that quantifies the gap without naming a cause or a solution, a goal statement that "
             "is measurable and time-bound, and an explicit in-scope/out-of-scope table that "
             "prevents scope creep later.",
        build="A complete one-page project charter with all seven sections signed off.",
        services="Project charter, problem statement, goal statement, scope, business case, milestones",
        steps=[
            ("Write the problem statement with all four components: the process, the time period, the measurable gap and the business impact.", ""),
            ("Check the problem statement names NO cause and NO solution — if it contains 'because' or 'by implementing', rewrite it.", ""),
            ("Write the goal statement using the metric, baseline, target and date: 'reduce late shipments from 8.5% to 3.0% by 31 December'.", ""),
            ("Build the in-scope / out-of-scope table — name the process start point, the stop point, and at least three things explicitly excluded.", ""),
            ("State the business case: the annualised COPQ from Lab 1 and the benefit expected if the goal is achieved.", ""),
            ("List the team: sponsor, process owner, Green Belt, Black Belt mentor and subject matter experts, with named individuals.", ""),
            ("Add the DMAIC milestone schedule with a tollgate review date for each of the five phases.", ""),
            ("Review the charter against the sponsor's priorities and confirm they would sign it.", ""),
        ],
        test="Your problem statement contains process, period, measurable gap and impact but no cause or solution; your goal statement contains metric, baseline, target and date.",
    ),
    dict(
        num=6, topic=1,
        title="SIPOC, Stakeholder Analysis and RACI",
        objective="Build the macro process view and map the stakeholders who must be engaged (A2).",
        desc="Before mapping the process in detail, agree its boundaries and its customers with "
             "SIPOC. Then identify every stakeholder the project touches and fix accountability "
             "with a RACI — because Green Belt projects fail on resistance far more often than "
             "on analysis.",
        build="A validated SIPOC (exported from the builder), a stakeholder power/interest grid and a RACI matrix.",
        services="SIPOC & Process Map Builder, process boundaries, pain points, stakeholder analysis, power/interest grid, RACI",
        steps=[
            ("Open the SIPOC & Process Map Builder — it walks you through the boundaries, the SIPOC and the pain points in order.", "https://alfredang.github.io/sipoc/"),
            ("Agree the process boundaries first — write the explicit start trigger and stop event for the Northwind order-fulfilment process. Boundary disputes are where most SIPOCs fail.", ""),
            ("List the Process steps: five to seven high-level steps only. Resist the urge to detail — that comes in Lab 7.", ""),
            ("Work outward: list the Outputs of the process and the Customers who receive each output.", ""),
            ("List the Inputs each step consumes and the Suppliers who provide them, internal and external.", ""),
            ("Tag at least three pain points on the process steps — the delays, rework loops and unclear handoffs you already suspect.", ""),
            ("Run 'Check my SIPOC' in the tool to validate your diagram against the lab and assessment criteria, then export it as PNG or PDF for your project pack.", ""),
            ("Validate the SIPOC with someone who does the work — SIPOCs built in a meeting room are usually wrong.", ""),
            ("Identify every stakeholder and plot them on a power/interest grid: manage closely, keep satisfied, keep informed, or monitor.", ""),
            ("Build the RACI for the project deliverables — exactly one Accountable per row, no more.", ""),
            ("For each high-power stakeholder, note their likely objection and your engagement approach.", ""),
        ],
        test="'Check my SIPOC' passes, all five columns are populated with explicit boundaries and at least three pain points tagged, and your RACI has exactly one Accountable per deliverable.",
    ),
]
