import numpy as np
data = np.arange(1, 13)
matrix = data.reshape(3, 4)
rowAvg = np.mean(matrix, axis=1)
print("Matrix:\n", matrix)
print("Row Averages:", rowAvg)