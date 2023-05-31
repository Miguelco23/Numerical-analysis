import java.util.Arrays;

public class Crout {
    public static double[] crout(double[][] A, double[] b) {
        int n = A.length;
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        double[] x = new double[n];

        for (int j = 0; j < n; j++) {
            L[j][j] = 1.0;

            for (int i = 0; i <= j; i++) {
                double sum_1 = 0.0;
                for (int k = 0; k < i; k++) {
                    sum_1 += L[i][k] * U[k][j];
                }
                U[i][j] = A[i][j] - sum_1;
            }

            for (int i = j; i < n; i++) {
                double sum_2 = 0.0;
                for (int k = 0; k < j; k++) {
                    sum_2 += L[i][k] * U[k][j];
                }
                L[i][j] = (A[i][j] - sum_2) / U[j][j];
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

        for (int i = n - 1; i >= 0; i--) {
            double dotProduct = 0.0;
            for (int j = i + 1; j < n; j++) {
                dotProduct += U[i][j] * x[j];
            }
            x[i] = (y[i] - dotProduct) / U[i][i];
        }

        return x;
    }

    public static void main(String[] args) {
        double[][] A = {{36, 3, -4, 5}, {5, -45, 10, -2}, {6, 8, 57, 5}, {2, 3, -8, -42}};
        double[] b = {-20, 69, 96, -32};
        double[] result = crout(A, b);
        System.out.println(Arrays.toString(result));
    }
}
