import numpy as np
values = np.array([10, 12, 15, 18, 100, 14, 13])
mean = np.mean(values)
std = np.std(values)
filtered = values[np.abs(values - mean) <= 2 * std]
print("Mean:", mean)
print("Standard Deviation:", std)
print("Filtered Values:", filtered)