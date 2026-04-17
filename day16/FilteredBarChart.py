import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 80, 60, 30, 90])
names = ["A", "B", "C", "D", "E"]

df=pd.DataFrame({
    "Marks":marks,
    "Names":names
})

filtered=df[df["Marks"]>50]

plt.bar(filtered["Names"],filtered["Marks"])
plt.xlabel("Names")
plt.ylabel("Marks")
plt.title("Students with above(>)50 Marks")

plt.show()