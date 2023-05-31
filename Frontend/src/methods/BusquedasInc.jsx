import React, { useState } from 'react';

const BusquedasInc = () => {
    const [func, setFunc] = useState('');
    const [x0, setX0] = useState('');
    const [h, setH] = useState('');
    const [nMax, setNMax] = useState('');
    const [result, setResult] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();

        if (nMax === "" || x0 === "" || func === "" || h === "") {
            alert("Rellena todos los campos");
        } else {
            const data = {
                f: func,
                x0: parseFloat(x0),
                h: parseFloat(h),
                nmax: parseFloat(nMax),
            };

            console.log(data);

            try { 
                const response = await fetch('http://127.0.0.1:8000/api/busquedainc', {
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
    
        }
    };

    return (
        <div>
            <h2>Incremental Searches</h2>
            <form onSubmit={handleSubmit}>
                <label>
                    Function:
                    <input type="text" value={func} onChange={(e) => setFunc(e.target.value)} />
                </label>
                <br />
                <label>
                    X0:
                    <input type="number" value={x0} onChange={(e) => setX0(e.target.value)} />
                </label>
                <br />
                <label>
                    h:
                    <input type="number" value={h} onChange={(e) => setH(e.target.value)} />
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

export default BusquedasInc;