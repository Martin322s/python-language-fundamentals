nums = input().split(", ")

result = [el for el in range(len(nums)) if int(nums[el]) % 2 == 0]

print(result)