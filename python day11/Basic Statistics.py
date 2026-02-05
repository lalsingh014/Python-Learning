import pandas as pd

df = pd.read_csv("students.csv")

print("Mean age:", df["age"].mean())
print("maximum age:", df["age"].max())
print("Minimum age:", df["age"].min())