def square(x):
    return x * x

nums = [54,34,32,22,134,584,65,31,78]

total = 0
for n in nums:
    total += square(n)

print("Sum of squares:", total)
