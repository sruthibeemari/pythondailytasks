import numpy as np
import pandas as pd
arr = np.array([
[100, 200],
[150, 250],
[80, 120],
[300, 400]
])
df=pd.DataFrame(arr,columns=["Sales","Profit"])
print(df)
filter=df[df["Sales"]>100]
print(filter)
avg=filter["Profit"].mean()
print("Average profit of filtered: \n",avg)