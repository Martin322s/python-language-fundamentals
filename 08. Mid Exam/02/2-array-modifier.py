numbers_list = [int(x) for x in input().split(" ")]

command = input()

while not command == "end":
	command_data = command.split(" ")

	if command_data[0] == "swap":
		first_index = int(command_data[1])
		second_index = int(command_data[2])

		numbers_list[first_index], numbers_list[second_index] = numbers_list[second_index], numbers_list[first_index]
	elif command_data[0] == "multiply":
		first_index = int(command_data[1])
		second_index = int(command_data[2])
		product = numbers_list[first_index] * numbers_list[second_index]
		numbers_list[first_index] = product
	elif command_data[0] == "decrease":
		numbers_list = [x - 1 for x in numbers_list]
	
	command = input()

# stringified_list = list(map(str, numbers_list))
# print(", ".join(stringified_list))

stringified_list = [str(x) for x in numbers_list]
print(", ".join(stringified_list))