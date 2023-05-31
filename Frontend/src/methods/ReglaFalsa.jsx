import React, { useState } from 'react';

const ReglaFalsa = () => {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [func, setFunc] = useState('');
  const [tolerance, setTolerance] = useState('');
  const [maxIter, setMaxIter] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (a === "" || b === "" || func === "" || tolerance === "" || maxIter === "") {
      alert("Rellena todos los campos");
    } else {
      const data = {
        a: parseFloat(a),
        b: parseFloat(b),
        f: func,
        tol: parseFloat(tolerance),
        max_iter: parseFloat(maxIter)
      };

      console.log(data);

      try { 
        const response = await fetch('http://127.0.0.1:8000/api/reglafalsa', {
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
      <h2>False Rule</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Interval [a]:
          <input type="number" value={a} onChange={(e) => setA(e.target.value)} />
        </label>
        <br />
        <label>
          Interval [b]:
          <input type="number" value={b} onChange={(e) => setB(e.target.value)} />
        </label>
        <br />
        <label>
          Function:
          <input type="text" value={func} onChange={(e) => setFunc(e.target.value)} />
        </label>
        <br />
        <label>
          Tolerance:
          <input type="number" value={tolerance} onChange={(e) => setTolerance(e.target.value)} />
        </label>
        <br />
        <label>
          Maximum Iteration:
          <input type="number" value={maxIter} onChange={(e) => setMaxIter(e.target.value)} />
        </label>
        <br />
        <button type="submit">Calculate</button>
      </form>
      {result && <p>Result: {result}</p>}
    </div>
  );
};

export default ReglaFalsa;