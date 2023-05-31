from math import*
import numpy as np

def Newton(f, derf, x0, tol, Nmax):
    xant = x0
    flambda = lambda x: eval(f)
    fant = flambda(xant)
    E = 1000
    cont = 0
    derflambda = lambda x: eval(derf)
    while E > tol and cont < Nmax:
      xact = xant-fant/(derflambda(xant))
      fact = flambda(xact)
      E = abs(xact-xant)
      cont = cont+1
      xant = xact
      fant = fact
      if E < tol:
        x = xact
        ite = cont
        err = E
        return "La función tiene una raíz en, ", x
      else:
        return "No tiene solucion"