''' 
============================================================
 Project Title: Railway Gauge Data Analysis
 Analyze railway gauge dataset using NumPy, Pandas, Matplotlib
============================================================

============================================================
 📦 1. Import Required Libraries
============================================================
👉 Import numpy
👉 Import pandas
👉 Import matplotlib.pyplot
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
===============================================================
1 Scenario 1: Basic Data Loading & Cleaning
===============================================================
 You are given a CSV file containing railway gauge data.
 �� Tasks:
 1. Load the dataset into a Pandas DataFrame.
 2. Display the first 5 rows and column names.
 3. Check for missing values and replace them with 0.
 4. Convert all gauge columns (Broad, Metre, Narrow, Total) to numeric types.
 '''

df=pd.read_csv('railway_gauges.csv')

print("First 5 Rows: ")
print(df.head())

print("\nFirst 5 columns: ")
print(df.columns)

print("\nMissing Values: ")
print(df.isnull().sum())
df=df.fillna(0)
print("\nAfter replacing with 0: ")
print(df.isnull().sum())

gauge_columns=["Broad Gauge","Metre Gauge","Narrow Gauge","Total"]
for col in gauge_columns:
    df[col]=pd.to_numeric(df[col])
print("\nData Types after conversion:")
print(df.dtypes)

'''
===========================================================
Scenario 2: Simple Visualization
===========================================================
You want a quick understanding of total railway track growth.
👉 Tasks:
1. Extract Year and Total columns.
2. Plot a line graph showing Total tracks over years.
3. Add:
○ Title
○ X and Y labels
4. Identify whether the trend is increasing or decreasing.
'''

year=df['Year']
total=df["Total"]

plt.figure()
plt.plot(year,total)
plt.title("Total Railway Track Growth Over Years")
plt.xlabel("Year")
plt.ylabel("Total Track")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Railway_Gauges1S2.png")
plt.show()

'''
#=================================================================
#Scenario 3: Filtering + Bar Chart
#=================================================================
You are asked to analyze modern railway expansion.
👉 Tasks:
1. Filter the dataset for years after 2000.
2. Select Broad Gauge, Metre Gauge, and Narrow Gauge.
3. Plot a grouped bar chart comparing all three gauges.
4. Add legend and proper labels.
5. Identify which gauge dominates in recent years.
'''

df["Year"] = df["Year"].str.split('-').str[0]
df["Year"] = pd.to_numeric(df["Year"], errors='coerce')
df["Year"] = pd.to_numeric(df["Year"])
df_filtered=df[df["Year"]>2000]
print(df_filtered)

years=df_filtered['Year']
broad_gauge=df_filtered["Broad Gauge"]
metre_gauge=df_filtered["Metre Gauge"]
narrow_gauge=df_filtered["Narrow Gauge"]

x=np.arange(len(years))
width=0.25
plt.figure()
plt.bar(x - width,broad_gauge,width,label="Broad Gauge")
plt.bar(x,metre_gauge,width,label="Metre Gauge")
plt.bar(x + width,narrow_gauge,width,label="Narrow Gauge")
plt.title("Gauge comparison after 2000")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.xticks(x,years,rotation=45)
plt.legend()
plt.tight_layout()
plt.savefig("Railway_Gauges2S3.png")
plt.show()

'''
#==================================================================
# Scenario 4: Feature Engineering + Pie Chart
#=================================================================
You want to analyze the contribution of each gauge type.
👉 Tasks:
1. Calculate total sum of each gauge across all years.
2. Create a new structure (Series/DataFrame) for totals.
3. Plot a pie chart showing percentage contribution.
4. Add percentage labels (autopct).
5. Interpret which gauge contributes the most.
'''

total_broad=df["Broad Gauge"].sum()
total_metre=df["Metre Gauge"].sum()
total_narrow=df["Narrow Gauge"].sum()
print("\nTotal Broad Gauge:", total_broad)
print("Total Metre Gauge:", total_metre)
print("Total Narrow Gauge:", total_narrow)

gauge_totals=pd.Series([total_broad,total_metre,total_narrow],
                       index=["Broad Gauge","Metre Gauge","Narrow Gauge"])
print("\nGauge Totals:")
print(gauge_totals)

plt.figure()
plt.pie(gauge_totals,labels=gauge_totals.index,autopct="%1.1f%%")
plt.title("Percentage contribution of each gauge type")
plt.tight_layout()
plt.savefig("Railway_Gauges3S4")
plt.show()

max_gauge=gauge_totals.idxmax()
print("\nGauge with highest contribution:", max_gauge)

'''
#==================================================================
# Scenario 5: Advanced Analysis + Multiple Graphs
#=================================================================
You are asked to perform a complete analysis of railway trends.
👉 Tasks:
1. Create new columns:
○ % Broad Gauge
○ % Metre Gauge
○ % Narrow Gauge
2. Use NumPy (np.diff) to calculate yearly growth of Total tracks.
3. Plot:
○ Line graph for all gauges
○ Stacked bar chart showing composition
4. Highlight:
○ Years with highest growth
○ Decline in any gauge
5. Provide a final conclusion:
👉 “Is the railway system shifting towards a single dominant gauge?”
'''

df["% Broad Gauge"] = (df["Broad Gauge"] / df["Total"]) * 100
df["% Metre Gauge"] = (df["Metre Gauge"] / df["Total"]) * 100
df["% Narrow Gauge"] = (df["Narrow Gauge"] / df["Total"]) * 100
print("\nPercentage Columns Added:")
print(df[["% Broad Gauge", "% Metre Gauge", "% Narrow Gauge"]].head())

growth=np.diff(df["Total"])
growth = np.insert(growth, 0, 0)  # to match length
df["Yearly Growth"]=growth
print("\nYearly Growth:")
print(df[["Year", "Total", "Yearly Growth"]].head())


plt.figure()
plt.plot(df["Year"],df["Broad Gauge"],label="Broad Gauge")
plt.plot(df["Year"],df["Metre Gauge"],label="Metre Gauge") 
plt.plot(df["Year"],df["Narrow Gauge"],label="Narrow Gauge") 
plt.title("Gauge Trends Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Railway_Gauges4S5.png")
plt.show()

plt.figure()
plt.bar(df["Year"],df["Broad Gauge"],label="Broad Gauge")
plt.bar(df["Year"],df["Metre Gauge"],bottom=df["Broad Gauge"],label="Metre Gauge")
plt.bar(df["Year"],df["Narrow Gauge"],
        bottom=df["Broad Gauge"]+df["Metre Gauge"],label="Narrow Gauge")
plt.title("Gauge Composition Over Years")
plt.xlabel("Year")
plt.ylabel("Track Length")
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("Railway_Gauges5S5.png")
plt.show()

max_growth_year = df.loc[df["Yearly Growth"].idxmax(), "Year"]
print("\nYear with Highest Growth:", max_growth_year)

decline_broad = df[df["Broad Gauge"].diff() < 0]
decline_metre = df[df["Metre Gauge"].diff() < 0]
decline_narrow = df[df["Narrow Gauge"].diff() < 0]

print("\nBroad Gauge Decline Years:")
print(decline_broad["Year"])
print("\nMetre Gauge Decline Years:")
print(decline_metre["Year"])
print("\nNarrow Gauge Decline Years:")
print(decline_narrow["Year"])
print("Yes, the railway system is clearly shifting towards a single dominant gauge — Broad Gauge.")