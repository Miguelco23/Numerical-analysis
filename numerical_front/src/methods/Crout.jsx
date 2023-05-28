import React, { useState } from "react";

const Crout = () => {
    const [matrix, setMatrix] = useState([[], [], []]);
    const [z, setZ] = useState([]);
    const [result, setResult] = useState(null);
  
    const handleMatrixChange = (rowIndex, columnIndex, value) => {
      const updatedMatrix = [...matrix];
      updatedMatrix[rowIndex][columnIndex] = value;
      setMatrix(updatedMatrix);
    };
  
    const handleZChange = (index, value) => {
      const updatedZ = [...z];
      updatedZ[index] = value;
      setZ(updatedZ);
    };
  
    const handleSubmit = async (e) => {
      e.preventDefault();
      const requestData = {
        matrix,
        z,
      };
  
      try {
        const response = await fetch('API_URL', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(requestData),
        });
  
        if (response.ok) {
          const result = await response.json();
          setResult(result);
        } else {
          console.log('Error:', response.status);
        }
      } catch (error) {
        console.log('Error:', error);
        alert('Error:', error);
      }
    };
  
    return (
      <div>
        <h2>Crout</h2>
        <form onSubmit={handleSubmit}>
          <div>
            <label>Matriz:</label>
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[0][0]}
              onChange={(e) => handleMatrixChange(0, 0, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[0][1]}
              onChange={(e) => handleMatrixChange(0, 1, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[0][2]}
              onChange={(e) => handleMatrixChange(0, 2, e.target.value)}
            />
          </div>
          <div style={{marginLeft: "50px"}}>
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[1][0]}
              onChange={(e) => handleMatrixChange(1, 0, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[1][1]}
              onChange={(e) => handleMatrixChange(1, 1, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[1][2]}
              onChange={(e) => handleMatrixChange(1, 2, e.target.value)}
            />
          </div>
          <div style={{marginLeft: "50px"}}>
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[2][0]}
              onChange={(e) => handleMatrixChange(2, 0, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[2][1]}
              onChange={(e) => handleMatrixChange(2, 1, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={matrix[2][2]}
              onChange={(e) => handleMatrixChange(2, 2, e.target.value)}
            />
          </div>
          <div>
            <label>Z:</label>
            <input
              type="number"
              style={{width: "40px"}}
              value={z[0]}
              onChange={(e) => handleZChange(0, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={z[1]}
              onChange={(e) => handleZChange(1, e.target.value)}
            />
            <input
              type="number"
              style={{width: "40px"}}
              value={z[2]}
              onChange={(e) => handleZChange(2, e.target.value)}
            />
          </div>
          <button type="submit">Calcular</button>
        </form>
        {result && (
          <div>
            <h3>Resultado</h3>
            <p>{result}</p>
          </div>
        )}
      </div>
    );
};

export default Crout;
