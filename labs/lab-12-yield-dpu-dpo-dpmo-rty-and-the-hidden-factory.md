# Lab 12 — Yield, DPU, DPO, DPMO, RTY and the Hidden Factory

**DMAIC phase:** MEASURE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Calculate the full family of process performance metrics from raw data (A4).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

A metrics worksheet with yield, FPY, RTY, DPU, DPO and DPMO calculated for the process.

**Tools and techniques:** Classic yield, first pass yield, rolled throughput yield, DPU, DPO, DPMO, DUDO analysis

## Steps

### Step 1

Run the DUDO analysis first: define the Defect, the Unit, the Defect Opportunities per unit and the Observed defects — every metric depends on these four definitions.

### Step 2

Calculate classic yield: units passing final inspection / units started, expressed as a percentage.

### Step 3

Calculate first pass yield for each process step: units passing that step first time without rework / units entering that step.

### Step 4

Calculate rolled throughput yield by multiplying the FPY of every step together — RTY = FPY1 x FPY2 x ... x FPYn.

### Step 5

Compare RTY against classic yield. The gap between them is the hidden factory: the rework you were paying for but not measuring.

### Step 6

Calculate DPU = total defects found / total units inspected.

### Step 7

Calculate DPO = defects / (units x opportunities per unit).

### Step 8

Calculate DPMO = DPO x 1,000,000, then convert to a sigma level using the conversion table.

### Step 9

For a five-step process where each step runs at 95% FPY, calculate RTY and note how a 'good' 95% per step collapses to roughly 77% end to end.

```
RTY = 0.95^5 = 0.7738, or 77.4%
```

### Step 10

Record the baseline figures — these are what the Improve phase must beat.

## Check your work

Your RTY is lower than your classic yield, you can explain the hidden factory gap between them, and your DPMO converts to a stated sigma level.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v2 · © 2026 Tertiary Infotech Academy Pte Ltd*
