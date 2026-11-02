# Weather and Hourly Bike-Sharing Demand: Data Science Research Capstone

## Research question
Among hourly observations in the UCI Bike Sharing dataset, are poor-weather hours associated with fewer total bike rentals than good-weather hours, after adjustment for hour of day, working-day status, season, and year?

This is an observational association study, not a causal analysis.

## Key result
The preregistered HC3-robust OLS model estimates a poor-weather coefficient of -0.658 on `log1p(cnt)` (95% CI -0.701 to -0.616; two-sided p=1.69e-203). The exponentiated coefficient is 0.518 (95% CI 0.496 to 0.540) on the transformed outcome scale. Interpret carefully: this is a conditional association in a log1p model, not a direct causal percentage change in arithmetic mean rentals.

## Dataset
- UCI Bike Sharing hourly dataset (`hour.csv`)
- 17,379 observations, 17 columns in supplied file
- 2011-01-01 through 2012-12-31
- No missing values and no duplicate rows in the supplied file
- Licensed CC BY 4.0; cite Hadi Fanaee-T (2013), UCI Machine Learning Repository, DOI: 10.24432/C5W894.

## Repository structure
```text
.
├── data/raw/hour.csv
├── figures/
├── notebooks/capstone_analysis.ipynb
├── preregistration/
├── reports/Capstone_Whitepaper.pdf
├── reports/generated/
├── src/analysis.py
├── tests/
├── requirements.txt
└── README.md
```

## Reproduce
```bash
python -m venv .venv
# activate the environment
pip install -r requirements.txt
python src/analysis.py --data data/raw/hour.csv --output reports/generated
jupyter notebook
```
Open `notebooks/capstone_analysis.ipynb` and run all cells.

## Main analysis
Exposure: poor weather = `weathersit` 3–4; reference = 1–2. Outcome: `log1p(cnt)`. Covariates: categorical hour, workingday, season, year. OLS with HC3 heteroskedasticity-robust standard errors. Secondary analyses are labelled as such in the report.

## Important caveats
- The dataset covers one system and two historical years; it is not automatically representative of other cities or current operations.
- Observational associations do not establish causality.
- The model's Breusch–Pagan diagnostic indicates heteroskedasticity; HC3 robust standard errors address inference sensitivity to heteroskedasticity but do not correct omitted-variable bias or temporal dependence.
- Residual dependence and the repeated hourly structure merit further time-series or clustered-error analysis in future work.
- `casual` and `registered` are not predictors because they sum to `cnt`.

## Sources
- UCI dataset: https://doi.org/10.24432/C5W894
- Fanaee-T & Gama (2013), *Event labeling combining ensemble detectors and background knowledge*.
- Bean, Pojani & Corcoran (2021), *How does weather affect bikeshare use?* https://doi.org/10.1016/j.jtrangeo.2021.103155
- Miranda-Moreno & Nosal (2011), *Weather or Not to Cycle*. https://doi.org/10.3141/2247-06
