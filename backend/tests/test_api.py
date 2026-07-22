from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_nutrition_endpoint():

    response = client.post(
        "/nutrition/calculate",
        json={
            "sport": "trail",
            "distance": 44,
            "elevation": 2600,
            "duration": 10,
            "temperature": 30,
            "weight": 57,
            "intensity": "moderate",
        },
    )

    assert response.status_code == 200

    data = response.json()

    assert data["requirements"]["water_per_hour"] == 800
