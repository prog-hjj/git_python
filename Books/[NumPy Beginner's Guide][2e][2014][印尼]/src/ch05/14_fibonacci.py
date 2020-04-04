import numpy as np

# 矩阵的连乘
F = np.matrix([[1, 1], [1, 0]])
print("F", F)
print("8th Fibonacci", (F ** 7)[0, 0])

# 黄金分割公式或通常所说的比奈公式（Binet’ s Formula）
n = np.arange(1, 9)
sqrt5 = np.sqrt(5)
phi = (1 + sqrt5)/2
fibonacci = np.rint((phi**n - (-1/phi)**n) / sqrt5)
print("Fibonacci", fibonacci)
