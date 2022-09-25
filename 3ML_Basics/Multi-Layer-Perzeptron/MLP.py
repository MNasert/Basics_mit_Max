# Aufgabe 1:
# Schreibe ein 3-Lagiges neuronales Netz, das 1-dimensionalen Input verarbeiten kann
# dazu gehören auch non-linearities damit wir keine lineare abbildung produzieren
# # Hier nochmal zur Mathematik:
# Wir nehmen an, dass wir ein 3-lagiges Netz haben d.h.:
#
# x -> x*w1 + b1 -> *w2 + b2 -> *w3 + b3 -> y
#
# Dann zur Berechnung:
# L = 1/2(Y-y)^2 #dL/dy = (Y-y)
# y = w*z_2 + b #dy/dz_2 = w
# z1 = sigmoid(y_1) # dz1/dy-1 = sigmoid(y_1) * (1-sigmoid(y_1)
# y1 = w_2*z_1 + b_2# dy1/dz1=w2
# z2 = sigmoid(y_2)#dz2/dy_2 = sigmoid(y_2) * (1-sigmoid(y_2)
# y2 = w_3*x + b_3#dy2/w_3 = x

# dL/dw  = dL/dy * dy/dw
# dL/dw2 = dL/dy * dy/dz_1 * dz_2/dy_1 * dy_1/dw_2
# dL/dw3 = dL/dy * dy/dz_1 * dz_2/dy_1 * dy_1/dz_2 * dz_2/dy_2 * dy_2/dw_3
# dL/b   = dL/dy * dy/db
# dL/b2  = dL/dy * dy/dz_1 * dz_2/dy_1 * dy_1/db_2
# dL/b3  = dL/dy *    dy/dz_1 *         dz_1/dy_1       * dy_1/z_2  *      dz_2/dy_2          * dy_2/db_3
#       =  Y-y  *       w    *    sg(y_1)(1-sg(y_1))   *    w_2    *  sg(y_2)(1-sg(y_2))
# Und nun in Code umsetzen

# Aufgabe 2:
# Schreibe: Eine Klasse, die eine Liste von "Layern" (Anderen Klassen) entgegennimmt und es ermöglicht, beliebig große
# Netze zu erstellen (Diese Aufgabe ist sehr schwer)
# Tipp:


# typehints ändern und erweitern
import numpy as np


class Layer:
    def __init__(self):
        self.wm = None
        self.bm = None
        self.gradW = None
        self.gradB = None

    def forward(self, x):
        raise NotImplementedError

    def backward(self, grad):
        raise NotImplementedError

    def step(self):
        raise NotImplementedError


class LinearLayer(Layer):
    def __init__(self, insize, outsize):
        super(LinearLayer, self).__init__()
        self.wm = np.random.rand(insize, outsize)
        self.bm = np.random.rand(1, outsize)

    def forward(self, x) -> np.ndarray:
        return x @ self.wm + self.bm

    def backward(self, grad) -> tuple[any, any]:
        self.gradW = None  # hier Berechnung
        self.gradB = None  # hier Berechnung
        return self.gradW, self.gradB

    def step(self):
        self.wm -= self.gradW
        self.bm -= self.gradB


class Sigmoid(Layer):
    def __init__(self):
        super(Sigmoid, self).__init__()
        pass

    def forward(self, x) -> any:
        return 0  # hier sigmoidfunktion implementieren

    def backward(self, grad) -> tuple[any, any]:
        return 0, 0  # hier gradienten berechnen

    def step(self):
        pass


class Sequential:
    def __init__(self, layers: list[Layer]):
        self.layers = layers
        self.prev_out = None
        self.prev_in = None

    def forward(self, x):
        out = x
        for layer in self.layers:
            out = layer.forward(x)
        return out

    def backward(self, target):
        for layer in reversed(self.layers):
            target = layer.backward(target)

    def step(self):
        for layer in self.layers:
            layer.step()


