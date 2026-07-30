from pydantic import BaseModel



class NutritionRequest(BaseModel):

    sport: str

    distance: float

    elevation: float

    duration: float

    temperature: float

    weight: float

    intensity: str




class NutritionRequirementsResponse(BaseModel):

    carbs_per_hour: int

    water_per_hour: int

    sodium_per_hour: int




class NutritionEventResponse(BaseModel):

    time: int

    type: str

    carbs: int




class NutritionResponse(BaseModel):

    activity: dict

    requirements: NutritionRequirementsResponse

    plan: list[NutritionEventResponse]