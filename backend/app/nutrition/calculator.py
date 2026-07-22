from app.nutrition.profiles import SPORT_PROFILES


def calculate_requirements(activity):

    profile = SPORT_PROFILES[activity.sport]

    carbs = profile["carbs"]

    water = profile["water"]

    sodium = profile["sodium"]

    if activity.temperature >= 25:

        water += 200

        sodium += 200

    if activity.intensity == "high":

        carbs += 10

    return {"carbs_per_hour": carbs, "water_per_hour": water, "sodium_per_hour": sodium}
