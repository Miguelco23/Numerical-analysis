import java.util.Arrays;

public class GaussSeidel {
    public static double[] gaussSeidel(double[][] A, double[] b, double[] x0, double tol, int Nmax) {
        int n = A.length;
        double[] x = Arrays.copyOf(x0, n);
        double[] xant = Arrays.copyOf(x0, n);
        double E = 1000;
        int cont = 0;

        // Inicialización de matrices
        double[][] D = new double[n][n];
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        double[][] T = new double[n][n];
        double[] C = new double[n];

        for (int i = 0; i < n; i++) {
            D[i][i] = A[i][i];
            for (int j = 0; j < n; j++) {
                if (i > j) {
                    L[i][j] = -A[i][j];
                } else if (i < j) {
                    U[i][j] = -A[i][j];
                }
            }
        }

        // Cálculo de matrices T y C
        double[][] DL = matrixSubtraction(D, L);
        double[][] invDL = matrixInverse(DL);
        T = matrixMultiplication(invDL, U);
        C = matrixMultiplication(invDL, b);

        // Ciclo
        while (E > tol && cont < Nmax) {
            x = matrixVectorMultiplication(T, xant);
            for (int i = 0; i < n; i++) {
                x[i] += C[i];
            }
            E = vectorNorm(matrixVectorSubtraction(xant, x));
            xant = Arrays.copyOf(x, n);
            cont++;
        }

        return x;
    }

    // Resta de matrices
    private static double[][] matrixSubtraction(double[][] A, double[][] B) {
        int n = A.length;
        int m = A[0].length;
        double[][] result = new double[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                result[i][j] = A[i][j] - B[i][j];
            }
        }

        return result;
    }

    // Producto de matrices
    private static double[][] matrixMultiplication(double[][] A, double[][] B) {
        int n = A.length;
        int m = B[0].length;
        int p = B.length;
        double[][] result = new double[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                for (int k = 0; k < p; k++) {
                    result[i][j] += A[i][k] * B[k][j];
                }
            }
        }

        return result;
    }

    // Inversa de una matriz
    private static double[][] matrixInverse(double[][] A) {
        int n = A.length;
        double[][] result = new double[n][n];
        double[][] augmentedMatrix = new double[n][2 * n];

        // Crear matriz aumentada [A | I]
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, augmentedMatrix[i], 0, n);
            augmentedMatrix[i][n + i] = 1;
        }

        //
