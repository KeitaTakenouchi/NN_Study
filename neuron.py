import numpy as np
import matplotlib.pyplot as plt


def sigmoid(x):
    return 1 / (1 + np.exp(-x))


X = np.arange(-1.0, 1.0, 0.2)
Y = np.arange(-1.0, 1.0, 0.2)
Z = np.zeros([10, 10])

w_x = -3
w_y = 3
bias = 0.1

for i in range(10):
    for j in range(10):
        y = sigmoid(X[i] * w_x + Y[j] * w_y + bias)
        Z[i][j] = y

plt.imshow(Z)
plt.colorbar()
plt.show()
