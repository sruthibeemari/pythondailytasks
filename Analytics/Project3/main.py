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
 
# ============================================================
# 🟢 SCENARIO 1: Data Loading & Basic Cleaning
# ============================================================
# 1.1 Load the dataset using Pandas.
df=pd.read_csv('scottish_hills.csv')
 
# 1.2 Display: ○ First 5 rows ○ Column names
# print("First five rows are:\n",df.head())
 
# 1.3 Check for missing values in: ○ Height ○ Region
# Creating column Region
# Midpoints
lat_mid = df["Latitude"].median()
lon_mid = df["Longitude"].median()
# Function to assign region
def assign_region(row):
    lat = row["Latitude"]
    lon = row["Longitude"]
    if lat >= lat_mid and lon >= lon_mid:
        return "North-East"
    elif lat >= lat_mid and lon < lon_mid:
        return "North-West"
    elif lat < lat_mid and lon >= lon_mid:
        return "South-East"
    else:
        return "South-West"
df["Region"] = df.apply(assign_region, axis=1)
print(df.head())
 
miss_values=df[['Height','Region']].isna().sum()
print(f"Missing value count:\n{miss_values}")
 
# 1.4 Fill missing values: ○ Height → use mean ○ Region → use mode
high=df['Height'].mean()
df['Height']=df['Height'].fillna(high)
reg=df['Region'].mode()[0]
df['Region']=df['Region'].fillna(reg)
 
# 1.5 Convert Height column to numeric if required.
print("Before converting Data type of Height column is:",df['Height'].dtype)
df['Height']=pd.to_numeric(df['Height'], errors='coerce')
print("After converting Data type of Height column is:",df['Height'].dtype)
 
# =========================================================

# ============================================================
# 🟢 SCENARIO 2: Line Graph + Save
# ============================================================
#2.1. Select: ○ Hill Name ○ Height
data = df[['Hill Name', 'Height']]

# 2.2 Take first 10 rows
data_10 = data.head(10)

# 2.3 Convert Height to NumPy array
height_array = np.array(data_10['Height'])

# 2.4 Plot line graph
plt.figure()
plt.plot(range(10), height_array, marker='o')

# 2.5 Add title and labels
plt.title("Hill Heights (First 10 Rows)")
plt.xlabel("Index (0-9)")
plt.ylabel("Height")

# 2.6 Save the graph
# plt.savefig("hill_heights_line.png")

# Show graph
plt.show()

# ============================================================
# 🟢 SCENARIO 3: Filtering + Bar Chart + Save
# ============================================================

# 3.1 Filter hills where: ○ Height > 900
filt=df[df['Height']>900]
print(filt[['Hill Name','Height']])
 
# 3.2 Count number of hills per Region.
count=filt['Region'].value_counts()
print(count)
 
# 3.3 Select top regions.
max_val = count.max() # Find the maximum value in the counts
top_regions = count[count == max_val].index.tolist() # Adding maximum count regions to list
print(f"Regions with top Hill counts: {top_regions}")
 
# 3.4 Convert results to NumPy arrays.
top_reg_arr=np.array(top_regions)
print(top_reg_arr,type(top_reg_arr))
 
# 3.5 Plot a bar chart: ○ X-axis → Region ○ Y-axis → count
plt.clf()
plt.bar(count.index,count,width=0.25)
plt.title('Tall Hills count per Region')
plt.xlabel('All Regions')
plt.ylabel('Top Hills Counts')
plt.tight_layout()
 
# 3.6 Rotate labels for clarity.

# plt.xticks(rotation=90) 
# Save graph:
plt.savefig("graphs/tall_hills_bar.png")
plt.show()

#=============================================================================
# �� Scenario 4: Pie Chart (Region Distribution) + Save
#=============================================================================
# 1. Count the number of hills per Region.
# 2. Select top 5 regions.
# 3. Prepare labels and values.
# 4. Plot a pie chart.
# 5. Add percentage labels.
# Save graph: plt.savefig("region_distribution.png")
#=============================================================================
# 4.1 Count the number of hills per Region
region_counts = df["Region"].value_counts()

# 4.2 Select top 5 regions
top_regions = region_counts.head(5)

# 4.3 Prepare labels and values
labels = top_regions.index
values = top_regions.values
# 4.4 Plot a pie chart & 4.5 Add percentage labels.
plt.pie(values, labels=labels, autopct='%1.1f%%')

# Title
plt.title("Region Distribution of Hills")

# Save the graph
# plt.savefig("graphs/region_distribution.png")

# Show plot
plt.show()
#=============================================================================

#========================================================================================================================
#Scenario 5: Advanced Analysis + Multiple Graphs (Hard)
#========================================================================================================================
#Task	Description
#1.	Create Height Category column: Height >= 1000 → "Very High", 800-999 → "High", < 800 → "Moderate".
#2.	Convert Height column to NumPy array.
#3.	Calculate height differences using np.diff().
#4.	Plot a Line Graph showing height trend for all hills.
#5.	Plot a Stacked Bar Chart: count of Height Category per Region.
#6.	Plot a Histogram: distribution of Height.
#7.	Save graphs: plt.savefig("height_trend.png"), plt.savefig("height_category_stacked.png"), plt.savefig("height_histogram.png")
#8.	Identify: Which region has the tallest hills, which category is most common, and the distribution pattern of heights.

#here is the condition that is given in the task
condition=[df['Height'] > 999 ,(df['Height'] <= 999) & 
           (df['Height'] >= 800), df['Height'] < 800]
#here are the options that are to be choosed  according to the condition
choose=['Very High','High','Moderate']
#here using np.select that works as if,elif,else.
df['Height Category']=np.select(condition,choose,default='Unknown')
#converting column to numpy
height_array=df['Height'].to_numpy() 
#here we are checking the difference between the heights of the hills
height_growth=np.diff(height_array)
#print(height_growth)

#print(df[df['Height Category']=='Unknown'])
#Line Graph
# #here we can use df.index or the matplotlib wil automatically take the index 
plt.plot(df.index, df['Height']) #marker='o')
plt.xticks(rotation=45)
plt.title("Height Trend of Hills")
plt.xlabel("Index")
plt.ylabel("Height")
# plt.savefig("graphs\height_trend.png")
plt.show()


#Stacked
category_region=df.groupby(['Region','Height Category']).size().unstack(fill_value=0)#this groups our data into combinations   
category_region.plot(kind='bar',stacked=True)

plt.title("Height Category Count per Region")
plt.xlabel("Region")
plt.ylabel("Count")
plt.tight_layout()
# plt.savefig("graphs\height_category_stacked.png")
plt.show()

#Histogram
plt.figure()
plt.hist(df['Height'],bins=10,color='skyblue',edgecolor='black')
plt.title("Height Distribution")
plt.xlabel("Height")
plt.ylabel("Frequency")
# plt.savefig("graphs\height_histogram.png")
plt.show()

#Insights
tall_region=df.loc[df['Height'].idxmax(),'Region']
common_category=df['Height Category'].value_counts().idxmax()
print("Region with tallest hills:",tall_region)
print("Most common height category:",common_category)