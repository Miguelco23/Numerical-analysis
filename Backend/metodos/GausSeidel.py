import numpy as np

def GausSeidel(A_, b_, x0_, tol, Nmax, Err):
    # Inicialización
    A = np.array(A_)
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
        E_abs = np.linalg.norm(xant - xact)
        E_rel = E_abs / np.linalg.norm(xact)
        xant = xact
        if Err == 1:
            E = E_abs
        elif Err == 2:
            E = E_rel
        else:
            return "Invalid value for Err. Please choose 1 for absolute error or 2 for relative error."
        cont += 1

    # Entrega de resultados
    x = xact
    iterations = cont
    
    if Err == 1:
        error = E_abs
        return {"x": x, "iterations": iterations, "absolute_error": error}
    elif Err == 2:
        error = E_rel
        return {"x": x, "iterations": iterations, "relative_error": error}
    else:
        return "Invalid value for Err. Please choose 1 for absolute error or 2 for relative error."
