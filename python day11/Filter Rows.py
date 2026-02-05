import pandas as pd 

df = pd.read_csv("students.csv")

filtered = df[df["age"]>21]

print("students with age >21:\n")
print(filtered)