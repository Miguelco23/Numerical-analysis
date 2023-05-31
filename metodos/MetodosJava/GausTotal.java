import java.util.Arrays;

public class GaussianEliminationTotal {
    public static double[] gaussianEliminationTotal(double[][] A, double[] b) {
        int n = A.length;
        double[][] M = new double[n][n + 1];
        int[][] cambios = new int[n - 1][2];
        double[] x = new double[n];

        // Inicialización de la matriz extendida M
        for (int i = 0; i < n; i++) {
            System.arraycopy(A[i], 0, M[i], 0, n);
            M[i][n] = b[i];
        }

        // Reducción del sistema
        for (int i = 0; i < n - 1; i++) {
            int[] maxIndex = findMaxIndex(M, i);
            int a = maxIndex[0];
            int b = maxIndex[1];

            // Cambio de columna
            if (b + i != i) {
                cambios[i][0] = i;
                cambios[i][1] = b + i;
                swapColumns(M, i, b + i);
            }

            // Cambio de filas
            if (a + i != i) {
                swapRows(M, i + a - 1, i);
            }

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

        // Reordenar el vector solución
        for (int i = cambios.length - 1; i >= 0; i--) {
            int temp = cambios[i][0];
            cambios[i][0] = cambios[i][1];
            cambios[i][1] = temp;
            double tempValue = x[cambios[i][0]];
            x[cambios[i][0]] = x[cambios[i][1]];
            x[cambios[i][1]] = tempValue;
        }

        return x;
    }

    private static int[] findMaxIndex(double[][] M, int startIndex) {
        int n = M.length;
        int[] maxIndex = new int[2];
        double maxValue = 0.0;

        for (int i = startIndex; i < n; i++) {
            for (int j = startIndex; j < n; j++) {
                double absValue = Math.abs(M[i][j]);
                if (absValue > maxValue) {
                    maxValue = absValue;
                    maxIndex[0] = i - startIndex;
                    maxIndex[1] = j - startIndex;
                }
            }
        }

        return maxIndex;
    }

    private static void swapColumns(double[][] M, int col1, int col2) {
        for (int i = 0; i < M.length; i++) {
            double temp = M[i][col1];
            M[i][col1] = M[i
