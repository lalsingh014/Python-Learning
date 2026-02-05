import json

with open("students.json", "r") as f:
    data = json.load(f)
    
for s in data:
    print(s["name"], s["age"], s["skills"])