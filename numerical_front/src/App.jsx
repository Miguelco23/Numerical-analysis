import './App.css';
import HomePage from './HomePage';

function App() {

  const fetchData = async () => {
    try {
      const response = await fetch('http://localhost:8000/api/endpoint'); // Reemplaza la URL con la URL de tu API de FastAPI
      const data = await response.json();
      console.log(data); // Haz algo con los datos de respuesta
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div className="App">
      <HomePage />
    </div>
  );
}

export default App;
