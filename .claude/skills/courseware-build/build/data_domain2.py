"""
Domain 2 — The MEASURE phase.

Labs 7-13. This is where the Green Belt clearly departs from the Yellow Belt: the
Yellow Belt fills in a check sheet, the Green Belt proves the measurement system is
trustworthy (MSA/Gage R&R), calculates how much data is enough (sample size), and
converts the baseline into a capability index.

Formulas used here are reproduced from the original v21 trainer deck, not invented:
    Sample size (continuous)  n = (1.96s / d)^2
    DPMO                      (defects / (units x opportunities)) x 1,000,000
    Takt time                 available working time / customer demand
"""

DOMAIN2 = [
    dict(
        num=7, topic=2,
        title="Detailed Process Mapping and Swimlane Analysis",
        objective="Map the as-is process to expose handoffs, delays and rework loops (A2).",
        desc="The SIPOC gave the macro view; now build the detailed map that shows every actor, "
             "system and handoff. Handoffs are where delay and defects are created, so a swimlane "
             "map that puts each actor in their own lane makes the problem visible in a way a "
             "flowchart cannot.",
        build="A detailed process map and a swimlane map with pain points and handoffs marked.",
        services="SIPOC & Process Map Builder, process symbols, flowchart, swimlane map, handoff analysis, pain points",
        steps=[
            ("Review the standard process symbols: oval for start/stop, rectangle for activity, diamond for decision, D-shape for delay, and the document symbol.", ""),
            ("Walk the process physically (go to gemba) and record every step in sequence as it actually happens — not as the SOP says it should.", ""),
            ("Build the detailed process map with columns: Step, Actor, Activity, System, Time, Handoff (Y/N).", ""),
            ("Continue in the SIPOC & Process Map Builder — assign an actor to each step and it generates the swimlane and the handoff table for you.", "https://alfredang.github.io/sipoc/"),
            ("Redraw the same flow as a swimlane map, giving each actor or department its own lane.", ""),
            ("Count the handoffs — every time the flow crosses a lane boundary. Mark each one, since each is a queue and a risk of information loss.", ""),
            ("Mark every decision diamond that creates a rework loop and note what percentage of work takes the rework path.", ""),
            ("Tag pain points: delays, rework, unclear ownership, duplicate data entry and waiting for approval.", ""),
            ("Identify the three steps you suspect consume the most elapsed time — you will test that suspicion with data in Lab 9.", ""),
        ],
        test="Every lane crossing on your swimlane map is marked as a handoff with a named owner on both sides, and every rework loop is labelled with its percentage.",
    ),
    dict(
        num=8, topic=2,
        title="Value Stream Mapping, Takt Time and the Eight Wastes",
        objective="Build a value stream map and compare value-added time against total lead time (A2, A4).",
        desc="A value stream map shows material AND information flow, plus the timeline ladder that "
             "exposes how little of the total lead time actually adds value. Combine it with a takt "
             "time calculation and a waste walk to quantify the opportunity.",
        build="A current-state VSM with a timeline ladder, a takt time calculation and a waste walk log.",
        services="VSM icons, material and information flow, timeline ladder, takt time, DOWNTIME wastes",
        steps=[
            ("Review the standard VSM icons: process box, data box, inventory triangle, push arrow, supermarket, kanban and the kaizen burst.", ""),
            ("Draw the process boxes left to right, then add a data box under each with cycle time, changeover time, uptime and number of operators.", ""),
            ("Add the information flow across the top — how does each step know what to work on next?", ""),
            ("Add inventory triangles between steps with the observed queue quantity, and convert each to days of supply.", ""),
            ("Draw the timeline ladder along the bottom: value-added time on the lower rungs, waiting time on the upper rungs.", ""),
            ("Sum both rows and calculate process cycle efficiency = value-added time / total lead time. Typical service processes run under 10%.", ""),
            ("Calculate takt time = available working time per shift / customer demand per shift, then compare each step's cycle time against takt.", ""),
            ("Run a waste walk and tag every observation against the eight wastes (DOWNTIME): Defects, Overproduction, Waiting, Non-utilised talent, Transport, Inventory, Motion, Extra-processing.", ""),
            ("Mark kaizen bursts on the VSM where waste is concentrated — these become improvement candidates in the Improve phase.", ""),
        ],
        test="Your VSM shows both material and information flow, your timeline ladder yields a process cycle efficiency percentage, and every step's cycle time is compared against takt.",
    ),
    dict(
        num=9, topic=2,
        title="Data Types, Operational Definitions and the Data Collection Plan",
        objective="Build a data collection plan with unambiguous operational definitions (A4).",
        desc="The data type determines which statistical tool is legal later — continuous data "
             "unlocks far more powerful analysis than discrete. Classify your data, write "
             "operational definitions that two people would apply identically, and plan the "
             "collection before touching the process.",
        build="A data type classification, operational definitions and a complete data collection plan.",
        services="Continuous vs discrete, nominal vs ordinal, operational definitions, check sheets, data collection plan",
        steps=[
            ("Classify data as qualitative or quantitative, then quantitative as discrete (countable) or continuous (measurable on a scale).", ""),
            ("Classify qualitative data as nominal (no order — carrier name, defect type) or ordinal (ordered — priority, satisfaction rating).", ""),
            ("For your project Y and each candidate X, record the data type. Note where a discrete measure could be converted to continuous — always prefer continuous.", ""),
            ("Write the operational definition for each measure: what exactly is counted, when the clock starts and stops, which system field, and what is excluded.", ""),
            ("Test each definition by having two people apply it to the same five records — if they disagree, the definition is not yet operational.", ""),
            ("Build the data collection plan table: measure, data type, operational definition, source, who collects, how often, sample size, and how it is recorded.", ""),
            ("Design the check sheet or data capture form so it takes under 30 seconds to complete — complex forms do not get filled in.", ""),
            ("Add a stratification plan: capture shift, product family, carrier and picker at the same time so the Analyze phase can slice the data.", ""),
        ],
        test="Two people applying your operational definitions to the same records produce identical values, and your plan captures stratification factors alongside the main measure.",
    ),
    dict(
        num=10, topic=2,
        title="Sampling Techniques and Sample Size Calculation",
        objective="Select a sampling method and calculate the required sample size (A4).",
        desc="Measuring the whole population is rarely affordable, and a biased sample invalidates "
             "every conclusion that follows. Choose the right sampling technique, then calculate "
             "how much data is actually needed using the Green Belt sample size formula rather "
             "than guessing.",
        build="A justified sampling plan and calculated sample sizes for continuous and discrete data.",
        services="Simple random, stratified, systematic and cluster sampling, sample size formulas",
        steps=[
            ("Review the four sampling techniques: simple random, stratified (sample within subgroups), systematic (every Nth), and cluster.", ""),
            ("Choose stratified sampling if your process has distinct subgroups — for Northwind, sample within each shift and each carrier so no group is missed.", ""),
            ("Note which techniques are non-random (convenience, judgment) and why they must not be used when the data will feed statistical analysis.", ""),
            ("For continuous data, apply the formula from the deck: n = (1.96s / d)^2, where s is the estimated standard deviation, d is the margin of error and 1.96 gives 95% confidence.", ""),
            ("Worked example: you want to estimate average order cycle time within 5 hours (d = 5) and a preliminary estimate of the standard deviation is 10 hours (s = 10). Calculate n.", "n = (1.96 x 10 / 5)^2 = (3.92)^2 = 15.4, round up to 16 observations"),
            ("For discrete/proportion data, calculate the sample size using the proportion defective and the margin of error given in the deck's formula.", ""),
            ("Worked example: the proportion defective is 20% and the margin of error is 0.0784. Calculate the required sample size.", ""),
            ("Compare the calculated n against what is practically collectable. If n is unaffordable, either widen the margin of error d or reduce the confidence level — and record that trade-off.", ""),
            ("Write the final sampling plan: technique, sample size, sampling interval, period covered and who collects.", ""),
        ],
        test="Your sample size is calculated from the formula rather than assumed, and your sampling technique is random or stratified — never convenience.",
    ),
    dict(
        num=11, topic=2,
        title="Measurement System Analysis and Gage R&R",
        objective="Prove the measurement system is trustworthy before trusting the data (A4).",
        desc="This is a defining Green Belt skill. If the measurement system itself varies, you "
             "will chase phantom process problems. MSA separates total variation into real process "
             "variation and measurement variation, then tests repeatability (same appraiser) and "
             "reproducibility (different appraisers).",
        build="An attribute Gage R&R study with repeatability, reproducibility and accuracy percentages.",
        services="MSA, components of variation, accuracy, repeatability, reproducibility, resolution, Gage R&R acceptance",
        steps=[
            ("Draw the components of variation tree: total observed variation = actual process variation + measurement system variation.", ""),
            ("Split measurement variation into its parts — repeatability (one appraiser, repeated measures) and reproducibility (between appraisers).", ""),
            ("Check resolution first using the ten-bucket rule: the measurement device must resolve to about one tenth of the tolerance you need to detect.", ""),
            ("Set up an attribute Gage R&R: take at least 20 sample records, label them opaquely so appraisers cannot recognise them, and record the known correct attribute for each.", ""),
            ("Have two or three appraisers independently classify every sample — for Northwind, classify each order as on-time or late from the system record.", ""),
            ("Repeat the exercise with the sample order randomised so appraisers cannot recall their first answer.", ""),
            ("Calculate repeatability per appraiser: the percentage of samples where that appraiser agreed with themselves across both trials.", ""),
            ("Calculate reproducibility: the percentage of samples where all appraisers agreed with each other.", ""),
            ("Calculate accuracy: the percentage where each appraiser matched the known correct attribute.", ""),
            ("Apply the acceptance criteria — a system agreeing only around 50% of the time is not fit for use. Record what must be fixed: the operational definition, training or the device.", ""),
        ],
        test="You can state your repeatability, reproducibility and accuracy percentages and give a clear go/no-go verdict on whether the measurement system can be trusted.",
    ),
    dict(
        num=12, topic=2,
        title="Yield, DPU, DPO, DPMO, RTY and the Hidden Factory",
        objective="Calculate the full family of process performance metrics from raw data (A4).",
        desc="Classic yield counts what came out good at the end and hides all the rework that got "
             "it there — the hidden factory. Rolled throughput yield multiplies the first pass "
             "yield of every step and exposes the true cost of a multi-step process.",
        build="A metrics worksheet with yield, FPY, RTY, DPU, DPO and DPMO calculated for the process.",
        services="Classic yield, first pass yield, rolled throughput yield, DPU, DPO, DPMO, DUDO analysis",
        steps=[
            ("Run the DUDO analysis first: define the Defect, the Unit, the Defect Opportunities per unit and the Observed defects — every metric depends on these four definitions.", ""),
            ("Calculate classic yield: units passing final inspection / units started, expressed as a percentage.", ""),
            ("Calculate first pass yield for each process step: units passing that step first time without rework / units entering that step.", ""),
            ("Calculate rolled throughput yield by multiplying the FPY of every step together — RTY = FPY1 x FPY2 x ... x FPYn.", ""),
            ("Compare RTY against classic yield. The gap between them is the hidden factory: the rework you were paying for but not measuring.", ""),
            ("Calculate DPU = total defects found / total units inspected.", ""),
            ("Calculate DPO = defects / (units x opportunities per unit).", ""),
            ("Calculate DPMO = DPO x 1,000,000, then convert to a sigma level using the conversion table.", ""),
            ("For a five-step process where each step runs at 95% FPY, calculate RTY and note how a 'good' 95% per step collapses to roughly 77% end to end.", "RTY = 0.95^5 = 0.7738, or 77.4%"),
            ("Record the baseline figures — these are what the Improve phase must beat.", ""),
        ],
        test="Your RTY is lower than your classic yield, you can explain the hidden factory gap between them, and your DPMO converts to a stated sigma level.",
    ),
    dict(
        num=13, topic=2,
        title="Descriptive Statistics, Normality and Baseline Process Capability",
        objective="Summarise the baseline statistically and calculate Cp and Cpk (A4, K1).",
        desc="Close the Measure phase by describing the data — central tendency, dispersion and "
             "shape — testing whether it is normal, and converting it into capability indices. "
             "Cp asks whether the process COULD fit inside the specification; Cpk asks whether it "
             "actually does, given where it is centred.",
        build="A descriptive statistics summary, a normality assessment and calculated Cp and Cpk values.",
        services="Mean, median, range, standard deviation, histogram, normal distribution, Cp, Cpk, sigma level",
        steps=[
            ("Calculate the measures of central tendency for your baseline data: mean, median and mode. Note which is more resistant to outliers.", ""),
            ("Calculate the measures of dispersion: range and standard deviation. Variation, not the average, is what the customer feels.", ""),
            ("Build a histogram of the baseline data and choose the bin count carefully — too few bins show nothing, too many look like a comb.", ""),
            ("Read the histogram shape: bell-shaped, skewed, or bi-modal. A bi-modal shape usually means you are measuring two processes as if they were one — stratify and re-plot.", ""),
            ("Recall the empirical rule for a normal curve: 68.26% of data within +/-1 standard deviation, 95.46% within +/-2, and 99.73% within +/-3.", ""),
            ("Assess normality — if the data is clearly non-normal, note that hypothesis tests assuming normality will not be valid in Lab 17.", ""),
            ("Mark the specification limits (USL and LSL) from your CTQ in Lab 4 onto the histogram and count how many observations fall outside.", ""),
            ("Calculate Cp using the formula from the deck: Cp = (USL - LSL) / 6s, that is specification width divided by process spread.", ""),
            ("Worked example: USL = 48 hours, LSL = 0 hours, standard deviation s = 6 hours. Calculate Cp.", "Cp = (48 - 0) / (6 x 6) = 48 / 36 = 1.33"),
            ("Calculate Cpk, which also accounts for how far off-centre the process sits, and compare against the Cp value.", ""),
            ("Interpret the result: Cp >= 1 means potentially capable, Cpk >= 1.33 is the usual minimum for customer satisfaction, and many organisations target 2.0.", ""),
            ("If Cp is acceptable but Cpk is poor, record the conclusion: the process spread is fine but the process is off-centre — a very different fix.", ""),
        ],
        test="You can state your baseline Cp and Cpk, explain the difference between them, and say whether the problem is spread, centring or both.",
    ),
]
