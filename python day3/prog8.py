def find_largest(nums):
    largest = nums[0]
    for n in nums:
        if n > largest:
            largest = n
    return largest


nums = []
for _ in range(5):
    nums.append(int(input("Enter number: ")))

print("Largest:", find_largest(nums))
