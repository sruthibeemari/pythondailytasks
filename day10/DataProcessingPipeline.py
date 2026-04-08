import numpy as np
arr=np.array([12, 7, 25, 3, 18, 10])
sortedArray=np.sort(arr)
splitting=np.split(sortedArray,2)
sum1=np.sum(splitting[0])
sum2=np.sum(splitting[1])
print("Sorted Array:")
print(sortedArray)
print("Two Arrays after Split:")
print(splitting)
print("Sum of Each Part:")
print(sum1,sum2)



