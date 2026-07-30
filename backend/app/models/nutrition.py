from dataclasses import dataclass


@dataclass
class NutritionRequirements:

    carbs_per_hour: int

    water_per_hour: int

    sodium_per_hour: int



@dataclass
class NutritionEvent:

    time: int

    type: str

    carbs: int

    quantity: int | None = None

    product: str | None = None



@dataclass
class NutritionPlan:

    events: list[NutritionEvent]



@dataclass
class NutritionResult:

    activity: object

    requirements: NutritionRequirements

    plan: NutritionPlan