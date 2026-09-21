import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

df=pd.read_csv("employee_data.csv")
print(df.head())
print(df.describe())
print(df.info())

print("Mean is : ",np.mean(df["Age"]))
print("Standard Deviation: ",np.std(df["Age"]))
print("Variance is: ",np.var(df["Age"]))

x=np.linspace(np.mean(df["Age"])-4*np.std(df["Age"]),1000)
y=norm.pdf(x,np.mean(df["Age"]),np.std(df["Age"]))
plt.figure(figsize=(8,5))
plt.plot(x,y,color="blue",label="Normal Distribution curve")
plt.title("Normal Distribution curve")
plt.xlabel("value ")
plt.ylabel("Probability Density")
plt.legend()
plt.show()