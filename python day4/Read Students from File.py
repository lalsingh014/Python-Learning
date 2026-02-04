with open("students.txt", "r") as f:
    for line in f:
        name,age = line.strip().split(",")
        print("His/Her Name is :", name, "\nand His/Her Age is :", age)