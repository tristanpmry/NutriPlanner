import type {
    NutritionRequest,
    NutritionResponse
} from "../types/nutrition";


const API_URL = "http://localhost:8000";


export async function calculateNutrition(
    data: NutritionRequest
): Promise<NutritionResponse> {


    const response = await fetch(

        `${API_URL}/nutrition/calculate`,

        {

            method: "POST",

            headers: {

                "Content-Type": "application/json",

            },

            body: JSON.stringify(data),

        }

    );


    if (!response.ok) {

        throw new Error(
            "Erreur calcul nutrition"
        );

    }


    return response.json();

}