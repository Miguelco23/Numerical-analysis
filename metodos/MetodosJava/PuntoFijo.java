import java.util.function.Function;

public class PuntoFijo {
    public static void puntoFijo(Function<Double, Double> f, Function<Double, Double> g, double x0, double tol, int nmax) {
        int iter = 0;
        double err = 9999;
        double xant = x0;

        while (err > tol && iter < nmax) {
            double xact = g.apply(xant);
            err = Math.abs(xant - xact);
            System.out.println(err);
            iter++;
            xant = xact;
        }

        System.out.println("x = " + xant);
        System.out.println("iters = " + iter);
        System.out.println("Error = " + err);
    }
}
