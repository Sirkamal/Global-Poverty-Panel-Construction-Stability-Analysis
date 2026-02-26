# Global Poverty Panel Construction & Stability Analysis

## Project Goal

This project converts raw World Bank Poverty & Inequality Platform (PIP) survey aggregates into an analysis-ready panel dataset and evaluates welfare stability across countries.

The focus is not machine learning accuracy, but decision-relevant data preparation and interpretation.

---

Data Source

World Bank – Poverty & Inequality Platform (PIP)
Indicator: Poverty headcount ratio at $2.15/day (2017 PPP)



Key Steps

1. Population Definition

Filtered observations to represent the national population:

* Total population only
* All ages
* Both sexes
* Annual frequency

 2. Structural Cleaning

Identified multiple survey measurements per country-year and harmonized them into a single national estimate.

Method:
Multiple survey observations → aggregated using mean.

3. Time Normalization

Converted reporting years into a proper time variable and constructed a country-year panel dataset.

4. Data Validation

Performed:

* range checks (0–100%)
* duplicate checks
* measurement consistency checks

5. Analysis

Using Kenya as a case study:

* Detected structural breaks in welfare trends
* Measured poverty volatility using standard deviation
* Identified shock-sensitivity rather than steady improvement

---

Key Finding

Poverty reduction is not monotonic.
Some countries experience welfare gains that reverse after shocks, suggesting vulnerability rather than sustained development.

---

Skills Demonstrated

* Data harmonization
* Panel data construction
* Measurement validation
* Exploratory structural analysis
* Risk interpretation

---

 Tools

Python, Pandas, Matplotlib
if you need me, get me sirkamaal@gmail.com 
