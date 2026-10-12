import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# df=pd.read_csv("employee_data.csv")
# print(df.head())

# print("Range of Age:")
# range=(df["Salary"].max())-(df["Salary"].min())
# print(range)

# print("Variance: ")
# vari=df["Salary"].var()
# print(vari)

# print("Standard Deviation : ")
# stand=df["Salary"].std()
# print(stand)

# print("Coefficient of variation: ")
# coe=(stand/df["Salary"].mean())*100
# print(coe)



print("Manually calculated central tendency:")
arr = np.array([20, 40, 25, 60, 50])

# Range
maximum = arr.max()
minimum = arr.min()
range_value = maximum - minimum
print("Range of array is:", range_value)

# Mean
total = arr.sum()
count = len(arr)
mean = total / count
print("Mean of array:", mean)

# Variance
sum1 = 0
for i in arr:
    diff = i - mean
    var = diff ** 2
    sum1 = sum1 + var
variance = sum1 / count
print("Variance is:", variance)

# Standard deviation
std_dev = np.sqrt(variance)
print("Standard Deviation is:", std_dev)

# Coefficient of variation
coe = (std_dev / mean) * 100
print("Coefficient of variation is:", coe)


plt.bar(range(len(arr)), arr)

plt.xlabel("Index")
plt.ylabel("Value")
plt.title("Values in Array")

plt.show()
