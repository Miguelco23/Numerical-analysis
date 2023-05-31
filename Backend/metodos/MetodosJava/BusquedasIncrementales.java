import java.util.function.Function;

public class BusquedaIncremental {
    public static String busquedaIncremental(Function<Double, Double> f, double x0, double h, int nmax) {
        double xant = x0;
        double fant = f.apply(xant);
        double xact = xant + h;
        double fact = f.apply(xact);
        for (int i = 0; i < nmax; i++) {
            System.out.printf("%f %f%n", fant, fact);
            if (fant * fact < 0) {
                double limiteInferior = xant;
                double limiteSuperior = xact;
                int iteraciones = i;
                return String.format("Raiz esta entre %f y %f. Salida con %d iteraciones", limiteInferior, limiteSuperior, iteraciones);
            }
            xant = xact;
            fant = fact;
            xact = xant + h;
            fact = f.apply(xact);
        }
        return "No se encontró raíz en el intervalo dado.";
    }
}
