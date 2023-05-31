import java.util.Arrays;

public class Doolittle {
    public static double[] doolittle(double[][] A, double[] b) {
        int n = A.length;
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        double[] x = new double[n];

        for (int i = 0; i < n; i++) {
            L[i][i] = 1.0;

            for (int j = i; j < n; j++) {
                double sum1 = 0.0;
                for (int k = 0; k < i; k++) {
                    sum1 += L[i][k] * U[k][j];
                }
                U[i][j] = A[i][j] - sum1;
            }

            for (int j = i + 1; j < n; j++) {
                double sum2 = 0.0;
                for (int k = 0; k < i; k++) {
                    sum2 += L[j][k] * U[k][i];
                }
                L[j][i] = (A[j][i] - sum2) / U[i][i];
            }
        }

        // Sustitución progresiva
        double[] y = new double[n];
        for (int i = 0; i < n; i++) {
            double sum = 0.0;
            for (int j = 0; j < i; j++) {
                sum += L[i][j] * y[j];
            }
            y[i] = (b[i] - sum) / L[i][i];
        }

        // Sustitución regresiva
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0.0;
            for (int j = i + 1; j < n; j++) {
                sum += U[i][j] * x[j];
            }
            x[i] = (y[i] - sum) / U[i][i];
        }

        return x;
    }
}
