import numpy as np

def cholesky(A, b, Err):
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

    # Cálculo de errores
    if Err == 1:
       Ax = np.dot(A, x)
       error_absoluto = np.linalg.norm(b - Ax)
       error_relativo = error_absoluto / np.linalg.norm(b)

       return ({"Solution: ":x, "Absolute error: ":error_absoluto})
      
    elif Err ==2:
       Ax = np.dot(A, x)
       error_absoluto = np.linalg.norm(b - Ax)
       error_relativo = error_absoluto / np.linalg.norm(b)

       return ({"Solution: ":x, "Relative error: ":error_relativo})
      
    else:
      return "Invalid value for parameter Err. It should be 1 (absolute error) or 2 (relative error)."
