products = {}

while True:
    line = input()
    if line == "buy":
        break

    name, price, qty = line.split()
    price = float(price)
    qty = int(qty)

    if name not in products:
        products[name] = [price, qty]
    else:
        products[name][0] = price
        products[name][1] += qty

for name, (price, qty) in products.items():
    total = price * qty
    print(f"{name} -> {total:.2f}")