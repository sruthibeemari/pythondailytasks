  # ============================================================
# 📊 Project Title: Car Data Analysis
# Analyze Car Data dataset using NumPy, Pandas, Matplotlib
# ============================================================


# ============================================================
# 📦 1. Import Required Libraries
# ============================================================
# 👉 Import numpy
# 👉 Import pandas
# 👉 Import matplotlib.pyplot
# 👉 (Optional) Import os for folder creation

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os


# ============================================================
# 📁 2. Setup Project Structure
# ============================================================
# 👉 Create a folder named "graphs"
# 👉 Ensure it does not throw error if already exists
os.makedirs("graphs", exist_ok=True)

'''
#============================================================
# 🟢 SCENARIO 1: Data Loading & Basic Cleaning
# ============================================================
Understand the dataset structure and prepare it for analysis.
👉 Tasks:
● Load the dataset using Pandas.
● Display:○ First 5 rows ○ Last 5 rows ○ Column names ○ Shape of dataset
● Check data types of all columns.
● Check for missing values in:○ Selling_Price ○ Present_Price ○ Kms_Driven ○ Fuel_Type
● Fill missing values:○ Selling_Price → mean ○ Present_Price → mean ○ Kms_Driven → mean ○ Fuel_Type → mode
● Convert numeric columns to proper numeric type if required:
○ Selling_Price
○ Present_Price
○ Kms_Driven
○ Year
● Convert Selling_Price and Kms_Driven into NumPy arrays.
● Use NumPy to calculate:
○ minimum selling price 
○ maximum selling price 
○ average selling price
'''
df = pd.read_csv("cardata.csv")

'''
#============================================================
# 🟢 Scenario 2: Selling Price Trend (Line Graph)
# ============================================================
👉 Tasks:
● Select:
○ Car_Name
○ Selling_Price
● Take the first 10 rows only using Pandas.
● Convert Selling_Price into a NumPy array.
● Plot a line graph using Matplotlib:
○ X-axis → row index (0–9)
○ Y-axis → Selling Price
● Add:
○ title
○ x-axis label
○ y-axis label
○ markers
● Save the graph with a suitable filename
'''
#<code here>
'''
#============================================================
# 🟡 Scenario 3: Expensive Cars Analysis (Filtering + Bar)
# ============================================================
👉 Tasks:
Find which fuel types are most common among expensive cars.
👉 Tasks:
● Filter cars where:
○ Selling_Price > 10
● Group the filtered data by:
○ Fuel_Type
● Count number of cars in each fuel type.
● Convert:
○ fuel type labels
○ counts
into NumPy arrays.
● Plot a bar chart using Matplotlib:
○ X-axis → Fuel Type
○ Y-axis → Count of expensive cars
● Add:○ title ○ x-label ○ y-label
● Save the graph.
'''
# Filter expensive cars
filt = df[df['Selling_Price'] > 10]

# Count cars by fuel type
fuel_counts = filt['Fuel_Type'].value_counts()

# Convert to NumPy arrays
labels = fuel_counts.index.to_numpy()
values = fuel_counts.values

# Plot bar chart
plt.figure()
plt.bar(labels, values)
plt.title("Expensive Cars by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Count of Cars")

# Save and show
# plt.savefig("expensive_cars_bar.png")
plt.show()

'''
#============================================================
# 🟡 Scenario 4: Fuel Type Distribution (Pie Chart)
# ============================================================
👉 Tasks:
● Count the number of cars in each:
○ Fuel_Type
● Select all categories or top categories if needed.
● Prepare:
○ labels
○ values
● Convert values into a NumPy array.
● Plot a pie chart using Matplotlib.
● Add:○ percentage labels ○ title
● Save the graph.
'''
fuel_count=df['Fuel_Type'].value_counts()
labels=fuel_count.index.tolist()
values=fuel_count.values

values=np.array(values)


plt.figure(figsize=(8,8))
plt.pie(values,labels=labels,autopct='%1.1f%%',)
plt.title("Distribution of cars by Fuel Type",fontweight='bold')

