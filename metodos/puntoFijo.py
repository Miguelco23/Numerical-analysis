from math import *
import numpy as np

def puntoFijo(f, g, x0, tol, nmax):
    iter = 0
    Err = 9999
    xant = x0
    flambda = lambda x: eval(f)
    glambda = lambda x: eval(g)

    while Err> tol and iter< nmax:
        xact = glambda(xant)
        Err  = abs(xant-xact)
        print(Err)
        iter+=1
        xant = xact


    print(f"x= {xact}")
    print(f"iters = {iter}")
    print(f"Error = {Err}")


# Ejemplo de como utilizar
# puntofijo("(e**-x)-x","(e**-x)",1,5*10**(-6),12)