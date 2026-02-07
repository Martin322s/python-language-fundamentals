numbers = [int(x) for x in input().split(" ")]
numbers_sum = 0
average = 0

for num in numbers:
	numbers_sum += num

average = numbers_sum // len(numbers)

result_list = [x for x in numbers if x > average]
result_list = list(sorted(result_list))
result_list = list(reversed(result_list))

if len(result_list) <= 0:
	print("No")
elif len(result_list) <= 5:
	for num in result_list:
		print(num, end=" ")
else:
	for i in range(5):
		print(result_list[i], end=" ")