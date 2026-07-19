# Lab 18 — Correlation, Regression and Quantifying the X-Y Relationship

**DMAIC phase:** ANALYZE  |  **Lab type:** Core  |  **Course:** Certified Lean Six Sigma Green Belt (CLSSGB) Training (TGS-2025055775)

## Objective

Quantify how strongly each X drives Y and build a predictive model (A3).

## Scenario

Northwind Retail Distribution Centre fulfils online orders from a 12,000 sqm warehouse. Customers are complaining about late deliveries and the company is receiving negative feedback on social media. The Distribution Manager has asked you, as Green Belt, to lead a DMAIC project on the order-fulfilment process — from order release to carrier handover.

## What you will build

A scatter plot, a correlation coefficient, a regression equation and a prediction with its limits.

**Tools and techniques:** Scatter plot, Pearson correlation coefficient R, coefficient of determination r-squared, linear regression, prediction

## Steps

### Step 1

Build a scatter plot with the suspected X on the horizontal axis and the project Y on the vertical axis.

### Step 2

Read the plot visually first: is the pattern positive, negative, or absent? Is it linear or curved? Are there outliers?

### Step 3

Calculate the correlation coefficient R. Recall R ranges from -1 to +1: +1 is perfect positive, -1 perfect negative, 0 no relationship.

### Step 4

Apply the decision threshold from the reference: correlation is considered to occur when R is 0.4 or greater, or -0.4 or less.

### Step 5

Calculate the coefficient of determination r-squared by squaring R.

### Step 6

Interpret r-squared as the proportion of variation in Y explained by X. If R = 0.86 then r-squared = 0.74, so about 74% of the variation in Y relates to X and 26% is unexplained.

### Step 7

Confirm the data type requirement: both correlation and regression need continuous or ratio data. Category names against outputs do not qualify — use Pareto instead.

### Step 8

Fit the regression line and record the equation in the form y = mx + c.

### Step 9

Use the equation to predict Y at two specific X values, and check the predictions against actual observed data at those points.

### Step 10

Solve the equation in reverse to find the X range that delivers your target Y — this becomes the operating window you will control in the Control phase.

### Step 11

Test the model's honesty: for a low r-squared, show a point where the prediction badly misses the actual value and explain why the model must not be used there.

### Step 12

Write the causation caution explicitly: strong correlation does not prove X causes Y. Confirm causation with process knowledge, a designed experiment, or a pilot.

### Step 13

Combine your evidence: list which Xs are now supported by BOTH a significant hypothesis test and a meaningful correlation — these are your validated vital few.

## Check your work

You can state R, r-squared and the regression equation, use it to predict Y, and explain in one sentence why the correlation alone does not prove causation.

## Deliverable

Save your output — it forms part of your Northwind improvement package and is your revision material for the assessment.

---

*Certified Lean Six Sigma Green Belt (CLSSGB) Training · TGS-2025055775 · Version v2 · © 2026 Tertiary Infotech Academy Pte Ltd*
