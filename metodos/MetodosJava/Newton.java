import java.util.function.DoubleUnaryOperator;

public class Newton {
    public static double newton(DoubleUnaryOperator f, DoubleUnaryOperator derf, double x0, double tol, int Nmax) {
        double xant = x0;
        double fant = f.applyAsDouble(xant);
        double E = 1000;
        int cont = 0;

        while (E > tol && cont < Nmax) {
            double xact = xant - fant / derf.applyAsDouble(xant);
            double fact = f.applyAsDouble(xact);
            E = Math.abs(xact - xant);
            cont++;
            xant = xact;
            fant = fact;
            if (E < tol) {
                return xact;
            }
        }

        throw new RuntimeException("No se encontró una raíz en el rango especificado.");
    }
}
