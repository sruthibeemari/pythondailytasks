'''
============================================================
📊 Project Title: Scottish Hills Dataset
Analyze Scottish Hills dataset using NumPy, Pandas, Matplotlib
============================================================
 
============================================================
📦 1. Import Required Libraries
============================================================
👉 Import numpy
👉 Import pandas
👉 Import matplotlib.pyplot
👉 (Optional) Import os for folder creation
'''
 
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd
import os
 
''' ============================================================
📁 2. Setup Project Structure
============================================================
👉 Create a folder named "graphs"
👉 Ensure it does not throw error if already exists
 '''
 
os.makedirs("graphs", exist_ok=True)
#===========================================================================================================================
#�� Scenario 1: Data Loading & Basic Cleaning
#===========================================================================================================================
'''�� Tasks:
1. Load the dataset using Pandas.
2. Display:
○ First 5 rows
○ Column names
3. Check for missing values in:
○ bedrooms
○ bathrooms
○ sqft_living
○ price
4. Fill missing values:
○ bedrooms → use mode
○ bathrooms → use mean
○ sqft_living → use mean
○ price → use mean
5. Convert these columns to numeric if required:
○ bedrooms
○ bathrooms
○ sqft_living
○ price'''
df= pd.read_csv('kc_House_data.csv')

print("First five Colunm Nmaes")
print(df.head(5))
print("Column Names\n",df.columns)

print(df[['bedrooms','bathrooms','sqft_living','price']].isnull().sum())
df['bedrooms']=df['bedrooms'].fillna(df['bedrooms'].mode())
df['bathrooms']=df['bathrooms'].fillna(df['bathrooms'].mean())
df['sqft_living']=df['sqft_living'].fillna(df['sqft_living'].mean())
df['price']=df['price'].fillna(df['price'].mean())

cols = ['bedrooms', 'bathrooms', 'sqft_living', 'price']
df[cols] = df[cols].apply(pd.to_numeric, errors='coerce')
print(df[cols].dtypes)
#===========================================================================================================================
#�� Scenario 2: Line Graph + Save
#===========================================================================================================================
'''�� Tasks:
1. Select:
○ id
○ price
2. Take the first 10 rows only.
3. Convert price into a NumPy array.
4. Plot a line graph:
○ X-axis → index (0–9)
○ Y-axis → Price
5. Add:
○ Title
○ X-label
○ Y-label
6. Save the graph: plt.savefig("house_prices_line.png")
'''

df_first10 = df[['id','price']].head(10)
price_arr = df_first10['price'].values

plt.plot(price_arr)
plt.title("House Prices Trend")
plt.xlabel("Index")
plt.ylabel("Price")

plt.savefig("graphs/house_prices_line.png")
plt.show()



#===========================================================================================================================
#�� Scenario 3: Filtering + Bar Chart + Save
#===========================================================================================================================
'''�� You want to analyze expensive houses.
�� Tasks:
1. Filter houses where:
○ price > 1000000
2. Count number of houses per:
○ bedrooms
3. Select top bedroom categories.
4. Convert results to NumPy arrays.
5. Plot a bar chart:
○ X-axis → Bedrooms
○ Y-axis → Count
6. Rotate labels if needed.
7. Save graph: plt.savefig("expensive_houses_bar.png")
'''

expensive_houses=df[df['price']>1000000]
print("Expensive houses count:", len(expensive_houses))

bedroom_counts = expensive_houses['bedrooms'].value_counts().sort_index()
top_bedrooms = bedroom_counts.head(5)

bedrooms_array = top_bedrooms.index.to_numpy()
counts_array = top_bedrooms.to_numpy()

plt.figure()
plt.bar(bedrooms_array, counts_array)
plt.xticks(rotation=45)
plt.title("Expensive Houses (>1M) by Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")

plt.savefig("graphs/expensive_houses_bar.png")
plt.show()


#===========================================================================================================================
#�� Scenario 4: Pie Chart (Bedroom Distribution) + Save
#===========================================================================================================================
'''�� You want to see the distribution of house types.
�� Tasks:
1. Count number of houses by:
○ bedrooms
2. Select top 5 bedroom categories.
3. Prepare:
○ Labels
○ Values
4. Plot a pie chart.
5. Add percentage labels.
6. Save graph: plt.savefig("bedroom_distribution.png")
'''
# 4.1 Count number of houses by:  ○ bedrooms
counts = df['bedrooms'].value_counts().sort_index()
print(counts)

# 4.2 Select top 5 bedroom categories.
top_5_bedrooms = df['bedrooms'].value_counts().nlargest(5)
print(top_5_bedrooms)

# 4.3 Prepare:  ○ Labels  ○ Values
labels = top_5_bedrooms.index
values = top_5_bedrooms.values

# 4.4 Plot a pie chart & 4.5 Add percentage labels.
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Top 5 Bedroom Categories")
plt.tight_layout()

