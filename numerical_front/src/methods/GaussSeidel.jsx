import React, { useState } from "react";

const GaussSeidel = () => {
    const [matrixData, setMatrixData] = useState([]);
    const [zData, setZData] = useState([]);
    const [x0, setX0] = useState("");
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
            x0: parseFloat(x0),
            tolerance: parseFloat(tolerance),
            nMax: parseFloat(nMax)
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
            <h2>Gauss-Seidel</h2>
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
            <br />
            <label>
                X0:
                <input type="number" value={x0} onChange={(e) => setX0(e.target.value)} />
            </label>
            <br />
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

export default GaussSeidel;