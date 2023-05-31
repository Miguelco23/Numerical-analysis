import numpy as np


def spline(x,y):
    n = len(x)
    poli=[]
    internos=[]
    outer=[]
    crit3 = []
    coef_matrix = np.zeros(3*(n-1),3*(n-1))
    if len(y) != n:
        raise ValueError("Las entradas deben tener la misma longitud")

    #Calcular polinomios internos

    for i in range(2,n):
        internos.append([x[i-1]**2,x[i-1],y[i]])
        internos.append([x[i-1]**2,x[i-1],y[i]])

    #Calcular 2 polinomios externos
    outer.append([x[0]**2,x[0],y[0]],[x[n-1]**2,x[n-1],y[n-1]])

    for i in range(2,n):
        crit3.append([x[i-1]**2,x[i-1],y[i]])
        internos.append([x[i-1]**2,x[i-1],y[i]])
    




# Example usage:
x = [3, 4.5, 7, 9]
y = [2.5, 1, 2.5, 0.5]
# query_points = [1.5, 2.5, 4.5]

interpolated_values = spline(x, y)
print(interpolated_values)
