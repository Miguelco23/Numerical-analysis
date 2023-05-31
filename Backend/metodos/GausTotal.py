import numpy as np

def GausTotal(A_, b_):
    # Inicialización
    A=np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.hstack((A, b.reshape(n, 1)))
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
