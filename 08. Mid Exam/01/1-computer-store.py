part_price = input()
total_price = 0

while True:
	if part_price == "special" or part_price == "regular":
		break

	price = float(part_price)

	if price < 0:
		print("Invalid price!")
	else:
		total_price += price
	
	part_price = input()

taxes = total_price * 0.20
total_price_with_taxes = total_price + taxes

if part_price == "special":
	total_price_with_taxes = total_price_with_taxes - (total_price_with_taxes * 0.10)

if total_price_with_taxes == 0:
	print("Invalid order!")
else:
	print("Congratulations you've just bought a new computer!")
	print(f"Price without taxes: {total_price:.2f}$")
	print(f"Taxes: {taxes:.2f}$")
	print("-----------")
	print(f"Total price: {total_price_with_taxes:.2f}$")