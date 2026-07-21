def calculate_nutrition(
    duration,
    temperature,
    weight,
    intensity="moderate"
):

    # Glucides
    if duration < 1.5:
        carbs = 30

    elif duration < 3:
        carbs = 50

    else:
        carbs = 70


    # Hydratation
    water = 500

    if temperature >= 25:
        water += 200


    if intensity == "high":
        water += 100


    # Sodium
    sodium = 500

    if temperature >= 25:
        sodium += 200


    return {

        "carbs_per_hour": carbs,

        "water_per_hour": water,

        "sodium_per_hour": sodium,

        "total_carbs": carbs * duration,

        "total_water": water * duration,

        "total_sodium": sodium * duration

    }