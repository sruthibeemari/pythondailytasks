import pandas as pd
cities = {"Delhi": 2000000, "Mumbai": 3000000, "Chennai": 1500000}
wanted=["Delhi","Chennai","Banglore"]
s=pd.Series(cities,index=wanted)
print(s)