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
                double sum_1 = 0.0;
                for (int k = 0; k < i; k++) {
                    sum_1 += L[i][k] * U[k][j];
                }
                U[i][j] = A[i][j] - sum_1;
            }

            for (int j = i + 1; j < n; j++) {
                double sum_2 = 0.0;
                for (int k = 0; k < i; k++) {
                    sum_2 += L[j][k] * U[k][i];
                }
                L[j][i] = (A[j][i] - sum_2) / U[i][i];
            }
        }

        double[] y = new double[n];
        for (int i = 0; i < n; i++) {
            double dotProduct = 0.0;
            for (int j = 0; j < i; j++) {
                dotProduct += L[i][j] * y[j];
            }
            y[i] = (b[i] - dotProduct) / L[i][i];
        }

