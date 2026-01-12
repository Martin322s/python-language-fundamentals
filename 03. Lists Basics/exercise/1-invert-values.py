input_string = input()

input_list = input_string.split(' ')

for i in range(len(input_list)):
	input_list[i] = int(input_list[i])

	if input_list[i] < 0:
		input_list[i] = input_list[i] + (abs(input_list[i]) * 2)
	else:
		input_list[i] = input_list[i] - (abs(input_list[i]) * 2)

print(input_list)