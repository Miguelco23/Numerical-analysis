import numpy as np

def GausTotal(A_, b_, x_exact, Err):
    # Inicialización
    A = np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.hstack((A, b.reshape(n, 1)))
    M_copy = M.copy()  # Copia de la matriz M
    cambi = []
    
    # Reducimos el sistema
    for i in range(n - 1):
        a, b = np.unravel_index(np.argmax(np.abs(M[i:, i:])), (n - i, n - i))
        
        # Cambio de columna
        if b + i != i:
            cambi.append([i, b + i])
            M[:, [b + i, i]] = M[:, [i, b + i]]
        
        # Cambio de filas
        if a + i != i:
            M[[a + i, i], i:] = M[[i, a + i], i:]
        
        for j in range(i + 1, n):
            if M[j, i] != 0:
                M[j, i:] = M[j, i:] - (M[j, i] / M[i, i]) * M[i, i:]
    
    # Entrega de resultados
    x = SustitucionRegresiva(M_copy)  # Utilizar la matriz copiada
    
    # Reordenamos el vector solución
    for i in range(len(cambi) - 1, -1, -1):
        aux = x[cambi[i][0]]
        x[cambi[i][0]] = x[cambi[i][1]]
        x[cambi[i][1]] = aux
    
    # Cálculo de errores
    error_absoluto = np.abs(x - x_exact)
    error_relativo = np.divide(error_absoluto, np.abs(x_exact))
    
    if Err == 1:
        return np.array2string(x), np.array2string(error_absoluto)
    elif Err == 2:
        return np.array2string(x), np.array2string(error_relativo)
    else:
        return "Invalid Error parameter value. Please use 1 for relative error or 2 for absolute error."

def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if np.abs(M[i, i]) < 1e-10:  # Verificación de división por cero
            x[i] = np.nan  # Establecer un valor NaN para indicar un resultado no válido
        else:
            x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return x
