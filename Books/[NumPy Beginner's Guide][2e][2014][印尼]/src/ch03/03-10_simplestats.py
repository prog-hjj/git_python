import numpy as np

c,v=np.loadtxt('data.csv', delimiter=',', usecols=(6,7), unpack=True)
print(f'c = {c!r}, v = {v!r}')

# Volume-Weighted Average Price，成交量加权平均价格
vwap = np.average(c, weights=v)
print(f'VWAP = {vwap}')

print(f'mean = {np.mean(c)}')

# Time-Weighted Average Price，时间加权平均价格
t = np.arange(c.size)
t += 1  # avoid ZeroDivisionError when c.size==1
cc = np.array([c]) if c.size == 1 else c
twap = np.average(cc, weights=t)
print(f'TWAP = {twap}')

h,l=np.loadtxt('data.csv',delimiter=',', usecols=(4,5), unpack=True)
print(f'highest = {np.max(h)}')
print(f'lowest = {np.min(l)}')
print((np.max(h) + np.min(l)) / 2)
print(f'Spread high price {np.ptp(h)}')
print(f'Spread low price {np.ptp(l)}')

c=np.loadtxt('data.csv', delimiter=',', usecols=(6,), unpack=True)
c.resize(c.size)
print("median =", np.median(c))

sorted_close = np.msort(c)
print("sorted =", sorted_close)
N = len(c)
if N % 2 != 0:
    index = int((N - 1)/2)
    print("middle =", sorted_close[index])
else:
    index = int(N/2)
    print("average middle =", (sorted_close[index] + sorted_close[index-1]) / 2)

print("variance =", np.var(c))
print("variance from definition =", np.mean((c - c.mean())**2))
