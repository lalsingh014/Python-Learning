import csv

new_row = ["Ritesh", 18, "B.Tech"]

with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_row)