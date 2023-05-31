
def RaicesMultiples(f, df, d2f, x0, tol, Nmax):
    # Inicialización
    xant = x0
    fant = f(xant)
    E = 1000
    cont = 0
    
    # Ciclo
    while E > tol and cont < Nmax:
        xact = xant - (fant * df(xant)) / ((df(xant)) ** 2 - fant * d2f(xant))
        fact = f(xact)
        E = abs(xact - xant)
        cont = cont + 1
        xant = xact
        fant = fact
    
    # Entrega de resultados
    x = xact
    iteraciones = cont
    err = E
    
    return ({"x":x,"Iter":iteraciones, "Error":err})

