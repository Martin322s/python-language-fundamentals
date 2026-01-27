wagons_count = int(input())
train = [0 for _ in range(wagons_count)]

command = input()

while command != "End":
	command_list = command.split(" ")

	if command_list[0] == "add":
		train[len(train) - 1] += int(command_list[1])
	elif command_list[0] == "insert":
		index = int(command_list[1])
		people = int(command_list[2])
		train[index] += people
	elif command_list[0] == "leave":
		index = int(command_list[1])
		people = int(command_list[2])
		train[index] -= people

	command = input()

print(train)