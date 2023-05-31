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

    public static void main(String[] args) {
        DoubleUnaryOperator f = x -> Math.pow(x, 3) - 2 * x - 5;
        DoubleUnaryOperator df = x -> 3 * Math.pow(x, 2) - 2;
        DoubleUnaryOperator d2f = x -> 6 * x;
        double x0 = 2.0;
        double tol = 1e-6;
        int Nmax = 100;

        double x = raicesMultiples(f, df, d2f, x0, tol, Nmax);
        System.out.println("La raíz encontrada es x = " + x);
    }
}
