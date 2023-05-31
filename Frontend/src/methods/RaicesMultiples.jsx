import React, { useState } from 'react';

const RaicesMultiples = () => {
    const [func, setFunc] = useState('');
    const [derivada, setDerivada] = useState('');
    const [dobleDerivada, setDobleDerivada] = useState('');
    const [x0, setX0] = useState('');
    const [tolerance, setTolerance] = useState('');
    const [nMax, setNMax] = useState('');
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (nMax === "" || x0 === "" || func === "" || tolerance === "" || derivada === "") {
            alert("Rellena todos los campos");
        } else {
            const data = {
                func,
                derivada,
                dobleDerivada,
                x0: parseFloat(x0),
                tolerance: parseFloat(tolerance),
                nMax: parseFloat(nMax),
            };

            console.log(data);

            // try {
            //   const response = await fetch('API_URL', {
            //     method: 'POST',
            //     headers: {
            //       'Content-Type': 'application/json',
            //     },
            //     body: JSON.stringify(data),
            //   });

            //   const resultData = await response.json();
            //   setResult(resultData.result);
            // } catch (error) {
            //   console.error('Error:', error);
            //   alert('Error:', error);
            // }
        }
    };

    return (
        <div>
            <h2>Multiple Roots</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Function:
                    <input type="text" value={func} onChange={(e) => setFunc(e.target.value)} />
                </label>
                <br />
                <label>
                    Derivative:
                    <input type="text" value={derivada} onChange={(e) => setDerivada(e.target.value)} />
                </label>
                <br />
                <label>
                    Second Derivative:
                    <input type="text" value={dobleDerivada} onChange={(e) => setDobleDerivada(e.target.value)} />
                </label>
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
                <button type="submit">Calculate</button>
            </form>
            {result && <p>Result: {result}</p>}
        </div>
    );
};

export default RaicesMultiples;