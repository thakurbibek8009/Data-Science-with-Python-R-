import pandas as pd
from src.analysis import preprocess, fit_primary

def test_preprocess_and_model():
    d = pd.DataFrame({
        "hr":[8,9,10,11,12,13,14,15],
        "workingday":[1]*8, "season":[1]*8, "yr":[0]*8,
        "weathersit":[1,2,3,4,1,2,3,4], "cnt":[10,20,5,3,12,21,6,4]
    })
    p = preprocess(d)
    assert len(p) == 8
    assert p["poor_weather"].sum() == 4
    model = fit_primary(p)
    assert "poor_weather" in model.params.index
