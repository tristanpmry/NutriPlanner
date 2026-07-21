interface Props {

    label:string;

    value:number;

    onChange:(value:number)=>void;

}



function InputField({
    label,
    value,
    onChange
}:Props){


return (

<div className="flex flex-col gap-2">


<label className="font-medium">

{label}

</label>


<input

className="
border
rounded-lg
p-2
focus:outline-none
focus:ring-2
"

type="number"

value={value}

onChange={
e => onChange(
Number(e.target.value)
)
}

/>


</div>

)


}


export default InputField;