numbers_count = int(input())

numbers_list = []
result_list = []

for _ in range(0, numbers_count):
	current_number = int(input())
	numbers_list.append(current_number)

filter_word = input()

if filter_word == 'even':
	for i in range(0, numbers_count):
		if numbers_list[i] % 2 == 0 or numbers_list[i] == 0:
			result_list.append(numbers_list[i])
elif filter_word == 'odd':
	for i in range(0, numbers_count):
		if numbers_list[i] % 2 != 0:
			result_list.append(numbers_list[i])
elif filter_word == 'positive':
	for i in range(0, numbers_count):
		if numbers_list[i] >= 0:
			result_list.append(numbers_list[i])
elif filter_word == 'negative':
	for i in range(0, numbers_count):
		if numbers_list[i] < 0:
			result_list.append(numbers_list[i])

print(result_list)