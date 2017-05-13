#
# データから複数のモデルを作成してプロットする。
# モデルは1次直線、2次曲線、100次曲線まで。
#
import scipy as sp
import matplotlib.pyplot as plt
import error as err

data = sp.genfromtxt("./data/web_traffic.tsv", delimiter="\t")
x = data[:,0]
y = data[:,1]

x = x[~sp.isnan(y)]
y = y[~sp.isnan(y)]

# 1つめのモデル（直線）
fp1, residuals, rank, sv, rcond = sp.polyfit(x, y, 1, full=True)
f1 = sp.poly1d(fp1)
print("Error: %f" % err.error(f1, x, y))

# 2つめのモデル（2次曲線）
fp2 = sp.polyfit(x, y, 2)
f2 = sp.poly1d(fp2)
print("Error: %f" % err.error(f2, x, y))

# 3つめのモデル（100次）
fp3 = sp.polyfit(x, y, 100)
f3 = sp.poly1d(fp3)
print("Error: %f" % err.error(f3, x, y))


## プロット

# 直線
fx = sp.linspace(0, x[-1], 1000)

plt.plot(fx, f1(fx), linewidth=4)
plt.plot(fx, f2(fx), linewidth=4)
plt.plot(fx, f3(fx), linewidth=4)

# 分布
plt.scatter(x, y)

plt.legend(["d=%i" % f1.order], loc="upper left")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.show()

