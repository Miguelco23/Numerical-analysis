import java.util.Arrays;

public class GaussSeidel {
    public static double[] gaussSeidel(double[][] A, double[] b, double[] x0, double tol, int Nmax) {
        int n = A.length;
        double[][] D = new double[n][n];
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        double[][] T = new double[n][n];
        double[] C = new double[n];
        double[] xant = Arrays.copyOf(x0, n);
        double E = 1000;
        int cont = 0;

        // Inicialización
        for (int i = 0; i < n; i++) {
            D[i][i] = A[i][i];
            for (int j = 0; j < n; j++) {
                if (j < i) {
                    L[i][j] = -A[i][j];
                } else if (j > i) {
                    U[i][j] = -A[i][j];
                }
            }
        }

        // Ciclo
        while (E > tol && cont < Nmax) {
            for (int i = 0; i < n; i++) {
                double sum = 0;
                for (int j = 0; j < n; j++) {
                    sum += T[i][j] * xant[j];
                }
                xant[i] = sum + C[i];
            }
            double[] xact = Arrays.copyOf(xant, n);
            E = norm(xant, xact);
            cont++;
        }

        // Entrega de resultados
        double[] x = Arrays.copyOf(xant, n);
        int iter = cont;
        double err = E;

        return x;
    }

    public static double norm(double[] x, double[] y) {
        int n = x.length;
        double sum = 0.0;
        for (int i = 0; i < n; i++) {
            sum += Math.pow(x[i] - y[i], 2);
        }
        return Math.sqrt(sum);
    }
