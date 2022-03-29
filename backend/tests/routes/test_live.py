from fastapi.testclient import TestClient
from src.main import app


def test_live():
    client = TestClient(app)

    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Hello World"}
