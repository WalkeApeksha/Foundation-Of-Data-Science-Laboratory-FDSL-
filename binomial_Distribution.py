import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import binom

df=pd.read_csv("clean_employee_data.csv")
print(df.head())
print(df.tail())
print(df.info())
print(df.describe())
n=10
p=(df["Department"].str.strip().str.lower()=="it").mean()
print("Probability of selecting IT department is:",p)
x=np.arange(0,n+1)
probability=binom.pmf(x,n,p)
for i in range(n + 1):
    print(f"{i} IT employees: {probability[i]:.4f}")
mean=n*p
plt.figure(figsize=(8,5))
plt.bar(x,probability,color="pink",edgecolor="blue",label='PMF')
plt.axvline(mean,color='red',linestyle='--',label='Mean')
plt.title("Binomial Distribution ")
plt.xlabel("NUmber of IT employees")
plt.ylabel("Probability")
plt.legend()
plt.show()


