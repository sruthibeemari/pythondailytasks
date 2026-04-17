import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 35, 33, 31, 29])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

df=pd.DataFrame({
    "Days":days,
    "Temperature":temps
    
})

high=np.sum(df["Temperature"]>30)
low=np.sum(df["Temperature"]<=30)

plt.figure(figsize=(16,8))

plt.subplot(2,3,1)
plt.plot(df["Days"],df["Temperature"])
plt.title("daily temperature trend")

plt.subplot(2,3,2)
plt.bar(df["Days"],df["Temperature"])
plt.title("day-wise temperature")

plt.subplot(2,3,3)
plt.pie([high,low],labels=["high","low"],autopct="%1.1f%%")
plt.title("proportion of high (>30) vs low temps")

plt.subplot(2,3,4)
plt.hist(df["Temperature"])
plt.title("temperature frequency")

plt.subplot(2,3,5)
plt.scatter(df.index,df["Temperature"])
plt.title("day index vs temperature")

plt.tight_layout()
plt.show()



