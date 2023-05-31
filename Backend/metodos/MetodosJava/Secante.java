import java.util.function.Function;

public class Secante {
    public static String secante(Function<Double, Double> f, double x0, double x1, double tol, int maxIter) {
        int iter = 0;
        double fx0 = f.apply(x0);
        double fx1 = f.apply(x1);

        while (iter < maxIter) {
            try {
                double dx = (x1 - x0) / (fx1 - fx0);
                x0 = x1;
                fx0 = fx1;
                x1 = x1 - fx1 * dx;
                fx1 = f.apply(x1);

                if (Math.abs(fx1) <= tol) {
                    return "La raíz de la función es: " + x1;
                }

                iter++;
            } catch (ArithmeticException e) {
                return "Error: División por cero.";
            }
        }

        return "El método no converge después de " + maxIter + " iteraciones.";
    }
}
