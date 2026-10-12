import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read CSV file
df = pd.read_csv("employee_data.csv")

# Display first 5 rows
print(df.head())

# Statistical summary
print(df.describe())

# Information about dataset
print(df.info())


# Select columns
x = df['Age']
y = df['Salary']
z = df['Department']


# ---------------------------------------------------
# 1. LINE CHART - Age vs Salary
# ---------------------------------------------------

plt.figure(figsize=(8, 5))

plt.plot(x, y, marker='o', color='red')

plt.title('Line Chart of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.show()


# ---------------------------------------------------
# 2. BAR CHART - Department vs Salary
# ---------------------------------------------------

plt.figure(figsize=(8, 5))

sns.barplot(x=z, y=y, color='pink')

plt.title('Bar Chart of Department vs Salary')
plt.xlabel('Department')
plt.ylabel('Salary')

plt.xticks(rotation=45)

plt.show()


# ---------------------------------------------------
# 3. BOX PLOT - Age vs Salary
# ---------------------------------------------------

plt.figure(figsize=(8, 5))

sns.boxplot(x=x, y=y, color='pink')

plt.title('Box Plot of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.show()


# ---------------------------------------------------
# 4. HISTOGRAM - Age Distribution
# ---------------------------------------------------

plt.figure(figsize=(8, 5))

sns.histplot(x=x, color='red', bins=10)

plt.title('Distribution of Age')
plt.xlabel('Age')
plt.ylabel('Number of Employees')

plt.show()


# ---------------------------------------------------
# 5. SCATTER PLOT - Age vs Salary
# ---------------------------------------------------

plt.figure(figsize=(8, 5))

sns.scatterplot(x=x, y=y, color='red')

plt.title('Scatter Plot of Age vs Salary')
plt.xlabel('Age')
plt.ylabel('Salary')

plt.show()


# ---------------------------------------------------
# 6. PIE CHART - Employees by Department
# ---------------------------------------------------

department_count = df['Department'].value_counts()

plt.figure(figsize=(8, 8))

plt.pie(
    department_count.values,
    labels=department_count.index,
    autopct='%1.1f%%',
    startangle=90
)

plt.title('Employees by Department')

plt.show()


# ---------------------------------------------------
# 7. HEATMAP - Correlation Matrix
# ---------------------------------------------------

plt.figure(figsize=(8, 6))

# Select numerical columns
numeric_df = df[['Employee_ID', 'Age', 'Salary']]

# Calculate correlation
correlation = numeric_df.corr()

# Create heatmap
sns.heatmap(
    correlation,
    annot=True,
    cmap='coolwarm',
    fmt='.2f'
)

plt.title('Correlation Heatmap')

plt.show()