import React, { useState } from 'react';
import * as Methods from './methods';
import Modal from 'react-modal';

Modal.setAppElement('#root');

const BusquedasInc = () => {
    return (
        <div id="BusquedasInc">
            <h2>Busquedas Incremenatales</h2>
        </div>
    );
}

const Newton = () => {
    return (
        <div id="Newton">
            <h2>Newton</h2>
        </div>
    );
}

const PuntoFijo = () => {
    return (
        <div id="PuntoFijo">
            <h2>Punto Fijo</h2>
        </div>
    );
}

const RaicesMultiples = () => {
    return (
        <div id="RaicesMultiples">
            <h2>Raices Multiples</h2>
        </div>
    );
}

const ReglaFalsa = () => {
    return (
        <div id="ReglaFalsa">
            <h2>Regla Falsa</h2>
        </div>
    );
}

const Secante = () => {
    return (
        <div id="Secante">
            <h2>Secante</h2>
        </div>
    );
}

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
                return <BusquedasInc />;
            case "Cholesky":
                return <Methods.Cholesky />;
            case "Crout":
                return <Methods.Crout />;
            case "Doolittle":
                return <Methods.Doolittle />;
            case "Newton":
                return <Newton />;
            case "puntoFijo":
                return <PuntoFijo />;
            case "RaicesMultiples":
                return <RaicesMultiples />;
            case "reglaFalsa":
                return <ReglaFalsa />;
            case "secante":
                return <Secante />;
            default:
                return null;
        }
    };

    return (
        <div className="home-page">
          <h1>Numerical Analysis</h1>
      
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
