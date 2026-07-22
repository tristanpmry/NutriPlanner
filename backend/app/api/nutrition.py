from fastapi import APIRouter

from app.activities.models import Activity
from app.nutrition.calculator import calculate_requirements
from app.nutrition.planner import generate_plan
from app.nutrition.schemas import NutritionRequest

router = APIRouter()


@router.post("/calculate")
def calculate_nutrition(data: NutritionRequest):

    activity = Activity(
        sport=data.sport,
        distance=data.distance,
        elevation=data.elevation,
        duration=data.duration,
        temperature=data.temperature,
        weight=data.weight,
        intensity=data.intensity,
    )

    requirements = calculate_requirements(activity)

    plan = generate_plan(activity.duration, requirements["carbs_per_hour"])

    return {
        "activity": {
            "sport": activity.sport,
            "distance": activity.distance,
            "duration": activity.duration,
        },
        "requirements": requirements,
        "plan": plan,
    }
