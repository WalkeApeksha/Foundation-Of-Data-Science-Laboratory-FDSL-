import numpy as np
import pandas as pd

df=pd.read_csv("employee_data.csv")
print(df.head())

#remove duplicates

df.drop_duplicates(inplace=True)
print(df.info())

#remove extra spaces
df = df.apply(lambda col: col.str.strip() if col.dtype == "object" else col)
df["Gender"]=df["Gender"].str.lower()
df["Gender"]=df["Gender"].replace({
    "m":"male",
    "f":"female",
    "male":"male",
    "female":"female"
})

#handle missing values
df["Age"]=df["Age"].fillna(df["Age"].median())
df["Salary"]=df["Salary"].fillna(df["Salary"].median())
df["Department"]=df["Department"].fillna("unknowm")

#remove invalid ages
df.loc[(df["Age"] < 18) | (df["Age"] > 60), "Age"] = np.nan
df["Age"] = df["Age"].fillna(df["Age"].median())

#convert salary to numerical
df["Salary"] = pd.to_numeric(df["Salary"], errors="coerce")
df["Salary"] = df["Salary"].fillna(df["Salary"].median())

#standardize date
df["Joining_Date"] = pd.to_datetime(
    df["Joining_Date"],
    errors="coerce",
    dayfirst=True
)

#validate emails
pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'

df["Email"] = df["Email"].where(
    df["Email"].str.match(pattern, na=False),
    np.nan
)

#fill missing values
df["Email"]=df["Email"].fillna("not available")

#standardize city names
df["City"]=df["City"].str.title()

#reset index
df.reset_index(drop=True, inplace=True)

print("\nCleaned Dataset")
print(df.head())

# Save cleaned dataset
df.to_csv("clean_employee_data.csv", index=False)

print("\nCleaning Completed Successfully!")


print(df.info())
print(df.describe())
print(df.isnull().sum())
print(df.nunique())
print(df["Department"].value_counts())
print(df["Gender"].value_counts())
print(df["Salary"].min())
print(df["Salary"].max())
print(df["Salary"].median())

print(df.corr(numeric_only=True))























