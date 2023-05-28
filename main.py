# Importamos fasAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
# Importamos los metodos numerico
from metodos.biseccion import biseccion
from metodos.busquedasinc import busqueda_inc
from metodos.Newton import Newton
from metodos.puntoFijo import puntoFijo
from metodos.RaicesMultiples import Raices_Multiples
from metodos.reglaFalsa import regla_falsa
from metodos.secante import secante
from metodos.Crout import crout
from metodos.Doolittle import doolittle
from metodos.Cholesky import cholesky



app = FastAPI()

# class ListModel(BaseModel):
#     l: list[int]

class MatrixSystemModel(BaseModel):
    A: list[list]
    b: list[int]


@app.get('/')
def main():
    return "Hola que mas?"

@app.post('/api/crout')
def solveCrout(input: MatrixSystemModel):
    return({"Result":crout(input.A, input.b)})

@app.post('/api/doolittle')
def solveDoolittle(input: MatrixSystemModel):
    return({"Result":doolittle(input.A, input.b)})

@app.post('/api/cholesky')
def solveCholesky(input: MatrixSystemModel):
    try:
        result = ({"Result":cholesky(input.A, input.b)})
    except:
        raise HTTPException(status_code=400, detail="revisar la matriz de entrada") 
    return result