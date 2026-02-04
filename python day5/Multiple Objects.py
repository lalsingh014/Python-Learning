class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        
        
students = []

for i in range(2):
    name = input("Name: ")
    age = int(input("Age: "))
    students.append(Student(name,age))
    
for s in students:
    s.display()