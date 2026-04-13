import pandas as pd
S1 = pd.Series([10, 20, 30], index=["a", "b", "c"])
S2 = pd.Series([5, 15, 25], index=["b", "c", "d"])
add=(S1+S2).fillna(0)
print(add)