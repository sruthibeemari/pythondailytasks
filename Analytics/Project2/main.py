''' 
============================================================
 Project Title:  IGN Game Reviews Analysis
 Analyze IGN Game dataset using NumPy, Pandas, Matplotlib
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
1 Scenario 1: Data Loading & Preprocessing
===============================================================
You are given the ign.csv dataset containing game reviews.
👉 Tasks:
1. Load the dataset using Pandas.
2. Display:
○ First 5 rows (head())
○ Last 5 rows (tail())
○ Shape of dataset
3. Remove the unnecessary column:
○ "Unnamed: 0" (index column)
4. Check for missing values in:
○ score, genre, platform
5. Handle missing values:
○ Fill numeric column score with mean
○ Fill categorical column genre with mode
6. Ensure correct data types:
○ score → float
○ release_year, release_month, release_day → integer

'''
df=pd.read_csv('ign.csv')
print(df.head())
print(df.tail())
print(df.shape)

df=df.drop("Unnamed: 0",axis=1)

print(df[["score","genre","platform"]].isnull().sum())

df["score"]=df["score"].fillna(df["score"].mean())
df["genre"]=df["genre"].fillna(df["genre"].mode()[0])
print(df.isnull().sum())

df["score"]=df["score"].astype(float)
df["release_year"]=df["release_year"].astype(int)
df["release_month"]=df["release_month"].astype(int)
df["release_day"]=df["release_day"].astype(int)
print(df.dtypes)

'''
===============================================================
2 Scenario 2: Line Graph (Score Trend) + Save
===============================================================
You want to analyze how game scores change over time.
👉 Tasks:
1. Group data by release_year.
2. Calculate average score per year using Pandas.
3. Convert results into NumPy arrays.
4. Plot a line graph:
○ X-axis → release_year
○ Y-axis → average score
5. Add:
○ Title: "Average Game Score Over Years"
○ Axis labels
6. Save the graph: plt.savefig("avg_score_trend.png")
'''
avg_score=df.groupby("release_year")["score"].mean()

years=np.array(avg_score.index)
scores=np.array(avg_score)

plt.plot(years,scores,marker='o')
plt.xlabel("Release Year")
plt.ylabel("Average Score")
plt.title("Average Game Score Over Years")
plt.tight_layout()
plt.xticks(rotation=45)
plt.savefig('avg_score_trend.png')
plt.show()

'''
===============================================================
3 Scenario 3: Filtering + Bar Chart + Save
===============================================================
You want to compare top platforms.
👉 Tasks:
1. Filter dataset where:
○ score > 7
2. Count number of high-rated games per platform.
3. Select top 10 platforms using Pandas.
4. Convert data into NumPy arrays.
5. Plot a bar chart:
○ X-axis → platform
○ Y-axis → count of games
6. Rotate x-axis labels for readability.
Save the graph: plt.savefig("top_platforms_bar.png")
'''
df_high=df[df["score"]>7]

platform_counts=df_high["platform"].value_counts()

top_platforms=platform_counts.head(10)

platforms=np.array(platform_counts.index)
counts=np.array(platform_counts)

plt.figure(figsize=(12,6))
plt.bar(platforms,counts)
plt.xlabel("Platform")
plt.ylabel("Count of games")
plt.title("Count of High-Rated games for Top 10 platforms")
plt.tight_layout()
plt.xticks(rotation=75)
plt.savefig("top_platforms_bar.png")
plt.show()

'''
===============================================================
4 Scenario 4: Aggregation + Pie Chart + Save
===============================================================
You want to analyze genre distribution.
👉 Tasks:
1. Count the number of games per genre.
2. Select top 5 genres using Pandas.
3. Prepare labels and values.
4. Plot a pie chart:
○ Labels → genre
○ Values → count
5. Add percentage labels (autopct).
Save the graph: plt.savefig("genre_distribution.png")
'''

genre_counts=df["genre"].value_counts()

top_genre=genre_counts.head()

labels=top_genre.index
values=top_genre.values

explode = [0.05, 0.05, 0.05, 0.05, 0.05]
plt.figure(figsize=(6,6))
plt.pie(
    values,
    labels=labels,
    autopct='%1.1f%%',
    explode=explode,
    shadow=True,
    wedgeprops={'edgecolor': 'black'}
)

plt.title("Top 5 Game Genres Distribution")
plt.tight_layout()
plt.savefig("genre_distribution.png")
plt.show()

'''
===============================================================
5 Scenario 5: Advanced Analysis + Multiple Graphs
===============================================================
You are asked to perform a detailed analysis of review patterns.
👉 Part 1: Feature Engineering
1. Create a new column:
○ score_category:
■ score >= 9 → "Excellent"
■ 7 <= score < 9 → "Good"
■ < 7 → "Average"
2. Convert editors_choice:
○ Y → 1, N → 0
👉 Part 2: NumPy Analysis
3. Use NumPy to:
○ Calculate yearly score growth using np.diff() on average yearly scores
👉 Part 3: Visualizations
📈 Line Graph
4. Plot trend of:
○ Average score per release_year
📊 Stacked Bar Chart
5. Show count of:
○ score_category per release_year
📉 Histogram
6. Plot distribution of:
○ score
👉 Part 4: Save All Graphs
plt.savefig("score_trend.png")
plt.savefig("score_category_stacked.png")
plt.savefig("score_distribution.png")
👉 Part 5: Insights
Identify:
● Which years had highest scores
● Whether high scores increased over time
● If editors_choice correlates with high scores
'''

df["score_category"]=df["score"].apply(
    lambda x: "Excellent" if x >= 9 else("Good" if x >= 7 else "Average"))

df["editors_choice"]=df["editors_choice"].map({"Y":1,"N":0})

avg_score = df.groupby("release_year")["score"].mean()

growth=np.diff(avg_score.values)

plt.figure(figsize=(8,5))
plt.plot(avg_score.index,avg_score.values,marker='o')
plt.xlabel("Year")
plt.ylabel("Average Score")
plt.title("Average Score Trend Over Years")
plt.xticks(rotation=40)
plt.tight_layout()
plt.savefig('score_trend.png')
plt.show()

category_counts = df.groupby(["release_year", "score_category"]).size().unstack(fill_value=0)

category_counts.plot(kind="bar", stacked=True, figsize=(10,6))

plt.title("Score Category Distribution Over Years")
plt.xlabel("Year")
plt.ylabel("Count")

plt.xticks(rotation=45)
plt.tight_layout()

plt.savefig("score_category_stacked.png")
plt.show()


plt.figure(figsize=(7,5))

plt.hist(df["score"],bins=10)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("score_distribution.png")
plt.show()

max_year = avg_score.idxmax()
print("Highest score year:", max_year)

print(df.groupby("editors_choice")["score"].mean())






