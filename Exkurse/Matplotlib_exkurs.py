import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(start=-12, stop=12, num=500)#wir erstellen einen Linspace
y = -.15*x**4 + 16*x**2#wir machen uns eine schöne Funktion

plt.plot(x, y)#wir "plotten" wir übergeben die x und y parameter in reihenfolge- sie _müssen_ gleich groß sein (size)
plt.xlabel("x")#wir sagen unter der x-achse steht x
plt.ylabel("y")#...
plt.grid(True)#und wir lassen uns ein gitter anzeigen
plt.show()#und das ganze auf den bildschirm werfen!
#das brauchen wir für den ML teil!