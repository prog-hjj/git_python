from scipy import stats
import matplotlib.pyplot as plt

# 按正态分布生成随机数
generated = stats.norm.rvs(size=900)

# 均值和标准差
print("Mean", "Std", stats.norm.fit(generated))

# 偏度（skewness）: 概率分布的偏斜（非对称）程度
print("Skewtest", "pvalue", stats.skewtest(generated))

# 峰度（kurtosis）: 概率分布曲线的陡峭程度
print("Kurtosistest", "pvalue", stats.kurtosistest(generated))

# 正态性检验（normality test）: 数据集服从正态分布的程度
print("Normaltest", "pvalue", stats.normaltest(generated))

# 数据所在的区段中某一百分比处的数值
print("95 percentile", stats.scoreatpercentile(generated, 95))

# 从数值 1 出发找到对应的百分比
print("Percentile at 1", stats.percentileofscore(generated, 1))

plt.hist(generated)
plt.show()
