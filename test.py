# -*- coding: utf-8 -*-
import pandas as pd

x1 = pd.Series([1, 2, 3, 4])
x2 = pd.Series(data=[1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 也可采用字典的方式来创建 Series
d = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
x3 = pd.Series(d, name='我是由字典创建的~')

print(x1, '\n')
print(x2, '\n')
print(x3)
