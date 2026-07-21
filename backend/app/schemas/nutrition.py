from pydantic import BaseModel


class NutritionRequest(BaseModel):

    sport: str

    distance: float

    elevation: float

    duration: float

    temperature: float

    weight: float

    intensity: str = "moderate"