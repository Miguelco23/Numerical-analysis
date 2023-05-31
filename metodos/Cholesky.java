import java.util.Arrays;

public class Cholesky {
    public static double[] cholesky(double[][] A, double[] b) {
        int n = A.length;
        double[][] L = new double[n][n];
        double[] x = new double[n];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                if (i == j) {
                    double sum_1 = 0.0;
                    for (int k = 0; k < j; k++) {
                        sum_1 += Math.pow(L[i][k], 2);
                    }
                    L[i][i] = Math.sqrt(A[i][i] - sum_1);
                } else {
                    double sum_2 = 0.0;
                    for (int k = 0; k < j; k++) {
                        sum_2 += L[i][k] * L[j][k];
                    }
                    L[i][j] = (A[i][j] - sum_2) / L[j][j];
                }
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
                dotProduct += L[j][i] * x[j];
            }
            x[i] = (y[i] - dotProduct) / L[i][i];
        }

        return x;
    }

    public static void main(String[] args) {
        double[][] A = {{1, -1, 1}, {-1, 5, -5}, {1, -5, 6}};
        double[] b = {2, -6, 9};
        double[] result = cholesky(A, b);
        System.out.println(Arrays.toString(result));
    }
}
