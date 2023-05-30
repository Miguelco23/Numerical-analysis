import numpy as np
from Crout import crout

def vandermonde(x, y, degree):
    n = len(x)
    if len(y) != n:
        raise ValueError("Las entradas deben tener la misma longitud")

    # Crear la matriz de vandermonde
    vander_matrix = np.vander(x, degree + 1, increasing=True)
    # print(vander_matrix)

    # Resolver el sistema lineal
    coefficients = crout(vander_matrix, y)

    return coefficients

# # Como usar:
# x = [-2, -1, 2, 3]
# y = [12.13533528, 6.367879441, -4.610943901, 2.085536923]
# degree = 3

# coefficients = vandermonde(x, y, degree)
# print(coefficients)
