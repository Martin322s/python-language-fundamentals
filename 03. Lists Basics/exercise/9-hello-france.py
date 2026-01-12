items_input = input()
budget = float(input())

bought_items = []
max_prices = {
    "Clothes": 50.00,
    "Shoes": 35.00,
    "Accessories": 20.50
}

items = items_input.split("|")

for item in items:
    item_type, price_str = item.split("->")
    price = float(price_str)

    if item_type not in max_prices:
        continue

    if price > max_prices[item_type]:
        continue

    if budget < price:
        continue

    budget -= price
    bought_items.append(price)

new_prices = []
for price in bought_items:
    new_price = price * 1.40
    new_prices.append(new_price)

profit = sum(new_prices) - sum(bought_items)

print(" ".join(f"{p:.2f}" for p in new_prices))
print(f"Profit: {profit:.2f}")

final_money = budget + sum(new_prices)

if final_money >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")