def regla_falsa(f, a, b, tol, max_iter):
    i = 0
    try:
        fa = eval(f.replace('x', 'a'))
        fb = eval(f.replace('x', 'b'))
        while abs(b - a) > tol and i < max_iter:
            c = (a * fb - b * fa) / (fb - fa)
            fc = eval(f.replace('x', 'c'))
            if fa * fc < 0:
                b = c
                fb = fc
            else:
                a = c
                fa = fc
            i += 1
        if abs(b - a) > tol:
            print("The method does not converge after %d iterations." % max_iter)
            return None
        return "The root of the function is:" + str(c)
    except ZeroDivisionError:
        print("Error: Division by zero.")
        return None



# # intervalo y toleracia
# f = "x**2 -2"
# a = 1
# b = 2
# tol = 1e-6
# max_iter = 100

# raiz = regla_falsa(f, a, b, tol, max_iter)
# print(raiz)
