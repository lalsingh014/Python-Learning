import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set(style="whitegrid")

# Load cleaned dataset
df = pd.read_csv("titanic_cleaned.csv")


# Age Distribution

plt.figure()
sns.histplot(df["age"], bins=30, kde=True)
plt.title("Age Distribution of Passengers")
plt.xlabel("Age")
plt.ylabel("Count")
plt.show()


# Age vs Survival

plt.figure()
sns.histplot(df, x="age", hue="survived", bins=30, kde=True)
plt.title("Age distribution by Survival")
plt.xlabel("Age")
plt.show()



# Gender vs Survival

plt.figure()
sns.barplot(x="sex", y="survived", data=df)
plt.title("Survival Rate by Gender")
plt.ylabel("Survival Probability")
plt.show()



# Passenger Class vs Survival

plt.figure()
sns.barplot(x="pclass", y="survived", data=df)
plt.title("Survival Rate by Passenger Class")
plt.ylabel("Survival Probability")
plt.show()



# Fare vs Survival

plt.figure()
sns.boxplot(x="survived", y="fare", data=df)
plt.title("Fare Distribution by Survival")
plt.xlabel("Survival (0 = No, 1 = Yes)")
plt.ylabel("Fare")
plt.show()



# Family Size vs Survival

plt.figure()
sns.barplot(x="family_size", y="survived", data=df)
plt.title("Survival Rate by Family Size")
plt.ylabel("Survival Probability")
plt.show()
