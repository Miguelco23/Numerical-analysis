from math import *
import numpy as np

def incremental_search(f, x0, h, nmax, Err):
    if Err == 1:
        show_absolute_error = True
        show_relative_error = False
    elif Err == 2:
        show_absolute_error = False
        show_relative_error = True
    else:
        return "Invalid value for the Err parameter. It should be 1 (absolute error) or 2 (relative error)."

    xant = x0
    flambda = lambda x: eval(f)
    fant = flambda(xant)
    xact = xant + h
    fact = flambda(xact)
    for i in range(nmax):
        absolute_error = abs(xact - xant)
        relative_error = abs((xact - xant) / xact) * 100

        if show_absolute_error:
            print(f"Absolute error: {absolute_error}")
        if show_relative_error:
            print(f"Relative error (%): {relative_error}")

        print(f"{fant} {fact}")
        if fant * fact < 0:
            return f"Root is between {xant} and {xact}. Output with {i} iterations"

        xant = xact
        fant = fact
        xact = xant + h
        fact = flambda(xact)

    return "No root found within the given interval."
