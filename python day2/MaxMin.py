nums = [12, 45, 7, 89, 23]

largest = nums[0]
smallest = nums[0]

for num in nums:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest:", largest)
print("Smallest:", smallest)
