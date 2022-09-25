import numpy as np


x = np.arange(10)
print(x)  # das ist cool!

# aber es geht noch cooler!
y = x**2 + 3
print(y)  # wow! das ist QoL!; So können wir beliebige Funktionen konstruieren!
# was können wir noch?:
evenly_spaced = np.linspace(start=0, stop=100, num=50)
print(evenly_spaced)  # Zahlen in mehr oder weniger gleichmäßigem Abstand! cool!
# aber was geht noch?
random = np.random.random([4, 4])
print(random)  # Wow ob das nochmal nützlich wird?
print(random * random)  # elementwise-product
print(np.dot(random, random))  # unterschied zu matmul= wir dürfen zb skalare benutzen ansonsten unterschied nur ab 3D
print(random @ random)  # matrixprodukt
