import {useState} from "react";
import api from "../api/axios";

import InputField from "../components/InputField";
import NutritionResult from "../components/NutritionResult";


function CreatePlan(){


const [result,setResult]=useState<any>(null);


const [form,setForm]=useState({

sport:"trail",

distance:44,

elevation:2600,

duration:10,

temperature:30,

weight:57,

intensity:"moderate"

});



function update(
field:string,
value:any
){

setForm({

...form,

[field]:value

})

}



async function generate(){


const response =
await api.post(
"/nutrition/calculate",
form
);


setResult(response.data);


}



return (

<div className="
max-w-3xl
mx-auto
p-8
">


<h1 className="
text-3xl
font-bold
mb-8
">

NutriPlanner

</h1>



<div className="
grid
gap-4
md:grid-cols-2
">


<select

className="
border
rounded-lg
p-2
"

value={form.sport}

onChange={
e=>update(
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

<InputField

label="Distance (km)"

value={form.distance}

onChange={
v=>update("distance",v)
}

/>


<InputField

label="D+ (m)"

value={form.elevation}

onChange={
v=>update("elevation",v)
}

/>



<InputField

label="Durée (h)"

value={form.duration}

onChange={
v=>update("duration",v)
}

/>



<InputField

label="Température °C"

value={form.temperature}

onChange={
v=>update("temperature",v)
}

/>



<InputField

label="Poids kg"

value={form.weight}

onChange={
v=>update("weight",v)
}

/>


</div>



<button

className="
mt-8
bg-black
text-white
px-6
py-3
rounded-xl
"

onClick={generate}

>

Générer mon plan

</button>



{
result &&
<NutritionResult result={result}/>
}



</div>

)


}


export default CreatePlan;