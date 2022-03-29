import numpy as np
import pandas as pd

ser = pd.Series([1, 2, 3])

idx = pd.Index([4, 5, 6])
print(type(idx))

ser = np.maximum(ser, idx)
print(type(ser), ser, sep='\n')

print(pd.DataFrame(np.random.randn(3, 12)))
