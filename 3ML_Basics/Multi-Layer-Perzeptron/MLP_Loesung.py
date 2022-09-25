# Lösung Teil 1:

# Wir haben hier nicht den Anspruch eine große Library zu schreiben, sondern mein erstes ML Projekt nachzuimplementieren
# Wir brauchen auch gar nicht viel dafür
# Ich optimiere das mal hier; wenn das unoptimiert gesehen werden will (was etwas verständlicher ist) dann habe ich
# hier den Github link zu dem projekt von vor 4 jahren (stand  2022)
# https://nbviewer.jupyter.org/github/MNasert/ML-projects/blob/master/Backprop.ipynb
# und nun ab zu jupyter! Das machen wir nicht hier! (auch wenn jupyter unelegant ist)


# Lösung Teil 2:
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
