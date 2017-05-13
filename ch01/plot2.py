import scipy as sp
import matplotlib.pyplot as plt
import error as err

inflection = (int)(3.5 * 7 * 24) # 変化点
print("Inflection %d" % inflection)

data = sp.genfromtxt("./data/web_traffic.tsv", delimiter="\t")
print(data.shape)
x = data[:,0]
y = data[:,1]

xa = x[:inflection]
ya = y[:inflection]

xb = x[inflection:]
yb = y[inflection:]

fpa = sp.polyfit(xa, ya, 1)
fpb = sp.polyfit(xb, yb, 1)
fa = sp.poly1d(fpa)
fb = sp.poly1d(fpb)

fa_error = err.error(fa, xa, ya)
fb_error = err.error(fb, xb, yb)

print("Error inflection=%s" % "{:,f}".format(fa_error + fb_error))

# プロット
fx = sp.linspace(0, x[-1], 1000)

# 直線
plt.plot(fx, fa(fx), linewidth=4)
plt.plot(fx, fb(fx), linewidth=4)

# 分布
plt.scatter(x, y)

#plt.legend(["d=%i" % f1.order], loc="upper left")
plt.xlabel("Time")
plt.ylabel("Hits/hour")
plt.xticks([w*7*24 for w in range(10)], ['week %i' % w for w in range(10)])
plt.autoscale(tight=True)
plt.grid()
plt.ylim([0, 6500])
plt.show()

