import numpy as np

ls = [1, 2, 3, 4, 5]  # Wir erstellen eine Liste mit ein paar zahlen

ls = np.array(ls)  # wir machen daraus einen anderen datentyp

print(type(ls))  # ist ein ndarray?

print(ls.dtype)  # ein ndarray aus int32ern!

# 2NumPy ist mit C optimiert und ermöglicht uns viel effektivere Möglichkeiten zu rechnen als wir mit
# Python allein könnten
# Wir können sehr viel rechen und speicherlast einsparen wenn wir numpy anstelle von listen u co benutzen
# außerdem hat numpy viele coole dinge die man machen kann
a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])

print(a + b)  # wow das funktioniert!
lsA = [1, 2, 3, 4]
lsB = [5, 6, 7, 8]
print(lsA + lsB)  # ? hat auch funktioniert aber nicht so wie wir es wollten

# das geht mit allen rechenoperationen; es geht sogar:
matA = [[1, 0],
        [0, 1]]
matA = np.array(matA)
matB = [[3, -1],
        [-4, 1]]
matB = np.array(matB)
print(matA * matB)  # unerwartet? das ist das elementweise-produkt!
print(np.matmul(matA, matB))  # matrixmultiplikation - alternativ zu matmul geht A @ B
