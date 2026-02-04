text = input("Enter a sentence: ")

chars = len(text)
words = len(text.split())

vowels = 0
for ch in text.lower():
    if ch in "aeiou":
        vowels += 1
        
        print("Characters:",chars)
        print("Words:",words)
        print("Vowels:",vowels)