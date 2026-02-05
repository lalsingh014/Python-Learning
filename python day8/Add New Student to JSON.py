import json

new_student = {"name": "Cy", "age": 26, "skills": ["Python", "ML", "Git"]}

with open("students.json", "r") as f:
    data = json.load(f)
    
data.append(new_student)

with open("students.json", "w") as f:
    json.dump(data, f, indent=4)