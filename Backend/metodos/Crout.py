import numpy as np

def crout(A, b, x_exacto, Err):
    A = np.array(A)
    b = np.array(b)
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    x = np.zeros(n)

    for j in range(n):
        U[j][j] = 1.0

        for i in range(j+1):
            sum_1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_1

        for i in range(j, n):
            sum_2 = sum(L[i][k] * U[k][j] for k in range(j))
            if U[j][j] != 0:
                L[i][j] = (A[i][j] - sum_2) / U[j][j]
            else:
                L[i][j] = 0

    # sub progresiva
    y = np.zeros(n)
    for i in range(n):
        if L[i, i] != 0:
            y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]
        else:
            y[i] = 0

    # sub regresiva
    for i in range(n - 1, -1, -1):
        if U[i, i] != 0:
            x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]
        else:
            x[i] = 0

    if Err == 1:
        error_absoluto = np.linalg.norm(x - x_exacto)
        error_relativo = error_absoluto / np.linalg.norm(x_exacto)
        return ({"Solution: ": x, "Absolute error: ": error_absoluto})
    elif Err == 2:
        error_absoluto = np.linalg.norm(x - x_exacto)
        error_relativo = error_absoluto / np.linalg.norm(x_exacto)
        return ({"Solution: ": x, "Relative error: ": error_relativo})
    else:
        return "Invalid value for parameter Err. It should be 1 (absolute error) or 2 (relative error)."
