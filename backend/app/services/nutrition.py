from app.services.profiles import SPORT_PROFILES



def calculate_nutrition(
    sport,
    duration,
    temperature,
    weight,
    intensity="moderate"
):


    profile = SPORT_PROFILES.get(
        sport,
        SPORT_PROFILES["trail"]
    )


    carbs = profile["carbs_base"]

    water = profile["water_base"]

    sodium = profile["sodium_base"]



    # Adaptation chaleur

    if temperature >= 25:

        water += 200

        sodium += 200



    # Adaptation intensité

    if intensity == "high":

        carbs += 10

        water += 100



    return {


        "sport": sport,


        "carbs_per_hour": carbs,


        "water_per_hour": water,


        "sodium_per_hour": sodium,


        "total_carbs": round(
            carbs * duration
        ),


        "total_water": round(
            water * duration
        ),


        "total_sodium": round(
            sodium * duration
        )

    }