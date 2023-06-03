def bisection(f, a, b, tol, Err):
    # Evaluate the string as a function
    def evaluate_function(x):
        return eval(f)

    if evaluate_function(a) * evaluate_function(b) >= 0:
        print("Error: The function does not change sign in the given interval.")
        return None
    elif Err == 1:
        error_function = lambda c: abs(evaluate_function(c))
    elif Err == 2:
        error_function = lambda c: abs((b - a) / c)
    else:
        print("Invalid value for the Err parameter. It should be 1 (absolute error) or 2 (relative error).")
        return None

    c = (a + b) / 2
    error = error_function(c)
    while error > tol:
        if evaluate_function(a) * evaluate_function(c) < 0:
            b = c
        else:
            a = c
        c = (a + b) / 2
        error = error_function(c)

    return c, error
