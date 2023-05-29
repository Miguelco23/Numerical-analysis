import React, { useState } from "react";

const Cholesky = () => {
  const [matrixSize, setMatrixSize] = useState(0);
  const [matrixData, setMatrixData] = useState([]);
  const [zData, setZData] = useState([]);
  const [result, setResult] = useState(null);

  const handleMatrixSizeChange = (event) => {
    let size = parseInt(event.target.value);
    if (event.target.value === "") {
      size = 0;
    }
    setMatrixSize(size);
    setMatrixData(Array.from({ length: size }, () => Array(size).fill(0)));
    setZData(Array(size).fill(0));
    setResult(null);
  };

  const handleMatrixInputChange = (event, rowIndex, colIndex) => {
    const { value } = event.target;
    setMatrixData((prevMatrix) => {
      const updatedMatrix = [...prevMatrix];
      updatedMatrix[rowIndex][colIndex] = parseFloat(value);
      return updatedMatrix;
    });
  };

  const handleZInputChange = (event, index) => {
    const { value } = event.target;
    setZData((prevZ) => {
      const updatedZ = [...prevZ];
      updatedZ[index] = parseFloat(value);
      return updatedZ;
    });
  };

  const handleSubmit = async () => {
    const data = {
      matrix: matrixData,
      z: zData,
    };

    console.log(data);
  };

  const renderMatrixInputs = () => {
    return matrixData.map((row, rowIndex) => (
      <div key={rowIndex}>
        {row.map((cell, colIndex) => (
          <input
            style={{ width: "30px" }}
            key={colIndex}
            type="number"
            onChange={(e) => handleMatrixInputChange(e, rowIndex, colIndex)}
          />
        ))}
      </div>
    ));
  };

  const renderZInputs = () => {
    return zData.map((value, index) => (
      <input
        style={{ width: "30px" }}
        key={index}
        type="number"
        onChange={(e) => handleZInputChange(e, index)}
      />
    ));
  };

  return (
    <div>
      <h2>Método de Cholesky</h2>
      <div>
        <label>Orden de la matriz:</label>
        <input type="number" min="1" onChange={handleMatrixSizeChange} />
      </div>
      <div>
        <label>Matriz:</label>
        {renderMatrixInputs()}
      </div>
      <div>
        <label>Vector Z:</label>
        {renderZInputs()}
      </div>
      <button onClick={handleSubmit}>Calcular</button>
      {result && (
        <div>
          <h3>Resultado:</h3>
          <p>{result}</p>
        </div>
      )}
    </div>
  );
};

export default Cholesky;
