import json
students = [
    {"name": "Ax", "age": 21, "skills": "Sleeping"},
    {"name": "Bz", "age": 19, "skills": "Eating"}
]

with open("students.json", "w") as f:
    json.dump(students, f, indent=4)