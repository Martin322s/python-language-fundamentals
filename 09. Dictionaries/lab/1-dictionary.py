def add_element(dict, key, value):
	dict[key] = int(value)

food_list = input().split(" ")
bakery_dict = {}

for i in range(len(food_list)):
	if i % 2 == 0:
		add_element(bakery_dict, food_list[i], food_list[i + 1])

print(bakery_dict)