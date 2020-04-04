# 摩尔·彭罗斯广义逆矩阵（Moore-Penrose pseudoinverse）

import numpy as np

A = np.mat("4 11 14; 8 7 -2")
print("A\n", A)

pseudoinv = np.linalg.pinv(A)
print("Pseudo inverse\n", pseudoinv)

print("Check", A * pseudoinv)
