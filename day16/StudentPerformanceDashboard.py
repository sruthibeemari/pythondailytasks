import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

marks = np.array([45, 67, 89, 56, 72, 91, 38])
students = ["A", "B", "C", "D", "E", "F", "G"]

df=pd.DataFrame({
    "Students":students,
    "Marks":marks
})

pass_count=np.sum(df["Marks"]>50)
fail_count=np.sum(df["Marks"]<=50)

plt.figure(figsize=(12,8))

plt.subplot(2,3,1)
plt.plot(df["Students"],df["Marks"])
plt.title("trend of marks")


plt.subplot(2,3,2)
plt.bar(df["Students"],df["Marks"])
plt.title("student vs marks")

plt.subplot(2,3,3)
plt.pie([pass_count,fail_count],labels=["Pass","Fail"],autopct="%1.1f%%")
plt.title("Pass (>50) vs Fail")

plt.subplot(2,3,4)
plt.hist(df["Marks"])
plt.title("Distribution of Marks")

plt.subplot(2,3,5)
plt.scatter(df.index,df["Marks"])
plt.title("Index vs Marks")

plt.tight_layout()
plt.show()