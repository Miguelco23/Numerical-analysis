import numpy as np

def vandermonde(x, y, Err):
    n = len(x)
    if len(y) != n:
        raise ValueError("Las entradas deben tener la misma longitud")

    degree = n - 1  # Grado del polinomio ajustado

    # Crear la matriz de Vandermonde
    vander_matrix = np.vander(x, degree + 1, increasing=False)

    # Resolver el sistema lineal
    coefficients = np.linalg.solve(vander_matrix, y)

    # Calcular las aproximaciones
    approximations = np.polyval(coefficients[::-1], x)

    if Err == 1:
        # Calcular los errores absolutos
        absolute_errors = np.abs(approximations - y)
        return coefficients, absolute_errors

    elif Err == 2:
        # Calcular los errores relativos
        absolute_errors = np.abs(approximations - y)
        relative_errors = (absolute_errors / np.abs(y)) * 100
        return coefficients, relative_errors

    else:
        return "Invalid value for parameter Err. It should be 1 (absolute error) or 2 (relative error)."
