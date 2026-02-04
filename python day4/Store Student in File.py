students = [
    {"name": "Ad", "age": 23},
    {"name": "Vinni", "age": 21}
]

with open("students.txt", "w") as f:
    for s in students:
        line = f"{s['name']},{s["age"]}\n"
        f.write(line)
    