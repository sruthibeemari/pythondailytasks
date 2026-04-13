import numpy as np
import pandas as pd
S = pd.Series([10, 50, 30, 80, 20])
updatedS=pd.Series(np.where(S>40,0,S))
print(updatedS)