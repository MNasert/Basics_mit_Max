import numpy as np
import matplotlib.pyplot as plt

class Perzeptron:
    def __init__(self, insize, outsize, lr):
        super(Perzeptron, self).__init__()
        self.wm = np.random.rand(insize, outsize)#dann müssen wir seltener transponieren
        self.in_prev = None
        self.out_prev = None
        self.lr = lr
        self.grd = None
    def forward(self, x):
        self.in_prev = x
        #x hat den shape [1,insize] wm hat den shape [outsize, insize]
        x = x.T @ self.wm# 1,insize * insize, outsize
        self.out_prev = x
        return x

    def backward(self, target):
        #wir benutzen nach newton das gradientenverfahren um das lokale minimum zu erreichen
        #wir haben als funktion:
        #y = w * x
        #der fehler ist L = 1/2(Y-y)^2 (wir nehmen einfach den mittl. quad fehler)
        #also ist L = (Y-(w * x))^2
        #wir müssen also partiell nach w ableiten
        #fangen wir mal an:
        #wir wollen dL/dw = dL/dy * dy/dw: alsoooo:
        #dL/dy = 1/2(Y^2 - 2Yy +y^2)'
        #      = 1/2(0 - 2Y +2y)
        #      = y-Y
        #dy/dw = x
        #damit ist dL/dw = x*(y-Y)
        self.grd = self.in_prev * (self.out_prev - target)

    def step(self):
        self.wm = self.wm - self.lr*self.grd
        #Da ein Gradient immer auf das MAXIMUM deutet, müssen wir den Gradienten von unserem Gewicht abziehen

x = np.array([[[1], [1]],[[1], [0]],[[0], [1]], [[0],[0]]])#Dummy data
y = np.array([[1], [0], [0], [0]])#dummy target
losses = []
ls = 0
perz = Perzeptron(2, 1, lr=.1)#dummy net
for epoch in range(10):#wie viele Epochen rechnen wir?
    for i in range(len(x)):#wir iterieren über alle elemente in der dummy data
        n = perz.forward(x[i])#forward
        loss = .5*(y[i]-n)**2#was ist unser loss? (hier erstmal irrelevant- wird in späteren projekten wichtig
        perz.backward(y[i])#backward
        perz.step()#update der parameter
        ls += loss# wir rechnen erstmal den ganzen loss zusammen
    losses.append(ls.squeeze()/len(x))#dann gucken wir wie groß der mittlere fehler auf den daten ist und merken uns das
    ls = 0# dann mal den laufparameter auf null setzen

plt.plot(np.arange(len(losses)), losses)#wir plotten alle losses
plt.xlabel("epochs")#xlabel
plt.ylabel("loss")#ylabel
plt.show()#anzeigen