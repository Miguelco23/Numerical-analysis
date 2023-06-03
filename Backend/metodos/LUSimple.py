import numpy as np

def LUSimple(A_, b_, Err):
    # Initialization
    A = np.array(A_)
    b = np.array(b_)
    n = A.shape[0]
    L = np.eye(n)
    U = np.zeros((n, n))
    M = A.copy()

    # Factorization
    for i in range(n-1):
        for j in range(i+1, n):
            if M[j, i] != 0:
                L[j, i] = M[j, i] / M[i, i]
                M[j, i:n] = M[j, i:n] - (M[j, i] / M[i, i]) * M[i, i:n]
        U[i, i:n] = M[i, i:n]
        U[i+1, i+1:n] = M[i+1, i+1:n]
    U[n-1, n-1] = M[n-1, n-1]

    # Results
    z = ForwardSubstitution(np.concatenate((L, b.reshape(n, 1)), axis=1))
    x = BackwardSubstitution(np.concatenate((U, z.reshape(n, 1)), axis=1))

    if Err == 1:
        # Relative Error
        absolute_error = np.linalg.norm(np.dot(A, x) - b)
        relative_error = absolute_error / np.linalg.norm(b)

        return {"x": np.array2string(x), "L": np.array2string(L), "U": np.array2string(U),
                "relative_error": relative_error}

    elif Err == 2:
        # Absolute Error
        absolute_error = np.linalg.norm(np.dot(A, x) - b)

        return {"x": np.array2string(x), "L": np.array2string(L), "U": np.array2string(U),
                "absolute_error": absolute_error}
    else:
        return "Invalid value for the 'Err' parameter. Please use 1 for relative error or 2 for absolute error."


def ForwardSubstitution(M):
    n = M.shape[0]
    z = np.zeros(n)
    for i in range(n):
        z[i] = (M[i, n] - np.dot(M[i, :i], z[:i])) / M[i, i]
    return z
