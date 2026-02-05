import csv

rows = [
    ["name", "age", "course"],
    ["Lemma", 23, "MS DS"],
    ["Aemy", 22, "BJMC"]
]

with open("students.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(rows)