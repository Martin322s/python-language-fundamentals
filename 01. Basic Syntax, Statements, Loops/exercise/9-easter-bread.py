budget = float(input())
flour_price = float(input())

eggs_price = flour_price * 0.75
milk_price_per_liter = flour_price * 1.25
milk_price_for_one = milk_price_per_liter / 4

cozonac_price = flour_price + eggs_price + milk_price_for_one

cozonacs_count = 0
colored_eggs = 0

while budget >= cozonac_price:
    budget -= cozonac_price
    cozonacs_count += 1
    colored_eggs += 3

    if cozonacs_count % 3 == 0:
        eggs_lost = cozonacs_count - 2
        colored_eggs -= eggs_lost

print(f"You made {cozonacs_count} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
