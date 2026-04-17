import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 180, 220, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]

df=pd.DataFrame({
    "Months":months,
    "Sales":sales
    
})


plt.figure(figsize=(16,8))

plt.subplot(2,3,1)
plt.plot(df["Sales"],df["Months"])
plt.title("sales trend")


plt.subplot(2,3,2)
plt.bar(df["Sales"],df["Months"])
plt.title("month-wise comparison")

plt.subplot(2,3,3)
plt.pie(df["Sales"],labels=df["Months"],autopct="%1.1f%%")
plt.title("contribution of each month")

plt.subplot(2,3,4)
plt.hist(df["Months"])
plt.title("frequency of sales values")

plt.subplot(2,3,5)
plt.scatter(df.index,df["Months"])
plt.title("month index vs sales")

plt.tight_layout()
plt.show()