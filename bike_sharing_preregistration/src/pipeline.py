"""Preregistered analysis pipeline for hourly bike-sharing data."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from scipy import stats
import statsmodels.formula.api as smf


REQUIRED_COLUMNS = {"weathersit", "cnt", "hr", "season", "workingday", "yr"}


def prepare_data(data: pd.DataFrame) -> pd.DataFrame:
    """Validate required fields and create the prespecified weather group."""
    missing_columns = REQUIRED_COLUMNS - set(data.columns)
    if missing_columns:
        raise ValueError(f"Missing required columns: {sorted(missing_columns)}")

    clean = data.copy()
    clean = clean.drop_duplicates()

    clean["weathersit"] = pd.to_numeric(clean["weathersit"], errors="coerce")
    clean["cnt"] = pd.to_numeric(clean["cnt"], errors="coerce")
    clean = clean.dropna(subset=["weathersit", "cnt"])
    clean = clean[clean["weathersit"].isin([1, 2, 3, 4])]
    clean = clean[clean["cnt"] >= 0].copy()

    clean["less_favorable_weather"] = (
        clean["weathersit"].isin([2, 3, 4]).astype(int)
    )
    clean["weather_group"] = np.where(
        clean["less_favorable_weather"].eq(1),
        "Less favorable (2-4)",
        "Clear/partly cloudy (1)",
    )
    return clean


def analyze(data: pd.DataFrame) -> dict:
    """Run the preregistered primary test and robustness regression."""
    clean = prepare_data(data)
    group_a = clean.loc[clean["less_favorable_weather"].eq(0), "cnt"].astype(float)
    group_b = clean.loc[clean["less_favorable_weather"].eq(1), "cnt"].astype(float)

    if len(group_a) < 2 or len(group_b) < 2:
        raise ValueError("Each weather group needs at least two observations.")

    test = stats.ttest_ind(group_b, group_a, equal_var=False, alternative="two-sided")
    mean_difference = float(group_b.mean() - group_a.mean())
    se = np.sqrt(group_b.var(ddof=1) / len(group_b) + group_a.var(ddof=1) / len(group_a))
    df_num = (group_b.var(ddof=1) / len(group_b) + group_a.var(ddof=1) / len(group_a)) ** 2
    df_den = (
        (group_b.var(ddof=1) / len(group_b)) ** 2 / (len(group_b) - 1)
        + (group_a.var(ddof=1) / len(group_a)) ** 2 / (len(group_a) - 1)
    )
    welch_df = df_num / df_den
    critical = stats.t.ppf(0.975, welch_df)
    ci_low = mean_difference - critical * se
    ci_high = mean_difference + critical * se

    pooled_sd = np.sqrt(
        ((len(group_b) - 1) * group_b.var(ddof=1)
         + (len(group_a) - 1) * group_a.var(ddof=1))
        / (len(group_b) + len(group_a) - 2)
    )
    cohens_d = mean_difference / pooled_sd if pooled_sd > 0 else float("nan")

    summary = clean.groupby("weather_group", observed=True)["cnt"].agg(
        n="count", mean="mean", std="std"
    ).reset_index()

    # Treat prespecified adjustment variables as categorical.
    model = smf.ols(
        "cnt ~ less_favorable_weather + C(hr) + C(season) + C(workingday) + C(yr)",
        data=clean,
    ).fit(cov_type="HC3")
    ci = model.conf_int().loc["less_favorable_weather"]

    results = {
        "n_total_eligible": int(len(clean)),
        "group_a_n": int(len(group_a)),
        "group_b_n": int(len(group_b)),
        "group_a_mean": float(group_a.mean()),
        "group_a_sd": float(group_a.std(ddof=1)),
        "group_b_mean": float(group_b.mean()),
        "group_b_sd": float(group_b.std(ddof=1)),
        "mean_difference_group_b_minus_group_a": mean_difference,
        "mean_difference_95ci": [float(ci_low), float(ci_high)],
        "welch_t_statistic": float(test.statistic),
        "welch_df": float(welch_df),
        "welch_p_value_two_sided": float(test.pvalue),
        "cohens_d_group_b_minus_group_a": float(cohens_d),
        "robustness_weather_coefficient": float(model.params["less_favorable_weather"]),
        "robustness_weather_coefficient_95ci": [float(ci.iloc[0]), float(ci.iloc[1])],
        "robustness_weather_p_value": float(model.pvalues["less_favorable_weather"]),
    }
    return {"clean_data": clean, "summary": summary, "results": results, "model": model}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True, help="Path to hour.csv")
    parser.add_argument("--output", required=True, help="Directory for reports")
    args = parser.parse_args()

    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)
    data = pd.read_csv(args.input)
    result = analyze(data)
    result["summary"].to_csv(output_dir / "group_summary.csv", index=False)
    with (output_dir / "primary_test.json").open("w", encoding="utf-8") as f:
        json.dump(result["results"], f, indent=2)
    (output_dir / "robustness_model.txt").write_text(
        result["model"].summary().as_text(), encoding="utf-8"
    )
    print(f"Analysis reports saved to: {output_dir.resolve()}")


if __name__ == "__main__":
    main()
