import numpy as np

def doolittle(A, b):
    n = len(A)
    L = np.zeros((n, n))
    U = np.zeros((n, n))
    x = np.zeros(n)

    for i in range(n):
        L[i][i] = 1.0

        for j in range(i, n):
            sum_1 = sum(L[i][k] * U[k][j] for k in range(i))
            U[i][j] = A[i][j] - sum_1

        for j in range(i + 1, n):
            sum_2 = sum(L[j][k] * U[k][i] for k in range(i))
            L[j][i] = (A[j][i] - sum_2) / U[i][i]

    # Substitucion progresiva
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # sub regresiva
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

    return x


# A = np.array([[36,3,-4,5],
#               [5,-45,10,-2],
#               [6,8,57,5],
#               [2,3,-8,-42]])

# b = np.array([-20,69,96,-32])
# print(doolittle(A,b))