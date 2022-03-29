import numpy as np
import pandas as pd

ser1 = pd.Series([21, 32, 63, 4], index=['a', 'b', 'c', 'd'])
ser2 = pd.Series([66, 88, 92, 0], index=['b', 'd', 'c', 'a'])

# np.remainder() 取余
print('ser1:\n', ser1, '\n', '-' * 30,
      '\nser2:\n', ser2, '\n', '-' * 30,
      '\n', 'np.remainder(ser1, ser2):\n', np.remainder(ser1, ser2))  # ser1 % ser2

# As usual, the union of the two indices is taken,
# and non-overlapping values are filled with missing values.
ser3 = pd.Series([2, 4, 6], index=["bbb", "c", "d"])
print('\nnp.remainder(ser1, ser3):\n', np.remainder(ser1, ser3))
