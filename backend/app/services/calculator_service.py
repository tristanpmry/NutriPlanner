from app.core.constants import (
    HOT_TEMPERATURE,
    HOT_WATER_BONUS,
    HOT_SODIUM_BONUS,
    HIGH_INTENSITY_CARBS_BONUS,
)

from app.core.logger import logger

from app.models.nutrition import (
    NutritionRequirements
)


class CalculatorService:


    def calculate(
        self,
        activity,
        profile
    ) -> NutritionRequirements:


        logger.info(
            f"Calcul nutrition : {activity.sport}"
        )


        carbs = profile.carbs
        water = profile.water
        sodium = profile.sodium


        if activity.temperature >= HOT_TEMPERATURE:

            logger.info(
                "Adaptation chaleur"
            )

            water += HOT_WATER_BONUS

            sodium += HOT_SODIUM_BONUS



        if activity.intensity == "high":

            logger.info(
                "Adaptation intensité"
            )

            carbs += HIGH_INTENSITY_CARBS_BONUS



        return NutritionRequirements(

            carbs_per_hour=carbs,

            water_per_hour=water,

            sodium_per_hour=sodium

        )