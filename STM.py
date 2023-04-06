import numpy as np
from scipy.linalg import eigh_tridiagonal
import matplotlib.pyplot as plt

la = -100
lb = 100
h = 0.1
n = (lb - la) / h

X = np.arange(la, lb, h)


def pot(X):
    dv = []
    for i in X:
        if i <= -25 or i >= 25:
            v = 0
        else:
            v = 0.05
        dv.append(v)
    return np.array(dv)


V = pot(X)

mat_len = len(X) - 1

d = 2 + (2 * h * h * V[1:-1])
e = np.ones(len(d)-1) * -0.5

                
w, v = eigh_tridiagonal(d, e)

plt.plot(X[1:-1],v.T[20])
plt.plot(X,V)
plt.show()
# plt.savefig("Tunneling STM 2")
