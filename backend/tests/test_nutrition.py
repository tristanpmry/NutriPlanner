from app.activities.models import Activity
from app.nutrition.calculator import calculate_requirements

def test_hot_trail():

    activity = Activity(
        sport="trail",
        distance=44,
        elevation=2600,
        duration=10,
        temperature=30,
        weight=57,
    )

    result = calculate_requirements(activity)

    assert result["water_per_hour"] == 800

    assert result["sodium_per_hour"] == 800
