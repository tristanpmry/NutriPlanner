import { useState } from "react";

import type {
    NutritionRequest
} from "../types/nutrition";


interface Props {

    onGenerate: (
        data: NutritionRequest
    ) => void;

        loading:boolean;


}

export default function ActivityForm(
    { onGenerate, loading }: Props
) {


    const [form, setForm] = useState<NutritionRequest>({
    sport: "trail",
    distance: 44,
    elevation: 2600,
    duration: 10,
    temperature: 30,
    weight: 57,
    intensity: "moderate"
});



    function update(
        key: string,
        value: string | number
    ) {

        setForm({

            ...form,

            [key]: value

        });

    }



    function submit(
        e: React.FormEvent
    ) {

        e.preventDefault();

        onGenerate(form);

    }



    return (

        <form onSubmit={submit}>

            <h2>
                Nouvelle activité
            </h2>


    <select
    value={form.sport}
    onChange={
        e => update(
            "sport",
            e.target.value
        )
    }
    >

    <option value="trail">
        Trail
    </option>

    <option value="cycling">
        Vélo
    </option>

    <option value="hiking">
        Randonnée
    </option>

    <option value="mtb">
        VTT
    </option>

    </select>





            <input
                min="0"
                step="0.1"
                value={form.distance}
                type="number"
                placeholder="Distance km"
                onChange={
                    e => update(
                        "distance",
                        Number(e.target.value)
                    )
                }
            />


            <input
                min="0"
                step="0.1"
                value={form.elevation}
                type="number"
                placeholder="D+"
                onChange={
                    e => update(
                        "elevation",
                        Number(e.target.value)
                    )
                }
            />


            <input
                min="0.1"
                step="0.1"
                value={form.duration}
                type="number"
                placeholder="Durée h"
                onChange={
                    e => update(
                        "duration",
                        Number(e.target.value)
                    )
                }
            />


            <input
                value={form.temperature}
                type="number"
                placeholder="Température"
                onChange={
                    e => update(
                        "temperature",
                        Number(e.target.value)
                    )
                }
            />

            
            <select
    value={form.intensity}
    onChange={
        e => update(
            "intensity",
            e.target.value
        )
    }
>

    <option value="low">
        Faible
    </option>

    <option value="moderate">
        Modérée
    </option>

    <option value="high">
        Élevée
    </option>

</select>



            <input
                min="20"
                value={form.weight}
                type="number"
                placeholder="Poids"
                onChange={
                    e => update(
                        "weight",
                        Number(e.target.value)
                    )
                }
            />


           <button type="submit"
           disabled={loading}>

            {
                loading
                ? "Calcul..."
                : "Générer"
            }

</button>


        </form>

    );

}