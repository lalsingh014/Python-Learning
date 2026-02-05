from utils import is_prime, factorial

n = int(input("Enter number: "))

print("Prime?", is_prime(n))
print("Factorial:", factorial(n))

from utils import count_vowels

s = input("Enter a sentence: ")
v = count_vowels(s)
print("Vowel count:", v)
