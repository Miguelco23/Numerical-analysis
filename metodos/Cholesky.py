import numpy as np

def cholesky(A, b):
    A = np.array(A)
    b = np.array(b)
    n = len(A)
    L = np.zeros((n, n))
    x = np.zeros(n)

    for i in range(n):
        for j in range(i + 1):
            if i == j:
                sum_1 = sum(L[i][k] ** 2 for k in range(j))
                L[i][i] = np.sqrt(A[i][i] - sum_1)
            else:
                sum_2 = sum(L[i][k] * L[j][k] for k in range(j))
                L[i][j] = (A[i][j] - sum_2) / L[j][j]

    # sub progresiva
    y = np.zeros(n)
    for i in range(n):
        y[i] = (b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

    # L^T * x = y sub regresiva
    for i in range(n - 1, -1, -1):
        x[i] = (y[i] - np.dot(L[i + 1:, i], x[i + 1:])) / L[i, i]

    return x

# A = [[1,-1,1],
#     [-1,5,-5],
#     [1,-5,6]]

# b = [2,-6,9]
# print(cholesky(A,b)