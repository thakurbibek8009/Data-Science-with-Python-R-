# Advanced Statistical Analysis & Hypothesis Testing

## Project Overview

This project demonstrates common statistical tests and hypothesis-testing techniques using the **Diabetes dataset** available through scikit-learn. The analysis explores distribution normality, compares two groups, tests differences across BMI groups, and evaluates whether results vary by the encoded sex group.

The main deliverable is the Jupyter notebook: `advanced_statistical_analysis_completed.ipynb`.

## Objectives

- Test whether BMI-based groups follow a normal distribution.
- Compare two groups using both a parametric and a non-parametric test.
- Test whether the outcome differs across BMI tertiles.
- Use Tukey HSD post-hoc comparisons to identify which BMI groups differ.
- Evaluate BMI group, encoded sex group, and their interaction with a two-way ANOVA.
- Report p-values, confidence intervals, effect size, plots, and interpretations.

## Dataset

The notebook uses the Diabetes dataset provided by `sklearn.datasets`.

- **Observations:** 442
- **Features:** Includes BMI and other baseline variables, along with a quantitative disease-progression measure.
- **Grouping variables:** BMI tertiles (Low, Medium, High) and an encoded sex group (A/B).

The BMI groups are created by dividing observations into three groups based on BMI. The sex variable is encoded as groups A and B for analysis.

## Statistical Methods

1. **Normality checks**
   - Shapiro–Wilk test
   - Kolmogorov–Smirnov test
   - Distribution plots

2. **Two-group comparison**
   - Welch's two-sample t-test
   - Mann–Whitney U test
   - 95% confidence interval for the mean difference

3. **One-way ANOVA**
   - Compares the outcome across Low, Medium, and High BMI groups
   - Tukey HSD post-hoc comparisons

4. **Two-way ANOVA**
   - Tests BMI group and encoded sex group
   - Tests the BMI-group-by-sex-group interaction

5. **Diagnostics and effect size**
   - Levene's test for variance equality
   - Eta-squared effect size

## Key Findings

The notebook's results show:

- The two-group comparison did **not** find a statistically significant difference between encoded sex groups using either Welch's t-test or Mann–Whitney U.
- The one-way ANOVA found a statistically significant difference across BMI tertiles.
- Tukey HSD found statistically significant pairwise differences among all three BMI groups.
- In the two-way ANOVA, BMI group was statistically significant, while encoded sex group and the interaction were not statistically significant.
- Levene's test indicated unequal variances across BMI groups, so ANOVA results should be interpreted with this assumption check in mind.
- The normality tests did not consistently support normality across all BMI groups.

See the notebook for exact test statistics, p-values, confidence intervals, plots, and detailed interpretations.

## Requirements

Install Python 3.9+ (or a compatible Python version) and the packages below:

```bash
pip install numpy pandas scipy matplotlib seaborn statsmodels scikit-learn jupyter
```

## How to Run

1. Download or clone this project folder.
2. Open a terminal in the project directory.
3. Start Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

4. Open `advanced_statistical_analysis_completed.ipynb`.
5. Choose **Kernel → Restart Kernel and Run All Cells** (menu wording may vary).

You can also open and run the notebook in Visual Studio Code with the Jupyter extension installed.

## Project Structure

```text
.
├── README.md
└── advanced_statistical_analysis_completed.ipynb
```

## Interpretation Notes and Limitations

- A small p-value is evidence against the relevant null hypothesis; it does not, by itself, measure practical importance.
- Normality-test results can be sensitive to sample size. Use the distribution plots alongside the test results.
- The standard one-way and two-way ANOVA models rely on assumptions, including independence and suitable residual behavior. The variance diagnostic suggests unequal variances across BMI groups.
- The Kolmogorov–Smirnov p-values in the notebook are approximate because the distribution parameters are estimated from the sample. A formal normality assessment should account for parameter estimation.
- The sex variable is represented as encoded groups A/B in this analysis; interpret it as a dataset grouping variable rather than as a causal explanation.
- These are statistical associations in a dataset, not evidence that BMI or sex causes a change in the outcome.

## Deliverables

- `advanced_statistical_analysis_completed.ipynb` — notebook containing code, statistical tests, plots, and interpretations.
- `README.md` — project overview and instructions.

## Author

Add your name, course, institution, and submission date here if required.
