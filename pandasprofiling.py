import pandas as pd
from ydata_profiling import ProfileReport

# 1. Load the dataset
df = pd.read_csv("clean_employee_data.csv")

# 2. Display basic information
print("Dataset Shape:", df.shape)
print("\nColumn Names:")
print(df.columns.tolist())

print("\nDataset Information:")
df.info()

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# 3. Generate Pandas Profiling report
profile = ProfileReport(
    df,
    title="Last-Mile Delivery Route Performance Analysis",
    explorative=True,
    minimal=False
)

# 4. Export report to HTML
profile.to_file("employee_report.html")

print("\nProfiling report generated successfully!")
print("Open employee_report.html in your browser.")