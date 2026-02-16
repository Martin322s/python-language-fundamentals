towns = {}

while True:
    line = input()
    if line == "Sail":
        break

    town, population, gold = line.split("||")
    population = int(population)
    gold = int(gold)

    if town not in towns:
        towns[town] = {"population": population, "gold": gold}
    else:
        towns[town]["population"] += population
        towns[town]["gold"] += gold

while True:
    line = input()
    if line == "End":
        break

    parts = line.split("=>")
    command = parts[0]
    town = parts[1]

    if command == "Plunder":
        people = int(parts[2])
        stolen_gold = int(parts[3])

        towns[town]["population"] -= people
        towns[town]["gold"] -= stolen_gold

        print(f"{town} plundered! {stolen_gold} gold stolen, {people} citizens killed.")

        if towns[town]["population"] <= 0 or towns[town]["gold"] <= 0:
            print(f"{town} has been wiped off the map!")
            del towns[town]

    elif command == "Prosper":
        gold_added = int(parts[2])

        if gold_added < 0:
            print("Gold added cannot be a negative number!")
            continue

        towns[town]["gold"] += gold_added
        print(f"{gold_added} gold added to the city treasury. {town} now has {towns[town]['gold']} gold.")

if towns:
    print(f"Ahoy, Captain! There are {len(towns)} wealthy settlements to go to:")
    for town, data in towns.items():
        print(f"{town} -> Population: {data['population']} citizens, Gold: {data['gold']} kg")
else:
    print("Ahoy, Captain! All targets have been plundered and destroyed!")