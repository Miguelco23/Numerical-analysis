def regla_falsa(f, a, b, tol, max_iter=100):

    fa = f(a)
    fb = f(b)
    i = 0
    while abs(b-a) > tol and i < max_iter:
        try:
            c = (a*fb - b*fa)/(fb - fa)
            fc = f(c)
            if fa*fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            i += 1
        except ZeroDivisionError:
            print("Error: División por cero.")
            return None
    if abs(b-a) > tol:
        print("El método no converge después de %d iteraciones." % max_iter)
        return None
    return c

# F(x)
def f(x):
    return x**2 - 2

# intervalo y toleracia
a = 1
b = 2
tol = 1e-6

# raiz = regla_falsa(f, a, b, tol)
# print("La raíz de la función es:", raiz)
