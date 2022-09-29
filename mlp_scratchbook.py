import random
import math
import matplotlib.pyplot as plt

# Ableitungen für die Gewichte:
# dL/dw_3 = (y - Y) * z_2
# dL/dw_2 = (y - Y) * w_3 + sig(y_2) * (1 - sig(y_2)) * z_1
# dL/dw_1 = (y - Y) * w_3 + sig(y_2) * (1 - sig(y_2)) * w_2 * sig(y_1) * (1 - sig(y_1)) * x

# Ableitungen für die Biases:
# dL/b_3  = (y - Y)
# dL/b_2  = (y - Y) * w_3 + sig(y_2) * (1 - sig(y_2)) * 1
# dL/b_1  = (y - Y) * w_3 + sig(y_2) * (1 - sig(y_2)) * w_2 * sig(y_1) * (1 - sig(y_1)) * 1

w_1 = random.random()
w_2 = random.random()
w_3 = random.random()

b_1 = random.random()
b_2 = random.random()
b_3 = random.random()

E = math.exp(1)


# forwardpass
def layer(x: float, w: float, b: float) -> float:
    return (x * w) + b


def sigmoid(ipt: float) -> float:
    return 1/(1 + math.exp(-ipt))


# backward - ableitungen
def derivative_sig(ipt: float) -> float:
    return sigmoid(ipt) * (1 - sigmoid(ipt))


def derivative_loss(y_target: float, var_y: float) -> float:
    return var_y - y_target


def derivative_w_3(y_target: float, var_y: float, var_z_2: float) -> float:
    return derivative_loss(y_target, var_y) * var_z_2


def derivative_b_3(y_target: float, var_y: float) -> float:
    return derivative_loss(y_target, var_y)


def derivative_w_2(y_target: float, var_y: float, var_w_3: float, var_y_2: float, var_z_1: float) -> float:
    return derivative_loss(y_target, var_y) * var_w_3 + derivative_sig(var_y_2) * var_z_1


def derivative_b_2(y_target: float, var_y: float, var_w_3: float, var_y_2:float) -> float:
    return derivative_loss(y_target, var_y) * var_w_3 + derivative_sig(var_y_2)


def derivative_w_1(y_target: float, var_y: float, var_w_3: float,
                   var_y_2: float, var_w_2: float, var_y_1: float, x: float) -> float:
    return derivative_loss(y_target, var_y) * var_w_3 + derivative_sig(var_y_2) * var_w_2 * derivative_sig(var_y_1) * x


def derivative_b_1(y_target: float, var_y: float, var_w_3: float,
                   var_y_2: float, var_w_2: float, var_y_1: float) -> float:
    return derivative_loss(y_target, var_y) * var_w_3 + derivative_sig(var_y_2) * var_w_2 * derivative_sig(var_y_1)


# utilities
def f(_: float) -> float:
    return sigmoid(3 * sigmoid(2 * sigmoid(_)))


def loss(target_value: float, prediction: float) -> float:
    return .5 * (target_value - prediction) ** 2


def forwardpass(ipt: float, var_w_1: float, var_w_2: float, var_w_3: float, var_b_1: float,
                var_b_2: float, var_b_3: float) -> list[float]:
    var_y_1 = layer(ipt, var_w_1, var_b_1)
    var_z_1 = sigmoid(var_y_1)
    var_y_2 = layer(var_z_1, var_w_2, var_b_2)
    var_z_2 = sigmoid(var_y_2)
    var_y = layer(var_z_2, var_w_3, var_b_3)
    return [var_y, var_z_2, var_z_1, var_y_2, var_y_1]


def backwardpass(var_y_target: float, var_y: float, var_z_2: float, var_z_1: float, var_y_2: float, var_y_1: float,
                 var_w_3: float, var_w_2: float, ipt: float) -> list[float]:
    var_grad_w_3 = derivative_w_3(var_y_target, var_y, var_z_2)
    var_grad_b_3 = derivative_b_3(var_y_target, var_y)
    var_grad_w_2 = derivative_w_2(var_y_target, var_y, var_w_3, var_y_2, var_z_1)
    var_grad_b_2 = derivative_b_2(var_y_target, var_y, var_w_3, var_y_2)
    var_grad_w_1 = derivative_w_1(var_y_target, var_y, var_w_3, var_y_2, var_w_2, var_y_1, ipt)
    var_grad_b_1 = derivative_b_1(var_y_target, var_y, var_w_3, var_y_2, var_w_2, var_y_1)
    return [var_grad_w_3, var_grad_w_2, var_grad_w_1, var_grad_b_3, var_grad_b_2, var_grad_b_1]


# mainloop
X_data = [x - 5 for x in range(10)]  # X-Werte
Y_data = [f(x) for x in X_data]  # Y-Werte
outputs = []
lr = 1
local_losshistory = []
global_losshistory = []


for epoch in range(10):
    for i in range(len(X_data)):
        y, z_2, z_1, y_2, y_1 = forwardpass(X_data[i], w_1, w_2, w_3, b_1, b_2, b_3)
        grad_w_3, grad_w_2, grad_w_1, grad_b_3, grad_b_2, grad_b_1 = backwardpass(Y_data[i], y, z_2, z_1, y_2, y_1,
                                                                                  w_3, w_2, X_data[i])

        instance_loss = loss(Y_data[i], y)
        local_losshistory.append(instance_loss)
        w_3 = w_3 - lr * grad_w_3
        w_2 = w_2 - lr * grad_w_2
        w_1 = w_1 - lr * grad_w_1
        b_3 = b_3 - lr * grad_b_3
        b_2 = b_2 - lr * grad_b_2
        b_1 = b_1 - lr * grad_b_1
    global_losshistory.append(sum(local_losshistory))
    local_losshistory = []

for i in range(len(X_data)):
    y, z_2, z_1, y_2, y_1 = forwardpass(X_data[i], w_1, w_2, w_3, b_1, b_2, b_3)
    grad_w_3, grad_w_2, grad_w_1, grad_b_3, grad_b_2, grad_b_1 = backwardpass(Y_data[i], y, z_2, z_1, y_2, y_1,
                                                                                  w_3, w_2, X_data[i])
    outputs.append(y)

plt.plot([x+1 for x in range(len(X_data))], [y for y in Y_data], label="Ziel")
plt.plot([x+1 for x in range(len(X_data))], [outputs[x] for x in range(len(X_data))], label="Vorhersage")
plt.legend()
plt.xlabel("X")
plt.ylabel("Y")

for i in range(len(X_data)):
    print(f"x: {X_data[i]}")
    print(f"y: {Y_data[i]}")
    print(f"prediction: {outputs[i]}")

plt.show()
