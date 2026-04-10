import numpy as np
data=np.random.rand(8)
print("Original data\n: ",data)
normalize=data*100
print("Normalized\n: ",normalize)
filter=normalize[normalize>50]
print("Filtered >50\n: ",filter)
sort=np.sort(filter)
print("Sorted Filtered Values\n: ",sort)