from math import *
import numpy as np

def busqueda_inc(f, x0, h, nmax):
    xant = x0
    flambda = lambda x: eval(f)
    fant = flambda(xant)
    xact = xant+h
    fact = flambda(xact)
    for i in range(nmax):
        print(f"{fant} {fact}")
        if fant * fact <0:
            # print(f"hay raiz entre {xant} y {xact}")
            # print(f"iters = {i}")
            return(f"Root is between {xant} and {xact}. output with {i} iterations") # Retorna dos limites de el intervalo y las iteraciones
        xant = xact
        fant = fact
        xact = xant+h
        fact = flambda(xact)


# Ejemplo de como utilizar
# busqueda_inc("(x**3)+3*x+2",-2,0.0075,1000)
