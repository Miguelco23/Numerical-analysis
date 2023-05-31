import numpy as np

def LUSimple(A_, b_):
    # Inicialización
    A=np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A.copy()

    # Factorización
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i] / M[i, i]
                M[j, i:n] = M[j, i:n] - (M[j, i] / M[i, i]) * M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
    U[n-1, n-1] = M[n-1, n-1]

    # Entrega de resultados
    z = SustitucionProgresiva(np.concatenate((L, b.reshape(n, 1)), axis=1))
    x = SustitucionRegresiva(np.concatenate((U, z.reshape(n, 1)), axis=1))
    return {"x": np.array2string(x),"L": np.array2string(L), "U":np.array2string(U)}

def SustitucionProgresiva(M):
    n = M.shape[0]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (M[i, n] - np.dot(M[i, :i], z[:i])) / M[i, i]
    return z

def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return (x)
