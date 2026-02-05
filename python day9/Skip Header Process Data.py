import csv  

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    next(reader) #skip header
    
    for name, age, course in reader:
        print (name, "is", age, "years old")