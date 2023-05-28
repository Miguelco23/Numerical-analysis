import numpy as np

def GausSimple(A, b):
    # Inicialización
    n = A.shape[0]
    M = np.concatenate((A, b.reshape(n, 1)), axis=1)
    
    # Reducción del sistema
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i]) * M[i, i:n+1]
    
    # Sustitución regresiva
    x = SustitucionRegresiva(M)
    
    # Entrega de resultados
    return x

def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return x
