import numpy as np
salaries=np.array([25000, 40000, 15000, 50000, 30000])
filter=salaries[salaries>30000]
count=np.sum(salaries>30000)
print("Filtered Array above 30k: ",filter)
print("count of employees above 30k: ",count)