import React, { useState } from 'react';
import Modal from 'react-modal';
import './HomePage.css';

Modal.setAppElement('#root');

const Biseccion = () => {
    return (
        <div id="biseccion">
            <h2>Biseccion</h2>
        </div>
    );
}

const BusquedasInc = () => {
    return (
        <div id="BusquedasInc">
            <h2>Busquedas Incremenatales</h2>
        </div>
    );
}

const Crout = () => {
    return (
        <div id="Crout">
            <h2>Crout</h2>
        </div>
    );
}

const Doolittle = () => {
    return (
        <div id="Doolittle">
            <h2>Doolittle</h2>
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
                return <Biseccion />;
            case "busquedasinc":
                return <BusquedasInc />;
            case "Crout":
                return <Crout />;
            case "Doolittle":
                return <Doolittle />;
            case "Newton":
                return <Newton />;
            case "puntoFijo":
                return <PuntoFijo />;
            case "RaicesMultiples":
                return <RaicesMultiples />;
            case "ReglaFalsa":
                return <reglaFalsa />;
            case "secante":
                return <Secante />;
            default:
                return null;
        }
    };

    return (
        <div className="home-page">
            <h1>Numerical Analysis</h1>
            <div className="grid">
                <button onClick={() => handleOpenModal("biseccion")}>Biseccion</button>
                <button onClick={() => handleOpenModal("busquedasinc")}>Busquedas incrementales</button>
                <button onClick={() => handleOpenModal("Crout")}>Busquedas incrementales</button>
                <button onClick={() => handleOpenModal("Doolittle")}>Busquedas incrementales</button>
                <button onClick={() => handleOpenModal("Newton")}>Newton</button>
                <button onClick={() => handleOpenModal("puntoFijo")}>Punto Fijo</button>
                <button onClick={() => handleOpenModal("RaicesMultiples")}>Raices Multiples</button>
                <button onClick={() => handleOpenModal("reglaFalsa")}>Regla Falsa</button>
                <button onClick={() => handleOpenModal("secante")}>Secante</button>
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
