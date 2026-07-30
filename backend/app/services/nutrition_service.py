from app.services.calculator_service import (
    CalculatorService
)

from app.services.planner_service import (
    PlannerService
)

from app.repositories.sport_profile_repository import (
    SportProfileRepository
)

from app.models.nutrition import (
    NutritionResult
)

from app.core.logger import logger



class NutritionService:


    def __init__(self):

        self.repository = (
            SportProfileRepository()
        )

        self.calculator = (
            CalculatorService()
        )

        self.planner = (
            PlannerService()
        )



    def generate_plan(
        self,
        activity
    ) -> NutritionResult:


        logger.info(
            "Début génération plan"
        )


        profile = (
            self.repository.get_profile(
                activity.sport
            )
        )


        requirements = (
            self.calculator.calculate(
                activity,
                profile
            )
        )


        plan = (
            self.planner.generate(
                activity,
                requirements
            )
        )


        return NutritionResult(

            activity=activity,

            requirements=requirements,

            plan=plan

        )