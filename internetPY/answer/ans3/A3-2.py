set_seed = 123

import numpy as np

x = np.random.RandomState(set_seed).randint(low=5, high=16, size=15)
print('隨機正整數：', x)

x = x.reshape(3, 5)
print('X矩陣內容：')
print(x)
print('最大：', np.max(x))
print('最小：', np.min(x))
print('總和：', np.sum(x))
print('四個角落元素：')
print(x[np.ix_([0, -1], [0, -1])])