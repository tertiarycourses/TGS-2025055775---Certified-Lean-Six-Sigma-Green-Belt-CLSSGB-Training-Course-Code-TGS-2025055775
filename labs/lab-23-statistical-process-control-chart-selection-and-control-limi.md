# Lab 23 — Statistical Process Control — Chart Selection and Control Limits

**DMAIC phase:** CONTROL  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Select, build and interpret the correct control chart for the process (A4, A5).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

A correctly selected control chart with calculated limits and the eight rules applied.

**Tools and techniques:** SPC, control chart selection tree, Xbar-R, Xbar-S, I-MR, p, np, c, u charts, control limits, zones

## Steps

### Step 1

Establish the difference between control limits and specification limits: control limits come from the process itself (the voice of the process), specification limits come from the customer (the voice of the customer). Never plot spec limits on a control chart.

### Step 2

Walk the control chart selection tree. First question: is your data continuous (variable) or discrete (attribute)?

### Step 3

For CONTINUOUS data, ask whether it can be sensibly subgrouped. If not, use an Individuals and Moving Range (I-MR) chart.

### Step 4

For continuous data in subgroups, use Xbar-R when the subgroup size is under 8, and Xbar-S when the subgroup size is 8 or more.

### Step 5

For DISCRETE data, ask whether you are counting DEFECTIVE UNITS or DEFECTS. This distinction decides the next branch.

### Step 6

For defective units (pass/fail): use a p-chart when the sample size varies, and an np-chart when the sample size is constant.

### Step 7

For counts of defects: use a u-chart when the sample size varies, and a c-chart when the sample size is constant.

### Step 8

Select the correct chart for your Northwind data and write down the justification against the tree.

### Step 9

Build the chart: plot the points in time order, calculate and draw the centre line, then the upper and lower control limits at +/- 3 standard deviations.

### Step 10

Divide the chart into zones: zone C within 1 sigma of the centre line, zone B between 1 and 2 sigma, zone A between 2 and 3 sigma.

### Step 11

Apply out-of-control rule 1: any single point beyond the UCL or LCL. Investigate immediately — the probability of this happening by chance is roughly 3 in 1,000.

### Step 12

Apply rule 2: nine consecutive points on the same side of the centre line, indicating the process level has shifted.

### Step 13

Apply rule 3: six consecutive points steadily increasing or decreasing, indicating a trend.

### Step 14

Apply rule 4: fourteen consecutive points alternating up and down, often caused by over-adjustment.

### Step 15

Apply rules 5 and 6: two of three consecutive points in zone A, or four of five in zone B or beyond, indicating a sudden shift.

### Step 16

Apply rules 7 and 8: fifteen consecutive points inside zone C (limits may need recalculating), or eight consecutive points with none in zone C (you may be charting two different processes).

### Step 17

Record every signal your chart shows and the assignable cause you found for each.

## Check your work

You can justify your chart choice against the selection tree, your limits are calculated at +/- 3 sigma, and you have applied all eight out-of-control rules.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v2 · © 2026 Tertiary Infotech Academy Pte Ltd*
