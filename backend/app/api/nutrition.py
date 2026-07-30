from fastapi import APIRouter


from app.models.activity import Activity


from app.schemas.nutrition import (
    NutritionRequest,
    NutritionResponse
)


from app.services.nutrition_service import (
    NutritionService
)



router = APIRouter()


nutrition_service = NutritionService()



@router.post(
    "/calculate",
    response_model=NutritionResponse
)
def calculate_nutrition(
    request: NutritionRequest
):


    activity = Activity(

        sport=request.sport,

        distance=request.distance,

        elevation=request.elevation,

        duration=request.duration,

        temperature=request.temperature,

        weight=request.weight,

        intensity=request.intensity

    )


    result = (
        nutrition_service.generate_plan(
            activity
        )
    )


    return {


        "activity": {

            "sport": result.activity.sport,

            "distance": result.activity.distance,

            "duration": result.activity.duration

        },


        "requirements": result.requirements,


        "plan": result.plan.events

    }