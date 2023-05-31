import java.util.Arrays;

public class JacobiMethod {
    public static double[] jacobiMethod(double[][] A, double[] b, double[] x0, double tol, int Nmax) {
        int n = A.length;
        double[] xant = Arrays.copyOf(x0, n);
        double[] xact = new double[n];
        double E = 1000;
        int cont = 0;
        
        // Construcción de las matrices D, L y U
        double[][] D = new double[n][n];
        double[][] L = new double[n][n];
        double[][] U = new double[n][n];
        
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
                double dotProduct = 0.0;
                for (int j = 0; j < n; j++) {
                    dotProduct += (L[i][j] + U[i][j]) * xant[j];
                }
                xact[i] = (b[i] - dotProduct) / D[i][i];
            }
            
            E = calculateError(xant, xact);
            xant = Arrays.copyOf(xact, n);
            cont++;
        }
        
        // Entrega de resultados
        double[] x = Arrays.copyOf(xact, n);
        int iter = cont;
        double err = E;
        
        return x;
    }
    
    private static double calculateError(double[] xant, double[] xact) {
        double error = 0.0;
        for (int i = 0; i < xant.length; i++) {
            error += Math.pow(xact[i] - xant[i], 2);
        }
        return Math.sqrt(error);
    }
}
