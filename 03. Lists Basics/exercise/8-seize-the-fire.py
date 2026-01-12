fires_input = input()
water = int(input())

cells_put_out = []
total_fire = 0
effort = 0.0

fires = fires_input.split("#")

for cell in fires:
    fire_type, value_str = cell.split(" = ")
    value = int(value_str)

    is_valid = False

    if fire_type == "High" and 81 <= value <= 125:
        is_valid = True
    elif fire_type == "Medium" and 51 <= value <= 80:
        is_valid = True
    elif fire_type == "Low" and 1 <= value <= 50:
        is_valid = True

    if not is_valid:
        continue

    if water < value:
        continue

    water -= value
    total_fire += value
    effort += value * 0.25
    cells_put_out.append(value)

print("Cells:")
for cell_value in cells_put_out:
    print(f" - {cell_value}")

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")