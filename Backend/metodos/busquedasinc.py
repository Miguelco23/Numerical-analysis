from math import *

def puntoFijo(f, g, x0, tol, nmax, Err):
    if Err == 1:
        error_type = "relative error"
    elif Err == 2:
        error_type = "absolute error"
    else:
        raise ValueError("Invalid value for the Err parameter. It should be 1 (absolute error) or 2 (relative error).")

    iter = 0
    xant = x0
    flambda = lambda x: eval(f)
    glambda = lambda x: eval(g)

    while iter < nmax:
        xant_ant = xant
        xact = glambda(xant)
        Err = abs(xant - xact)
        err_abs = abs(xact - xant)
        err_rel = abs((xact - xant) / xant)
        iter += 1
        xant = xact

    if Err == 1:
        print(f"Error relativo = {err_rel}")
    elif Err == 2:
        print(f"Error absoluto = {err_abs}")

    print(f"x = {xact}")
    print(f"iters = {iter}")
    print(f"Error = {Err} ({error_type})")

    return {"x": xact, "iters": iter, "Error": Err}
