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
from metodos.GausPar import GausPar
from metodos.GausSimple import GausSimpe
from metodos.Jacobi import Jacobi
from metodos.LUSimple import LUSimple



app = FastAPI()

# class ListModel(BaseModel):
#     l: list[int]

class MatrixSystemModel(BaseModel):
    A: list[list]
    b: list[int]

class PuntoFijoModel(BaseModel):
    f:str
    g:str
    x0:float
    tol:float
    nmax:int

class BusquedaIncModel(BaseModel):
    f:str
    x0: float
    h:float
    nmax:int
class NewtonModel(BaseModel):
    f:str
    derf:str
    x0:float
    tol:float
    nmax:int
    
class RaciesMultiples(BaseModel):
    f:str
    derf:str
    doblederf:str
    x0:float
    tol:float
    nmax:int
        
@app.get('/')
def main():
    return "Hola que mas?"

@app.post('/api/puntofijo')
def solvePuntoFijo(input: PuntoFijoModel):
    return({"Result":puntoFijo(input.f, input.g, input.x0,input.tol,input.nmax)})

@app.post('/api/busquedainc')
def SolveBusquedaInc(input: BusquedaIncModel):
    return({"Result":busqueda_inc(input.f, input.x0, input.h,input.nmax)})


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

@app.post('/api/newton')
def solveNewton(input: NewtonModel):
    return({"Result":Newton(input.f, input.derf, input.x0,input.tol,input.nmax)})

@app.post('/api/raicesmultiples')
def solveRaicesMultiples(input: RaicesMultiplesModel):
    return({"Result":RaicesMultiples(input.f, input.derf, input.doblederf, input.x0,input.tol,input.nmax)})
