import React, { useState } from 'react';

const Biseccion = () => {
  const [a, setA] = useState('');
  const [b, setB] = useState('');
  const [func, setFunc] = useState('');
  const [tolerance, setTolerance] = useState('');
  const [url, setUrl] = useState('');
  const [result, setResult] = useState('');

  const handleSubmit = async (e) => {
    e.preventDefault();

    const data = {
      a: parseFloat(a),
      b: parseFloat(b),
      func,
      tolerance: parseFloat(tolerance),
    };
    
    //Setear la plantillad del url
    setUrl(data.a + '-' + data.b + '-' + data.func + '-' + data.tolerance);

    try {
      const response = await fetch(url, {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      const resultData = await response.json();
      setResult(resultData.result);
    } catch (error) {
      console.error('Error:', error);
      alert('Error:', error);
    }
  };

  return (
    <div>
      <h2>Biseccion</h2>
      <form onSubmit={handleSubmit}>
        <label>
          Intervalo [a]:
          <input type="number" value={a} onChange={(e) => setA(e.target.value)} />
        </label>
        <br />
        <label>
          Intervalo [b]:
          <input type="number" value={b} onChange={(e) => setB(e.target.value)} />
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
        <button type="submit">Calcular</button>
      </form>
      {result && <p>Resultado: {result}</p>}
    </div>
  );
};

export default Biseccion;
