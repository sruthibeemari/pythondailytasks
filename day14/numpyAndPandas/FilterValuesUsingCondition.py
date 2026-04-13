import numpy as np
import pandas as pd
arr = np.array([10, 25, 30, 15, 40])
s=pd.Series(arr)
filter=s[s>20]
print(filter)
