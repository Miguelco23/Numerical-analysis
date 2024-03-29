import React, { useState } from 'react';
import * as Methods from './methods';
import Modal from 'react-modal';

Modal.setAppElement('#root');

const HomePage = () => {
  const [modalIsOpen, setModalIsOpen] = useState(false);
  const [selectedButton, setSelectedButton] = useState(null);

  const handleOpenModal = (buttonId) => {
    setSelectedButton(buttonId);
    setModalIsOpen(true);
  };

  const handleCloseModal = () => {
    setSelectedButton(null);
    setModalIsOpen(false);
  };

  let selectedMethod = () => {
    switch (selectedButton) {
      case "biseccion":
        return <Methods.Biseccion />;
      case "busquedasinc":
        return <Methods.BusquedasInc />;
      case "Cholesky":
        return <Methods.Cholesky />;
      case "Crout":
        return <Methods.Crout />;
      case "Doolittle":
        return <Methods.Doolittle />;
      case "Newton":
        return <Methods.Newton />;
      case "puntoFijo":
        return <Methods.PuntoFijo />;
      case "RaicesMultiples":
        return <Methods.RaicesMultiples />;
      case "reglaFalsa":
        return <Methods.ReglaFalsa />;
      case "secante":
        return <Methods.Secante />;
      case "GausSimple":
        return <Methods.GaussSencilla />;
      case "GausPar":
        return <Methods.GaussParcial />;
      case "GausTotal":
        return <Methods.GaussTotal />;
      case "LUSimple":
        return <Methods.LuGaussiana />;
      case "GausSeidel":
        return <Methods.GaussSeidel />;
      case "Jacobi":
        return <Methods.Jacobi />;
      case "Vandermonde":
        return <Methods.Vandermonde />;
      case "Splines":
        return <Methods.Splines />;
      default:
        return null;
    }
  };

  return (
    <div className="home-page">
      <h1>Numerical analysis</h1>

      <h2 className="sectionTitle">One variable Equations</h2>
      <div className="grid">
        <button className="homeButton" onClick={() => handleOpenModal("biseccion")}>
          Bisection
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("busquedasinc")}>
          Incremental Searches
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Newton")}>
          Newton
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("puntoFijo")}>
          Fixed Point
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("RaicesMultiples")}>
          Multiple Roots
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("reglaFalsa")}>
          False Rule
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("secante")}>
          Secant
        </button>
      </div>

      <h2 className="sectionTitle">Equation systems</h2>
      <div className="grid">
        <button className="homeButton" onClick={() => handleOpenModal("Cholesky")}>
          Cholesky
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Crout")}>
          Crout
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Doolittle")}>
          Doolittle
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausSimple")}>
          Simple Gaussian Elimination
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausPar")}>
          Gaussian elimination with partial pivoting
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausTotal")}>
          Gaussian elimination with full pivoting
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("LUSimple")}>
          LU factorization with Gaussian elimination
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausSeidel")}>
          Gauss-Seidel
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Jacobi")}>
          Jacobi
        </button>

      </div>

      <h2 className="sectionTitle">Interpolation</h2>
      <div className="grid">
        <button className="homeButton" onClick={() => handleOpenModal("Vandermonde")}>
          Vandermonde
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Splines")}>
          Quadratic Splines
        </button>
      </div>

      <Modal
        isOpen={modalIsOpen}
        onRequestClose={handleCloseModal}
        className="modal"
        overlayClassName="overlay"
      >
        {selectedMethod()}
        <button onClick={handleCloseModal}>Close</button>
      </Modal>
    </div>
  );

};

export default HomePage;
