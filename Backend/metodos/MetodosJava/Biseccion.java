import java.util.function.Function;

public class Biseccion {
    public static double biseccion(Function<Double, Double> f, double a, double b, double tol) {
        if (f.apply(a) * f.apply(b) >= 0) {
            System.out.println("Error: La función no cambia de signo en el intervalo dado.");
            return Double.NaN;
        } else {
            double c = (a + b) / 2;
            while (Math.abs(f.apply(c)) > tol) {
                if (f.apply(a) * f.apply(c) < 0) {
                    b = c;
                } else {
                    a = c;
                }
                c = (a + b) / 2;
            }
            return c;
        }
    }
}
