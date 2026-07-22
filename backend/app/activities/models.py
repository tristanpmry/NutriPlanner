from dataclasses import dataclass


@dataclass
class Activity:

    sport: str

    distance: float

    elevation: float

    duration: float

    temperature: float

    weight: float

    intensity: str = "moderate"
