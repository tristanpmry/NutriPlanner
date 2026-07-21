import {
  BrowserRouter,
  Routes,
  Route
} from "react-router-dom";

import CreatePlan from "./pages/CreatePlan";


function App() {


  return (

    <BrowserRouter>

      <Routes>

        <Route
          path="/"
          element={<CreatePlan />}
        />

      </Routes>


    </BrowserRouter>

  );

}


export default App;