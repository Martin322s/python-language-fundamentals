key_value_pair = input()
products = {}

total_products = 0
total_quantity = 0

while not key_value_pair == "statistics":
	product, quantity = key_value_pair.split(": ")

	if not product in products:
		products[product] = int(quantity)
		total_products += 1
	else:
		products[product] += int(quantity)

	total_quantity += int(quantity)

	key_value_pair = input()

print("Products in stock:")
for key, value in products.items():
	print(f"- {key}: {value}")
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")