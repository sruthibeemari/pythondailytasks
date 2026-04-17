import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

names = ["A", "B", "C", "D"]
marks = np.array([70, 85, 60, 90])

df=pd.DataFrame({
    "Names":names,
    "Marks":marks
})

print(df)

plt.bar(df["Names"],df["Marks"])

plt.xlabel("Student Names")
plt.ylabel("Marks")
plt.title("Student Marks Bar Chart")

plt.show()