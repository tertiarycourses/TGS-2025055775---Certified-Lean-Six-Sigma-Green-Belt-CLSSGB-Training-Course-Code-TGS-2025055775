"""
Domain 3 — The ANALYZE phase.

Labs 14-18. The statistical heart of the Green Belt. The Yellow Belt asserts a root
cause from a Fishbone; the Green Belt PROVES it with a hypothesis test and quantifies
the relationship with correlation and regression.

Decision rules used here come from the CSSC handbook and the v21 trainer deck:
    p < alpha            -> reject H0, accept Ha
    alpha = 0.05         -> 95% confidence
    |R| >= 0.4           -> correlation is considered to occur
    r^2                  -> proportion of variation in Y explained by X
"""

DOMAIN3 = [
    dict(
        num=14, topic=3,
        title="Variation, Run Charts and Stability Analysis",
        objective="Distinguish common cause from special cause variation using run charts (A3).",
        desc="Before hunting root causes, establish whether the process is stable. Common cause "
             "variation is built into the process and requires a process change; special cause "
             "variation is an assignable external event. Confusing the two leads to tampering — "
             "reacting to noise and making the process worse.",
        build="A run chart of the baseline data with the six non-random patterns assessed.",
        services="Common vs special cause, run chart, median line, trend, shift, cluster, mixture, oscillation, bias",
        steps=[
            ("Plot your baseline Y data in time order — time order matters, so never sort the data first.", ""),
            ("Draw the median line through the plotted points.", ""),
            ("Test for a TREND: six or more consecutive points steadily increasing or decreasing.", ""),
            ("Test for a SHIFT: eight or more consecutive points on the same side of the median, indicating the process level changed.", ""),
            ("Test for CLUSTERING: groups of points bunched together, suggesting a batch or intermittent effect.", ""),
            ("Test for MIXTURES: points avoiding the median line, which usually means two different processes are being plotted as one.", ""),
            ("Test for OSCILLATION: fourteen or more points alternating up and down, often over-adjustment by operators.", ""),
            ("Test for BIAS: too few or too many runs above and below the median compared with what randomness would produce.", ""),
            ("Classify your process: stable with common cause variation only, or unstable with special causes present.", ""),
            ("If special causes are present, investigate and record what changed at that point in time before proceeding — an unstable process cannot be meaningfully capable.", ""),
            ("Explain the tampering trap: adjusting a stable process in response to common cause variation always increases variation.", ""),
        ],
        test="You can state whether your process is stable, name every non-random pattern you tested for, and explain what tampering is and why it makes things worse.",
    ),
    dict(
        num=15, topic=3,
        title="Pareto Analysis, Stratification and Boxplots",
        objective="Prioritise the vital few causes using Pareto and stratified analysis (A3).",
        desc="The 80/20 rule states that roughly 80% of the effect comes from 20% of the causes. "
             "Build a Pareto chart to find the vital few, then stratify the data by shift, carrier "
             "and product family to test whether the problem is universal or concentrated — a "
             "concentrated problem is far easier to fix.",
        build="A Pareto chart with cumulative line, stratified Pareto charts and comparative boxplots.",
        services="Pareto principle, Pareto chart, cumulative percentage, stratification, boxplot, quartiles, outliers",
        steps=[
            ("Categorise the defects from your data collection: for Northwind, the reasons orders shipped late.", ""),
            ("Count the frequency of each category and sort the categories in descending order of frequency.", ""),
            ("Calculate the cumulative percentage across the sorted categories.", ""),
            ("Draw the Pareto chart: descending bars on the left axis, cumulative percentage line on the right axis.", ""),
            ("Read where the cumulative line crosses 80% — the categories to the left of that point are your vital few.", ""),
            ("Stratify: rebuild the Pareto separately for each shift, each carrier and each product family.", ""),
            ("Compare the stratified charts. If one shift or carrier dominates, the problem is concentrated and your project scope should narrow to it.", ""),
            ("Build a boxplot of cycle time by stratification factor — read the median, the interquartile box, the whiskers and any outliers.", ""),
            ("Use the boxplots to compare groups visually: if the boxes barely overlap, the groups are probably genuinely different — a hypothesis you will test formally in Lab 17.", ""),
            ("Write your prioritisation conclusion: which categories you will pursue and which you are explicitly deferring.", ""),
        ],
        test="Your Pareto identifies the vital few crossing 80% cumulative, and your stratified charts show whether the problem is universal or concentrated in a subgroup.",
    ),
    dict(
        num=16, topic=3,
        title="Fishbone, 5 Whys, Multi-Voting and Cause Prioritisation",
        objective="Generate, organise and prioritise candidate root causes (A3, K2).",
        desc="Structured cause generation prevents the team jumping to a favourite theory. Use a "
             "Fishbone to organise causes by category, 5 Whys to drill from symptom to actionable "
             "cause, and multi-voting to converge on the few worth testing with data.",
        build="A Fishbone diagram, three 5 Whys chains and a multi-voted shortlist of causes to test.",
        services="Ishikawa/Fishbone, 5M+E categories, 5 Whys, brainstorming, multi-voting, nominal group technique",
        steps=[
            ("Write the effect — your project problem — in the fish head. State it as a measurable problem, not a vague complaint.", ""),
            ("Draw the main bones using the 5M+E categories: Manpower, Method, Machine, Material, Measurement and Environment.", ""),
            ("Brainstorm causes onto each bone. Set brainstorming ground rules first: no criticism, quantity over quality, build on others' ideas.", ""),
            ("For each major bone, ask 'why does this happen?' to add sub-causes — a bone with no sub-causes has not been explored.", ""),
            ("Select the three most promising causes and run a 5 Whys chain on each, asking why repeatedly until you reach an actionable process cause.", ""),
            ("Stop each 5 Whys chain when the answer becomes a process or system, not a person — 'the picker was careless' is a symptom, not a root cause.", ""),
            ("Check each chain for logical validity by reading it backwards with 'therefore' — if it does not read logically, the chain is broken.", ""),
            ("Run multi-voting to converge: each participant gets N/3 votes to distribute across the candidate causes.", ""),
            ("Rank the causes by votes and select the top three to five for statistical validation.", ""),
            ("For each shortlisted cause, write the hypothesis you will test in Lab 17 and name the data you need to test it.", ""),
            ("Record explicitly that a cause is only a ROOT cause once data supports it — until then it remains a theory.", ""),
        ],
        test="Every Fishbone bone has sub-causes, each 5 Whys chain ends at a process cause rather than a person, and each shortlisted cause has a testable hypothesis written for it.",
    ),
    dict(
        num=17, topic=3,
        title="Hypothesis Testing — Test Selection, p-values and Conclusions",
        objective="Prove or disprove a suspected root cause statistically (A3, K2).",
        desc="The defining Green Belt skill. Instead of asserting that the night shift is slower, "
             "state it as a hypothesis, choose the correct test for your data type and question, "
             "and let the p-value decide. This is how a Green Belt replaces opinion with evidence.",
        build="Stated hypotheses, a justified test selection, and a documented statistical conclusion.",
        services="H0 and Ha, alpha, p-value, Type I and Type II error, t-tests, paired t, chi-square, ANOVA, Mann-Whitney",
        steps=[
            ("Write the null hypothesis H0 as a statement of NO difference or no effect — it always contains an equals relationship.", ""),
            ("Write the alternative hypothesis Ha as the difference you suspect — not equal, greater than, or less than.", ""),
            ("Remember hypotheses are statements about the POPULATION, not the sample. You can simply calculate the sample mean; you infer about the population.", ""),
            ("Set the confidence level and hence alpha: 95% confidence gives alpha = 0.05; 99% gives 0.01.", ""),
            ("Understand the two error types: Type I rejects a true H0 (producer risk, measured by alpha); Type II accepts a false H0 (consumer risk, measured by beta).", ""),
            ("Select the correct test using four questions: what data type, how many levels of X, is the data normal, and are you testing means, medians, variances or proportions.", ""),
            ("Apply the selection rules — 1-Sample t compares a sample mean to a target; 2-Sample t compares means of two different populations; Paired t compares the same subjects before and after.", ""),
            ("Note the classic trap: the same team measured before and after training needs a PAIRED t-test, while team A versus team B needs a 2-SAMPLE t-test.", ""),
            ("For non-normal data comparing medians, use the non-parametric equivalents: One-Sample Wilcoxon or Mann-Whitney.", ""),
            ("For comparing proportions use 1-Proportion or 2-Proportion; for comparing variances use the chi-square or F-test; for more than two groups use ANOVA.", ""),
            ("Test your Northwind hypothesis: is the mean order cycle time on the night shift significantly greater than on the day shift? State H0, Ha and the test you selected.", ""),
            ("Run the test and read the p-value. Apply the decision rule: if p < alpha, reject H0 and accept Ha; if p > alpha, fail to reject H0.", ""),
            ("Worked interpretation: with alpha set at 0.05, a returned p-value of 0.031 means reject H0 — the difference is statistically significant.", ""),
            ("Translate the statistical result into business language for your sponsor — never present a p-value without saying what it means for the process.", ""),
            ("Record the caution: failing to reject H0 does not prove H0 is true; it means you lack sufficient evidence to reject it, which may simply mean too small a sample.", ""),
        ],
        test="For each tested cause you can state H0, Ha, the test selected with justification, the p-value, the decision against alpha, and the business conclusion in plain language.",
    ),
    dict(
        num=18, topic=3,
        title="Correlation, Regression and Quantifying the X-Y Relationship",
        objective="Quantify how strongly each X drives Y and build a predictive model (A3).",
        desc="Hypothesis testing tells you whether a difference exists; correlation and regression "
             "tell you how strongly two variables move together and let you predict Y from X. This "
             "is how a Green Belt identifies which Xs are worth controlling — while never "
             "forgetting that correlation does not prove causation.",
        build="A scatter plot, a correlation coefficient, a regression equation and a prediction with its limits.",
        services="Scatter plot, Pearson correlation coefficient R, coefficient of determination r-squared, linear regression, prediction",
        steps=[
            ("Build a scatter plot with the suspected X on the horizontal axis and the project Y on the vertical axis.", ""),
            ("Read the plot visually first: is the pattern positive, negative, or absent? Is it linear or curved? Are there outliers?", ""),
            ("Calculate the correlation coefficient R. Recall R ranges from -1 to +1: +1 is perfect positive, -1 perfect negative, 0 no relationship.", ""),
            ("Apply the decision threshold from the reference: correlation is considered to occur when R is 0.4 or greater, or -0.4 or less.", ""),
            ("Calculate the coefficient of determination r-squared by squaring R.", ""),
            ("Interpret r-squared as the proportion of variation in Y explained by X. If R = 0.86 then r-squared = 0.74, so about 74% of the variation in Y relates to X and 26% is unexplained.", ""),
            ("Confirm the data type requirement: both correlation and regression need continuous or ratio data. Category names against outputs do not qualify — use Pareto instead.", ""),
            ("Fit the regression line and record the equation in the form y = mx + c.", ""),
            ("Use the equation to predict Y at two specific X values, and check the predictions against actual observed data at those points.", ""),
            ("Solve the equation in reverse to find the X range that delivers your target Y — this becomes the operating window you will control in the Control phase.", ""),
            ("Test the model's honesty: for a low r-squared, show a point where the prediction badly misses the actual value and explain why the model must not be used there.", ""),
            ("Write the causation caution explicitly: strong correlation does not prove X causes Y. Confirm causation with process knowledge, a designed experiment, or a pilot.", ""),
            ("Combine your evidence: list which Xs are now supported by BOTH a significant hypothesis test and a meaningful correlation — these are your validated vital few.", ""),
        ],
        test="You can state R, r-squared and the regression equation, use it to predict Y, and explain in one sentence why the correlation alone does not prove causation.",
    ),
]
