import re

pattern = r'%(?P<name>[A-Z][a-z]+)%[^|$%.]*<(?P<product>\w+)>[^|$%.]*\|(?P<count>\d+)\|[^|$%.]*?(?P<price>\d+(\.\d+)?)\$'

total_income = 0.0

while True:
    line = input()
    if line == "end of shift":
        break

    match = re.search(pattern, line)
    if not match:
        continue

    name = match.group('name')
    product = match.group('product')
    count = int(match.group('count'))
    price = float(match.group('price'))

    total_price = count * price
    total_income += total_price

    print(f"{name}: {product} - {total_price:.2f}")

print(f"Total income: {total_income:.2f}")