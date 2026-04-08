import numpy as np
BranchA=np.array([[10,20],[30,40]])
BranchB=np.array([[5,15],[25,35]])
combine=np.concatenate((BranchA,BranchB))
total=np.sum(combine)
print("Combined Matrix:")
print(combine)
print("Total employees:")
print(total)

