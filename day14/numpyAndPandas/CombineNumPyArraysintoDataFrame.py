import numpy as np
import pandas as pd
names = np.array(["A", "B", "C"])
marks = np.array([80, 90, 70])
df=pd.DataFrame({
    "Names":names,
    "Marks":marks


})
print(df)
filtered=df[df["Marks"]>75]
print("Above 75: \n",filtered)