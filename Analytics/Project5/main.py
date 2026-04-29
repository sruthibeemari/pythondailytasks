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

