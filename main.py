# Importamos fasAPI
from fastapi import FastAPI

# Importamos los metodos numerico
from metodos.biseccion import biseccion
from metodos.busquedasinc import busqueda_inc
from metodos.Newton import Newton
from metodos.puntoFijo import puntoFijo
from metodos.RaicesMultiples import Raices_Multiples
from metodos.reglaFalsa import regla_falsa
from metodos.secante import secante


app = FastAPI()

@app.get('/')
def main():
    return "Hola que mas?"
