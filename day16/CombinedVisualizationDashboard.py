import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

sales = np.array([100, 200, 150, 300])
products = ["A", "B", "C", "D"]

df=pd.DataFrame({
    "Sales":sales,
    "Products":products
})
print(df)

plt.figure(figsize=(12,4))

plt.subplot(1,3,1)
plt.plot(df["Products"],df["Sales"])
plt.title("Sales Trend")

plt.subplot(1,3,2)
plt.bar(df["Products"],df["Sales"])
plt.title("Sales Comparision")

plt.subplot(1,3,3)
plt.pie(df["Sales"],labels=df["Products"],autopct="%1.1f%%")
plt.title("Sales Distribution")

plt.show()