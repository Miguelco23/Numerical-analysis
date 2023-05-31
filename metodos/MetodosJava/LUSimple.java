import java.util.Arrays;

public class LUSimple {
    public static double[][] LUSimple(double[][] A, double[] b) {
        // Inicialización
        int n = A.length;
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        double[][] M = new double[n][n];

        // Copia de la matriz A a M
        for (int i = 0; i < n; i++) {
            M[i] = Arrays.copyOf(A[i], n);
        }

        // Factorización
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (M[j][i] != 0) {
                    L[j][i] = M[j][i] / M[i][i];
                    for (int k = i; k < n; k++) {
                        M[j][k] = M[j][k] - (M[j][i] / M[i][i]) * M[i][k];
                    }
                }
            }
            for (int k = i; k < n; k++) {
                U[i][k] = M[i][k];
            }
            for (int k = i + 1; k < n; k++) {
                U[i + 1][k] = M[i + 1][k];
            }
        }
        U[n - 1][n - 1] = M[n - 1][n - 1];

        // Entrega de resultados
        double[] z = SustitucionProgresiva(concatenateArrays(L, b));
        double[] x = SustitucionRegresiva(concatenateArrays(U, z));
        return new double[][] { x, L, U };
    }

    public static double[] SustitucionProgresiva(double[][] M) {
        int n = M.length;
        double[] z = new double[n];
        for (int i = 0; i < n; i++) {
            double sum = 0;
            for (int j = 0; j < i; j++) {
                sum += M[i][j] * z[j];
            }
            z[i] = (M[i][n] - sum) / M[i][i];
        }
        return z;
    }

    public static double[] SustitucionRegresiva(double[][] M) {
        int n = M.length;
        double[] x = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += M[i][j] * x[j];
            }
            x[i] = (M[i][n] - sum) / M[i][i];
        }
        return x;
    }

    public static double[][] concatenateArrays(double[][] arr1, double[] arr2) {
        int n = arr1.length;
        int m = arr2.length;
        double[][] result = new double[n][n + 1];
        for (int i = 0; i < n; i++) {
            result[i] = Arrays.copyOf(arr1[i], n + 1);
            result[i][n] = arr2[i];
        }
        return result;
    }

    public static void main(String[] args) {
        double[][] A = {{2, 1, -1}, {-3, -1, 2}, {-2, 1, 2}};
        double[] b = {8, -11, -3};

        double[][] result = LUSimple(A, b);
        double[] x = result[0];
        double[][] L = result[1];
        double[][] U = result[2];

        System.out.println("Solution (x): " + Arrays.toString(x));
        System.out.println("L: ");
        for (int i = 0; i < L.length; i++) {
            System.out.println(Arrays.toString(L[i]));
        }
        System.out.println("U: ");
        for (int i = 0; i < U.length; i++) {
            System.out.println(Arrays.toString(U[i]));
        }
    }
}
