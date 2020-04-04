import numpy as np
from scipy import io

a = np.arange(7)

io.savemat("a.mat", {"array": a})

mat_dict = io.loadmat("a.mat")
print(mat_dict['array'])
