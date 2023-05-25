def secante(f, x0, x1, tol, max_iter=100):
    fx0 = f(x0)
    fx1 = f(x1)
    i = 0
    while abs(fx1) > tol and i < max_iter:
        try:
            dx = (x1 - x0)/(fx1 - fx0)
            x0 = x1
            fx0 = fx1
            x1 = x1 - fx1*dx
            fx1 = f(x1)
            i += 1
        except ZeroDivisionError:
            print("Error: División por cero.")
            return None
    if abs(fx1) > tol:
        print("El método no converge después de %d iteraciones." % max_iter)
        return None
    return x1

# F(x)
def f(x):
    return x**2 - 2

# intervalo y toleracia
x0 = 1
x1 = 2
tol = 1e-6

raiz = secante(f, x0, x1, tol)
print("La raíz de la función es:", raiz)

