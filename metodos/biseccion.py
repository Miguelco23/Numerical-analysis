def biseccion(f, a, b, tol):

    if f(a)*f(b) >= 0:
        print("Error: La función no cambia de signo en el intervalo dado.")
        return None
    else:
        c = (a+b)/2
        while abs(f(c)) > tol:
            if f(a)*f(c) < 0:
                b = c
            else:
                a = c
            c = (a+b)/2
        return c

# F(x)
def f(x):
    return x**2 - 2

# intervalo y toleracia
a = 0
b = 2
tol = 1e-6

raiz = biseccion(f, a, b, tol)
print("La raíz de la función es:", raiz)
