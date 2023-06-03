import numpy as np

def GausPar(A_, b_, Err=1):
    # Initialization
    A = np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.concatenate((A, b.reshape(n, 1)), axis=1)
    
    # System reduction
    for i in range(n-1):
        # Row swapping
        aux0, aux = np.max(np.abs(M[i+1:n, i])), np.argmax(np.abs(M[i+1:n, i]))
        if aux0 > np.abs(M[i, i]):
            aux2 = M[i+aux, i:n+1].copy()
            M[aux+i, i:n+1] = M[i, i:n+1]
            M[i, i:n+1] = aux2
        
        for j in range(i+1, n):
            if M[j, i] != 0:
                if not np.isclose(M[i, i], 0):
                    M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i]) * M[i, i:n+1]
    
    # Results delivery
    x = SustitucionRegresiva(M)  # Backward substitution
    
    # Error calculation
    if Err == 1:
        error = np.abs(np.dot(A, x) - b)
        return np.array2string(x), np.array2string(error)
    elif Err == 2:
        error = np.abs(np.dot(A, x) - b) / np.abs(b)
        return np.array2string(x), np.array2string(error)
    else:
        return "Warning: Invalid value for parameter Err. It has been set to 1 (absolute error)."
    

def SustitucionRegresiva(M):
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if not np.isclose(M[i, i], 0):
            x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
    return x
