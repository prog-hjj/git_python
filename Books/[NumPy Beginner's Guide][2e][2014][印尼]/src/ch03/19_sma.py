# 简单移动平均线（simple moving average）

import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

try:
    N = int(sys.argv[1])
except IndexError as e:
    N = 5

weights = np.ones(N) / N
print("Weights", weights)

c = np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
sma = np.convolve(weights, c)[N-1:-N+1]
t = np.arange(N - 1, len(c))
plot(t, c[N-1:], lw=1.0)
plot(t, sma, lw=2.0)
show()
