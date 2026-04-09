import numpy as np
scores=np.array([50, 60, 70, 80, 90, 100, 110, 120])
newarr=np.array_split(scores,4)
print("After Splitting: ",newarr)