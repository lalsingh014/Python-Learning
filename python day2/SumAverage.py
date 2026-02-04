nums = []

n = int(input("How many numbers? "))

for i in range(n):
    val = int(input("Enter number: "))
    nums.append(val)

total = sum(nums)
avg = total / n

print("Numbers:", nums)
print("Sum:", total)
print("Average:", avg)
