import React, { useState } from 'react';

const PuntoFijo = () => {
    const [x0, setX0] = useState('');
    const [gx, setGx] = useState('');
    const [func, setFunc] = useState('');
    const [tolerance, setTolerance] = useState('');
    const [nMax, setNMax] = useState('');
    const [result, setResult] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (x0 === "" || gx === "" || func === "" || tolerance === "" || nMax === "") {
            alert("Rellena todos los campos");
        } else {
            const data = {
                x0: parseFloat(x0),
                g: gx,
                f: func,
                tol: parseFloat(tolerance),
                nmax: parseFloat(nMax)
            };
            console.log(JSON.stringify(data));

            try {
                const response = await fetch('http://127.0.0.1:8000/api/puntofijo', {
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
                setResult(`X: ${resultData.Result.x} - Iterations: ${resultData.Result.iters} - Error: ${resultData.Result.Error}`);
                console.log(result);
            } catch (error) {
                console.error('Error:', error);
                alert('Error:', error);
            }

        }
    };

    return (
        <div>
            <h2>Fixed point</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    F(x):
                    <input type="text" value={func} onChange={(e) => setFunc(e.target.value)} />
                </label>
                <br />
                <label>
                    G(x):
                    <input type="text" value={gx} onChange={(e) => setGx(e.target.value)} />
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
                    N max:
                    <input type="number" value={nMax} onChange={(e) => setNMax(e.target.value)} />
                </label>
                <br />
                <button type="submit">Calculate</button>
            </form>
            {result && <p>Result: {result}</p>}
        </div>
    );
};

export default PuntoFijo;