import java.util.ArrayList;
import java.util.List;

public class Vandermonde {
    public static List<Double> vandermonde(List<Double> x, List<Double> y, int degree) {
        int n = x.size();
        if (y.size() != n) {
            throw new IllegalArgumentException("Las entradas deben tener la misma longitud");
        }

        // Crear la matriz de Vandermonde
        List<List<Double>> vanderMatrix = new ArrayList<>();

        for (int i = 0; i < n; i++) {
            List<Double> row = new ArrayList<>();
            for (int j = 0; j <= degree; j++) {
                row.add(Math.pow(x.get(i), j));
            }
            vanderMatrix.add(row);
        }

        // Resolver el sistema lineal
        List<Double> coefficients = Crout.crout(vanderMatrix, y);

        return coefficients;
    }
}
