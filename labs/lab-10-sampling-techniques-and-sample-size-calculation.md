# Lab 10 — Sampling Techniques and Sample Size Calculation

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Select a sampling method and calculate the required sample size (A4).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

A justified sampling plan and calculated sample sizes for continuous and discrete data.

**Tools and techniques:** Simple random, stratified, systematic and cluster sampling, sample size formulas

## Steps

### Step 1

Review the four sampling techniques: simple random, stratified (sample within subgroups), systematic (every Nth), and cluster.

### Step 2

Choose stratified sampling if your process has distinct subgroups — for Northwind, sample within each shift and each carrier so no group is missed.

### Step 3

Note which techniques are non-random (convenience, judgment) and why they must not be used when the data will feed statistical analysis.

### Step 4

For continuous data, apply the formula from the deck: n = (1.96s / d)^2, where s is the estimated standard deviation, d is the margin of error and 1.96 gives 95% confidence.

### Step 5

Worked example: you want to estimate average order cycle time within 5 hours (d = 5) and a preliminary estimate of the standard deviation is 10 hours (s = 10). Calculate n.

```
n = (1.96 x 10 / 5)^2 = (3.92)^2 = 15.4, round up to 16 observations
```

### Step 6

For discrete/proportion data, calculate the sample size using the proportion defective and the margin of error given in the deck's formula.

### Step 7

Worked example: the proportion defective is 20% and the margin of error is 0.0784. Calculate the required sample size.

### Step 8

Compare the calculated n against what is practically collectable. If n is unaffordable, either widen the margin of error d or reduce the confidence level — and record that trade-off.

### Step 9

Write the final sampling plan: technique, sample size, sampling interval, period covered and who collects.

## Check your work

Your sample size is calculated from the formula rather than assumed, and your sampling technique is random or stratified — never convenience.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v3 · © 2026 Tertiary Infotech Academy Pte Ltd*
