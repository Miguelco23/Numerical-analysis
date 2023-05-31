import React, { useState } from "react";

const Vandermonde = () => {
    const [xData, setXData] = useState([]);
    const [yData, setYData] = useState([]);
    const [result, setResult] = useState(null);

    const handleMatrixSizeChange = (event) => {
        let size = parseInt(event.target.value);
        if (event.target.value === "") {
            size = 0;
        }
        setXData(Array(size).fill(0));
        setYData(Array(size).fill(0));
        setResult(null);
    };

    const handleXInputChange = (event, index) => {
        const { value } = event.target;
        setXData((prevX) => {
            const updatedX = [...prevX];
            updatedX[index] = parseFloat(value);
            return updatedX;
        });
    };

    const handleYInputChange = (event, index) => {
        const { value } = event.target;
        setYData((prevY) => {
            const updatedY = [...prevY];
            updatedY[index] = parseFloat(value);
            return updatedY;
        });
    };

    const handleSubmit = async () => {
        const data = {
            x: xData,
            y: yData,
            degree: xData.length -1
        };

        console.log(JSON.stringify(data));

        try { 
            const response = await fetch('http://127.0.0.1:8000/api/vandermonde', {
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
            setResult(resultData.Result);
          } catch (error) {
            console.error('Error:', error);
            alert('Error:', error);
          }
          
    };

    const renderXInputs = () => {
        return xData.map((value, index) => (
            <input
                style={{ width: "30px" }}
                key={index}
                type="number"
                onChange={(e) => handleXInputChange(e, index)}
            />
        ));
    };

    const renderYInputs = () => {
        return yData.map((value, index) => (
            <input
                style={{ width: "30px" }}
                key={index}
                type="number"
                onChange={(e) => handleYInputChange(e, index)}
            />
        ));
    };

    return (
        <div>
            <h2>Vandermonde</h2>
            <div>
                <label>X and Y order:</label>
                <input type="number" min="1" onChange={handleMatrixSizeChange} />
            </div>
            <div>
                <label>X vector:</label>
                {renderXInputs()}
            </div>
            <br />
            <div>
                <label>Y vector:</label>
                {renderYInputs()}
            </div>
            <br />
            <button onClick={handleSubmit}>Calculate</button>
            {result && (
                <div>
                    <h3>Result:</h3>
                    <p><b>{result}</b></p>
                </div>
            )}
        </div>
    );
};

export default Vandermonde;