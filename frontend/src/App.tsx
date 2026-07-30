import { useState } from "react";

import ActivityForm from "./components/ActivityForm";

import NutritionSummary from "./components/NutritionSummary";

import NutritionPlan from "./components/NutritionPlan";

import type {
    NutritionRequest,
} from "./types/nutrition";


import {
    calculateNutrition
} from "./api/nutrition";


import type {
    NutritionResponse
} from "./types/nutrition";



function App() {


    const [
        result,
        setResult
    ] = useState<NutritionResponse | null>(null);

    const [loading, setLoading] =
    useState(false);

    async function generate(
    data: NutritionRequest
) {

    setLoading(true);

    try {

        const response =
            await calculateNutrition(data);

        setResult(response);

    }
    catch(error){

        console.error(error);

    }
    finally {

        setLoading(false);

    }

}

    return (

<div>

    <h1>
        NutriPlanner
    </h1>


    <ActivityForm
        onGenerate={generate}
        loading={loading}
    />


    {
        result &&

        <>

            <NutritionSummary
                requirements={
                    result.requirements
                }
            />


            <NutritionPlan
                events={
                    result.plan
                }
            />

        </>

    }


</div>

);
}
export default App;