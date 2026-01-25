inventory = input().split(", ")

command = input()

while command != "Craft!":
    parts = command.split(" - ")
    action = parts[0]

    if action == "Collect":
        item = parts[1]
        if item not in inventory:
            inventory.append(item)

    elif action == "Drop":
        item = parts[1]
        if item in inventory:
            inventory.remove(item)

    elif action == "Combine Items":
        old_item, new_item = parts[1].split(":")
        if old_item in inventory:
            index = inventory.index(old_item) + 1
            inventory.insert(index, new_item)

    elif action == "Renew":
        item = parts[1]
        if item in inventory:
            inventory.remove(item)
            inventory.append(item)

    command = input()

print(", ".join(inventory))