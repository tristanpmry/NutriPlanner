from fastapi import APIRouter

from app.schemas.nutrition import NutritionRequest
from app.services.nutrition import calculate_nutrition


router = APIRouter()


@router.post("/calculate")
def calculate(
    data: NutritionRequest
):

    result = calculate_nutrition(
        duration=data.duration,
        temperature=data.temperature,
        weight=data.weight,
        intensity=data.intensity
    )

    return result