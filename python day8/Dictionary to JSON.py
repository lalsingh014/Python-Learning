import json

student = {
    "name": "Shivya",
    "age": 23,
    "course": "MBA"
}

with open("student.json", "w") as f:
    json.dump(student, f, indent=4)