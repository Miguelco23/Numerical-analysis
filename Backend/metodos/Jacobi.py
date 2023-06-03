import numpy as np

def Jacobi(A_, b_, x0_, tol, Nmax, Err):
    # Initialization
    A = np.array(A_)
    b = np.array(b_)
    x0 = np.array(x0_)
    D = np.diag(np.diag(A))
    L = -np.tril(A) + D
    U = -np.triu(A) + D
    T = np.linalg.inv(D).dot(L + U)
    C = np.linalg.inv(D).dot(b)
    xant = np.array(x0)
    E = 1000
    cont = 0
    
    # Iteration
    while E > tol and cont < Nmax:
        xact = T.dot(xant) + C
        E = np.linalg.norm(xant - xact)
        xant = xact
        cont += 1

    if Err == 1:
       # Calculate absolute error
       err_abs = np.linalg.norm(b - A.dot(xact))
       return {
          "x": np.array2string(xact),
          "iterations": cont,
          "absolute_error": err_abs,
       }
    elif Err == 2:
       # Calculate relative error
       err_abs = np.linalg.norm(b - A.dot(xact))
       err_rel = err_abs / np.linalg.norm(b)
       return {
          "x": np.array2string(xact),
          "iterations": cont,
          "relative_error": err_rel,
       }
    else:
       return "Invalid Error parameter value. Please use 1 for relative error or 2 for absolute error."
