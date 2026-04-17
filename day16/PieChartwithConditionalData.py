import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


scores = np.array([40, 60, 80, 30, 90])

s=pd.Series(scores)

result=s.apply(lambda x: "Pass" if x>50 else "Fail")
print("Result: \n",result )

count=result.value_counts()

print("Count: ",count)

plt.pie(count,labels=count.index,autopct="%1.1f%%")

plt.title("Students Marks percentage Pass / Fail")
plt.show()
