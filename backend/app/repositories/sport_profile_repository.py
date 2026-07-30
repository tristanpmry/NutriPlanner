from app.models.sport_profile import SportProfile


SPORT_PROFILES = {

    "trail": SportProfile(

        carbs=70,

        water=600,

        sodium=600

    ),


    "cycling": SportProfile(

        carbs=80,

        water=700,

        sodium=500

    ),


    "hiking": SportProfile(

        carbs=50,

        water=500,

        sodium=500

    ),


    "mtb": SportProfile(

        carbs=70,

        water=600,

        sodium=600

    )

}



class SportProfileRepository:


    def get_profile(
        self,
        sport: str
    ) -> SportProfile:


        if sport not in SPORT_PROFILES:

            raise ValueError(
                f"Sport inconnu : {sport}"
            )


        return SPORT_PROFILES[sport]