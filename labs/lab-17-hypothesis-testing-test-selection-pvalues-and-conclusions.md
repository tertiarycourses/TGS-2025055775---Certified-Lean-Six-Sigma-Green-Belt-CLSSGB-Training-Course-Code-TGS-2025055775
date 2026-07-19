# Lab 17 — Hypothesis Testing — Test Selection, p-values and Conclusions

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Prove or disprove a suspected root cause statistically (A3, K2).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

Stated hypotheses, a justified test selection, and a documented statistical conclusion.

**Tools and techniques:** H0 and Ha, alpha, p-value, Type I and Type II error, t-tests, paired t, chi-square, ANOVA, Mann-Whitney

## Steps

### Step 1

Write the null hypothesis H0 as a statement of NO difference or no effect — it always contains an equals relationship.

### Step 2

Write the alternative hypothesis Ha as the difference you suspect — not equal, greater than, or less than.

### Step 3

Remember hypotheses are statements about the POPULATION, not the sample. You can simply calculate the sample mean; you infer about the population.

### Step 4

Set the confidence level and hence alpha: 95% confidence gives alpha = 0.05; 99% gives 0.01.

### Step 5

Understand the two error types: Type I rejects a true H0 (producer risk, measured by alpha); Type II accepts a false H0 (consumer risk, measured by beta).

### Step 6

Select the correct test using four questions: what data type, how many levels of X, is the data normal, and are you testing means, medians, variances or proportions.

### Step 7

Apply the selection rules — 1-Sample t compares a sample mean to a target; 2-Sample t compares means of two different populations; Paired t compares the same subjects before and after.

### Step 8

Note the classic trap: the same team measured before and after training needs a PAIRED t-test, while team A versus team B needs a 2-SAMPLE t-test.

### Step 9

For non-normal data comparing medians, use the non-parametric equivalents: One-Sample Wilcoxon or Mann-Whitney.

### Step 10

For comparing proportions use 1-Proportion or 2-Proportion; for comparing variances use the chi-square or F-test; for more than two groups use ANOVA.

### Step 11

Test your Northwind hypothesis: is the mean order cycle time on the night shift significantly greater than on the day shift? State H0, Ha and the test you selected.

### Step 12

Run the test and read the p-value. Apply the decision rule: if p < alpha, reject H0 and accept Ha; if p > alpha, fail to reject H0.

### Step 13

Worked interpretation: with alpha set at 0.05, a returned p-value of 0.031 means reject H0 — the difference is statistically significant.

### Step 14

Translate the statistical result into business language for your sponsor — never present a p-value without saying what it means for the process.

### Step 15

Record the caution: failing to reject H0 does not prove H0 is true; it means you lack sufficient evidence to reject it, which may simply mean too small a sample.

## Check your work

For each tested cause you can state H0, Ha, the test selected with justification, the p-value, the decision against alpha, and the business conclusion in plain language.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v2 · © 2026 Tertiary Infotech Academy Pte Ltd*
