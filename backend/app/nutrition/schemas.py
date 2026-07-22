from pydantic import BaseModel, Field


class NutritionRequest(BaseModel):

    sport: str

    distance: float = Field(gt=0)

    elevation: float = Field(ge=0)

    duration: float = Field(gt=0)

    temperature: float

    weight: float = Field(gt=0)

    intensity: str = "moderate"