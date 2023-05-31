import numpy as np

def crout(A, b):
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
            L[i][j] = (A[i][j] - sum_2) / U[j][j]

    # sub progresiva
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # sub regresiva
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return np.array2string(x)


# A =           [[36,3,-4,5],
#               [5,-45,10,-2],
#               [6,8,57,5],
#               [2,3,-8,-42]]

# b = [-20,69,96,-32]

# print(crout(A,b))