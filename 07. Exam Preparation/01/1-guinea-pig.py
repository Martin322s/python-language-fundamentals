food_quantity_per_month = float(input()) * 1000
hay_quantity_per_month = float(input()) * 1000
cover_quantity_per_month = float(input()) * 1000
pig_weight = float(input()) * 1000

for day in range(1, 31):
	food_quantity_per_month -= 300

	if day % 2 == 0:
		food_amount = food_quantity_per_month * 0.05
		hay_quantity_per_month -= food_amount

	if day % 3 == 0:
		cover_quantity = (1/3) * pig_weight
		cover_quantity_per_month -= cover_quantity

if food_quantity_per_month <= 0 or hay_quantity_per_month <= 0 or cover_quantity_per_month <= 0:
	print("Merry must go to the pet store!")
else:
	print(f"Everything is fine! Puppy is happy! Food: {(food_quantity_per_month / 1000):.2f}, Hay: {(hay_quantity_per_month / 1000):.2f}, Cover: {(cover_quantity_per_month / 1000):.2f}.")