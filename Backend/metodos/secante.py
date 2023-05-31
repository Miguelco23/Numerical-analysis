def secante(f, x0, x1, tol, max_iter):
    i = 0
    while i < max_iter:
        try:
            fx0 = eval(f.replace('x', str(x0)))
            fx1 = eval(f.replace('x', str(x1)))
            dx = (x1 - x0) / (fx1 - fx0)
            x0 = x1
            fx0 = fx1
            x1 = x1 - fx1 * dx
            fx1 = eval(f.replace('x', str(x1)))
            if abs(fx1) <= tol:
                return("The root of the function is: "+ str(x1))
            i += 1
        except ZeroDivisionError:
            return("Error: Division by zero.")
    return("The method does not converge after %d iterations." % max_iter)


# intervalo y toleracia
# f = "x**2 - 2"
# x0 = 1
# x1 = 2
# tol = 1e-6
# max_iter = 5

# raiz = secante(f, x0, x1, tol, max_iter)
# print(raiz)

