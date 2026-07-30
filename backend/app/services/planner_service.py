from app.core.constants import (
    DEFAULT_PLANNING_INTERVAL
)

from app.core.logger import logger

from app.models.nutrition import (
    NutritionEvent,
    NutritionPlan
)



class PlannerService:


    def generate(
        self,
        activity,
        requirements
    ) -> NutritionPlan:


        logger.info(
            "Génération du plan nutrition"
        )


        events = []


        current_time = DEFAULT_PLANNING_INTERVAL


        # Nombre de prises nécessaires
        # en fonction de la durée
        while current_time < activity.duration * 60:


            events.append(

                NutritionEvent(

                    time=current_time,

                    type="gel",

                    product="Gel énergétique",

                    quantity=1,

                    carbs=25

                )

            )


            current_time += DEFAULT_PLANNING_INTERVAL



        logger.info(
            f"{len(events)} événements générés"
        )


        return NutritionPlan(

            events=events

        )