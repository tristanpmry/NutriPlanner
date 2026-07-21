interface Props {

result:any;

}


function NutritionResult({
result
}:Props){


return (

<div className="
mt-6
grid
gap-4
md:grid-cols-3
">


<div className="
rounded-xl
border
p-4
">

<p>
Glucides
</p>

<h2 className="text-2xl font-bold">

{result.carbs_per_hour} g/h

</h2>

</div>



<div className="
rounded-xl
border
p-4
">

<p>
Hydratation
</p>

<h2 className="text-2xl font-bold">

{result.water_per_hour} ml/h

</h2>

</div>



<div className="
rounded-xl
border
p-4
">

<p>
Sodium
</p>

<h2 className="text-2xl font-bold">

{result.sodium_per_hour} mg/h

</h2>

</div>



</div>

)

}


export default NutritionResult;