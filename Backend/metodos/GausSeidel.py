import numpy as np

def GausSeidel(A_, b_, x0_, tol, Nmax):
    # Inicialización
    A=np.array(A_)
    b = np.array(b_)
    x0 = np.array(x0_)
    D = np.diag(np.diag(A))
    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.linalg.inv(D - L) @ U
    C = np.linalg.inv(D - L) @ b
    xant = np.array(x0)
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
    iterations = cont
    err = E

    return x, iterations, err
