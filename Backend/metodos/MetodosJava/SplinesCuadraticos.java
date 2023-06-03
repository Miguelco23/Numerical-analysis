import java.util.ArrayList;

public class SplinesCuadratico {
    public static Object[] calcular(double[] x_, double[] y_, int Err) {
        if (x_.length != y_.length) {
            return new Object[] {"Los tamaños ingresados de X y Y no son iguales. Por lo tanto no se puede calcular"};
        }

        int m = x_.length;
        int n = m - 1;
        double[][] A = new double[3 * n][3 * n];
        double[][] b = new double[3 * n][1];

        A[0][0] = Math.pow(x_[0], 2);
        A[0][1] = x_[0];
        A[0][2] = 1;
        b[0][0] = y_[0];

        int i = 1;  // Contador de filas primer cambio
        int j = 0;  // Contador de columnas primer cambio
        int c = 1;  // Contador de filas segundo cambio
        int v = 3;  // Contador de columnas segundo cambio

        for (int k = 1; k < n; k++) {
            A[i][j] = Math.pow(x_[k], 2);
            A[i][j + 1] = x_[k];
            A[i][j + 2] = 1;
            b[i][0] = y_[k];
            A[c + 1][v] = Math.pow(x_[k], 2);
            A[c + 1][v + 1] = x_[k];
            A[c + 1][v + 2] = 1;
            b[c + 1][0] = y_[k];
            c += 2;
            v += 3;
            i += 2;
            j += 3;
        }

        A[i][j] = Math.pow(x_[n], 2);
        A[i][j + 1] = x_[n];
        A[i][j + 2] = 1;
        b[i][0] = y_[n];
        i += 1;
        j = 0;
        int f = 3;

        for (int t = 1; t < n; t++) {
            A[i][j] = 2 * x_[t];
            A[i][j + 1] = 1;
            A[i][f] = -2 * x_[t];
            A[i][f + 1] = -1;
            i += 1;
            j += 3;
            f += 3;
        }

        A[i][0] = 2;
        double[][] coeficientes = solve(A, b);
        int d = coeficientes.length / 3;
        ArrayList<String> Polinomios = new ArrayList<>();
        ArrayList<Double> errores_absolutos = new ArrayList<>();
        ArrayList<Double> errores_relativos = new ArrayList<>();
        int NumPol = 1;
        int temp = 0;

        for (int g = 0; g < d; g++) {
            String polinomio = "Polinomio " + NumPol + ": " + coeficientes[temp][0] + "x^2 + " + coeficientes[temp + 1][0] + "x + " + coeficientes[temp + 2][0];
            Polinomios.add(polinomio);
            NumPol += 1;
            temp += 3;
        }

        // Calcular errores
        if (Err == 1 || Err == 2) {
            for (int j = 0; j < x_.length; j++) {
                double[] polinomio_actual = {coeficientes[j / 2 * 3][0], coeficientes[j / 2 * 3 + 1][0], coeficientes[j / 2 * 3 + 2][0]};
                double x_actual = x_[j];
                double y_real = y_[j];
                double y_interpolado = evaluarPolinomio(polinomio_actual, x_actual);
                double error_absoluto = Math.abs(y_real - y_interpolado);
                double error_relativo = error_absoluto / Math.abs(y_real);
                errores_absolutos.add(error_absoluto);
                errores_relativos.add(error_relativo);
            }

            if (Err == 1) {
                return new Object[] {Polinomios, errores_absolutos};
            } else {
                return new Object[] {Polinomios, errores_relativos};
            }
        } else {
            return new Object[] {"El valor ingresado para los errores no corresponde a ninguno de los errores que se pueden solicitar"};
        }
    }

    private static double[][] solve(double[][] A, double[][] b) {
        int n = A.length;
        double[][] augmentedMatrix = new double[n][n + 1];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                augmentedMatrix[i][j] = A[i][j];
            }

            augmentedMatrix[i][n] = b[i][0];
        }

        for (int i = 0; i < n; i++) {
            double[] pivotRow = augmentedMatrix[i];
            int pivotIdx = i;
            double pivotValue = pivotRow[i];

            for (int j = i + 1; j < n; j++) {
                if (Math.abs(augmentedMatrix[j][i]) > Math.abs(pivotValue)) {
                    pivotRow = augmentedMatrix[j];
                    pivotIdx = j;
                    pivotValue = pivotRow[i];
                }
            }

            augmentedMatrix[pivotIdx] = augmentedMatrix[i];
            augmentedMatrix[i] = pivotRow;

            for (int j = i + 1; j < n; j++) {
                double[] currentRow = augmentedMatrix[j];
                double factor = currentRow[i] / pivotValue;

                for (int k = i; k < n + 1; k++) {
                    currentRow[k] -= factor * pivotRow[k];
                }
            }
        }

        double[][] x = new double[n][1];

        for (int i = n - 1; i >= 0; i--) {
            double sum = 0.0;

            for (int j = i + 1; j < n; j++) {
                sum += augmentedMatrix[i][j] * x[j][0];
            }

            x[i][0] = (augmentedMatrix[i][n] - sum) / augmentedMatrix[i][i];
        }

        return x;
    }

    private static double evaluarPolinomio(double[] coeficientes, double x) {
        double resultado = 0.0;

        for (int i = 0; i < coeficientes.length; i++) {
            resultado += coeficientes[i] * Math.pow(x, coeficientes.length - 1 - i);
        }

        return resultado;
    }
}
