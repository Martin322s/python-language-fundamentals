def add_element(dict, key, value):
	dict[key] = int(value)

food_list = input().split(" ")
bakery_dict = {}

for i in range(len(food_list)):
	if i % 2 == 0:
		add_element(bakery_dict, food_list[i], food_list[i + 1])

searched_stocks = input().split(" ")

for stock in searched_stocks:
	if bakery_dict.get(stock):
		print(f"We have {bakery_dict.get(stock)} of {stock} left")
	else:
		print(f"Sorry, we don't have {stock}")