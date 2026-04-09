import numpy as np
arr=np.array([28, 31, 35, 27, 40, 22])
filter=[]
for i in arr:
    if i>30:
        filter.append(True)
    else:
        filter.append(False)
newArr=arr[filter]
print(newArr)
print(filter)

