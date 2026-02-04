s = input("Enter a sentence: ")
result = ""

for ch in s:
    if ch != " ":
        result += ch
        
print("without spaces:", result)