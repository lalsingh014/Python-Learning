import pandas as pd

data = {
    "name": ["Lemma", "Aemy", "Riva"],
    "age": [24, 21, 23],
    "course": ["MCA AI", "BS", "M.Tech"]
}

df = pd.DataFrame(data)

print("Full DataFrame:\n")
print(df)