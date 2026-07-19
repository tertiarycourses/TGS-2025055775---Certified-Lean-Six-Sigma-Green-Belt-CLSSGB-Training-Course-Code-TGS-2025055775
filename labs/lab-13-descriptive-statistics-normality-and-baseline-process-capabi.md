# Lab 13 — Descriptive Statistics, Normality and Baseline Process Capability

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Summarise the baseline statistically and calculate Cp and Cpk (A4, K1).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

A descriptive statistics summary, a normality assessment and calculated Cp and Cpk values.

**Tools and techniques:** Mean, median, range, standard deviation, histogram, normal distribution, Cp, Cpk, sigma level

## Steps

### Step 1

Calculate the measures of central tendency for your baseline data: mean, median and mode. Note which is more resistant to outliers.

### Step 2

Calculate the measures of dispersion: range and standard deviation. Variation, not the average, is what the customer feels.

### Step 3

Build a histogram of the baseline data and choose the bin count carefully — too few bins show nothing, too many look like a comb.

### Step 4

Read the histogram shape: bell-shaped, skewed, or bi-modal. A bi-modal shape usually means you are measuring two processes as if they were one — stratify and re-plot.

### Step 5

Recall the empirical rule for a normal curve: 68.26% of data within +/-1 standard deviation, 95.46% within +/-2, and 99.73% within +/-3.

### Step 6

Assess normality — if the data is clearly non-normal, note that hypothesis tests assuming normality will not be valid in Lab 17.

### Step 7

Mark the specification limits (USL and LSL) from your CTQ in Lab 4 onto the histogram and count how many observations fall outside.

### Step 8

Calculate Cp using the formula from the deck: Cp = (USL - LSL) / 6s, that is specification width divided by process spread.

### Step 9

Worked example: USL = 48 hours, LSL = 0 hours, standard deviation s = 6 hours. Calculate Cp.

```
Cp = (48 - 0) / (6 x 6) = 48 / 36 = 1.33
```

### Step 10

Calculate Cpk, which also accounts for how far off-centre the process sits, and compare against the Cp value.

### Step 11

Interpret the result: Cp >= 1 means potentially capable, Cpk >= 1.33 is the usual minimum for customer satisfaction, and many organisations target 2.0.

### Step 12

If Cp is acceptable but Cpk is poor, record the conclusion: the process spread is fine but the process is off-centre — a very different fix.

## Check your work

You can state your baseline Cp and Cpk, explain the difference between them, and say whether the problem is spread, centring or both.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v4 · © 2026 Tertiary Infotech Academy Pte Ltd*
