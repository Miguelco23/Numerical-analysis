import numpy as np

def GausTotal(A_, b_):
    # Inicialización
    A=np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.concatenate((A, b), axis=1)
    cambi = []

    # Reducimos el sistema
    for i in range(n - 1):
        a, b = np.unravel_index(np.argmax(np.abs(M[i:, i:])), (n - i, n - i))
        
        # Cambio de columna
        if b[0] + i != i:
            cambi.append([i, b[0] + i])
            aux2 = M[:, b[0] + i].copy()
            M[:, b[0] + i] = M[:, i]
            M[:, i] = aux2
        
        # Cambio de filas
        if a[0] + i != i:
            aux2 = M[i + a[0] - 1, i:n + 1].copy()
            M[a[0] + i - 1, i:n + 1] = M[i, i:n + 1]
            M[i, i:n + 1] = aux2
        
        for j in range(i + 1, n):
            if M[j, i] != 0:
                M[j, i:n + 1] = M[j, i:n + 1] - (M[j, i] / M[i, i]) * M[i, i:n + 1]
    
    # Entrega de resultados
    x = SustitucionRegresiva(M)  # Sustitución regresiva
    
    # Reordenamos el vector solución
    for i in range(len(cambi) - 1, -1, -1):
        aux = x[cambi[i][0]]
        x[cambi[i][0]] = x[cambi[i][1]]
        x[cambi[i][1]] = aux
    
    return np.array2string(x)
  
def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return x
