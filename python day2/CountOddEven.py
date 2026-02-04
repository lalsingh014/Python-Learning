nums = [10, 21, 34, 55, 62, 77]

even = 0
odd = 0

for num in nums:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Even count:", even)
print("Odd count:", odd)
