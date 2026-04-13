import pandas as pd
df = pd.DataFrame({
"Name": ["A", "B", "C", "D"],
"Marks": [50, 80, 30, 90]
})

# df["Status"]=df["Marks"].apply(lambda x : "Pass" if x>=50 else "Fail")
status=[]
for x in df["Marks"]:
    if x>=50:
        status.append("Pass")
    else:
        status.append("Fail")
df["Status"]=status
print(df)
passed=df[df["Status"]=="Pass"]
print("Passed Students: \n",passed)
avg=passed["Marks"].mean()
print("Average Marks of Passed Students: \n",avg)
