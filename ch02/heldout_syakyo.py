from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from threshold_syakyo import learn_model, apply_model, accuracy


data = load_iris()
features = data['data']
labels = data['target_names'][data['target']]

setosa = (labels == 'setosa')
features = features[~setosa]
labels = labels[~setosa]
virginica = (labels == 'virginica')
print(virginica.shape)
print(virginica)

print(features.shape)
#np.tile()でT,Fの配列を順序よく作る
#testing = np.tile([True, False], int(features.shape[0] / 2))
#flags = np.tile([True, False], int(features.shape[0] / 2))
# 2つの値を50回繰り返して要素100個の配列を作る
flags = np.tile([True, False], int(features.shape[0] / 2))
np.random.shuffle(flags)
testing = flags
training = ~testing

print(testing)
print(training)

print(features.shape)
print(features)

model = learn_model(features[training], virginica[training])
train_error = accuracy(features[training], virginica[training], model)
test_error = accuracy(features[testing], virginica[testing], model)

print('''\
Training error was {0:.1%}.
Testing error was {1:.1%} (N = {2}).
'''.format(train_error, test_error, testing.sum()))
