events = input().split('|')

energy = 100
coins = 100

is_closed = False

for event in events:
    event = event.strip()
    name, value_str = event.split('-', 1)
    value_str = value_str.strip('> ')
    value = int(float(value_str))

    if name == "rest":
        old_energy = energy
        energy += value
        if energy > 100:
            energy = 100
        gained = energy - old_energy
        print(f"You gained {gained} energy.")
        print(f"Current energy: {energy}.")

    elif name == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        cost = value
        if coins >= cost:
            coins -= cost
            print(f"You bought {name}.")
        else:
            print(f"Closed! Cannot afford {name}.")
            is_closed = True
            break

if not is_closed:
    print("Day completed!")
    print(f"Coins: {coins}")
    print(f"Energy: {energy}")