import numpy as np
import pandas as pd

import matplotlib.pyplot as plt

sales = np.array([100, 150, 200, 250, 300])
months = ["Jan", "Feb", "Mar", "Apr", "May"]

df=pd.DataFrame({
    "Months":months,
    "Sales":sales
})

print(df)

plt.plot(df["Months"],df["Sales"])
plt.xlabel("Months")
plt.ylabel("Sales")
plt.title("Monthly Sales Line Graph")

plt.show()