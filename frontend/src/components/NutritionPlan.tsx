import Card from "./Card";

import type {
    NutritionEvent
} from "../types/nutrition";


interface Props {

    events: NutritionEvent[];

}



function formatTime(minutes: number) {

    const hours = Math.floor(minutes / 60);

    const mins = minutes % 60;


    return `${hours}h${mins
        .toString()
        .padStart(2, "0")}`;

}



export default function NutritionPlan(
    { events }: Props
) {


    return (

        <Card title="Plan nutrition">


            {
                events.length === 0 &&

                <p>
                    Aucun apport planifié
                </p>

            }



            {
                events.map(
                    (event, index) => (

                        <div key={index}>


                            <p>

                                ⏱️ {formatTime(event.time)}

                            </p>


                            <p>

                                Type :
                                {" "}
                                {event.type}

                            </p>


                            <p>

                                Glucides :
                                {" "}
                                {event.carbs} g

                            </p>


                        </div>

                    )
                )
            }


        </Card>

    );

}