#!/usr/bin/env python3
"""Define teaching slides - Green Belt depth, DMAIC order."""
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


def define_phase(d):
    K = "DEFINE"

    # ---------------- 1. What Define delivers ----------------
    d.tile_grid(
        "What the Define phase must deliver", [
            ("An approved Project Charter", "Problem, goal, business case, scope, team, milestones and benefits - signed by the Champion."),
            ("Validated Voice of the Customer", "Real verbatims from real customers, not the team's assumptions."),
            ("CTQs with operational definitions", "Each critical-to-quality measure has a metric, target and spec limit."),
            ("A high-level process map (SIPOC)", "Agreed start and stop points so everyone scopes the same process."),
            ("A stakeholder plan", "Who has power, who has interest, who signs off, who resists."),
            ("A passed tollgate review", "Champion approval to spend measurement effort in the next phase."),
        ], kicker=K, cols=2, accent=BLUE)

    d.flow_h(
        "The steps of the Define phase",
        ["Collect and validate the Voice of the Customer",
         "Translate VOC into needs, then into measurable CTQs",
         "Draft the problem and goal statements from baseline data",
         "Build the SIPOC and fix the process boundary",
         "Analyse stakeholders and plan the change",
         "Charter sign-off at the Define tollgate"],
        kicker=K, color=BLUE)

    p = _dg(d, "define-steps")
    if p:
        d.image_slide("Define phase - the standard sequence", p, kicker=K,
                      caption="Each step feeds the next: VOC drives CTQs, CTQs drive the goal, the goal drives the charter.",
                      accent=BLUE)

    d.content(
        "Northwind Retail Distribution Centre - our running case", [
            "12,000 sqm distribution centre fulfilling online retail orders across Singapore.",
            "Customers complain about late deliveries; negative feedback is spreading on social media.",
            "Baseline: 4,200 orders shipped last month, 357 of them late - 8.5 percent late shipments.",
            "Target: reduce late shipments from 8.5 percent to 3.0 percent.",
            "We will carry this one case through Define, Measure, Analyse, Improve and Control.",
        ], kicker=K, size=19)

    # ---------------- 2. Voice of the Customer ----------------
    d.compare_panels(
        "Two families of VOC sources", [
            ("REACTIVE", "Data that arrives whether you ask or not", [
                "Complaints and contact-centre call logs",
                "Returns and refund requests",
                "Warranty and service claims",
                "Social media posts, reviews and ratings",
                "Cheap and continuous - but biased to the angry",
            ]),
            ("PROACTIVE", "Data you must deliberately go and collect", [
                "Structured surveys with a sampling plan",
                "One-to-one customer interviews",
                "Focus groups with 6-10 customers",
                "Gemba observation - watch the customer use it",
                "Costlier, but reaches the silent majority",
            ]),
        ], kicker=K, accent=TEAL)

    p = _dg(d, "voc-sources")
    if p:
        d.image_slide("The VOC source map", p, kicker=K,
                      caption="Use both families. Reactive data tells you what broke; proactive data tells you what matters.",
                      accent=TEAL)

    d.two_col(
        "Northwind - VOC verbatims from three channels",
        [("'It said two-day delivery and it arrived on day five.'", 0),
         ("'Nobody told me it was delayed - I had to chase.'", 0),
         ("'The tracking page still said packed for three days.'", 0),
         ("Source: 214 contact-centre calls, last 30 days", 1)],
        [("'I ordered for a birthday and it missed the date.'", 0),
         ("'Two of the four items came, the rest never did.'", 0),
         ("'Late again. Third time. Switching to a competitor.'", 0),
         ("Source: 61 social posts + 12 customer interviews", 1)],
        kicker=K, lhead="REACTIVE - calls and complaints",
        rhead="PROACTIVE - interviews and social listening")

    # ---------------- 3. VOC -> Need -> CTQ ----------------
    d.flow_h(
        "The three-level drill-down",
        ["VOC - the raw verbatim in the customer's own words",
         "NEED - the general requirement behind that statement",
         "CTQ - a specific measure with a metric, target and limits"],
        kicker=K, color=VIOLET)

    d.compare_panels(
        "Northwind - one verbatim drilled to a CTQ", [
            ("VOC", "What the customer said", [
                "'It said two-day delivery and",
                "it arrived on day five.'",
                "Emotional, vague, unmeasurable",
                "But it is the truth of the problem",
            ]),
            ("NEED", "What they actually require", [
                "My order must arrive by the date",
                "that was promised at checkout",
                "Still not measurable as written",
                "One need can spawn several CTQs",
            ]),
            ("CTQ", "What we will measure", [
                "Metric: order dispatch lead time",
                "Target: 100 pct shipped same day",
                "USL: 24 hours order to despatch",
                "Defect: any order past 24 hours",
            ]),
        ], kicker=K, accent=VIOLET)

    # ---------------- 4. Affinity diagram ----------------
    d.flow_h(
        "The six steps of an affinity diagram",
        ["Write each verbatim on its own card - one thought per card",
         "Sort in SILENCE - no debating, no negotiating",
         "Let clusters form naturally - move any card, any time",
         "Name each cluster with a header card",
         "Review aloud - now discussion is allowed",
         "Prioritise the clusters by frequency and impact"],
        kicker=K, color=BLUE)

    d.tile_grid(
        "Why silence is the rule", [
            ("Silence kills seniority", "The loudest or most senior voice cannot dominate the grouping."),
            ("It is faster", "Ten people sorting silently beat ten people arguing about one card."),
            ("It surfaces intuition", "Pattern recognition works before it can be justified in words."),
            ("Duplicate moves are fine", "If two people keep moving a card, that card belongs in a new cluster."),
        ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "affinity-diagram")
    if p:
        d.image_slide("Affinity diagram in practice", p, kicker=K,
                      caption="Cards first, clusters second, names last. Never name the cluster before the cards decide it.",
                      accent=BLUE)

    d.tile_grid(
        "Northwind - the five clusters that emerged", [
            ("Missed promise date", "148 verbatims. The order arrived after the date shown at checkout."),
            ("No proactive notification", "97 verbatims. Customer discovered the delay, we never told them."),
            ("Stale tracking information", "64 verbatims. Tracking status not updated after packing."),
            ("Split and partial shipments", "41 verbatims. Multi-line orders arriving in pieces."),
            ("Wrong or damaged items", "23 verbatims. Out of scope - handled by a separate quality project."),
        ], kicker=K, cols=1, accent=BLUE)

    # ---------------- 5. Kano analysis ----------------
    d.compare_panels(
        "The three primary Kano categories", [
            ("MUST-BE", "Basic / expected / dissatisfier", [
                "Assumed, never articulated",
                "Absent: severe dissatisfaction",
                "Present: NO satisfaction at all",
                "Northwind: the parcel arrives intact",
                "You cannot win here - only lose",
            ]),
            ("ONE-DIMENSIONAL", "Performance / linear / spoken", [
                "The more you give, the happier",
                "Customers ask for it explicitly",
                "This is where you compete",
                "Northwind: speed of delivery",
                "Satisfaction rises with performance",
            ]),
            ("DELIGHTER", "Attractive / excitement / unspoken", [
                "Unexpected - never requested",
                "Absent: no dissatisfaction at all",
                "Present: disproportionate delight",
                "Northwind: live courier tracking map",
                "Decays into a Must-Be over time",
            ]),
        ], kicker=K, accent=AMBER)

    d.tile_grid(
        "The two categories most teams forget", [
            ("INDIFFERENT", "Performance changes but satisfaction does not move. Pure waste - stop funding it."),
            ("REVERSE", "More of the feature makes satisfaction fall. Over-packaging, over-notification, forced registration."),
        ], kicker=K, cols=1, size=16, accent=AMBER)

    d.big_statement(
        "Delighters decay into Must-Bes.",
        "Car air-conditioning was a delighter in 1965, a performance feature in 1985, and a "
        "must-be by 2005. Today its absence causes outrage and its presence earns nothing. "
        "Re-run Kano every 12 to 18 months or your CTQs quietly go stale.",
        K, color=RED)

    p = _dg(d, "kano-model")
    if p:
        d.image_slide("The Kano model", p, kicker=K,
                      caption="Vertical axis is satisfaction, horizontal is performance delivered. Only the middle curve passes through the origin.",
                      accent=AMBER)

    # ---------------- 6. CTQ tree ----------------
    d.flow_h(
        "How a CTQ tree is built",
        ["NEED - one general customer requirement from the affinity clusters",
         "DRIVERS - the 2-4 things that must be true for the need to be met",
         "CTQ - a metric, a target and a specification limit for each driver"],
        kicker=K, color=VIOLET)

    p = _dg(d, "ctq-tree")
    if p:
        d.image_slide("CTQ tree structure", p, kicker=K,
                      caption="Read left to right. If a leaf cannot be measured this week, it is not yet a CTQ.",
                      accent=VIOLET)

    d.tile_grid(
        "Northwind CTQ tree - need: my order arrives when promised", [
            ("Driver 1 - Pick accuracy", "CTQ: pick error rate. Target 0.2 pct. USL 0.5 pct of order lines."),
            ("Driver 2 - Despatch speed", "CTQ: order-to-despatch hours. Target 12 h. USL 24 h from order receipt."),
            ("Driver 3 - Carrier collection", "CTQ: on-time carrier pickup. Target 100 pct. LSL 98 pct of scheduled slots."),
            ("Driver 4 - Delay notification", "CTQ: hours from delay detected to customer told. Target 1 h. USL 4 h."),
        ], kicker=K, cols=1, size=16, accent=VIOLET)

    d.compare_panels(
        "Operational definitions - the discipline that saves the project", [
            ("WHAT IS MEASURED", "The characteristic, unambiguously", [
                "Order-to-despatch elapsed hours",
                "Clock starts at payment confirmed",
                "Clock stops at carrier scan-out",
                "Excludes pre-orders and backorders",
            ]),
            ("HOW IT IS MEASURED", "Method, instrument and rounding", [
                "Source: WMS timestamp table",
                "Reported to one decimal place",
                "Calendar hours, not working hours",
                "Extracted daily at 06:00",
            ]),
            ("WHAT COUNTS AS A DEFECT", "The decision rule", [
                "Any order exceeding 24.0 hours",
                "Partial shipment: each line judged",
                "Cancelled orders are excluded",
                "Two people must agree on any edge case",
            ]),
        ], kicker=K, accent=VIOLET)

    # ---------------- 7. Project Charter ----------------
    d.tile_grid(
        "The seven sections of a project charter", [
            ("1. Problem statement", "What is wrong, in which process, over what period, how big the gap, what it costs."),
            ("2. Goal statement", "The same metric, with a baseline, a target and a completion date."),
            ("3. Business case", "Why now, why this project, what happens if we do nothing."),
            ("4. Scope", "In-scope and out-of-scope, plus the process start and stop points."),
            ("5. Team and roles", "Champion, Sponsor, Green Belt, Black Belt mentor, process owner, members."),
            ("6. Milestones", "Tollgate dates for D, M, A, I and C - with named review owners."),
            ("7. Benefits", "Hard savings, soft savings and the customer-facing benefit."),
        ], kicker=K, cols=2, accent=BLUE)

    p = _dg(d, "project-charter")
    if p:
        d.image_slide("Project charter template", p, kicker=K,
                      caption="A charter is a living document - it is revised at every tollgate, never written once and filed.",
                      accent=BLUE)

    d.tile_grid(
        "Charter rules that separate Green Belts from amateurs", [
            ("One page, always", "If it needs three pages, the scope is too big - split the project."),
            ("Signed by the Champion", "An unsigned charter has no resources and no authority behind it."),
            ("Numbers, never adjectives", "'Significantly improve' is not a goal. '8.5 pct to 3.0 pct by 31 Oct' is."),
            ("Revised at each tollgate", "Measure often changes the baseline. Update the charter, do not hide it."),
        ], kicker=K, cols=2, accent=BLUE)

    # ---------------- 8. Problem statement ----------------
    d.big_statement(
        "A problem statement has four components.",
        "Process, time period, measurable gap, business impact. Anything else you add is either "
        "a cause or a solution - and both are forbidden at this stage.",
        K, color=RED)

    d.flow_h(
        "The four required components",
        ["PROCESS - which process and where, precisely",
         "TIME PERIOD - the window the data covers",
         "MEASURABLE GAP - actual versus expected, in numbers",
         "BUSINESS IMPACT - what the gap costs the organisation"],
        kicker=K, color=RED)

    d.compare_panels(
        "The two forbidden things", [
            ("NO CAUSE", "Do not state why it happens", [
                "'because the WMS is slow' is a hypothesis",
                "Causes are proved in Analyse, not asserted",
                "Naming a cause pre-closes the investigation",
                "It also assigns blame before evidence",
            ]),
            ("NO SOLUTION", "Do not state what to do about it", [
                "'we need a new WMS' is a solution",
                "Solutions are selected in Improve",
                "A solution in the problem statement",
                "turns a DMAIC project into a purchase order",
            ]),
        ], kicker=K, accent=RED)

    d.compare_panels(
        "Northwind - BAD versus GOOD problem statements", [
            ("BAD", "Vague, causal and solution-loaded", [
                "'Deliveries are always late because the",
                "warehouse system is slow and understaffed,",
                "so we need to buy new scanners.'",
                "No process, no period, no number, no cost",
                "States a cause AND a solution",
            ]),
            ("GOOD", "Four components, zero cause, zero fix", [
                "'In the Northwind DC outbound process,",
                "in the month of September, 357 of 4,200",
                "orders shipped late - 8.5 pct against a",
                "3.0 pct standard - driving 214 complaint",
                "calls and an estimated $186,000 annual COPQ.'",
            ]),
        ], kicker=K, accent=RED)

    p = _dg(d, "problem-statement-good-bad")
    if p:
        d.image_slide("Problem statements - good and bad", p, kicker=K,
                      caption="Read every statement back and ask: is there a why, or a what-to-do, hiding in here?",
                      accent=RED)

    # ---------------- 9. Goal statement ----------------
    d.tile_grid(
        "The four elements of a goal statement", [
            ("METRIC", "The identical measure used in the problem statement - percentage of orders shipped late."),
            ("BASELINE", "Where it is today, from real data - 8.5 percent, September, 4,200 orders."),
            ("TARGET", "Where it must get to - 3.0 percent, a 65 percent reduction in the defect rate."),
            ("DATE", "When it must be achieved and verified - 31 October, confirmed by Control-phase data."),
        ], kicker=K, cols=2, accent=TEAL)

    d.big_statement(
        "Northwind goal statement",
        "Reduce late outbound shipments in the Northwind DC from 8.5 percent to 3.0 percent of "
        "orders by 31 October, sustained for three consecutive months, without increasing "
        "outbound cost per order.",
        K, color=TEAL)

    # ---------------- 10. Scope ----------------
    d.two_col(
        "Northwind - in scope and out of scope",
        [("Outbound order fulfilment in the Singapore DC", 0),
         ("Order receipt through carrier scan-out", 0),
         ("Standard retail e-commerce orders", 0),
         ("Pick, pack, label and stage activities", 0),
         ("All three outbound shifts, Mon to Sat", 0),
         ("WMS despatch data, Jan to Sep", 0)],
        [("Inbound receiving and put-away", 0),
         ("Carrier transit time after scan-out", 0),
         ("B2B pallet and wholesale orders", 0),
         ("Returns, refunds and reverse logistics", 0),
         ("Product quality and packaging design", 0),
         ("The overseas fulfilment centres", 0)],
        kicker=K, lhead="IN SCOPE", rhead="OUT OF SCOPE", lcolor=TEAL, rcolor=RED)

    d.tile_grid(
        "Process start and stop points - the boundary that matters most", [
            ("START POINT", "Payment confirmed and order released to the warehouse management system."),
            ("STOP POINT", "Carrier scan-out at the outbound dock door - custody transfers to the carrier."),
            ("Why fix it in Define", "Different boundaries produce different baselines and different root causes."),
            ("Test the boundary", "Everyone on the team must state the same start and stop point, unprompted."),
        ], kicker=K, cols=2, accent=AMBER)

    d.tile_grid(
        "Scope creep - how it starts and how to stop it", [
            ("'While we are in there...'", "A stakeholder adds a pet problem mid-project. Log it in the parking lot, do not adopt it."),
            ("Root causes outside the boundary", "Legitimate finding - raise a separate project, do not silently expand this one."),
            ("Solution shopping", "Improve ideas that need capex outside scope belong to a follow-on project."),
            ("The defence", "Any scope change requires a re-signed charter and a revised milestone date."),
        ], kicker=K, cols=2, accent=AMBER)

    # ---------------- 11. Business case and COPQ ----------------
    d.tile_grid(
        "What a Green Belt business case must contain", [
            ("The current cost of the problem", "COPQ today, calculated from real volumes and verified unit costs."),
            ("The size of the opportunity", "The portion of that COPQ the goal statement actually recovers."),
            ("Why now", "A regulatory date, a contract renewal, a churn trend or a capacity ceiling."),
            ("The cost of doing nothing", "Project the trend forward twelve months and state the number."),
            ("Finance validation", "A named Finance partner has agreed the assumptions in writing."),
            ("Strategic linkage", "Which corporate objective this project moves, and by how much."),
        ], kicker=K, cols=2, accent=VIOLET)

    d.formula_card(
        "Northwind - building the COPQ number", [
            ("Late shipment rate", "357 / 4200 = 8.5 pct", "September actual against a 3.0 pct internal standard"),
            ("Excess late orders", "8.5 pct - 3.0 pct = 5.5 pct", "5.5 pct x 4,200 = 231 avoidable late orders per month"),
            ("Monthly COPQ", "231 x $67 = $15,477", "$67 = expedite freight + service call + goodwill credit per order"),
            ("Annualised COPQ", "$15,477 x 12 = $185,724", "Rounded to $186,000 - the figure in the problem statement"),
        ], kicker=K, accent=VIOLET,
        note="Every figure here is traceable to WMS volumes and Finance-agreed unit costs - never to an estimate on a whiteboard.")

    d.compare_panels(
        "Hard savings versus soft savings", [
            ("HARD SAVINGS", "Finance will book them", [
                "Removed expedite freight charges",
                "Reduced overtime hours in outbound",
                "Avoided goodwill credits and refunds",
                "Show up on the P&L within 12 months",
                "Count these in the project benefit",
            ]),
            ("SOFT SAVINGS", "Real, but not bookable", [
                "Hours freed but not headcount removed",
                "Improved customer satisfaction score",
                "Reduced complaint-handling effort",
                "Lower risk of contract penalties",
                "Report them separately, never inflate",
            ]),
        ], kicker=K, accent=VIOLET)

    # ---------------- 12. SIPOC ----------------
    d.sipoc_diagram(
        "Northwind DC - outbound order fulfilment SIPOC", [
            ["E-commerce platform",
             "Merchandise vendors",
             "Inbound receiving team",
             "Carrier partners (SG Post, Ninja)",
             "WMS / ERP system",
             "Packaging supplier"],
            ["Confirmed customer order",
             "Stock on hand in pick face",
             "Pick list and route",
             "Cartons, labels, dunnage",
             "Staffed pick and pack shift",
             "Carrier collection schedule"],
            ["Release order to WMS",
             "Allocate stock and generate pick",
             "Pick items from pick face",
             "Pack, weigh and label carton",
             "Stage at outbound dock",
             "Carrier scan-out"],
            ["Packed and labelled carton",
             "Despatch confirmation to customer",
             "Tracking number",
             "Updated inventory record",
             "Manifest to carrier",
             "Despatch timestamp in WMS"],
            ["Online retail customer",
             "Carrier partner",
             "Customer service team",
             "Finance (revenue recognition)",
             "Inventory planning",
             "Merchandising"],
        ], kicker=K)

    d.flow_h(
        "How to build a SIPOC - the working sequence",
        ["Name the process and agree the START and STOP points first",
         "List the 5-7 high-level process steps between them",
         "List the Outputs of that process, then the Customers who receive them",
         "List the Inputs the process consumes, then the Suppliers who provide them",
         "Validate with the process owner and walk the gemba to confirm"],
        kicker=K, color=TEAL)

    d.tile_grid(
        "SIPOC rules Green Belts get wrong", [
            ("Build P first, not S", "Fix the process steps and boundary before anything else - the rest hangs off them."),
            ("5 to 7 steps only", "SIPOC is a boundary tool, not a process map. Detail comes in the Measure phase."),
            ("Outputs before inputs", "Work backwards from what the customer receives - it exposes missing steps."),
            ("Customers can be internal", "Finance and Customer Service are customers of this process too."),
            ("Verbs for the process column", "Every P entry starts with a verb: release, allocate, pick, pack, stage."),
            ("Walk it, do not imagine it", "A SIPOC built in a meeting room is a hypothesis until you walk the floor."),
        ], kicker=K, cols=2, accent=TEAL)

    p = _dg(d, "sipoc-example")
    if p:
        d.image_slide("SIPOC - worked example", p, kicker=K,
                      caption="The SIPOC is the contract on scope: if it is not in the P column, it is not in this project.",
                      accent=TEAL)

    # The browser tool used in Labs 6 and 7 to build the SIPOC, the swimlane and
    # the handoff table. No install, no licence — it runs in the browser.
    d.tile_grid(
        "Build it in the browser - SIPOC & Process Map Builder", [
            ("alfredang.github.io/sipoc", "The tool you will use in Lab 6 and Lab 7. No install, no licence."),
            ("Boundaries first", "It makes you name the process, the trigger and the end state before anything else."),
            ("SIPOC + pain points", "Build all five columns, then tag at least three pain points on the steps."),
            ("Swimlane, generated", "Assign an actor to each step and it draws the swimlane and the handoff table."),
            ("Check my SIPOC", "Validates your diagram against the lab and assessment criteria before you submit."),
            ("Export and share", "Export to PNG or PDF for your project pack, or share the session with your team."),
        ], kicker=K, cols=2, size=14, accent=TEAL)

    # ---------------- 13. Stakeholder analysis ----------------
    d.matrix2x2(
        "Power / interest grid",
        "Level of interest in the project  ->",
        "Power to affect it",
        [("KEEP SATISFIED", "High power, low interest. Northwind: the Finance Director. Brief them concisely at tollgates - never surprise them, never overload them."),
         ("MANAGE CLOSELY", "High power, high interest. Northwind: the DC Operations Manager and the Champion. Involve in every decision, consult before every change."),
         ("MONITOR", "Low power, low interest. Northwind: the packaging supplier. Minimum effort - watch for a shift in either axis."),
         ("KEEP INFORMED", "Low power, high interest. Northwind: pick and pack team leaders. Regular updates - they hold the process knowledge you need.")],
        kicker=K, accent=BLUE)

    d.tile_grid(
        "Running the stakeholder analysis", [
            ("List everyone affected", "Anyone who touches the process, funds it, measures it or feels its output."),
            ("Score power and interest", "High or low on each axis - be honest, not political."),
            ("Record current versus needed", "Where is each stakeholder now on resist-neutral-support, and where must they be?"),
            ("Assign an owner per person", "Every named stakeholder has one team member responsible for the relationship."),
            ("Re-map at every tollgate", "Reorganisations and results move people between quadrants."),
        ], kicker=K, cols=1, size=15, accent=BLUE)

    d.big_statement(
        "RACI: exactly one A per row.",
        "Responsible does the work. Accountable owns the outcome and there is never more than one. "
        "Consulted gives input before the decision. Informed is told after it.",
        K, color=BLUE)

    d.compare_panels(
        "The four RACI letters", [
            ("R - RESPONSIBLE", "Performs the task", [
                "Can be several people per activity",
                "Northwind: Green Belt runs the analysis",
                "Doing the work, not owning the result",
            ]),
            ("A - ACCOUNTABLE", "Owns the outcome", [
                "EXACTLY ONE per row, no exceptions",
                "Northwind: DC Ops Manager owns delivery",
                "Two As means nobody is accountable",
            ]),
            ("C - CONSULTED", "Two-way, before", [
                "Their input shapes the decision",
                "Northwind: Finance on the COPQ model",
                "Consult too many and you stall",
            ]),
            ("I - INFORMED", "One-way, after", [
                "Told the outcome, no input expected",
                "Northwind: Customer Service team",
                "Cheap - so do not skip it",
            ]),
        ], kicker=K, accent=BLUE)

    d.two_col(
        "Northwind - the project RACI in practice",
        [("Charter approval - A: Champion", 0),
         ("Data collection plan - A: Green Belt", 0),
         ("Baseline validation - A: Green Belt", 0),
         ("Root cause confirmation - A: Green Belt", 0),
         ("Solution sign-off - A: DC Ops Manager", 0),
         ("Control plan handover - A: Process Owner", 0)],
        [("Common failure: two names in the A column", 0),
         ("Common failure: the Champion listed as R", 0),
         ("Common failure: everyone marked C", 0),
         ("Common failure: no I for the shop floor", 0),
         ("Fix: one A per row, then read it aloud", 0),
         ("Fix: the A must be able to say 'no'", 0)],
        kicker=K, lhead="ACCOUNTABLE BY ACTIVITY", rhead="RACI FAILURE MODES",
        lcolor=TEAL, rcolor=RED)

    # ---------------- 14. Change management ----------------
    d.tile_grid(
        "Why people resist a Six Sigma project", [
            ("Fear of job loss", "Efficiency has historically meant headcount cuts. Say what will happen to roles, early."),
            ("Loss of expertise status", "Standard work threatens the person who was the only one who knew the workaround."),
            ("Change fatigue", "The fourth initiative this year. Show what you are stopping, not only starting."),
            ("Not invited, only informed", "People defend what they helped build. Involve the floor in the fishbone."),
            ("No visible sponsorship", "If the Champion never appears at the gemba, the team reads it as optional."),
            ("Measurement feels like policing", "Explain that you are measuring the process, never the individual."),
        ], kicker=K, cols=2, accent=RED)

    d.tile_grid(
        "Practical change tactics for a Green Belt", [
            ("Communicate the why first", "People accept a change they understand the reason for - twice as fast."),
            ("Make the Champion visible", "One gemba walk by the Champion outweighs ten emails from you."),
            ("Pilot small, publicise early", "One shift, two weeks, then show the run chart to everyone."),
            ("Give credit to the floor", "Name the operators who found the root cause, in front of management."),
            ("Address the loudest sceptic", "Convert them and the rest follow. Ignore them and they run the project."),
            ("Plan the handover from day one", "Control is designed in Define, not improvised at the end."),
        ], kicker=K, cols=2, accent=RED)

    # ---------------- 15. Tollgate ----------------
    d.tile_grid(
        "Define tollgate checklist", [
            ("Charter signed", "All seven sections complete, approved by the Champion and the process owner."),
            ("VOC evidence attached", "Real verbatims from named sources, with volumes and dates."),
            ("CTQs operationally defined", "Metric, target, spec limit and a defect rule two people agree on."),
            ("Baseline is from real data", "8.5 pct comes from 4,200 WMS records, not from a manager's estimate."),
            ("SIPOC agreed and walked", "Start and stop points confirmed at the gemba by the process owner."),
            ("Stakeholders mapped, RACI set", "One A per row, engagement plan owned by a named team member."),
            ("Business case validated", "COPQ assumptions agreed in writing by a named Finance partner."),
            ("Risks and resources logged", "Team time released, risks named, escalation route agreed."),
        ], kicker=K, cols=2, accent=AMBER)

    d.compare_panels(
        "Three legitimate tollgate outcomes", [
            ("PROCEED", "Define is complete", [
                "Charter signed, CTQs defined",
                "Baseline data validated",
                "Move to the Measure phase",
            ]),
            ("REWORK", "Something is not yet solid", [
                "Scope too broad, or baseline unverified",
                "Fix the named gap, return in 1-2 weeks",
                "Far cheaper than discovering it in Analyse",
            ]),
            ("STOP", "The project should not continue", [
                "Solution already known - just implement it",
                "Benefit does not justify the effort",
                "Stopping early is a success, not a failure",
            ]),
        ], kicker=K, accent=AMBER)

    d.checkpoint(
        "Define phase - checkpoint",
        ["Name the four components of a problem statement and the two things it must never contain.",
         "Take one Northwind verbatim and drill it down to a CTQ with a metric and a limit.",
         "Why does a Delighter become a Must-Be, and what must you do about it?",
         "Which SIPOC column do you build first, and why does that order matter?",
         "How many people can be Accountable in one RACI row, and what breaks if there are two?",
         "State the Northwind goal statement with metric, baseline, target and date."],
        K)
