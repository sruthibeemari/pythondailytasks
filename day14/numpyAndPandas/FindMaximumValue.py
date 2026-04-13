import numpy as np
import pandas as pd

arr = np.array([12, 45, 22, 67, 34])
s=pd.Series(arr)
maximum=max(s)
print(s)
print("Maximum Value: \n",maximum)