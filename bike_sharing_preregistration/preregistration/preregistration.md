Analysis Preregistration

Project: Weather conditions and hourly bike-sharing demand  
Dataset file:`data/raw/hour.csv`  
Status: Plan written before examining the relationship between weather and rental counts  
Version: 1.0  
Preregistration date:2026-10-10

1. Research question

Among the hourly records in this bike-sharing dataset, is the mean number of bike rentals lower during less favorable weather conditions (weather categories 2–4) than during clear or partly cloudy conditions (category 1)?

This is an observational question. The analysis will estimate an association and will not claim that weather alone causes any observed difference.

2. Hypotheses

Let Group A be hours with `weathersit == 1`, and Group B be hours with `weathersit` in `{2, 3, 4}`.

- Null hypothesis (H₀): The population mean hourly rental count is equal in Group A and Group B.
- Alternative hypothesis (H₁): The population mean hourly rental count is lower in Group B than in Group A.

Although the alternative has a direction, the primary test will be two-sided at α = 0.05. The direction and magnitude of the estimated difference will be reported.

3. Population, sample, and exclusions

- Target population: Hourly bike-sharing demand under the conditions represented by the source dataset.
- Unit of analysis: One recorded hour.
- Available sample: All rows in `hour.csv` that pass the prespecified data-quality checks.
- Inclusion rules: A row must have a valid weather category (`weathersit` 1–4) and a non-missing, non-negative rental count (`cnt`).
- Exclusion rules: Exclude exact duplicate rows after checking the record identifier; exclude rows missing the primary exposure or outcome; exclude impossible values such as negative rental counts or invalid weather codes. Do not exclude a row merely because its rental count is unusually high or low.
- Stopping rule: Use all eligible rows in the provided dataset. Do not stop early or add rows based on the results.
- Rare category note:Weather category 4 may be very rare. Categories 2–4 are combined for the primary comparison; category 4 will not be analyzed as a standalone group.

4. Variables and measures

- Primary outcome:`cnt`, total bike rentals recorded in an hour.
- Primary exposure: `weathersit`.
- Primary comparison: Category 1 (clear/few clouds/partly cloudy) versus categories 2–4 (worse weather categories, according to the dataset codebook).
- Prespecified adjustment variables for robustness analysis:`hr` (hour), `season`, `workingday`, and `yr` (year indicator).
- Identifiers/date fields: `instant` is a record identifier; `dteday` is the observation date. They will not be treated as primary predictors in the main comparison.
- Transformations:Create a binary indicator `less_favorable_weather = 1` for weather categories 2–4 and `0` for category 1. No transformation of `cnt` will be used in the primary analysis.
- Missing data:The primary analysis will use complete cases for the outcome and exposure. The number of rows removed and reasons will be reported. No outcome values will be imputed.
- Data integrity:Check valid ranges, duplicate identifiers, and whether `cnt` equals `casual + registered` when those columns are available. Integrity checks will be documented before analysis.

5. Analysis plan

Primary analysis
1. Report the number of eligible hourly observations in each weather group.
2. Estimate each group's mean and standard deviation for `cnt`.
3. Estimate the mean difference as **Group B minus Group A**. A negative value indicates fewer rentals in less favorable weather.
4. Use a Welch independent-samples t-test (two-sided, α = 0.05), which does not assume equal population variances.
5. Report the estimated mean difference, a 95% confidence interval, the p-value, and Cohen's d (with the sign defined as Group B minus Group A).

Assumptions and diagnostics
Check data validity and inspect the distribution of rental counts and group sizes. Hourly observations may not be independent because nearby hours can be related; this limitation will be stated when interpreting the primary test.

Robustness check
Fit an ordinary least-squares regression with `cnt` as the outcome, the binary less-favorable-weather indicator as the exposure, and `hr`, `season`, `workingday`, and `yr` as categorical adjustment variables. Use HC3 heteroskedasticity-robust standard errors and report the weather coefficient with a 95% confidence interval. This is a robustness analysis, not a causal estimate.

Reporting
Report sample sizes, group means and standard deviations, mean difference, confidence interval, p-value, effect size, and the robustness-model estimate. Do not use statistical significance alone to judge importance.

6. Deviations

Any deviation from this plan will be recorded below with a timestamp, the original decision, the change made, and the reason. Results-driven changes will be labeled exploratory.

| Timestamp | Planned method | Deviation | Reason | Before/after outcome inspection |
|---|---|---|---|---|
| None yet | Follow Version 1.0 above | None | Not applicable | Not applicable |


(Dataset source)

Dataset name:Bike Sharing Dataset

Source:UCI Machine Learning Repository

Official URL: https://archive.ics.uci.edu/dataset/275/bike+sharing+dataset

file used:data/raw/hour.csv

Dataset type: Observational, hourly bike-sharing records.