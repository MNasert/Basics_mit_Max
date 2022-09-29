# Lösung Teil 1:

# Wir haben hier nicht den Anspruch eine große Library zu schreiben, sondern mein erstes ML Projekt nachzuimplementieren
# Wir brauchen auch gar nicht viel dafür
# Ich optimiere das mal hier; wenn das unoptimiert gesehen werden will (was etwas verständlicher ist) dann habe ich
# hier den Github link zu dem projekt von vor 4 jahren (stand  2022)
# https://nbviewer.jupyter.org/github/MNasert/ML-projects/blob/master/Backprop.ipynb
# und nun ab zu jupyter! Das machen wir nicht hier! (auch wenn jupyter unelegant ist)


# Lösung Teil 2:
"""
###########                           WIP                      ###############################
"""
import numpy as np
import matplotlib.pyplot as plt


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
        out_grad = grad @ self.wm.T
        self.gradW = self.prevX.T @ grad
        return out_grad

    def step(self) -> None:
        self.wm += self.lr * self.gradW


class Sigmoid(Layer):
    def __init__(self) -> None:
        super(Sigmoid, self).__init__()

    def forward(self, _x) -> any:
        self.prevX = _x
        return 1 / (1 + np.exp(-_x))  # hier sigmoidfunktion implementieren

    def backward(self, _grad) -> np.ndarray:
        return self.forward(_grad) * (1 - self.forward(_grad))  # hier gradienten berechnen

    def step(self) -> None:
        pass


class Sequential:
    def __init__(self, layers: list[Layer], criterion) -> None:
        self.layers = layers
        self.criterion = criterion
        self.prev_out = None
        self.prev_in = None

    def forward(self, _x) -> any:
        self.prev_in = _x
        out = _x
        for _layer in self.layers:
            out = _layer.forward(out)
        self.prev_out = out
        return out

    def backward(self, _target, _prediction) -> None:
        grad = self.criterion.backward(_target, self.prev_out)
        for _layer in reversed(self.layers):
            grad = _layer.backward(grad)

    def step(self) -> None:
        for _layer in self.layers:
            _layer.step()


class MSE:
    @staticmethod
    def forward(_target, _prediction):
        return (1/_target.size) * (_target - _prediction)**2

    @staticmethod
    def backward(_target, _prediction):
        return 2*(_target - _prediction)/_target.size


model = Sequential([
    LinearLayer(2, 10),
    Sigmoid(),
    LinearLayer(10, 1)
], MSE())

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
tries = 3

while True:
    for index in range(len(x)):
        output = model.forward(x[index])
        model.backward(y[index], output)
        model.step()
        local_losshist.append(model.criterion.forward(y[index], output).item())
    global_losshist.append(sum(local_losshist))
    if len(global_losshist) > 1:
        if global_losshist[-2] < global_losshist[-1]:
            tries -= 1
            if tries <= 0:
                break

    local_losshist = []

for idx in range(len(x)):
    output = model.forward(x[idx])
    print(f"X ->{x[idx]} -> Target: {y[idx]} vs prediction:{output}")

plt.plot([x for x in range(len(global_losshist))], global_losshist)
plt.xlabel("Epochen")
plt.ylabel("Fehler")
plt.show()
