def secante(f, x0, x1, tol, max_iter, err):
    if err != 1 and err != 2:
        return "Invalid value for the Err parameter. It should be 1 (absolute error) or 2 (relative error)."

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
                return "The root of the function is: " + str(x1)
            if i > 0:
                if err == 1:
                    error = abs(fx1)
                    print("Iteration %d - Absolute Error: %f" % (i, error))
                elif err == 2:
                    error = abs((x1 - x0) / x1)
                    print("Iteration %d - Relative Error: %f" % (i, error))
            i += 1
        except ZeroDivisionError:
            return "Error: Division by zero."
    return "The method does not converge after %d iterations." % max_iter
