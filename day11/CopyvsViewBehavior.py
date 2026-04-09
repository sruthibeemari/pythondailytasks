import numpy as np
#using copy
arr=np.array([10, 20, 30, 40])
copied_arr=arr.copy()
arr[1]=50
print("Modified Array: ",arr)

print("Copied Array: ",copied_arr)




# Using view
view_arr=arr.view()
arr[0]=11
print("Original Array: ",arr)
print("Viewed Array: ",view_arr)


