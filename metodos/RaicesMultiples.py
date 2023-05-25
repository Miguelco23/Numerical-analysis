from math import*
import numpy as np

def Raices_Multiples(f, derf, doblederf, x0, tol, Nmax):
    xant = x0
    flambda = lambda x: eval(f)
    fant = flambda(xant)
    E = 1000
    cont = 0
    derflambda = lambda x: eval(derf)
    dobderflambda = lambda x: eval(derf)
    while E > tol and cont < Nmax:
      xact = xant-fant*derflambda(xant)/((derflambda(xant))**2-fant*dobderflambda(xant))
      fact = flambda(xact)
      E = abs(xact-xant)
      cont = cont+1
      xant = xact
      fant = fact
      if E < tol
        x = xact
        ite = cont
        err = E
        print("La función tiene raíz multiple en, " x, "con una tolerancia de, " E, "y un número de iteraciones de " ite)
      else
        print("No tiene solucion")
