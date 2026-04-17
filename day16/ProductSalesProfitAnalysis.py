import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([200, 300, 250, 400, 350])
profit = np.array([50, 70, 60, 90, 80])
products = ["A", "B", "C", "D", "E"]

df=pd.DataFrame({
    "Sales":sales,
    "Profit":profit,
    "Product":products
})

plt.figure(figsize=(16,8))

plt.subplot(2,3,1)
plt.plot(df["Product"], df["Sales"])
plt.title("Sales Trend")

plt.subplot(2,3,2)
plt.bar(df["Product"], df["Sales"])
plt.title("Product Sales")

plt.subplot(2,3,3)
plt.pie(df["Sales"], labels=df["Product"], autopct='%1.1f%%')
plt.title("Sales Contribution")

plt.subplot(2,3,4)
plt.hist(df["Profit"])
plt.title("Profit Distribution")

plt.subplot(2,3,5)
plt.scatter(df["Sales"], df["Profit"])
plt.title("Sales vs Profit")

plt.tight_layout()
plt.show()




