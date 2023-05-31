import numpy as np

def GausPar(A_, b_):
    # Inicialización
    A=np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.concatenate((A, b.reshape(n, 1)), axis=1)
    
    # Reducción del sistema
    for i in range(n-1):
        # Cambio de filas
        aux0, aux = np.max(np.abs(M[i+1:n, i])), np.argmax(np.abs(M[i+1:n, i]))
        if aux0 > np.abs(M[i, i]):
            aux2 = M[i+aux, i:n+1].copy()
            M[aux+i, i:n+1] = M[i, i:n+1]
            M[i, i:n+1] = aux2
        
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i]) * M[i, i:n+1]
    
    # Entrega de resultados
    x = SustitucionRegresiva(M)  # Sustitución regresiva
    return {"x": np.array2string(x)}

def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return x
