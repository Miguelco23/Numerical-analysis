import java.util.Arrays;

public class GaussianEliminationSimple {
    public static double[] gaussianEliminationSimple(double[][] A, double[] b) {
        int n = A.length;
        double[][] M = new double[n][n + 1];
        double[] x = new double[n];

        // Inicialización de la matriz extendida M
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, M[i], 0, n);
            M[i][n] = b[i];
        }

        // Reducción del sistema
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (M[j][i] != 0) {
                    double factor = M[j][i] / M[i][i];
                    for (int k = i; k <= n; k++) {
                        M[j][k] -= factor * M[i][k];
                    }
                }
            }
        }

        // Sustitución regresiva
        for (int i = n - 1; i >= 0; i--) {
            double dotProduct = 0.0;
            for (int j = i + 1; j < n; j++) {
                dotProduct += M[i][j] * x[j];
            }
            x[i] = (M[i][n] - dotProduct) / M[i][i];
        }

        return x;
    }
}
