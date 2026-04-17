import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

salaries = np.array([25000, 30000, 28000, 40000, 50000, 35000])
departments = ["HR", "IT", "HR", "IT", "Sales", "Sales"]

df=pd.DataFrame({
    "Departments":departments,
    "Salaries":salaries
    
})


plt.figure(figsize=(16,8))

plt.subplot(2,3,1)
plt.plot(df.index,df["Salaries"])
plt.title("salary trend")


plt.subplot(2,3,2)
plt.bar(df["Departments"],df["Salaries"])
plt.title("department-wise salary comparison")

plt.subplot(2,3,3)
count=df["Departments"].value_counts()
plt.pie(count, labels=count.index,autopct="%1.1f%%")
plt.title("department distribution")

plt.subplot(2,3,4)
plt.hist(df["Salaries"])
plt.title("salary distribution")

plt.subplot(2,3,5)
plt.scatter(df.index,df["Salaries"])
plt.title("index vs salary")

plt.tight_layout()
plt.show()