import { useEffect, useState } from "react";
import api from "./api/axios";


function App() {

  const [message, setMessage] = useState("");


  useEffect(() => {

    api.get("/test")
      .then(response => {
        setMessage(response.data.message);
      })
      .catch(error => {
        console.error(error);
        setMessage("Erreur backend");
      });

  }, []);


  return (
    <div>
      <h1>
        NutriPlanner
      </h1>

      <p>
        {message}
      </p>
    </div>
  );
}


export default App;