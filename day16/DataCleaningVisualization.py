import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = np.array([100, np.nan, 200, 150, np.nan, 300])

s=pd.Series(data)
mean_value=s.mean()
print(mean_value)
s=s.fillna(mean_value)

print("Cleaned Data:\n", s)


plt.figure(figsize=(10, 4))


plt.subplot(1, 2, 1)
plt.plot(s)
plt.title("Cleaned Data (Line Graph)")


plt.subplot(1, 2, 2)
filtered = s[s > mean_value]
plt.bar(filtered.index, filtered.values)
plt.title("Values > Average")


plt.tight_layout()
plt.show()