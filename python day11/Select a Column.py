import pandas as pd

df = pd.read_csv("students.csv")

print("Names column:\n")
print(df["name"])