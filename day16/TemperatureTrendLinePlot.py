import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

temps = np.array([28, 30, 32, 31, 29])

s=pd.Series(temps)
print(s)

plt.plot(s)

plt.grid()
plt.title(" Daily Temperature")

plt.show()