import numpy as np
matrix=np.random.randint(0,50,(3,3))
print("3X3 Matrix:")
print(matrix)
filter=matrix[matrix>25]
print("Filtered Matrix",filter)