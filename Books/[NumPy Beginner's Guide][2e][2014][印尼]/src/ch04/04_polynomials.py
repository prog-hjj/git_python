import numpy as np
import sys
from matplotlib.pyplot import plot
from matplotlib.pyplot import show

bhp=np.loadtxt('BHP.csv', delimiter=',', usecols=(6,), unpack=True)
vale=np.loadtxt('VALE.csv', delimiter＝',', usecols=(6,), unpack=True)

try:
    N = int(sys.argv[1])
except IndexError as e:
    N = 3

t = np.arange(len(bhp))
poly = np.polyfit(t, bhp - vale, N)
print("Polynomial fit", poly)

print("Next value", np.polyval(poly, t[-1] + 1))

print("Roots", np.roots(poly))

der = np.polyder(poly)
print("Derivative", der)

print("Extremas", np.roots(der))
vals = np.polyval(poly, t)
print(np.argmax(vals))
print(np.argmin(vals))

plot(t, bhp - vale)
plot(t, vals)
show()
