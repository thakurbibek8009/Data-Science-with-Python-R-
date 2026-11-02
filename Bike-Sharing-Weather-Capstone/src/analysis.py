"""Reproducible preregistered weather-demand analysis."""
from pathlib import Path
import argparse
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

REQUIRED = ["hr", "workingday", "season", "yr", "weathersit", "cnt"]

def preprocess(frame: pd.DataFrame) -> pd.DataFrame:
    missing = [c for c in REQUIRED if c not in frame.columns]
    if missing:
        raise ValueError(f"Missing required columns: {missing}")
    out = frame.drop_duplicates().copy()
    out = out[out["weathersit"].isin([1,2,3,4]) & (out["cnt"] >= 0)]
    out = out.dropna(subset=REQUIRED).copy()
    out["poor_weather"] = (out["weathersit"] >= 3).astype(int)
    out["log_cnt"] = np.log1p(out["cnt"])
    return out

def fit_primary(data):
    formula = "log_cnt ~ poor_weather + C(hr) + C(workingday) + C(season) + C(yr)"
    return smf.ols(formula, data=data).fit(cov_type="HC3")

def run(data_path, output_dir):
    raw = pd.read_csv(data_path)
    data = preprocess(raw)
    output_dir = Path(output_dir); output_dir.mkdir(parents=True, exist_ok=True)
    data.to_csv(output_dir/"analysis_data.csv", index=False)
    model = fit_primary(data)
    (output_dir/"primary_model_summary.txt").write_text(model.summary().as_text())
    result = {"n":len(data), "coefficient":model.params["poor_weather"],
              "ci_low":model.conf_int().loc["poor_weather",0],
              "ci_high":model.conf_int().loc["poor_weather",1],
              "p_value_two_sided":model.pvalues["poor_weather"],
              "adjusted_ratio_exp_beta":np.exp(model.params["poor_weather"]),
              "r_squared":model.rsquared}
    pd.Series(result).to_csv(output_dir/"primary_results.csv", header=["value"])
    print(pd.Series(result).to_string())

if __name__ == "__main__":
    parser=argparse.ArgumentParser()
    parser.add_argument("--data", default="data/raw/hour.csv")
    parser.add_argument("--output", default="reports/generated")
    args=parser.parse_args()
    run(args.data,args.output)
