# 布莱克曼窗（Blackman window）

import numpy as np
from matplotlib.pyplot import plot, show, legend
from matplotlib.dates import datestr2num
import sys

closes=np.loadtxt('AAPL.csv', delimiter=',', usecols=(6,),
                  converters={1:datestr2num}, unpack=True)
try:
    N = int(sys.argv[1])
except IndexError as e:
    N = 5
window = np.blackman(N)
smoothed = np.convolve(window/window.sum(), closes, mode='same')
plot(smoothed[N:-N], lw=2, label="smoothed")
plot(closes[N:-N], label="closes")
legend(loc='best')
show()
