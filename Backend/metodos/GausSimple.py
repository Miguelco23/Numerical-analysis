import numpy as np

def GausSimple(A_, b_, x_true, Error):
    # Initialization
    A = np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    M = np.concatenate((A, b.reshape(n, 1)), axis=1)
    
    # System reduction
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                M[j, i:n+1] = M[j, i:n+1] - (M[j, i]/M[i, i]) * M[i, i:n+1]
    
    # Back substitution
    x = BackSubstitution(M)
    
    # Error calculation
    r = np.dot(A, x) - b
    absolute_error = np.abs(x - x_true)
    relative_error = (absolute_error / np.abs(x_true)) * 100
    
    # Return error based on the Error parameter
    if Error == 1:
        return np.array2string(x), np.array2string(relative_error)
    elif Error == 2:
        return np.array2string(x), np.array2string(absolute_error)
    else:
        return "Invalid Error parameter value. Please use 1 for relative error or 2 for absolute error."

def BackSubstitution(M):
    # Back substitution implementation
    n = M.shape[0]
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        if M[i, i] != 0:
            x[i] = (M[i, n] - np.dot(M[i, i+1:n], x[i+1:n])) / M[i, i]
        else:
            x[i] = 0  # Or handle the case differently
    return x
