import numpy as np
arr=np.array([5, 12, 18, 7, 25, 30])
filter=np.where(arr>15,0,arr)
print(filter)