# plt.savefig('fuel_type_distribution.png')
plt.show()
'''
#============================================================
# 🟡 Scenario 5: Present Price vs Selling Price (Scatter Plot)
# ============================================================
Check whether cars with higher present price also have higher selling price.
👉 Tasks:
● Select:
○ Present_Price
○ Selling_Price
● Remove missing values if any.
● Take a smaller sample (for example first 50 or 100 rows) using Pandas.
● Convert both columns into NumPy arrays.
● Plot a scatter plot using Matplotlib:
○ X-axis → Present_Price
○ Y-axis → Selling_Price
● Add:○ title ○ x-label ○ y-label
● Observe whether there is a positive relationship.
● Save the graph.
'''
#5.1 Select Present_Price and Selling_Price columns
data = df[['Present_Price', 'Selling_Price']]


# 5.2 Remove missing values
data = data.dropna()


#5.3 Take a smaller sample (first 100 rows)
sample_data = data.head(100)


#5.4 Convert columns to NumPy arrays
x = np.array(sample_data['Present_Price'])
y = np.array(sample_data['Selling_Price'])


#5.5 Plot scatter plot (X-axis → Present_Price, Y-axis → Selling_Price)
plt.figure(figsize=(8, 6))
plt.scatter(x, y, color='blue', alpha=0.7)


#5.6 Add title and labels
plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")


#5.7 & 5.8 Save the graph
# plt.savefig("scatter_plot.png")


# Show the plot
plt.show()

#=====================================================================
# Scenario 6: Car Age Category Analysis + Bar Chart
#=====================================================================
# ● Create a new column using Pandas:
# Car Age Category
# ● Year >= 2015 → "New"
# ● 2010 to 2014 → "Medium"
# ● < 2010 → "Old"
# ● Count number of cars in each:
# ○ Car Age Category
# ● Convert category names and counts into NumPy arrays.
# ● Plot a bar chart using Matplotlib:
# ○ X-axis → Car Age Category
# ○ Y-axis → Count
# ● Add title and labels.
# ● Save the graph.
#=====================================================================
#code
#=====================================================================
# Scenario 7: Kms Driven Distribution (Histogram
#=====================================================================
# ● Select:
# ○ Kms_Driven
# ● Convert it into a NumPy array.
# ● Plot a histogram using Matplotlib:
# ○ X-axis → Kms Driven
# ○ Y-axis → Frequency
# ● Choose suitable number of bins.
# ● Add:
# ○ title
# ○ x-label
# ○ y-label
# ● Save the graph.
# ● Observe whether most cars have lower or higher mileage.
#=====================================================================
#code

#=====================================================================
#Scenario 8: Transmission-wise Selling Price Comparison
#=====================================================================
# ● Group data by:
# ○ Transmission
# ● Calculate:
# ○ average Selling_Price
# ● Convert transmission labels and average prices into NumPy arrays.
# ● Plot a bar chart using Matplotlib:
# ○ X-axis → Transmission
# ○ Y-axis → Average Selling Price
# ● Add title and labels.
# ● Save the graph.
#=====================================================================
#code

#=====================================================================
#Scenario 9: Seller Type Analysi
#=====================================================================
# ● Count number of cars by:
# ○ Seller_Type
# ● Convert results into NumPy arrays.
# ● Plot a bar chart or pie chart using Matplotlib.
# ● Add labels and title.
# ● Save the graph.
# ● Identify which seller type is more common.
#=====================================================================

# Count number of cars by Seller_Type
seller_counts = df['Seller_Type'].value_counts()

# Convert results into NumPy arrays
seller_types = np.array(seller_counts.index)
counts = np.array(seller_counts.values)

# Print arrays 
print("Seller Types:", seller_types)
print("Counts:", counts)

# Plot Bar Chart
plt.figure(figsize=(6,4))
plt.bar(seller_types, counts, color=['skyblue', 'orange'])
plt.xlabel("Seller Type")
plt.ylabel("Number of Cars")
plt.title("Number of Cars by Seller Type")

# Save the graph
plt.savefig("seller_type_bar_chart.png")

# Show plot
plt.show()

# Optional: Pie Chart
plt.figure(figsize=(6,6))
plt.pie(counts, labels=seller_types, autopct='%1.1f%%', startangle=90)
plt.title("Seller Type Distribution")

# Save pie chart
# plt.savefig("seller_type_pie_chart.png")

plt.show()

