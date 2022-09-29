# Aufgabe 1:
# Schreibe ein 3-Lagiges neuronales Netz, das 1-dimensionalen Input verarbeiten kann
# dazu gehören auch non-linearities damit wir keine lineare abbildung produzieren
# # Hier nochmal zur Mathematik:
# Wir nehmen an, dass wir ein 3-lagiges Netz haben d.h.:
#
# x -> x * w1 + b1 -> sig -> * w2 + b2 -> sig -> * w3 + b3 -> y
#
# Dann zur Berechnung:
# y_1 = x * w_1 + b_1     -> Ergebnis nach Layer 1
# z_1 = sigmoid(y_1)      -> Unsere Non-Linearity nach Layer 1
# y_2 = z_1 * w_2 + b_2   -> Ergebnis nach Layer 2
# z_2 = sigmoid(y_2)      -> Unsere Non-Linearity nach Layer 2
# y = z_2 * w_3 + b_3     -> Unser Output - Ergebnis nach Layer 3
# L = 1/2 * (Y - y)^2     -> Unser Loss / Fehler auf unsere Prediction y


# Ableitungen für die Gewichte:
# dL/dw_3  = dL/dy * dy/dw_3
# dL/dw_2 = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/dw_2
# dL/dw_1 = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/dz_1 * dz_1/dy_1 * dy_1/dw_1

# Ableitungen für die Biases:
# dL/b_3   = dL/dy * dy/db_3
# dL/b_2  = dL/dy * dy/dz_2 * dz_2/dy_2 * dy_2/db_2
# dL/b_1  = dL/dy *    dy/dz_2 *         dz_2/dy_2       * dy_2/z_1  *      dz_1/dy_1          * dy_1/db_1

# Ableitung sig:
# = sig(t) * (1 - sig(t))


# Und nun in Code umsetzen


# Aufgabe 2:
# Schreibe: Eine Klasse, die eine Liste von "Layern" (Anderen Klassen) entgegennimmt und es ermöglicht, beliebig große
# Netze zu erstellen (Diese Aufgabe ist sehr schwer)
# Tipp:


# typehints ändern und erweitern
import numpy as np


class Layer:
    def __init__(self, lr: float = .05) -> None:
        self.wm = np.array([])
        self.gradW = None
        self.prevX = None
        self.lr = lr

    def forward(self, *args, **kwargs) -> any:
        raise NotImplementedError

    def backward(self, *args, **kwargs) -> any:
        raise NotImplementedError

    def step(self) -> None:
        raise NotImplementedError


class LinearLayer(Layer):
    def __init__(self, insize, outsize) -> None:
        super(LinearLayer, self).__init__()
        self.wm = np.random.rand(insize, outsize)

    def forward(self, _x) -> np.ndarray:
        self.prevX = _x
        return _x @ self.wm

    def backward(self, grad: np.ndarray) -> np.ndarray:
        out_grad = 0  # berechnung
        self.gradW = 0  # berechnung
        return out_grad  # Berechnungen ausfüllen

    def step(self) -> None:
        self.wm -= self.lr * self.gradW


class Sigmoid(Layer):
    def __init__(self) -> None:
        super(Sigmoid, self).__init__()

    def forward(self, _x: np.ndarray) -> np.ndarray:
        self.prevX = _x
        return  # hier sigmoidfunktion implementieren

    def backward(self, _grad: np.ndarray) -> np.ndarray:
        return  # hier gradienten berechnen

    def step(self) -> None:
        pass


class Sequential:
    def __init__(self, layers: list[Layer], criterion) -> None:
        self.layers = layers
        self.criterion = criterion
        self.prev_out = None
        self.prev_in = None

    def forward(self, _x: np.ndarray) -> np.ndarray:
        self.prev_in = _x
        out = _x
        for _layer in self.layers:  # wir gehen über jeden Layer
            out = _layer.forward(out)
        self.prev_out = out
        return out

    def backward(self, _target: np.ndarray, _prediction: np.ndarray) -> None:
        grad = self.criterion.backward(_target, self.prev_out)
        for _layer in reversed(self.layers):  # wir gehen rückwärts über jeden Layer
            grad = _layer.backward(grad)

    def step(self) -> None:
        for _layer in self.layers:  # wir führen step() in jedem layer aus
            _layer.step()


class MSE:
    @staticmethod  # sagt uns dass diese Methode auch ohne Klassenobjekt funktioniert (ohne self)
    def forward(_target: np.ndarray, _prediction: np.ndarray) -> np.ndarray:
        return (1/_target.size) * (_target - _prediction)**2

    @staticmethod
    def backward(_target: np.ndarray, _prediction: np.ndarray) -> np.ndarray:
        return  # hier gradienten berechnen


model = Sequential([
    # hier passende Layer einfügen z.b. LinearLayer(2, y), Sigmoid()

])

# XOR funktion input
x = np.array([
        [[1, 1]],
        [[1, 0]],
        [[0, 1]],
        [[0, 0]]
])
# XOR funktion output
y = np.array([
    [[0]],
    [[1]],
    [[1]],
    [[0]]
])

local_losshist = []
global_losshist = []