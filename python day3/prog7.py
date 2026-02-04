def count_vowels(word):
    count = 0
    for ch in word.lower():
        if ch in "aeiou":
            count += 1
    return count


sentence = input("Enter sentence: ")
words = sentence.split()

for w in words:
    print(w, "->", count_vowels(w))