# Identify most common seller type
most_common = seller_counts.idxmax()
print("Most common seller type:", most_common)
#=====================================================================
#Scenario 10: Advanced Analysis + Multiple Graphs
#=====================================================================
#----------------------------------------------------------------------
# �� Part 1: Feature Creation
#----------------------------------------------------------------------
# Create a new column:
# Price Difference
# ● Price Difference = Present_Price - Selling_Price
# This shows how much value the car has depreciated.
#----------------------------------------------------------------------
df['Price_Difference'] = df['Present_Price'] - df['Selling_Price']

#----------------------------------------------------------------------
# Part 2: NumPy Usage
#----------------------------------------------------------------------
# ● Convert Selling_Price into a NumPy array.
# ● Use NumPy to calculate price changes between consecutive rows using:
# ○ np.diff()
# ● Convert Price Difference column into a NumPy array.
# ● Find:
# ○ average depreciation
# ○ maximum depreciation
# ○ minimum depreciation
#----------------------------------------------------------------------
#10.2.1 Convert Selling_Price into a NumPy array
selling_array = df['Selling_Price'].to_numpy()

#10.2.2 Calculate price changes between consecutive rows using np.diff()
price_changes = np.diff(selling_array)

#10.2.3 Convert Price Difference column into a NumPy array
diff_array = df['Price_Difference'].to_numpy()

#10.2.4 Calculate average, maximum, and minimum depreciation
avg_depreciation = np.mean(diff_array)
max_depreciation = np.max(diff_array)
min_depreciation = np.min(diff_array)

# Print results
print("Average Depreciation:", avg_depreciation)
print("Maximum Depreciation:", max_depreciation)
print("Minimum Depreciation:", min_depreciation)
#----------------------------------------------------------------------
# Part 3: Visualizations
#----------------------------------------------------------------------
# �� Line Graph
# ● Plot Selling_Price trend for all cars.
# �� Bar Chart
# ● Show average Selling_Price by Fuel_Type.
# �� Histogram
# ● Plot distribution of Selling_Price.
#----------------------------------------------------------------------
# -------- Line Graph --------
#10.3.1 Plot Selling_Price trend for all cars
plt.figure(figsize=(8, 5))
plt.plot(df['Selling_Price'], color='blue')
plt.title("Selling Price Trend")
plt.xlabel("Car Index")
plt.ylabel("Selling Price")
# plt.savefig("line_plot.png")
plt.show()


# -------- Bar Chart --------
#10.3.2 Show average Selling_Price by Fuel_Type
fuel_avg = df.groupby('Fuel_Type')['Selling_Price'].mean()

plt.figure(figsize=(8, 5))
fuel_avg.plot(kind='bar', color='orange')
plt.title("Average Selling Price by Fuel Type")
plt.xlabel("Fuel Type")
plt.ylabel("Average Selling Price")
# plt.savefig("bar_chart.png")
plt.show()


# -------- Histogram --------
#10.3.3 Plot distribution of Selling_Price
plt.figure(figsize=(8, 5))
plt.hist(df['Selling_Price'], bins=20, color='green', edgecolor='black')
plt.title("Distribution of Selling Price")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
# plt.savefig("histogram.png")
plt.show()


#----------------------------------------------------------------------
#�� Part 4: Insights
#----------------------------------------------------------------------
# Answer these:
# ● Which fuel type has the highest average selling price?
# ● Which transmission type has higher average selling price?
# ● Are most cars concentrated in lower selling prices or higher selling prices?
# ● Do older cars tend to have lower selling prices?
#----------------------------------------------------------------------
#10.4.1 Which fuel type has the highest average selling price?
print("\nFuel Type with Highest Avg Selling Price:")
print(fuel_avg.idxmax())


#10.4.2 Which transmission type has higher average selling price?
trans_avg = df.groupby('Transmission')['Selling_Price'].mean()
print("\nTransmission Type with Higher Avg Selling Price:")
print(trans_avg.idxmax())


#10.4.3 Are most cars concentrated in lower or higher selling prices?
print("\nObservation:")
print("Check histogram → If bars are taller on lower values, most cars are low-priced.")


#10.4.4 Do older cars tend to have lower selling prices?
print("\nObservation:")
print("Compare Year vs Selling_Price (older cars generally show lower prices).")

#----------------------------------------------------------------------
#=====================================================================
