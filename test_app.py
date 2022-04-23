from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_quality():
    response = client.get("/winequality?free_sulfur_dioxide=3.3&fixed_acidity=3.3&alcohol=3.3&density=3.3&sulphates=3.3&residual_sugar=3.3&citric_acid=3.3&total_sulfur_dioxide=3.3&pH=3.3&chlorides=3.3&volatile_acidity=3.3")
    assert response.status_code == 200