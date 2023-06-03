from math import *
import numpy as np

def Newton(f, derf, x0, tol, Nmax, Err):
    xant = x0
    flambda = lambda x: eval(f)
    fant = flambda(xant)
    E = 1000
    cont = 0
    derflambda = lambda x: eval(derf)
    
    error_abs = []  # Lista para almacenar los errores absolutos
    error_rel = []  # Lista para almacenar los errores relativos
    
    while E > tol and cont < Nmax:
        xact = xant - fant / (derflambda(xant))
        fact = flambda(xact)
        E = abs(xact - xant)  # Error absoluto
        error_abs.append(E)

        if xact != 0:
            error_relativo = abs((xact - xant) / xact)  # Error relativo
            error_rel.append(error_relativo)

        cont = cont + 1
        xant = xact
        fant = fact

    if E < tol:
        x = xact
        ite = cont
        err = E
        if Err == 1:
          return ("The function has a root at ", x, " with absolute errors: ", error_abs)
        elif Err == 2:
          return ("The function has a root at ", x, " with relative errors: ", error_rel)
        else:
          return "Invalid value for the 'Err' parameter. Please use 1 for relative error or 2 for absolute error."

    else:
        return ("No solution exists")
