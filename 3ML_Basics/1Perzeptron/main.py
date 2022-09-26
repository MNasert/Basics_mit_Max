import numpy as np
import matplotlib.pyplot as plt


class Perzeptron:
    def __init__(self, insize, outsize, lr=.1) -> None:  # lr ist ein modifikator für unseren gradienten
        self.wm = np.random.rand(insize, outsize)  # unsere weight - Matrix der Form [insize, outsize]
        self.prev_x = None
        self.grad = None
        self.prev_out = None

        self.insize = insize
        self.outsize = outsize
        self.lr = lr

    def forward(self, ipt: np.ndarray) -> np.ndarray:
        self.prev_x = ipt
        self.prev_out = ipt @ self.wm  # ipt * weight
        return self.prev_out  # [1, insize] x [insize, outsize] = [1, outsize]

    def backward(self, target: np.ndarray) -> None:
        # wir rechnen ja: y = x * wm
        # also brauchen wir eine Metrik, um den Fehler auszurechnen: wir nehmen den mittl. quad. fehler:
        # L = (1/ insize) * (target - prediction) ^ 2
        # = (1/ insize) * (target^2 - 2*target*prediction + prediction^2)
        # also rechnen wir:
        # dL/dprediction =  (1/insize) * (2*prediction - 2*target)
        # dann dprediction/dwm = x
        # also ist dL/dwm = dL/dprediction * dprediction/dwm = (1/insize) * x * (2*prediction - 2*target)
        # also
        self.grad = (1/self.insize) * self.prev_x * (self.prev_out - target)

    def step(self) -> None:
        # der gradient deutet in richtung maximum also rechnen wir - den gradienten:
        self.wm -= self.lr * self.grad.T  # wir müssen transponieren, da:
        # wm = [insize, outsize], grad aber = [outsize, insize]


# UND funktion - input
x = np.array([
        [[1, 1]],
        [[1, 0]],
        [[0, 1]],
        [[0, 0]]
])
# UND funktion output
y = np.array([
    [[1]],
    [[0]],
    [[0]],
    [[0]]
])

net = Perzeptron(2, 1, .1)  # wir erstellen eine Perzeptron instanz
print(f"net weights: {net.wm} \n")


def quad_loss(pred, targ) -> any:  # warum any? es kann eine zahl aber auch ein np.ndarray rauskommen -> wir könnten auch
    # sagen float or np.ndarray aber das ist nicht hübsch
    return (pred - targ)**2  # ziel - start, einfach der abstand


loss_history = []  # fehler pro instanz
global_loss = []  # fehler pro epoche

for epoch in range(20):
    for idx in range(len(x)):
        out = net.forward(x[idx])
        net.backward(y[idx])
        net.step()
        loss_history.append(quad_loss(out.squeeze(), y[idx].squeeze()))
    global_loss.append(sum(loss_history)/len(loss_history))
    loss_history = []

# und hier erstellen wir einen graphen, der erste parameter ist das x ( wir erstellen eine liste mit 0,1,2,3 ...)
# der zweite ist unsere losshistory


print(f"net weights: {net.wm} \n")
for _ in x:
    print(f"{_} -> net -> {net.forward(_)}")


plt.plot(np.arange(len(global_loss)), global_loss)
plt.xlabel("Epoche")
plt.ylabel("Fehler")
plt.show()

# 1 Aufgabe: Wie müssen wir die Ergebnisse deuten, um tatsächlich Vorhersagen machen zu können?
# 2 Aufgabe: Versuche das selbe mit der ODER, XOR und NAND Funktion
#           Welche davon funktionieren? welche nicht? warum?
#           Und wie müssen die Daten bei den jeweiligen Methoden gedeutet werden?
