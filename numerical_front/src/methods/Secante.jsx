import React, { useState } from 'react';

const Secante = () => {
  const [x0, setX0] = useState('');
  const [x1, setX1] = useState('');
  const [func, setFunc] = useState('');
  const [tolerance, setTolerance] = useState('');
  const [maxIter, setMaxIter] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (x0 === "" || x1 === "" || func === "" || tolerance === "" || maxIter === "") {
      alert("Rellena todos los campos");
    } else {
      const data = {
        x0: parseFloat(x0),
        x1: parseFloat(x1),
        func,
        tolerance: parseFloat(tolerance),
        maxIter: parseFloat(maxIter)
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
      <h2>Secante</h2>
      <form onSubmit={handleSubmit}>
        <label>
          X0:
          <input type="number" value={x0} onChange={(e) => setX0(e.target.value)} />
        </label>
        <br />
        <label>
          X1:
          <input type="number" value={x1} onChange={(e) => setX1(e.target.value)} />
        </label>
        <br />
        <label>
          Funcion:
          <input type="text" value={func} onChange={(e) => setFunc(e.target.value)} />
        </label>
        <br />
        <label>
          Tolerancia:
          <input type="number" value={tolerance} onChange={(e) => setTolerance(e.target.value)} />
        </label>
        <br />
        <label>
          Iteracion maxima:
          <input type="number" value={maxIter} onChange={(e) => setMaxIter(e.target.value)} />
        </label>
        <br />
        <button type="submit">Calcular</button>
      </form>
      {result && <p>Resultado: {result}</p>}
    </div>
  );
};

export default Secante;