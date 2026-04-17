import numpy as np
import pandas as pd


marks=np.random.randint(0,101,10)

df=pd.DataFrame({
    "Student":[f"S{i+1}" for i in range(10)],
    "Marks":marks
})

print(df)

passed=df[df["Marks"]>50]
print("\nPassed Students: \n",passed)

mean_marks=np.mean(df["Marks"])
print("Mean :\n",mean_marks)

for i in range (len(df)):
    name=df.loc[i,"Student"]
    mark=df.loc[i,"Marks"]
    
    if mark>=50:
        status="pass"
    else:
        status="fail"
    print(name,mark,status)

