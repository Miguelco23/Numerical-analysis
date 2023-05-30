import numpy as np

def GausSediel(A, b, x0, tol, Nmax):
    # Inicialización
    D = np.diag(np.diag(A))
    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.linalg.inv(D - L) @ U
    C = np.linalg.inv(D - L) @ b
    xant = x0
    E = 1000
    cont = 0

    # Ciclo
    while E > tol and cont < Nmax:
        xact = T @ xant + C
        E = np.linalg.norm(xant - xact)
        xant = xact
        cont += 1

    # Entrega de resultados
    x = xact
    iter = cont
    err = E

    return x, iter, err
