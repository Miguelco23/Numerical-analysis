import React, { useState } from "react";

const Splines = () => {
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
            y: yData
        };

        console.log(data);
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
            <h2>Quadratic Splines</h2>
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
                    <p>{result}</p>
                </div>
            )}
        </div>
    );
};

export default Splines;