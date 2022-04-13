from fastapi.testclient import TestClient
from app import app


client = TestClient(app)


def test_root():
    response = client.get("/")
    assert response.status_code == 200

def test_predict_quality():
    response = client.get("/winequality")
    assert response.status_code == 200