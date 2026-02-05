import pandas as pd

df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Python Prog\python day9\students.csv")

print("\nData from CSV in Previous Chapter:\n")
print(df)

df = pd.read_csv("students.csv")

print("\nData from its own CSV:\n")
print(df)