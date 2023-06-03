def RaicesMultiples(f, df, d2f, x0, tol, Nmax, Err):
    # Inicialización
    xant = x0
    fant = f(xant)
    E = 1000
    cont = 0
    errores = []  # Lista para almacenar los errores
    
    # Ciclo
    while E > tol and cont < Nmax:
        xact = xant - (fant * df(xant)) / ((df(xant)) ** 2 - fant * d2f(xant))
        fact = f(xact)
        E = abs(xact - xant)
        cont = cont + 1
        xant = xact
        fant = fact
        errores.append(E)  # Agregar el error a la lista
        
    # Entrega de resultados
    x = xact
    iteraciones = cont
    
    if Err == 1:  # Error absoluto
        return {"x": x, "Iter": iteraciones, "Errores": errores}
    elif Err == 2:  # Error relativo
        errores_relativos = [e / abs(x) for e in errores]  # Calcular errores relativos
        return {"x": x, "Iter": iteraciones, "Errores": errores_relativos}
    else:
        return "Invalid value for the 'Err' parameter. Please use 1 for relative error or 2 for absolute error."
