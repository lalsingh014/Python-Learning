import csv
rows = [
    ["name", "age", "course"],
    ["Ankur", 23, "MS"],
    ["Palash", 19, "M.Tech"],
    ["Pragati", 21, "B.Com"]
]


with open("students.csv", "w", newline = "") as f:
    writer = csv.writer(f)
    writer.writerows(rows)
    
print("students.csv created")