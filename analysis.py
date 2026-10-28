from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 1. Load CSV
BASE_DIR = Path(__file__).resolve().parent
csv_file = BASE_DIR / "student_performance.csv"
df = pd.read_csv(csv_file)

print("\n=== 1. ORIGINAL DATA ===")
print(df)

# 2. Dataset structure
print("\n=== 2. DATASET STRUCTURE ===")
print("Rows and columns:", df.shape)
print("Column names:", list(df.columns))
print("\nData types:")
print(df.dtypes)
print("\nInfo:")
df.info()

# 3. Missing values and duplicates
print("\n=== 3. DATA QUALITY CHECK ===")
print("Missing values per column:")
print(df.isnull().sum())
print("Duplicate rows:", df.duplicated().sum())

# 4. Clean data
clean_df = df.drop_duplicates().copy()

# Fill numeric missing values with each column's mean.
numeric_cols = ["Age", "Study_Hours", "Marks"]
for col in numeric_cols:
    clean_df[col] = clean_df[col].fillna(clean_df[col].mean())

print("\n=== 4. CLEANED DATA ===")
print(clean_df)
print("Missing values after cleaning:")
print(clean_df.isnull().sum())
print("Duplicate rows after cleaning:", clean_df.duplicated().sum())

# 5. Basic statistics
print("\n=== 5. STATISTICS ===")
print(clean_df[["Age", "Study_Hours", "Marks"]].describe())
print("Average marks:", round(clean_df["Marks"].mean(), 2))
print("Highest marks:", clean_df["Marks"].max())
print("Lowest marks:", clean_df["Marks"].min())
print("Average study hours:", round(clean_df["Study_Hours"].mean(), 2))

# 6. Save graphs
graph_dir = BASE_DIR / "graphs"
graph_dir.mkdir(exist_ok=True)

# Bar chart: marks by student
plt.figure(figsize=(9, 5))
plt.bar(clean_df["Name"], clean_df["Marks"])
plt.title("Student Marks")
plt.xlabel("Student")
plt.ylabel("Marks")
plt.xticks(rotation=35, ha="right")
plt.tight_layout()
plt.savefig(graph_dir / "1_student_marks.png")
plt.close()

# Scatter plot: study hours vs marks
plt.figure(figsize=(7, 5))
plt.scatter(clean_df["Study_Hours"], clean_df["Marks"])
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")
plt.tight_layout()
plt.savefig(graph_dir / "2_study_hours_vs_marks.png")
plt.close()

# Histogram: marks distribution
plt.figure(figsize=(7, 5))
plt.hist(clean_df["Marks"], bins=5, edgecolor="black")
plt.title("Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.savefig(graph_dir / "3_marks_histogram.png")
plt.close()

print("\nGraphs saved in:", graph_dir)
print("Project analysis completed!")
print("\n clean data-----")
print(df.head())
print("\n Total student:",len(df))
print("\n average",round(df["Marks"].mean(),2))
print("\nhightest Marks:",df["Marks"].max())
print(df)
print("\nlowest Marks:",df["Marks"].min())
print("Average study Hours:",round(df["Study_Hours"].mean(),2))
print("\n---student Marks---")
print(df[["Name","Marks"]])
print("\nStudent scoring 80 or more:")
print(df[df["Marks"]>=80][["Name","Marks"]])
print(df[["Name","Study_Hours","Marks"]])







