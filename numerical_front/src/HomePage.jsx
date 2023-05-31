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
      default:
        return null;
    }
  };

  return (
    <div className="home-page">
      <h1>Metodos Numericos</h1>

      <h2 className="sectionTitle">Ecuaciones de una variable</h2>
      <div className="grid">
        <button className="homeButton" onClick={() => handleOpenModal("biseccion")}>
          Bisección
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("busquedasinc")}>
          Búsquedas Incrementales
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Newton")}>
          Newton
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("puntoFijo")}>
          Punto Fijo
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("RaicesMultiples")}>
          Raíces Múltiples
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("reglaFalsa")}>
          Regla Falsa
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("secante")}>
          Secante
        </button>
      </div>

      <h2 className="sectionTitle">Sistemas de ecuaciones</h2>
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
          Eliminacion Gaussiana Sencilla
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausPar")}>
          Eliminacion Gaussiana con pivoteo parcial
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausTotal")}>
          Gaussian elimination with full pivoting
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("LUSimple")}>
          Factorizacion LU con eliminacion Gaussiana
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("GausSeidel")}>
          Gauss-Seidel
        </button>
        <button className="homeButton" onClick={() => handleOpenModal("Jacobi")}>
          Jacobi
        </button>

      </div>

      <h2 className="sectionTitle">Interpolación</h2>
      <div className="grid">
        {/* Agrega aquí los botones correspondientes a los métodos de interpolación */}
      </div>

      <Modal
        isOpen={modalIsOpen}
        onRequestClose={handleCloseModal}
        className="modal"
        overlayClassName="overlay"
      >
        {selectedMethod()}
        <button onClick={handleCloseModal}>Cerrar</button>
      </Modal>
    </div>
  );

};

export default HomePage;
