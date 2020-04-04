import numpy as np
from matplotlib.pyplot import plot
from matplotlib.pyplot import show
import sys

try:
    N = float(sys.argv[1])
except IndexError as e:
    N = 100.0

t = np.linspace(-np.pi, np.pi, 201)
k = np.arange(1, N)
k = 2 * k - 1
f = np.zeros_like(t)

for i in range(len(t)):
    f[i] = np.sum(np.sin(k * t[i]) / k)

f = (4 / np.pi) * f
plot(t, f)
show()
