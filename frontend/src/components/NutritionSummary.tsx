import Card from "./Card";

import type {
    NutritionRequirements
} from "../types/nutrition";


interface Props {

    requirements: NutritionRequirements;

}


export default function NutritionSummary(
    { requirements }: Props
) {


    return (

        <Card title="Besoins nutritionnels">


            <p>
                🍞 Glucides :
                {" "}
                {requirements.carbs_per_hour}
                g/h
            </p>


            <p>
                💧 Eau :
                {" "}
                {requirements.water_per_hour}
                ml/h
            </p>


            <p>
                🧂 Sodium :
                {" "}
                {requirements.sodium_per_hour}
                mg/h
            </p>


        </Card>

    );

}