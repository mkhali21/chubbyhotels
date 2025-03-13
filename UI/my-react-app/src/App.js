import React, { useEffect, useState } from "react";
import "./App.css";

function App() {
  const [data, setData] = useState([]); // State to store data

  // Fetch data from API when the component mounts
  useEffect(() => {
    fetch("http://3.133.125.38:8080/properties/") // Example API
      .then((response) => response.json())
      .then((data) => setData(data)); // Store fetched data in state
  }, []);

  return (
    <div className="App">
      <h1>API Data</h1>
      <ul>
        {data.map((item) => (
          <li key={item.PropertyID}>
            <strong>{item.Name}</strong>
            <br />
            <strong>{item.Country}</strong>
            <br />
            <strong>{item.City}</strong>
            <br /> <br /> <br /> <br />
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
