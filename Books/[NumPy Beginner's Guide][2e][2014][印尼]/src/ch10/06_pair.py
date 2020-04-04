from matplotlib.finance import quotes_historical_yahoo # py3已废
from datetime import date
import numpy as np
from scipy import stats
from statsmodels.stats.stattools import jarque_bera
import matplotlib.pyplot as plt

def get_close(symbol):
    today = date.today()
    start = (today.year - 1, today.month, today.day)

    quotes = quotes_historical_yahoo(symbol, start, today)
    quotes = np.array(quotes)

    return quotes.T[4]

spy = np.diff(np.log(get_close("SPY")))
dia = np.diff(np.log(get_close("DIA")))

# 均值检验 : 检查两组不同的样本是否有相同的均值
print("Means comparison", stats.ttest_ind(spy, dia))

# Kolmogorov-Smirnov检验 : 判断两组样本同分布的可能性
print("Kolmogorov smirnov test", stats.ks_2samp(spy, dia))

# Jarque-Bera正态性检验
print("Jarque Bera test", jarque_bera(spy - dia)[1])

plt.hist(spy, histtype="step", lw=1, label="SPY")
plt.hist(dia, histtype="step", lw=2, label="DIA")
plt.hist(spy - dia, histtype="step", lw=3, label="Delta")
plt.legend()
plt.show()
