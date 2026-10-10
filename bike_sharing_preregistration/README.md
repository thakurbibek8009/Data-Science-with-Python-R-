# Weather and Bike-Sharing Demand: Preregistered Analysis

This project investigates whether hourly bike rentals differ between clear/partly cloudy weather (`weathersit == 1`) and less favorable weather (`weathersit` in 2–4).

## Important research rule

The analysis plan is written in `preregistration/preregistration.md` before examining outcome relationships. If the plan changes, document the change in the preregistration's **Deviations** table.

This is an observational analysis. Results show association, not proof of causation.

## Repository structure

```text
bike_sharing_preregistration/
├── data/
│   ├── raw/hour.csv
│   ├── interim/
│   └── processed/
├── notebooks/
├── preregistration/preregistration.md
├── reports/
├── src/
│   └── pipeline.py
├── tests/
│   └── test_pipeline.py
├── requirements.txt
└── README.md
```

## Setup

Use Python 3.10 or newer.

```bash
python -m venv .venv
```

Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run the synthetic pipeline tests

```bash
python -m pytest -q
```

The tests use small synthetic data, not the real dataset's outcome patterns.

## Run the analysis

Only after the preregistration is saved and reviewed:

```bash
python -m src.pipeline --input data/raw/hour.csv --output reports
```

The script writes summary outputs to `reports/`. Do not edit the raw file. Keep `data/raw/hour.csv` unchanged.

## Expected outputs

- `reports/group_summary.csv`
- `reports/primary_test.json`
- `reports/robustness_model.txt`

## Interpretation limits

The records are observational and hourly observations may be temporally related. Weather categories 2–4 are grouped because some categories may have few observations. The analysis should not be interpreted as demonstrating causation.
