# Importamos fasAPI
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import numpy as np
from fastapi.middleware.cors import CORSMiddleware

# Importamos los metodos numerico
from metodos.biseccion import biseccion
from metodos.busquedasinc import busqueda_inc
from metodos.Newton import Newton
from metodos.puntoFijo import puntoFijo
from metodos.RaicesMultiples import RaicesMultiples
from metodos.reglaFalsa import regla_falsa
from metodos.secante import secante
from metodos.Crout import crout
from metodos.Doolittle import doolittle
from metodos.Cholesky import cholesky
from metodos.GausPar import GausPar
from metodos.GausTotal import GausTotal
from metodos.GausSeidel import GausSeidel
from metodos.GausSimple import GausSimple
from metodos.Jacobi import Jacobi
from metodos.LUSimple import LUSimple
from metodos.Vandermonde import vandermonde



app = FastAPI()

# Configurar los orígenes permitidos en CORS
origins = [
    "http://localhost:3000",
]

# Configurar el middleware de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class ListModel(BaseModel):
#     l: list[int]

class MatrixSystemModel(BaseModel):
    A: list[list]
    b: list[float]

class InterpolationModel(BaseModel):
    x: list
    y:list
    degree:int

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
    
class RaicesMultiplesModel(BaseModel):
    f:str
    derf:str
    doblederf:str
    x0:float
    tol:float
    nmax:int
 
class JacobiandSeidelModel(BaseModel):
    A: list[list]
    b: list[float]
    x0:list[float]
    tol:float
    nmax:float

class SplineModel(BaseModel):
    x:list[float]
    y:list[float]
    
class IterativeModel(BaseModel):
    f:str
    a:float | None = None
    b:float | None = None
    tol:float
    x0:float | None = None
    x1:float | None = None
    max_iter:int | None = None

    


@app.get('/')
def main():
    return "Hola que mas?"



@app.post('/api/biseccion')
def solvePuntoFijo(input: IterativeModel):
    return({"Result":biseccion(input.f, input.a, input.b,input.tol)})

@app.post('/api/reglafalsa')
def solvePuntoFijo(input: IterativeModel):
    return({"Result":regla_falsa(input.f, input.a, input.b,input.tol,input.max_iter)})


@app.post('/api/secante')
def solvePuntoFijo(input: IterativeModel):
    return({"Result":secante(input.f, input.x0,input.x1,input.tol, input.max_iter)})

@app.post('/api/puntofijo')
def solvePuntoFijo(input: PuntoFijoModel):
    return({"Result":puntoFijo(input.f, input.g, input.x0,input.tol,input.nmax)})

@app.post('/api/busquedainc')
def SolveBusquedaInc(input: BusquedaIncModel):
    return({"Result":busqueda_inc(input.f, input.x0, input.h,input.nmax)})

@app.post('/api/newton')
def solveNewton(input: NewtonModel):
    return({"Result":Newton(input.f, input.derf, input.x0,input.tol,input.nmax)})

@app.post('/api/raicesmultiples')
def solveRaicesMultiples(input: RaicesMultiplesModel):
    return({"Result":RaicesMultiples(input.f, input.derf, input.doblederf, input.x0,input.tol,input.nmax)})

@app.post('/api/crout')
def solveCrout(input: MatrixSystemModel):
    return({"Result":crout(input.A, input.b)})

@app.post('/api/doolittle')
def solveDoolittle(input: MatrixSystemModel):
    return({"Result":doolittle(input.A, input.b)})

@app.post('/api/GausPar')
def solveGausPar(input: MatrixSystemModel):
    return({"Result":GausPar(input.A, input.b)})

@app.post('/api/GausSimple')
def solveGausSimple(input: MatrixSystemModel):
    return({"Result":GausSimple(input.A, input.b)})

@app.post('/api/GausTotal') #   NO SIRVE
def solveGausTotal(input: MatrixSystemModel):
    return({"Result":GausTotal(input.A, input.b)})

@app.post('/api/LUSimple')
def solveLUSImple(input: MatrixSystemModel):
    return({"Result":LUSimple(input.A, input.b)})

@app.post('/api/cholesky')
def solveCholesky(input: MatrixSystemModel):
    try:
        result = ({"Result":cholesky(input.A, input.b)})
    except:
        raise HTTPException(status_code=400, detail="revisar la matriz de entrada") 
    return result

@app.post('/api/Jacobi')
def solveJacobi(input: JacobiandSeidelModel):
    return({"Result":Jacobi(input.A, input.b, input.x0, input.tol, input.nmax)})

@app.post('/api/GausSeidel')
def solveGausSeidel(input: JacobiandSeidelModel):
    return({"Result":GausSeidel(input.A, input.b, input.x0, input.tol, input.nmax)})

@app.post('/api/vandermonde')
def solveDoolittle(input: InterpolationModel):
    return({"Result":vandermonde(input.x, input.y,input.degree)})
