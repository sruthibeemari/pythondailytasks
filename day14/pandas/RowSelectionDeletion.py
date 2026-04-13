import pandas as pd
df = pd.DataFrame({
"A": [10, 20, 30],
"B": [5, 15, 25]
}, index=["x", "y", "z"])
print(df.loc["y"])

df=df.drop("x")
print("After Deletion")
print(df)