def biseccion(f, a, b, tol):

    # Evaluar la cadena de texto como una función
    def evaluar_funcion(x):
        return eval(f)

    if evaluar_funcion(a) * evaluar_funcion(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        return None
    else:
        c = (a + b) / 2
        while abs(evaluar_funcion(c)) > tol:
            if evaluar_funcion(a) * evaluar_funcion(c) < 0:
                b = c
            else:
                a = c
            c = (a + b) / 2
        return c

# Cadena de texto que representa la función
f = "x**2 - 2"

# Intervalo y tolerancia
a = 0
b = 2
tol = 1e-6

# raiz = biseccion(f, a, b, tol)
# print("La raíz de la función es:", raiz)