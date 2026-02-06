import pandas as pd
import seaborn as sns


#step 1
# Load real dataset

df = sns.load_dataset("titanic")

print("First 5rows:\n", df.head())

print("\nShape of data:", df.shape)

print("\nColumns:\n", df.columns)

print("\nInfo:\n")
print(df.info())

print("\nMissing values:\n")
print(df.isnull().sum())

#Basic statistics
print("\nStatistical summary:\n")
print(df.describe())



#step 2
#Data Cleaning

#Fill missing age with median
df["age"] = df["age"].fillna(df["age"].median())

#Drop 'deck' column (too many missing values)
df.drop(columns=["deck"], inplace=True)

print("\nAfter cleaning:\n")
print(df.isnull().sum())



#step 3

#what fraction of passengers survived?
survival_rate = df["survived"].mean()
print("Overall survival rate:", survival_rate)

#did gender affect survival?
survival_by_gender = df.groupby("sex")["survived"].mean()
print("\nSurvival rate by gender:\n", survival_by_gender)

#did passenger class matter?
survival_by_class = df.groupby("pclass")["survived"].mean()
print("\nSurvial rate by passenger class:\n", survival_by_class)

#what is the age distribution by class?
avg_age_by_class = df.groupby("pclass")["age"].mean()
print("\nAverage age by class:\n", avg_age_by_class)




#step 4
#Feature Engineering

df["family_size"] = df["sibsp"] + df["parch"]
print("\nFamily size (first 5 rows):\n", df["family_size"].head())




#step 5
#Export Cleaned Dataset 

df.to_csv("titanic_cleaned.csv", index=False)
print("\nCleaned and engineered dataset saved as titanic_cleaned.csv")