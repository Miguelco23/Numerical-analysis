import java.util.function.DoubleUnaryOperator;

public class RaicesMultiples {
    public static double raicesMultiples(DoubleUnaryOperator f, DoubleUnaryOperator df, DoubleUnaryOperator d2f,
                                         double x0, double tol, int Nmax) {
        double xant = x0;
        double fant = f.applyAsDouble(xant);
        double E = 1000;
        int cont = 0;

        while (E > tol && cont < Nmax) {
            double xact = xant - (fant * df.applyAsDouble(xant)) / (Math.pow(df.applyAsDouble(xant), 2)
                    - fant * d2f.applyAsDouble(xant));
            double fact = f.applyAsDouble(xact);
            E = Math.abs(xact - xant);
            cont++;
            xant = xact;
            fant = fact;
        }

        return xact;
    }
}
