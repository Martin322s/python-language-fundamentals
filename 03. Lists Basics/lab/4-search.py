strings_count = int(input())
search_word = input()

strings_list = []
filtered_list = []

while strings_count > 0:
	current_string = input()
	strings_list.append(current_string)

	if search_word in current_string:
		filtered_list.append(current_string)
	
	strings_count -= 1

print(strings_list)
print(filtered_list)