plants_count = int(input())
plants = {}

for _ in range(plants_count):
    plant_data = input()
    plant, rarity = plant_data.split("<->")
    rarity = int(rarity)

    if plant not in plants:
        plants[plant] = {'rarity': rarity, 'ratings': []}
    else:
        plants[plant]['rarity'] = rarity

command = input()

while command != "Exhibition":
    parts = command.split(": ")
    action = parts[0]

    if action == "Rate":
        plant_name, rating = parts[1].split(" - ")
        if plant_name in plants:
            plants[plant_name]['ratings'].append(int(rating))
        else:
            print("error")

    elif action == "Update":
        plant_name, new_rarity = parts[1].split(" - ")
        if plant_name in plants:
            plants[plant_name]['rarity'] = int(new_rarity)
        else:
            print("error")

    elif action == "Reset":
        plant_name = parts[1]
        if plant_name in plants:
            plants[plant_name]['ratings'] = []
        else:
            print("error")

    command = input()

print("Plants for the exhibition:")
for plant in plants:
    rarity = plants[plant]['rarity']
    ratings = plants[plant]['ratings']

    if len(ratings) > 0:
        average = sum(ratings) / len(ratings)
    else:
        average = 0

    print(f"- {plant}; Rarity: {rarity}; Rating: {average:.2f}")