import numpy as np

def SplinesCuadratico(x_, y_, Err):
    if len(x_) != len(y_):
        return "The entered sizes of X and Y are not equal. Therefore it cannot be calculated"
    
    m = len(x_)
    n = m-1
    A = np.zeros((3*n, 3*n))
    b = np.zeros((3*n, 1))
    
    A[0, 0:3] = [x_[0]**2, x_[0], 1]
    b[0] = y_[0]
    
    i = 1  # Contador de filas primer cambio
    j = 0  # Contador de columnas primer cambio
    c = 1  # Contador de filas segundo cambio
    v = 3  # Contador de columnas segundo cambio
    
    for k in range(1, n):
        A[i, j] = x_[k]**2
        A[i, j+1] = x_[k]
        A[i, j+2] = 1
        b[i] = y_[k]
        A[c+1, v] = x_[k]**2
        A[c+1, v+1] = x_[k]
        A[c+1, v+2] = 1
        b[c+1] = y_[k]
        c += 2
        v += 3
        i += 2
        j += 3
    
    A[i, j] = x_[k+1]**2
    A[i, j+1] = x_[k+1]
    A[i, j+2] = 1
    b[i] = y_[k+1]
    i += 1
    j = 0
    f = 3
    
    for t in range(1, n):
        A[i, j] = 2*x_[t]
        A[i, j+1] = 1
        A[i, f] = -2*x_[t]
        A[i, f+1] = -1
        i += 1
        j += 3
        f += 3
    
    A[i, 0] = 2
    coeficientes = np.linalg.solve(A, b)
    d = len(coeficientes)/3
    intd = int(d)
    Polinomios = []
    errores_absolutos = []
    errores_relativos = []
    NumPol = 1
    temp = 0
    
    for g in range(0, intd):
        polinomio = "Polynomial " + str(NumPol) + ": " + str(coeficientes[temp]) + "x^2 + " + str(coeficientes[temp+1]) + "x + " + str(coeficientes[temp+2])
        Polinomios.append(polinomio)
        NumPol += 1
        temp += 3
    
    # Calcular errores
    if Err == 1:
        for j in range(len(x_)):
            polinomio_actual = coeficientes[j//2*3:j//2*3+3]
            x_actual = x_[j]
            y_real = y_[j]
            y_interpolado = np.polyval(polinomio_actual, x_actual)
            error_absoluto = np.abs(y_real - y_interpolado)
            error_relativo = error_absoluto / np.abs(y_real)
            errores_absolutos.append(error_absoluto)
            errores_relativos.append(error_relativo)
    
        return ({"Polynomials: ":Polinomios, "Absolute error: ":errores_absolutos})
    elif Err == 2:
        for j in range(len(x_)):
            polinomio_actual = coeficientes[j//2*3:j//2*3+3]
            x_actual = x_[j]
            y_real = y_[j]
            y_interpolado = np.polyval(polinomio_actual, x_actual)
            error_absoluto = np.abs(y_real - y_interpolado)
            error_relativo = error_absoluto / np.abs(y_real)
            errores_absolutos.append(error_absoluto)
            errores_relativos.append(error_relativo)
    
        return ({"Polynomials: ":Polinomios, "Relative errors: ":errores_relativos})
    else:
        return "The value entered for the errors does not correspond to any of the errors that I know can request"
