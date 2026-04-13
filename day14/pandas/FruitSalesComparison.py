import pandas as pd
S1 = pd.Series([10, 20, 30], index=["apple", "banana", "cherry"])
S2 = pd.Series([5, 15, 25], index=["apple", "banana", "cherry"])
s=S1+S2
total=sum(s)
print(s)
print("Total Sales: ",total)