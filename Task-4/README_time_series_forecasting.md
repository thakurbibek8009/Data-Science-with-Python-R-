# Time-Series Forecasting with ARIMA

## Overview
This project builds an end-to-end daily demand forecasting workflow using the supplied `daily-demand-series.csv` file. The notebook explores the demand series, decomposes it into trend/seasonal/residual components, evaluates stationarity with the Augmented Dickey-Fuller (ADF) test, compares ARIMA orders, evaluates a chronological holdout, and generates a 30-day forecast.

## Dataset
The provided CSV contains 30 daily observations from June 1 to June 30, 2026, with columns:
- `date`: observation date
- `demand`: daily demand value
- `marketing_event`: indicator for a marketing event
- `holiday`: indicator for a holiday

Because the history is short, weekly decomposition and forecast results are exploratory. The primary ARIMA model uses demand only because future marketing-event and holiday values are not supplied.

## Notebook contents
- Historical demand and rolling-mean plots
- Additive decomposition with a 7-day seasonal period
- ADF stationarity test on original demand and first differences
- Chronological train/test split (last 7 days held out)
- ARIMA order selection by training-set AIC
- Baseline comparison using MAPE and RMSE
- Holdout forecast plot
- 30-day forecast with forecast intervals
- Limitations and reproducibility notes

## Requirements
Python 3.9+ is recommended. Install packages with:

```bash
pip install pandas numpy matplotlib seaborn statsmodels scikit-learn jupyter
```

## How to run
1. Place `time_series_forecasting_arima.ipynb` and `daily-demand-series.csv` in the same folder.
2. Open a terminal in that folder.
3. Run:

   ```bash
   jupyter notebook
   ```

4. Open the notebook and choose **Kernel → Restart Kernel and Run All Cells**.

You can also use Visual Studio Code with its Jupyter extension.

## Project structure

```text
.
├── README.md
├── daily-demand-series.csv
└── time_series_forecasting_arima.ipynb
```

## Limitations
- Thirty observations are not enough to estimate stable long-term or annual seasonality.
- The 7-day test split leaves 23 observations for model training, so ARIMA selection may be unstable.
- Forecasts are projections, not guarantees. Compare ARIMA metrics with the baseline before claiming improvement.
- MAPE and RMSE measure different aspects of forecast error.
- Future marketing and holiday indicators are unknown, so they are not used as future regressors in the primary forecast.

## Submission
Upload the notebook to a public GitHub repository (include the CSV and this README if allowed by the assignment), then copy the public notebook URL as the single submission link. Confirm that the URL opens without signing in.

## Author
Add your name, course, institution, and submission date if required.
