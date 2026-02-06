groceries = input().split("!")
command_data = input()

while not command_data == "Go Shopping!":
	data = command_data.split(" ")

	if data[0] == "Urgent":
		item = data[1]

		if item not in groceries:
			groceries.insert(0, item)
	elif data[0] == "Unnecessary":
		item = data[1]

		if item in groceries:
			groceries.remove(item)
	elif data[0] == "Correct":
		old_item = data[1]
		new_item = data[2]

		if old_item in groceries:
			index = groceries.index(old_item)
			groceries[index] = new_item
	elif data[0] == "Rearrange":
		item = data[1]

		if item in groceries:
			groceries.remove(item)
			groceries.append(item)

	command_data = input()

print(", ".join(groceries))