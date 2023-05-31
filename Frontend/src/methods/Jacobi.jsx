import React, { useState } from "react";

const Jacobi = () => {
    const [matrixData, setMatrixData] = useState([]);
    const [zData, setZData] = useState([]);
    const [x0, setX0] = useState([]);
    const [tolerance, setTolerance] = useState("");
    const [nMax, setNMax] = useState("");
    const [result, setResult] = useState(null);

    const handleMatrixSizeChange = (event) => {
        let size = parseInt(event.target.value);
        if (event.target.value === "") {
            size = 0;
        }
        setMatrixData(Array.from({ length: size }, () => Array(size).fill(0)));
        setZData(Array(size).fill(0));
        setX0(Array(size).fill(0));
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

    const handleX0InputChange = (event, index) => {
        const { value } = event.target;
        setX0((prevX0) => {
            const updatedX0 = [...prevX0];
            updatedX0[index] = parseFloat(value);
            return updatedX0;
        });
    };

    const handleSubmit = async () => {
        const data = {
            A: matrixData,
            b: zData,
            x0: x0,
            tol: parseFloat(tolerance),
            nmax: parseFloat(nMax)
        };

        console.log(data);

        try { 
            const response = await fetch('http://127.0.0.1:8000/api/Jacobi', {
              method: 'POST',
              headers: {
                'Content-Type': 'application/json',
              },
              body: JSON.stringify(data),
            });
          
            if (!response.ok) {
              throw new Error('Error al realizar la petición');
            }
          
            const resultData = await response.json();
            setResult(`X: ${resultData.Result.x} - Iterations: ${resultData.Result.iterations} - Error: ${resultData.Result.Error}`);
          } catch (error) {
            console.error('Error:', error);
            alert('Error:', error);
          }

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

    const renderX0Inputs = () => {
        return x0.map((value, index) => (
            <input
                style={{ width: "30px" }}
                key={index}
                type="number"
                onChange={(e) => handleX0InputChange(e, index)}
            />
        ));
    };

    return (
        <div>
            <h2>Jacobi</h2>
            <div>
                <label>Matrix order:</label>
                <input type="number" min="1" onChange={handleMatrixSizeChange} />
            </div>
            <div>
                <label>Matrix:</label>
                {renderMatrixInputs()}
            </div>
            <div>
                <label>b:</label>
                {renderZInputs()}
            </div>
            <div>
                <label>X0:</label>
                {renderX0Inputs()}
            </div>
            <label>
                Tolerance:
                <input type="number" value={tolerance} onChange={(e) => setTolerance(e.target.value)} />
            </label>
            <br />
            <label>
                NMax:
                <input type="number" value={nMax} onChange={(e) => setNMax(e.target.value)} />
            </label>
            <br />
            <button onClick={handleSubmit}>Calculate</button>
            {result && (
                <div>
                    <h3>Result:</h3>
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
};

export default Jacobi;