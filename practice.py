import numpy as np
# 1. Array creation
marks = np.array([[85, 90, 78], [65, 72, 88], [92, 81, 76]])
zeros_arr = np.zeros((2, 3))
range_arr = np.arange(0, 10, 2)
lin_arr = np.linspace(0, 1, 5)
# 2. Array attributes
print('Shape:', marks.shape)
print('Size:', marks.size)
print('Dimensions:', marks.ndim)
print('Data type:', marks.dtype)
# 3. Indexing and slicing
print('First student marks:', marks[0])
print('First subject marks:', marks[:, 0])
print('Sub-array:', marks[0:2, 1:3])
# 4. Reshaping and stacking
reshaped = marks.reshape(9, 1)
flattened = marks.flatten()
stacked = np.vstack([marks, np.array([70, 75, 80])])
# 5. Universal functions (ufuncs)

sqrt_marks = np.sqrt(marks)
scaled_marks = marks * 1.05 # broadcasting
# 6. Statistical functions
print('Mean per subject:', np.mean(marks, axis=0))
print('Max marks:', np.max(marks))
print('Standard deviation:', np.std(marks))
# 7. Linear algebra
matrix_a = np.array([[1, 2], [3, 4]])
matrix_b = np.array([[5, 6], [7, 8]])
print('Matrix product:', np.matmul(matrix_a, matrix_b))
print('Determinant:', np.linalg.det(matrix_a))
# 8. Random module
random_arr = np.random.randint(1, 100, size=(3, 3))
print('Random array:', random_arr)

#Case Study
import numpy as np
# 1. Case Study A: Analyzing Student Grades with NumPy
grades = np.array([[78, 82, 91], [65, 70, 74], [88, 95, 90], [55, 60, 58]])
print('Average per student:', np.mean(grades, axis=1))
print('Average per subject:', np.mean(grades, axis=0))
print('Topper score:', np.max(grades))
print('Standard deviation:', np.std(grades))
# 2. Case Study B: Analyzing Historical Stock Prices
prices = np.array([100, 102, 101, 105, 107, 110, 108, 112, 115, 113])
# Daily returns (vectorized, no explicit loop)
daily_returns = (prices[1:] - prices[:-1]) / prices[:-1]
print('Daily returns:', daily_returns)
# Moving average using array slicing
window = 3
moving_avg = np.array([
np.mean(prices[i:i + window]) for i in range(len(prices) - window + 1)
])
print('Moving average:', moving_avg)
# Volatility (standard deviation of daily returns)
volatility = np.std(daily_returns)
print('Volatility:', volatility)
# 3. Vectorized operation vs loop (performance benefit)
scaled_prices = prices * 1.02 # broadcasting, no explicit loop
print('Scaled prices:', scaled_prices)








asignment 2 :
    
    
    
    
    
    
    import pandas as pd
# 1. Load and display data
df = pd.read_csv('SuperstoreSales.csv') # or Covid19.csv / StudentPerformance.csv
print(df.head())
print(df.info())
print(df.describe())
# 2. Access and manipulate specific data segments
print(df['Sales']) # single column
print(df[['Region', 'Sales', 'Profit']]) # multiple columns
print(df.loc[0:5, ['Region', 'Sales']]) # label based indexing
print(df.iloc[0:5, 0:3]) # position based indexing
high_profit = df[df['Profit'] > 100] # boolean filtering
# 3. Group-by and aggregation operations
region_sales = df.groupby('Region')['Sales'].sum()
print(region_sales)
summary = df.groupby('Category').agg(
Total_Sales=('Sales', 'sum'),
Avg_Profit=('Profit', 'mean'),

Order_Count=('Order ID', 'count')
)
print(summary)
# 4. Transform and enrich data structures
df['Profit_Margin'] = df['Profit'] / df['Sales']
df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Order_Month'] = df['Order Date'].dt.month
df.fillna(0, inplace=True) # handling missing values
df.rename(columns={'Sales': 'Revenue'}, inplace=True)
# 5. Domain-specific analysis
monthly_trend = df.groupby('Order_Month')['Revenue'].sum()
top_products = df.groupby('Product Name')
['Revenue'].sum().sort_values(ascending=False).head(10)
print('Monthly Revenue Trend:\n', monthly_trend)
print('Top 10 Products:\n', top_products)     








assignment 3: 
    
    
    
    
    
    
import pandas as pd
import numpy as np
from scipy import stats
# 1. Load data (Superstore Sales / COVID-19 / Student Performance dataset)
df = pd.read_csv('StudentPerformance.csv') # replace with dataset of choice
print(df.head())
print(df.describe())
# 2. Mean, Median, Mode using Pandas
mean_val = df['Marks'].mean()
median_val = df['Marks'].median()
mode_val = df['Marks'].mode()[0]
print('Mean:', mean_val)
print('Median:', median_val)
print('Mode:', mode_val)

# 3. Mean, Median, Mode using NumPy / SciPy
marks_array = df['Marks'].to_numpy()
print('NumPy Mean:', np.mean(marks_array))
print('NumPy Median:', np.median(marks_array))
print('SciPy Mode:', stats.mode(marks_array, keepdims=True))
# 4. Central tendency grouped by a category (e.g., Gender, Region, Country)
group_summary = df.groupby('Gender')['Marks'].agg(['mean', 'median',
lambda x: x.mode()[0]])
group_summary.columns = ['Mean', 'Median', 'Mode']
print(group_summary)
# 5. Comparing measures to understand data distribution/skewness
print('Skewness:', df['Marks'].skew())
if mean_val > median_val:
print('Distribution is right (positively) skewed')
elif mean_val < median_val:
print('Distribution is left (negatively) skewed')
else:
print('Distribution is approximately symmetric')



assignment 4:
    
    
    
 import pandas as pd
import numpy as np
# 1. Load data (e.g., Daily Temperatures in Two Cities / Customer Wait Times)
df = pd.read_csv('CityTemperatures.csv') # columns: 'City_A', 'City_B'
print(df.head())
print(df.describe())
# 2. Range
range_a = df['City_A'].max() - df['City_A'].min()
range_b = df['City_B'].max() - df['City_B'].min()
print('Range - City A:', range_a)
print('Range - City B:', range_b)
# 3. Variance
var_a = df['City_A'].var() # sample variance (ddof=1 by default in Pandas)
var_b = df['City_B'].var()
print('Variance - City A:', var_a)
print('Variance - City B:', var_b)

# 4. Standard Deviation
std_a = df['City_A'].std()
std_b = df['City_B'].std()
print('Std Dev - City A:', std_a)
print('Std Dev - City B:', std_b)
# 5. Coefficient of Variation (relative variability, unit-free comparison)
cv_a = (std_a / df['City_A'].mean()) * 100
cv_b = (std_b / df['City_B'].mean()) * 100
print('CV% - City A:', cv_a)
print('CV% - City B:', cv_b)
# 6. Interpretation
if std_a < std_b:
print('City A has more consistent temperatures than City B')
else:
print('City B has more consistent temperatures than City A')   
    
    