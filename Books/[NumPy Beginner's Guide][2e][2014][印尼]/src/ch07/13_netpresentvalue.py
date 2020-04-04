# 净现值（net present value）

import numpy as np

cashflows = np.random.randint(100, size=5)
cashflows = np.insert(cashflows, 0, -100)
print("Cashflows", cashflows)

# 利率3%
print("Net present value", np.npv(0.03, cashflows))
