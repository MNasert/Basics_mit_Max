# Aufgabe 1:
# Schreibe ein 3-Lagiges neuronales Netz, das 1-dimensionalen Input verarbeiten kann
# dazu gehören auch non-linearities damit wir keine lineare abbildung produzieren
# # Hier nochmal zur Mathematik:
# Wir nehmen an, dass wir ein 3-lagiges Netz haben d.h.:
#
# x -> x * w1 + b1 -> sig -> * w2 + b2 -> sig -> * w3 + b3 -> y
#
# Dann zur Berechnung:
# L = 1/2(Y-y)^2  -> Unser Loss
# y_1 = w_1 * z_2 + b -> Ergebnis nach Layer 1
# z_1 = sigmoid(y_1)  -> Unsere Non-Linearity nach Layer 1
# y_2 = w_2 * z_1 + b_2 -> Ergebnis nach Layer 2
# z_2 = sigmoid(y_2) -> Unsere Non-Linearity nach Layer 2
# y = w_3 * z_2 + b_3 -> Unser Output - Ergebnis nach Layer 3


# Ableitungen für die Gewichte:
# dL/dw_3  = dL/dy * dy/dw_3
# dL/dw_2 = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/dw_2
# dL/dw_1 = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/dz_1 * dz_1/dy_1 * dy_1/dw_1

# Ableitungen für die Biases:
# dL/b_3   = dL/dy * dy/db_3
# dL/b_2  = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/db_2
# dL/b_1  = dL/dy *    dy/dz_2 *         dz_2/dy_2       * dy_2/z_1  *      dz_1/dy_1          * dy_1/db_1

# Und nun in Code umsetzen


# Aufgabe 2:
# Schreibe: Eine Klasse, die eine Liste von "Layern" (Anderen Klassen) entgegennimmt und es ermöglicht, beliebig große
# Netze zu erstellen (Diese Aufgabe ist sehr schwer)
# Tipp:


# typehints ändern und erweitern
import numpy as np


class Layer:
    def __init__(self) -> None:
        self.wm = None
        self.bm = None
        self.gradW = None
        self.gradB = None
        self.prevX = None

    def forward(self, x) -> any:
        raise NotImplementedError

    def backward(self, grad) -> any:
        raise NotImplementedError

    def step(self) -> None:
        raise NotImplementedError


class LinearLayer(Layer):
    def __init__(self, insize, outsize) -> None:
        super(LinearLayer, self).__init__()
        self.wm = np.random.rand(insize, outsize)
        self.bm = np.random.rand(1, outsize)

    def forward(self, x) -> np.ndarray:
        self.prevX = x
        return x @ self.wm + self.bm

    def backward(self, grad) -> tuple[any, any]:
        self.gradW = None  # hier Berechnung
        self.gradB = None  # hier Berechnung
        return self.gradW, self.gradB

    def step(self) -> None:
        self.wm -= self.gradW
        self.bm -= self.gradB


class Sigmoid(Layer):
    def __init__(self) -> None:
        super(Sigmoid, self).__init__()
        pass

    def forward(self, x) -> any:
        self.prevX = x
        return 0  # hier sigmoidfunktion implementieren

    def backward(self, grad) -> tuple[any, any]:
        return 0, 0  # hier gradienten berechnen

    def step(self) -> None:
        pass


class Sequential:
    def __init__(self, layers: list[Layer]) -> None:
        self.layers = layers
        self.prev_out = None
        self.prev_in = None

    def forward(self, x) -> any:
        out = x
        for layer in self.layers:
            out = layer.forward(x)
        return out

    def backward(self, target) -> None:
        for layer in reversed(self.layers):
            target = layer.backward(target)

    def step(self) -> None:
        for layer in self.layers:
            layer.step()
