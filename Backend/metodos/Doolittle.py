import numpy as np

def doolittle(A, b, Err):
    class DoolittleSolver:
        def __init__(self, A, b):
            self.A = A
            self.b = b

        def solve(self):
            n = len(self.A)
            L = np.zeros((n, n))
            U = np.zeros((n, n))
            x = np.zeros(n)

            for i in range(n):
                L[i][i] = 1.0

                for j in range(i, n):
                    sum_1 = sum(L[i][k] * U[k][j] for k in range(i))
                    U[i][j] = self.A[i][j] - sum_1

                for j in range(i + 1, n):
                    sum_2 = sum(L[j][k] * U[k][i] for k in range(i))
                    L[j][i] = (self.A[j][i] - sum_2) / U[i][i]

            # Forward substitution
            y = np.zeros(n)
            for i in range(n):
                y[i] = (self.b[i] - np.dot(L[i, :i], y[:i])) / L[i, i]

            # Backward substitution
            for i in range(n - 1, -1, -1):
                x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i, i]

            # Reference solution
            x_true = np.linalg.solve(self.A, self.b)

            # Calculation of absolute and relative errors
            absolute_error = np.linalg.norm(x_true - x)
            relative_error = absolute_error / np.linalg.norm(x_true)

            if Err == 1:
                return x, absolute_error
            elif Err == 2:
                return x, relative_error
            else:
                return "Invalid value for parameter Err. It should be 1 (absolute error) or 2 (relative error)."

    solver = DoolittleSolver(A, b)
    result = solver.solve()
    return result

A = np.array([[36, 3, -4, 5],
              [5, -45, 10, -2],
              [6, 8, 57, 5],
              [2, 3, -8, -42]])

b = np.array([-20, 69, 96, -32])

# Calculate solution and absolute error
solution, absolute_error = doolittle(A, b, Err=1)
print("Solution:", solution)
print("Absolute error:", absolute_error)

# Calculate solution and relative error
solution, relative_error = doolittle(A, b, Err=2)
print("Solution:", solution)
print("Relative error:", relative_error)

# Test case with invalid Err value
result = doolittle(A, b, Err=3)
print(result)
