input_list = input().split(', ')

zeroes_count = 0

while '0' in input_list:
	input_list.remove('0')
	zeroes_count += 1

for _ in range(zeroes_count):
	input_list.append('0')

for i in range(len(input_list)):
	input_list[i] = int(input_list[i])

print(input_list)