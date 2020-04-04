# 终值

import numpy as np
from matplotlib.pyplot import plot, show

# 利率3%、每季度支付金额10、存款周期5年以及现值1000
print("Future value", np.fv(0.03/4, 5 * 4, -10, -1000))

fvals = []

# for i in xrange(1, 10):
for i in range(1, 10):
    fvals.append(np.fv(.03/4, i * 4, -10, -1000))

plot(fvals, 'bo')
show()


# 现值（present value）
print("Present value", np.pv(0.03/4, 5 * 4, -10, 1376.09633204))
