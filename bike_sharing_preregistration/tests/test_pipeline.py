"""Synthetic-only checks for the preregistered pipeline."""
import pandas as pd
import pytest

from src.pipeline import prepare_data, analyze


@pytest.fixture
def synthetic_data():
    # Fake fixture created only to test code behavior; not real observations.
    return pd.DataFrame({
        "instant": [1, 2, 3, 4, 5, 6, 7, 8],
        "weathersit": [1, 1, 1, 1, 2, 2, 3, 4],
        "cnt": [100, 110, 120, 130, 60, 70, 50, 40],
        "hr": [8, 9, 10, 11, 8, 9, 10, 11],
        "season": [1, 1, 1, 1, 1, 1, 1, 1],
        "workingday": [1, 1, 1, 1, 1, 1, 1, 1],
        "yr": [0, 0, 0, 0, 0, 0, 0, 0],
    })


def test_prepare_data_creates_weather_groups(synthetic_data):
    clean = prepare_data(synthetic_data)
    assert len(clean) == 8
    assert clean["less_favorable_weather"].tolist() == [0, 0, 0, 0, 1, 1, 1, 1]
    assert set(clean["weather_group"]) == {
        "Clear/partly cloudy (1)", "Less favorable (2-4)"
    }


def test_prepare_data_drops_missing_outcome(synthetic_data):
    synthetic_data.loc[0, "cnt"] = None
    clean = prepare_data(synthetic_data)
    assert len(clean) == 7


def test_prepare_data_rejects_invalid_weather_code(synthetic_data):
    synthetic_data.loc[0, "weathersit"] = 9
    clean = prepare_data(synthetic_data)
    assert len(clean) == 7


def test_analyze_returns_expected_contract(synthetic_data):
    result = analyze(synthetic_data)
    expected = {
        "n_total_eligible", "group_a_n", "group_b_n",
        "mean_difference_group_b_minus_group_a",
        "mean_difference_95ci", "welch_p_value_two_sided",
        "cohens_d_group_b_minus_group_a",
        "robustness_weather_coefficient",
    }
    assert expected.issubset(result["results"].keys())
    assert result["results"]["group_a_n"] == 4
    assert result["results"]["group_b_n"] == 4


def test_missing_required_column_raises_error(synthetic_data):
    with pytest.raises(ValueError, match="Missing required columns"):
        prepare_data(synthetic_data.drop(columns=["cnt"]))
