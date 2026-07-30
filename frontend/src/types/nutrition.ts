export type Sport =
    | "trail"
    | "cycling"
    | "hiking"
    | "mtb";


export type Intensity =
    | "low"
    | "moderate"
    | "high";

export interface NutritionRequest {

    sport: Sport;

    distance: number;

    elevation: number;

    duration: number;

    temperature: number;

    weight: number;

    intensity: Intensity;

}


export interface NutritionRequirements {

    carbs_per_hour: number;

    water_per_hour: number;

    sodium_per_hour: number;

}


export interface NutritionEvent {

    time:number;

    type:string;

    carbs:number;

}


export interface NutritionResponse {

    activity: {

        sport: string;

        distance: number;

        duration: number;

    };


    requirements: NutritionRequirements;


    plan: NutritionEvent[];

}