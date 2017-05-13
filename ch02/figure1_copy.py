import numpy as np
from sklearn.datasets import load_iris
from matplotlib import pyplot as plt

data = load_iris()
print(data)
features = data['data']
feature_names = data['feature_names']
target = data['target']

# がく片の長さ,幅と花弁の長さ,幅の組み合わせで可視化してみる
# 0: sepal-length, 1: sepal-width, 2: petal-length, 3:petal-width
pairs = [(0, 1), (0, 2), (0, 3), (1, 2), (1, 3), (2, 3)]

for i, (p0, p1) in enumerate(pairs):
    plt.subplot(2, 3, i + 1)
    # 品種ごとにプロットする
    for t, marker, c in zip(range(3), ">ox", "rgb"):
        plt.scatter(features[target == t, p0], features[target == t, p1], marker=marker, c=c)
        plt.xlabel(feature_names[p0])
        plt.ylabel(feature_names[p1])
        plt.xticks([])
        plt.yticks([])

plt.savefig('../1400_02_01.png')
