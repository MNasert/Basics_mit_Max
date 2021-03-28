import numpy as np
#nach dem schema a*x = b
#also im sinne der Matrixrechnung
#so lösen wir lineare Gleichungssysteme:
a = np.array([[1, 2],
              [3, 5]])
b = np.array([1, 2])
x = np.linalg.solve(a, b)#wobei x dann unsere matrix x=[x0 x1 x2(...)] ist (wenn wir sie transponieren)
print(x)
