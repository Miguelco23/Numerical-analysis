import java.util.function.Function;

public class ReglaFalsa {
    public static String reglaFalsa(Function<Double, Double> f, double a, double b, double tol, int maxIter) {
        int iter = 0;
        double fa = f.apply(a);
        double fb = f.apply(b);

        while (Math.abs(b - a) > tol && iter < maxIter) {
            double c = (a * fb - b * fa) / (fb - fa);
            double fc = f.apply(c);

            if (fa * fc < 0) {
                b = c;
                fb = fc;
            } else {
                a = c;
                fa = fc;
            }

            iter++;
        }

        if (Math.abs(b - a) > tol) {
            return "El método no converge después de " + maxIter + " iteraciones.";
        } else {
            return "La raíz de la función es: " + c;
        }
    }
}