# 4.6 Save graph: plt.savefig("bedroom_distribution.png")
plt.savefig("graphs/bedroom_distribution.png")
plt.show()

#===========================================================================================================================
#�� Scenario 5: Advanced Analysis + Multiple Graphs
#===========================================================================================================================
'''�� You want deeper insights from the house dataset.
�� Part 1: Feature Creation
Create a new column:
Price Category
● price >= 1000000 → "Luxury"
● 500000 – 999999 → "Mid Range"
● < 500000 → "Affordable"
�� Part 2: NumPy Usage
1. Convert price column to a NumPy array.
2. Calculate price differences using:
np.diff()
�� Part 3: Visualizations
�� Line Graph
Plot price trend for all houses.
�� Stacked Bar Chart
Show count of Price Category per Bedrooms.
�� Histogram
Plot distribution of:
● price
�� Part 4: Save All Graphs
plt.savefig("price_trend.png")
plt.savefig("price_category_stacked.png")
plt.savefig("price_histogram.png")
�� Part 5: Insights
Answer these:
1. Which bedroom category has the most expensive houses?
2. Which price category is most common?
3. What is the distribution pattern of house prices?
○ Right-skewed?
○ Normal?
○ Concentrated in a lower price range?
'''
#------------------------------------------------------------------------------
# �� Part 1: Feature Creation
#------------------------------------------------------------------------------
# Create a new column:
# Price Category
# ● price >= 1000000 → "Luxury"
# ● 500000 – 999999 → "Mid Range"
# ● < 500000 → "Affordable"
#------------------------------------------------------------------------------
def categorize_price(price):
    if price >= 1000000:
        return "Luxury"
    elif 500000 <= price < 1000000:
        return "Mid Range"
    else:
        return "Affordable"

df["Price Category"] = df["price"].apply(categorize_price)
#------------------------------------------------------------------------------
# �� Part 2: NumPy Usage
#------------------------------------------------------------------------------
# 1. Convert price column to a NumPy array.
# 2. Calculate price differences using:
# np.diff()
#------------------------------------------------------------------------------
price_array = df["price"].to_numpy()

price_diff = np.diff(price_array)

print("Price differences (first 10):", price_diff[:10])
#------------------------------------------------------------------------------
# �� Part 3: Visualizations
#------------------------------------------------------------------------------
# �� Line Graph
# Plot price trend for all houses.
# �� Stacked Bar Chart
# Show count of Price Category per Bedrooms.
# �� Histogram
# Plot distribution of:
# ● price
#------------------------------------------------------------------------------
# 1. LINE GRAPH - Price trend
plt.figure(figsize=(10,5))
plt.plot(df.index, df["price"], marker='o')
plt.title("House Price Trend")
plt.xlabel("House Index")
plt.ylabel("Price")
plt.grid()

plt.savefig("graphs/price_trend.png")
plt.show()

# 2. STACKED BAR CHART - Price Category vs Bedrooms
category_bedroom = pd.crosstab(df["bedrooms"], df["Price Category"])

category_bedroom.plot(kind="bar", stacked=True, figsize=(10,6))
plt.title("Price Category per Bedrooms")
plt.xlabel("Bedrooms")
plt.ylabel("Count")

plt.savefig("graphs/price_category_stacked.png")
plt.show()

# 3. HISTOGRAM - Price distribution
plt.figure(figsize=(10,5))
plt.hist(df["price"], bins=30, edgecolor='black')
plt.title("House Price Distribution")
plt.xlabel("Price")
plt.ylabel("Frequency")

plt.savefig("graphs/price_histogram.png")
plt.show()
#------------------------------------------------------------------------------
# �� Part 4: Save All Graphs
#------------------------------------------------------------------------------
# plt.savefig("price_trend.png")
# plt.savefig("price_category_stacked.png")
# plt.savefig("price_histogram.png")
#------------------------------------------------------------------------------
#------------------------------------------------------------------------------
# �� Part 5: Insights
#------------------------------------------------------------------------------
# Answer these:
# 1. Which bedroom category has the most expensive houses?
# 2. Which price category is most common?
# 3. What is the distribution pattern of house prices?
# ○ Right-skewed?
# ○ Normal?
# ○ Concentrated in a lower price range?
#------------------------------------------------------------------------------
# Q1: Which bedroom category has the most expensive houses?
expensive_by_bedroom = df.groupby("bedrooms")["price"].mean().sort_values(ascending=False)
print("\nMost expensive bedrooms category:\n", expensive_by_bedroom.head(1))


# Q2: Which price category is most common?
print("\nMost common price category:\n", df["Price Category"].value_counts())


# Q3: What is the distribution pattern of house prices?
# (Check skewness to understand distribution shape)
print("\nPrice skewness check:")
print(df["price"].skew())

if df["price"].skew() > 1:
    print("Distribution is Right-skewed (most houses are low price, few very expensive)")
elif df["price"].skew() < -1:
    print("Distribution is Left-skewed")
else:
    print("Distribution is approximately Normal (balanced distribution)")

